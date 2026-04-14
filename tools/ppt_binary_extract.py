"""Extract text from legacy .ppt files by parsing PowerPoint binary record structures.

PowerPoint 97-2003 stores text in the 'PowerPoint Document' OLE stream.
Text records use type codes:
  - 4000 (0x0FA0): TextCharsAtom (UTF-16LE encoded text)
  - 4008 (0x0FA8): TextBytesAtom (ASCII/Latin-1 encoded text)
  - 4080 (0x0FF0): SlideListWithText container (marks slide boundaries)
"""
import os, struct, hashlib, datetime
import olefile

VAULT = r"C:\Users\itg\Desktop\lpg-trading-knowledge-base"
INBOX = os.path.join(VAULT, "00_Inbox")

RECORD_HEADER_SIZE = 8
TEXT_CHARS_ATOM = 0x0FA0   # 4000 - UTF-16LE text
TEXT_BYTES_ATOM = 0x0FA8   # 4008 - ASCII text
SLIDE_LIST_WITH_TEXT = 0x0FF0  # 4080 - container for slide text


def parse_ppt_text(path):
    ole = olefile.OleFileIO(path)

    stream_name = None
    for candidate in [["PowerPoint Document"], ["PP97_DUALSTORAGE", "PowerPoint Document"]]:
        if ole.exists(candidate):
            stream_name = candidate
            break

    if not stream_name:
        available = ["/".join(s) for s in ole.listdir()]
        ole.close()
        return f"[No PowerPoint Document stream found. Available: {available}]"

    data = ole.openstream(stream_name).read()
    ole.close()

    texts = []
    slide_num = 0
    pos = 0

    while pos + RECORD_HEADER_SIZE <= len(data):
        rec_ver_inst = struct.unpack_from("<H", data, pos)[0]
        rec_type = struct.unpack_from("<H", data, pos + 2)[0]
        rec_len = struct.unpack_from("<I", data, pos + 4)[0]

        rec_ver = rec_ver_inst & 0x0F
        is_container = (rec_ver == 0x0F)

        if rec_type == TEXT_CHARS_ATOM and not is_container:
            # UTF-16LE encoded text
            text_data = data[pos + RECORD_HEADER_SIZE: pos + RECORD_HEADER_SIZE + rec_len]
            try:
                text = text_data.decode("utf-16-le", errors="replace").strip()
                if text and len(text) > 0:
                    # Filter out binary garbage
                    printable_ratio = sum(1 for c in text if c.isprintable() or c in "\n\r\t") / max(len(text), 1)
                    if printable_ratio > 0.5:
                        texts.append(text)
            except:
                pass

        elif rec_type == TEXT_BYTES_ATOM and not is_container:
            # ASCII/Latin-1 encoded text
            text_data = data[pos + RECORD_HEADER_SIZE: pos + RECORD_HEADER_SIZE + rec_len]
            try:
                text = text_data.decode("latin-1", errors="replace").strip()
                if text and len(text) > 1:
                    printable_ratio = sum(1 for c in text if c.isprintable() or c in "\n\r\t") / max(len(text), 1)
                    if printable_ratio > 0.5:
                        texts.append(text)
            except:
                pass

        if is_container:
            pos += RECORD_HEADER_SIZE
        else:
            pos += RECORD_HEADER_SIZE + rec_len

    # Deduplicate consecutive identical texts
    deduped = []
    for t in texts:
        if not deduped or t != deduped[-1]:
            deduped.append(t)

    return "\n\n".join(deduped)


def save_to_inbox(filename, content):
    short_hash = hashlib.md5(filename.encode()).hexdigest()[:8]
    safe_name = os.path.splitext(filename)[0]
    for ch in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
        safe_name = safe_name.replace(ch, '_')
    out_name = f"{safe_name}_{short_hash}.txt"
    out_path = os.path.join(INBOX, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Source: {filename}\n")
        f.write(f"# Extracted: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"# Characters: {len(content)}\n\n")
        f.write(content)
    return out_name, len(content)


PPT_FILES = [
    r"D:\Users\itg\xwechat_files\wxid_4360143601512_6947\msg\file\2026-04\油轮合同.ppt",
    r"D:\Users\itg\xwechat_files\wxid_4360143601512_6947\msg\file\2026-04\报关流程总结.ppt",
]

print("Re-extracting .ppt files via binary record parsing...\n")
for path in PPT_FILES:
    fname = os.path.basename(path)
    try:
        content = parse_ppt_text(path)
        out_name, chars = save_to_inbox(fname, content)
        print(f"  OK  {fname} -> {out_name} ({chars:,} chars)")
    except Exception as e:
        print(f"  ERR {fname}: {e}")
        import traceback
        traceback.print_exc()

print("\nDone.")
