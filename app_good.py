"""
GUTES BEISPIEL: Secrets kommen aus Umgebungsvariablen/Secret-Manager.
Niemals im Code hinterlegen. In CI: als GitHub Secret setzen.
"""
import os
import sys

def get_env_or_fail(name: str) -> str:
    value = os.getenv(name)
    if not value:
        print(f"[FEHLT] Umgebungsvariable {name} ist nicht gesetzt.", file=sys.stderr)
        sys.exit(1)
    return value

def connect_to_cloud():
    access_key = get_env_or_fail("AWS_ACCESS_KEY_ID")
    secret_key = get_env_or_fail("AWS_SECRET_ACCESS_KEY")
    print("Nutze Zugangsdaten aus ENV (Demo).")
    return True

if __name__ == "__main__":
    connect_to_cloud()
    print("Gutes Beispiel: Secrets kommen aus ENV. ✅")
