# SBOM Demo Version 2
import requests
import pandas as pd
import numpy as np

def main():
    r = requests.get("https://api.github.com")
    print("GitHub API status:", r.status_code)

if __name__ == "__main__":
    main()
