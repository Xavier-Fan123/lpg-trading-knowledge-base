# LPG Trading Knowledge Base

A structured, LLM-powered knowledge base for LPG (Liquefied Petroleum Gas) trading — covering market fundamentals, pricing benchmarks, physical logistics, trading strategies, and key market entities.

Built with Claude Code as the AI backbone, Obsidian as the viewing frontend, and a suite of Python CLI tools for automated knowledge ingestion, extraction, search, and maintenance.

## Architecture

```
User asks LPG question
  │
  ▼
CLAUDE.md (behavioral rules)
  │
  ├─ Rule 1: Search KB first ──► search.py / semantic_search.py
  │                                    │
  │                                    ▼
  │                              Read wiki notes → Answer with citations
  │
  ├─ Rule 2: Save valuable Q&A ──► qa_file.py → Append to wiki note
  │
  ├─ Rule 3: Ingest new content ──► web_clip.py → miner.py → Enrich wiki
  │
  ├─ Rule 4: Detect knowledge gaps ──► knowledge_gaps.md
  │
  └─ Rule 5: Weekly maintenance ──► vault_lint.py → Health report
```

## Knowledge Base Stats

| Metric | Value |
|--------|-------|
| Wiki notes | 37 |
| Total words | ~65,000 |
| Mined facts | 2,147 |
| Source documents | 287 |
| Entity profiles | 17 |
| Python tools | 8 |

## Directory Structure

```
├── 10_Atlas/                  # Index & health reports
│   ├── Master_Index.md        # Map of Content with all WikiLinks
│   └── Health_Report.md       # Auto-generated vault health check
│
├── 20_Market_Fundamentals/    # Supply, demand & macro drivers
│   ├── LPG_Market_Fundamentals.md
│   ├── Chinese_PDH_Margin.md
│   ├── LPG_Supply_Chain_Structure.md
│   └── Seasonal_Trading_Patterns.md
│
├── 21_Pricing_and_Valuation/  # Benchmarks, formulas & risk pricing
│   ├── Saudi_Aramco_Contract_Price.md
│   ├── AFEI_Benchmark.md
│   ├── Propane_Naphtha_Spread.md
│   ├── Physical_Hedging_Architecture.md
│   └── ... (7 notes)
│
├── 22_Physical_Logistics/     # Freight, shipping & terminal ops
│   ├── VLGC_Freight_Dynamics.md
│   ├── Demurrage_and_Laytime.md
│   ├── Physical_LPG_Contract_Logic.md
│   └── ... (5 notes)
│
├── 30_Trading_Strategies/     # Arbitrage & trade frameworks
│   ├── Geographical_Arbitrage.md
│   └── US_Asia_LPG_Arb_Framework.md
│
├── 40_Entities/               # Counterparties, infrastructure, data providers
│   ├── Saudi_Aramco.md
│   ├── Mont_Belvieu.md
│   ├── Panama_Canal.md
│   └── ... (17 notes)
│
├── 00_Inbox/                  # Raw data & incoming content
│   ├── notes/                 # Original NotebookLM notes
│   ├── sources/               # 287 source texts (gitignored, 16MB)
│   └── knowledge_gaps.md      # Auto-detected knowledge gaps
│
├── 50_Outputs/                # Generated slides & reports
│
├── tools/                     # Python CLI toolkit
│   ├── search.py              # Full-text keyword search
│   ├── semantic_search.py     # TF-IDF vector search (ChromaDB)
│   ├── miner.py               # LLM-powered fact extraction pipeline
│   ├── compile.py             # Inbox → wiki note auto-classifier
│   ├── qa_file.py             # Q&A filing into wiki notes
│   ├── web_clip.py            # Web page → Markdown clipper
│   ├── slides.py              # Wiki → Marp slide generator
│   └── post_conversation.py   # Stop hook: gap detection
│
├── vault_lint.py              # Health check: broken links, contradictions, orphans
├── CLAUDE.md                  # AI behavioral rules (auto-loaded by Claude Code)
└── .gitignore
```

## Tools

### Search

```bash
# Keyword search
python tools/search.py "VLGC freight rate" --top 5

# Semantic search (TF-IDF cosine similarity)
python tools/semantic_search.py --query "What drives PDH margins?" --top 5

# Rebuild search index
python tools/semantic_search.py --rebuild
```

### Knowledge Ingestion

```bash
# Clip a web article
python tools/web_clip.py "https://example.com/article" --title "LPG Market Update"

# Extract facts from source documents (LLM-powered, Map-Route-Reduce)
python tools/miner.py --run --limit 10
python tools/miner.py --status

# Auto-classify inbox files into wiki notes
python tools/compile.py --process --auto
```

### Q&A Filing

```bash
# Save a Q&A pair to the most relevant wiki note
python tools/qa_file.py -q "What is AFEI?" -a "Argus Far East Index, the primary Asian LPG spot benchmark..." -t AFEI_Benchmark
```

### Maintenance

```bash
# Health check: broken links, data contradictions, orphan notes
python vault_lint.py

# Generate Marp slides from wiki notes
python tools/slides.py --all-market
```

## Auto-Learning System

The knowledge base is designed to grow automatically through use:

1. **Search-first answering** — Every LPG question triggers a KB search before answering
2. **Q&A write-back** — Valuable insights from conversations are saved back to wiki notes
3. **Gap detection** — Topics not covered by the KB are automatically logged for future research
4. **Weekly health check** — Claude proactively reminds you when maintenance is overdue (>7 days)

This is powered by `CLAUDE.md` (behavioral rules for Claude Code) and a `Stop` hook (`post_conversation.py`) that detects knowledge gaps after each conversation turn.

## Note Format

Every wiki note follows a standardized structure:

- **YAML frontmatter**: aliases, tags, date, status
- **Empirical Facts vs Analytical Assumptions**: hard data separated from interpretive claims
- **Scenario Analysis**: Base / Bull / Bear / Invalidation Triggers
- **Downside Risks**: WikiLinked to specific risk entities
- **Mined Data**: Facts extracted from source documents by `miner.py`

## Tech Stack

- **AI**: [Claude Code](https://claude.ai/claude-code) (Opus 4.6) + Anthropic API (Haiku for mining)
- **Frontend**: [Obsidian](https://obsidian.md/) (Markdown viewer with WikiLinks & graph view)
- **Search**: TF-IDF vector search + full-text keyword search
- **Data Source**: NotebookLM export (287 source documents, 26 notes)
- **Language**: Python 3.13

## Getting Started

1. Clone the repo
2. Set up your Anthropic API key in `.env`:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   ```
3. Install dependencies:
   ```bash
   pip install anthropic chromadb
   ```
4. Build the search index:
   ```bash
   python tools/semantic_search.py --rebuild
   ```
5. Open the directory in [Claude Code](https://claude.ai/claude-code) — `CLAUDE.md` loads automatically
6. (Optional) Open in [Obsidian](https://obsidian.md/) for graph view and visual browsing

## Inspired By

This project follows the "LLM Knowledge Base" pattern described by [Andrej Karpathy](https://x.com/karpathy) — using LLMs to ingest raw data, compile structured wikis, answer complex queries, and incrementally enhance the knowledge base through use.

## License

MIT
