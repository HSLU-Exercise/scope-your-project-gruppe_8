# kleine Änderung für SBOM-Demo

import requests
import pandas as pd
import numpy as np

def main():
    r = requests.get("https://api.github.com")
    print("GitHub API status:", r.status_code)

    df = pd.DataFrame({"Name": ["Kajeenan", "ChatGPT"], "Score": [10, 9]})
    print("Durchschnitt:", np.mean(df["Score"]))

if __name__ == "__main__":
    main()
