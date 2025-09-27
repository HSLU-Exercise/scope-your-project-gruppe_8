"""
ACHTUNG: SCHLECHTES BEISPIEL (FAKE Secrets, nur Demo)
Bitte niemals echte Zugangsdaten im Code speichern!
"""

AWS_ACCESS_KEY_ID = "AKIAFAKEEXAMPLEKEYID12"        # FAKE
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYFAKEEXAMPLE"  # FAKE
GITHUB_TOKEN = "ghp_FAKEexampleTokenForDemoONLY1234567890"            # FAKE

def connect_to_cloud():
    print("Verbinde mit Cloud-API (Demo) ...")
    return True

if __name__ == "__main__":
    connect_to_cloud()
    print("Schlechtes Beispiel ausgeführt. (Nur Demo)")
