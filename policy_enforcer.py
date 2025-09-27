#!/usr/bin/env python3
"""
Kleiner Security Policy Checker.
Prüft Code auf:
- Hardcoded passwords
- eval()
- Debug-Prints
"""

import re, sys, os

POLICIES = [
    ("Hardcoded password", r'password\s*=\s*["\'][^"\']+["\']'),
    ("Use of eval()", r'\beval\('),
    ("Debug print", r'print\("DEBUG'),
]

def check_file(path):
    findings = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    for name, pattern in POLICIES:
        if re.search(pattern, text):
            findings.append(name)
    return findings

if __name__ == "__main__":
    # alle Dateien im Repo prüfen
    files = [f for f in os.listdir(".") if f.endswith(".py")]
    violations = {}
    for file in files:
        res = check_file(file)
        if res:
            violations[file] = res

    if violations:
        print("❌ Policy violations found:")
        for file, rules in violations.items():
            print(f"- {file}: {', '.join(rules)}")
        sys.exit(1)
    else:
        print("✅ No policy violations.")
