import re
import os
import math
import json
import sys

# Erweiterte / praktische Patterns — füge hier weitere hinzu wenn nötig
PATTERNS = {
    "GitHub Secret-Scanner test token": re.compile(r"secret_scanning_[0-9a-f]{40}_[a-z0-9]+"),
    "AWS Access Key ID (AKIA...)": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "AWS Secret Access Key (inline)": re.compile(r"(?i)aws_secret_access_key\s*[:=]\s*([A-Za-z0-9/+=]{40})"),
    "AWS Secret Access Key (bare)": re.compile(r"\b[A-Za-z0-9/+=]{40}\b"),
    "RSA/PRIVATE KEY block": re.compile(r"-----BEGIN (RSA|PRIVATE) KEY-----"),
    "JWT-like (three parts)": re.compile(r"\b[A-Za-z0-9-_]{10,}\.[A-Za-z0-9-_]{10,}\.[A-Za-z0-9-_]{6,}\b"),
    "Stripe Key (sk_live/sk_test)": re.compile(r"\bsk_(live|test)_[A-Za-z0-9]{24,}\b"),
    "GitHub Token (ghp_)": re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),
    "SendGrid (SG.)": re.compile(r"\bSG\.[A-Za-z0-9_\-\.]{20,}\b"),
    "Generic API Key / Key assignment": re.compile(
        r'(?i)\b(?:api[_-]?key|secret|token|password|passwd|pwd|access[_-]?key)\b\s*[:=]\s*["\']?([A-Za-z0-9_\-+/=\.]{8,})["\']?'
    ),
    "Long hex token (30+ hex chars)": re.compile(r"\b[0-9a-fA-F]{30,}\b"),
    "Long base64-like (40+ chars)": re.compile(r"\b[A-Za-z0-9_\-+/=]{40,}\b")
}

IGNORED_DIRS = {'.git', '__pycache__', '.venv', 'venv', '.terraform'}

# Entropie-Berechnung
def shannon_entropy(s: str) -> float:
    if not s:
        return 0.0
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    entropy = 0.0
    length = len(s)
    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)
    return entropy

def scan_file(path):
    findings = []
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
    except Exception:
        return findings

    # Regex-basierte Treffer
    for name, pattern in PATTERNS.items():
        for m in pattern.finditer(text):
            snippet = m.group(0)
            lineno = text[:m.start()].count('\n') + 1
            findings.append({"type": name, "file": path, "line": lineno, "snippet": snippet})

    # Heuristischer Scan: lange Tokens ohne Whitespace
    for m in re.finditer(r"\b[A-Za-z0-9_\-+/=\.]{20,}\b", text):
        token = m.group(0)
        lineno = text[:m.start()].count('\n') + 1
        ent = shannon_entropy(token)
        # Aggressivere Schwellen: Länge > 25 und Entropie > 4.0
        if len(token) > 25 and ent > 4.0:
            findings.append({"type": "High-entropy token (heuristic)", "file": path, "line": lineno, "snippet": f"{token} (entropy={ent:.2f})"})

    return findings

def walk_and_scan(root='.'):
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for fname in filenames:
            path = os.path.join(dirpath, fname)
            if fname.endswith(('.png', '.jpg', '.jpeg', '.gif', '.exe', '.dll', '.so')):
                continue
            items = scan_file(path)
            if items:
                results.extend(items)
    return results

def main(output_json=False):
    results = walk_and_scan('.')
    if not results:
        print("Keine Secrets gefunden.")
        return 0
    if output_json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for r in results:
            print(f"{r['file']}:{r['line']}  [{r['type']}] {r['snippet']}")
    # non-zero exit so hooks/CI can fail
    return 2

if __name__ == "__main__":
    # wenn --json übergeben wird, gibt JSON aus
    out_json = '--json' in sys.argv
    code = main(output_json=out_json)
    sys.exit(code)
