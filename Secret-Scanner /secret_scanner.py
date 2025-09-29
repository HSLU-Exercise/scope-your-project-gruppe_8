#!/usr/bin/env python3
"""
Minimaler Secret-Scanner (Demo)
- Sucht einfache, typische Secret-Patterns per Regex.
- Gibt Exit-Code 1 zurück, wenn etwas gefunden wird (CI/Actions blockieren dann).
- Schreibt .secret_scan_report.json mit Details.
"""

import re, sys, json, os

# ganz einfache Demo-Regeln — in echt erweitern!
RULES = [
    ("API Key (DEMO)", r"\bDEMO-API-KEY-[A-Za-z0-9\-]{6,}\b"),
    ("Potential base64-like", r"\b[A-Za-z0-9+/]{32,}={0,2}\b"),
    ("Private key header", r"-----BEGIN (RSA |)PRIVATE KEY-----"),
]

def scan_file(path):
    findings = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except Exception:
        return findings
    for name, pattern in RULES:
        for m in re.finditer(pattern, text):
            findings.append({
                "file": path,
                "rule": name,
                "match": m.group(0)[:120]
            })
    return findings

def main(paths=None):
    if paths is None or len(paths)==0:
        # scan all text-like files in repo root (simple demo)
        paths = [p for p in os.listdir(".") if os.path.isfile(p)]
    findings = []
    for p in paths:
        findings += scan_file(p)
    with open(".secret_scan_report.json", "w", encoding="utf-8") as out:
        json.dump(findings, out, indent=2)
    if findings:
        print("❌ Gefundene mögliche Secrets:")
        for f in findings:
            print(f" - {f['file']}: {f['rule']} -> {f['match']}")
        sys.exit(1)
    print("✅ Keine möglichen Secrets gefunden.")
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])
