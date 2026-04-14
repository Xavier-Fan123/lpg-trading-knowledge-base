"""Re-extract old .ppt files using win32com (PowerPoint COM automation)."""
import os, sys, hashlib, datetime

VAULT = r"C:\Users\itg\Desktop\lpg-trading-knowledge-base"
INBOX = os.path.join(VAULT, "00_Inbox")

def extract_ppt_com(path):
    import win32com.client
    import pythoncom
    pythoncom.CoInitialize()

    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    ppt_app.Visible = False

    abs_path = os.path.abspath(path)
    presentation = ppt_app.Presentations.Open(abs_path, ReadOnly=True, WithWindow=False)

    lines = []
    for i, slide in enumerate(presentation.Slides, 1):
        lines.append(f"\n--- Slide {i} ---")
        for shape in slide.Shapes:
            if shape.HasTextFrame:
                tf = shape.TextFrame
                try:
                    text = tf.TextRange.Text.strip()
                    if text:
                        lines.append(text)
                except:
                    pass
            if shape.HasTable:
                table = shape.Table
                for r in range(1, table.Rows.Count + 1):
                    row_cells = []
                    for c in range(1, table.Columns.Count + 1):
                        try:
                            cell_text = table.Cell(r, c).Shape.TextFrame.TextRange.Text.strip()
                            row_cells.append(cell_text)
                        except:
                            row_cells.append("")
                    row_text = " | ".join(row_cells)
                    if row_text.replace("|", "").strip():
                        lines.append(row_text)

    presentation.Close()
    ppt_app.Quit()
    pythoncom.CoUninitialize()

    return "\n".join(lines)

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

print("Re-extracting .ppt files via PowerPoint COM...\n")
for path in PPT_FILES:
    fname = os.path.basename(path)
    try:
        content = extract_ppt_com(path)
        out_name, chars = save_to_inbox(fname, content)
        print(f"  OK  {fname} -> {out_name} ({chars:,} chars)")
    except Exception as e:
        print(f"  ERR {fname}: {e}")

print("\nDone.")
