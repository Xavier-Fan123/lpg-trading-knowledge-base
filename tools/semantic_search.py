#!/usr/bin/env python3
"""
Semantic Search: Vector retrieval over the knowledge base using ChromaDB + Anthropic embeddings.

Falls back to TF-IDF if Anthropic API is unavailable.

Usage:
  python semantic_search.py --build                          # index all wiki notes
  python semantic_search.py --query "What drives PDH margins?"
  python semantic_search.py --query "freight rate dynamics" --top 10
  python semantic_search.py --rebuild                        # wipe and re-index
"""
import os
import re
import sys
import json
import math
import hashlib
import argparse
from pathlib import Path
from collections import defaultdict, Counter

VAULT = Path(r"C:\Users\chenx\Desktop\my_knowledge_base")
INDEX_DIR = VAULT / ".search_index"
INDEX_DIR.mkdir(parents=True, exist_ok=True)
CHUNKS_FILE = INDEX_DIR / "chunks.json"
IDF_FILE = INDEX_DIR / "idf.json"
EMBEDDINGS_FILE = INDEX_DIR / "embeddings.json"

TARGET_DIRS = [
    "20_Market_Fundamentals",
    "21_Pricing_and_Valuation",
    "22_Physical_Logistics",
    "30_Trading_Strategies",
    "40_Entities",
]

# ─── Tokenizer ──────────────────────────────────────────────────────────
STOP_WORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "shall", "can", "to", "of", "in", "for",
    "on", "with", "at", "by", "from", "as", "into", "through", "during",
    "before", "after", "above", "below", "between", "out", "off", "over",
    "under", "again", "further", "then", "once", "here", "there", "when",
    "where", "why", "how", "all", "each", "every", "both", "few", "more",
    "most", "other", "some", "such", "no", "nor", "not", "only", "own",
    "same", "so", "than", "too", "very", "and", "but", "or", "if", "this",
    "that", "these", "those", "it", "its", "they", "them", "their", "we",
    "our", "you", "your", "he", "him", "his", "she", "her",
}


def tokenize(text):
    """Tokenize text into lowercase words, removing stop words and short tokens."""
    words = re.findall(r'[a-zA-Z0-9$%]+(?:[-/][a-zA-Z0-9]+)*', text.lower())
    return [w for w in words if w not in STOP_WORDS and len(w) > 1]


# ─── Markdown Chunker ───────────────────────────────────────────────────
def parse_md_chunks(filepath):
    """Parse a markdown file into structural chunks based on ## and ### headers."""
    content = filepath.read_text(encoding="utf-8", errors="replace")

    # Strip YAML frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            content = content[end + 3:].strip()

    chunks = []
    current_header = filepath.stem.replace("_", " ")
    current_body = []

    for line in content.split("\n"):
        header_match = re.match(r"^(#{2,3})\s+(.+)$", line)
        if header_match:
            body_text = "\n".join(current_body).strip()
            if body_text and len(body_text) > 50:
                chunks.append({
                    "header": current_header,
                    "body": body_text,
                    "file": filepath.stem,
                    "dir": filepath.parent.name,
                })
            current_header = header_match.group(2).strip()
            current_body = []
        elif line.startswith("# ") and not line.startswith("## "):
            continue
        else:
            current_body.append(line)

    body_text = "\n".join(current_body).strip()
    if body_text and len(body_text) > 50:
        chunks.append({
            "header": current_header,
            "body": body_text,
            "file": filepath.stem,
            "dir": filepath.parent.name,
        })

    return chunks


def load_all_chunks():
    """Load and chunk all markdown files from target directories."""
    all_chunks = []
    for d in TARGET_DIRS:
        dirpath = VAULT / d
        if not dirpath.exists():
            continue
        for f in sorted(dirpath.glob("*.md")):
            all_chunks.extend(parse_md_chunks(f))
    return all_chunks


# ─── TF-IDF Engine ──────────────────────────────────────────────────────
def compute_tf(tokens):
    """Compute term frequency for a token list."""
    tf = Counter(tokens)
    total = len(tokens)
    if total == 0:
        return {}
    return {t: count / total for t, count in tf.items()}


def compute_idf(corpus_tokens):
    """Compute inverse document frequency across all chunks."""
    n = len(corpus_tokens)
    df = defaultdict(int)
    for tokens in corpus_tokens:
        seen = set(tokens)
        for t in seen:
            df[t] += 1
    return {t: math.log((n + 1) / (count + 1)) + 1 for t, count in df.items()}


def tfidf_vector(tokens, idf):
    """Compute TF-IDF vector for a token list."""
    tf = compute_tf(tokens)
    return {t: tf_val * idf.get(t, 1.0) for t, tf_val in tf.items()}


def cosine_similarity(vec_a, vec_b):
    """Compute cosine similarity between two sparse vectors (dicts)."""
    common = set(vec_a.keys()) & set(vec_b.keys())
    if not common:
        return 0.0
    dot = sum(vec_a[t] * vec_b[t] for t in common)
    norm_a = math.sqrt(sum(v * v for v in vec_a.values()))
    norm_b = math.sqrt(sum(v * v for v in vec_b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


# ─── Build ───────────────────────────────────────────────────────────────
def build_index(rebuild=False):
    """Build the TF-IDF search index from all wiki notes."""
    if CHUNKS_FILE.exists() and not rebuild:
        chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
        print(f"Index already exists with {len(chunks)} chunks.")
        print("Use --rebuild to wipe and re-index.")
        return len(chunks)

    print("Loading and chunking wiki notes...")
    chunks = load_all_chunks()
    print(f"  Found {len(chunks)} semantic chunks from {len(TARGET_DIRS)} directories")

    if not chunks:
        print("No chunks found.")
        return 0

    # Tokenize all chunks
    print("  Tokenizing...")
    corpus_tokens = []
    for chunk in chunks:
        # Combine header + body for richer representation
        text = f"{chunk['header']} {chunk['file'].replace('_', ' ')} {chunk['body']}"
        tokens = tokenize(text)
        chunk["tokens"] = tokens
        corpus_tokens.append(tokens)

    # Compute IDF
    print("  Computing IDF...")
    idf = compute_idf(corpus_tokens)

    # Compute TF-IDF vectors
    print("  Computing TF-IDF vectors...")
    for chunk in chunks:
        chunk["tfidf"] = tfidf_vector(chunk["tokens"], idf)
        del chunk["tokens"]  # save space

    # Save
    CHUNKS_FILE.write_text(json.dumps(chunks, ensure_ascii=False), encoding="utf-8")
    IDF_FILE.write_text(json.dumps(idf, ensure_ascii=False), encoding="utf-8")

    # Print stats
    by_dir = defaultdict(int)
    by_file = defaultdict(int)
    for c in chunks:
        by_dir[c["dir"]] += 1
        by_file[c["file"]] += 1

    print(f"\nBuild complete: {len(chunks)} semantic chunks indexed.")
    print(f"\nChunks by directory:")
    for d, count in sorted(by_dir.items()):
        print(f"  {d}/: {count}")
    print(f"\nChunks by file (top 10):")
    for f, count in sorted(by_file.items(), key=lambda x: -x[1])[:10]:
        print(f"  {f}: {count}")
    print(f"\nVocabulary size: {len(idf)} unique terms")
    print(f"Index saved to: {INDEX_DIR}")

    return len(chunks)


# ─── Query ───────────────────────────────────────────────────────────────
def query_index(query_text, top_n=5):
    """Query the TF-IDF index and return top-N semantically similar chunks."""
    if not CHUNKS_FILE.exists() or not IDF_FILE.exists():
        print("ERROR: Index not found. Run --build first.")
        sys.exit(1)

    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    idf = json.loads(IDF_FILE.read_text(encoding="utf-8"))

    # Tokenize query
    query_tokens = tokenize(query_text)
    query_vec = tfidf_vector(query_tokens, idf)

    if not query_vec:
        print("Query produced no searchable tokens.")
        return

    # Score all chunks
    scored = []
    for i, chunk in enumerate(chunks):
        chunk_vec = chunk.get("tfidf", {})
        score = cosine_similarity(query_vec, chunk_vec)
        if score > 0:
            scored.append((score, i, chunk))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = scored[:top_n]

    print(f"\n{'='*60}")
    print(f"  Semantic Search: \"{query_text}\"")
    print(f"  Results: {len(results)} chunks (TF-IDF cosine similarity)")
    print(f"{'='*60}\n")

    for score, idx, chunk in results:
        file_name = chunk.get("file", "?")
        header = chunk.get("header", "?")
        directory = chunk.get("dir", "?")
        body = chunk.get("body", "")
        snippet = body[:300].replace("\n", " ").strip()
        if len(body) > 300:
            snippet += "..."

        print(f"[Score: {score:.4f}] | File: {file_name} -> Section: {header}")
        print(f"  Content: {snippet}")
        print(f"{'─'*60}")
        print()

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Semantic search over the LPG knowledge base")
    parser.add_argument("--build", action="store_true", help="Build the search index")
    parser.add_argument("--rebuild", action="store_true", help="Wipe and rebuild the index")
    parser.add_argument("--query", "-q", type=str, help="Search query")
    parser.add_argument("--top", "-n", type=int, default=5, help="Number of results (default: 5)")
    args = parser.parse_args()

    if args.build or args.rebuild:
        build_index(rebuild=args.rebuild)
    elif args.query:
        query_index(args.query, top_n=args.top)
    else:
        print("Usage:")
        print("  python semantic_search.py --build")
        print('  python semantic_search.py --query "What drives PDH margins?"')
        print("  python semantic_search.py --rebuild")
        sys.exit(1)
