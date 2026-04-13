#!/usr/bin/env python3
"""
One-time setup for a new machine.

Detects the local Python path and vault root, then generates
.claude/settings.local.json with correct paths for hooks and permissions.

Usage:
    python setup.py
"""
import json
import sys
import os
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent


def detect_python() -> str:
    """Return the Unix-style path to the current Python interpreter."""
    raw = sys.executable  # e.g. C:\Users\itg\AppData\Local\Programs\Python\Python311\python.exe
    # Convert Windows backslashes to forward slashes for bash/git-bash
    return raw.replace("\\", "/")


def to_bash_path(win_path: str) -> str:
    """Convert C:/Users/... to /c/Users/... for git-bash."""
    p = win_path.replace("\\", "/")
    if len(p) >= 2 and p[1] == ":":
        drive = p[0].lower()
        p = f"/{drive}{p[2:]}"
    return p


def main():
    python_win = detect_python()
    python_bash = to_bash_path(python_win)
    vault_win = str(VAULT_ROOT).replace("\\", "/")
    vault_bash = to_bash_path(vault_win)

    print(f"Detected Python:    {python_win}")
    print(f"  bash-style:       {python_bash}")
    print(f"Detected Vault:     {vault_win}")
    print(f"  bash-style:       {vault_bash}")

    hook_command = (
        f"PYTHONIOENCODING=utf-8 {python_bash} "
        f"{vault_win}/tools/post_conversation.py"
    )

    settings = {
        "permissions": {
            "allow": [
                f"Bash(PYTHONIOENCODING=utf-8 {python_bash}:*)",
                f"Bash({python_bash}:*)",
                f"Bash({python_win}:*)",
                "WebSearch",
                "Skill(schedule)",
                "Bash(gh auth:*)",
                "Bash(git config:*)",
                "Bash(ls:*)",
                "Bash(rm:*)",
                "Bash(env)",
            ]
        },
        "hooks": {
            "Stop": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": hook_command,
                            "timeout": 15000,
                        }
                    ]
                }
            ]
        },
    }

    out_dir = VAULT_ROOT / ".claude"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "settings.local.json"

    # Warn if overwriting
    if out_file.exists():
        print(f"\nWARNING: {out_file} already exists.")
        answer = input("Overwrite? [y/N] ").strip().lower()
        if answer != "y":
            print("Aborted.")
            sys.exit(0)

    out_file.write_text(json.dumps(settings, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGenerated: {out_file}")
    print("Done! Claude Code hooks and permissions are configured for this machine.")


if __name__ == "__main__":
    main()
