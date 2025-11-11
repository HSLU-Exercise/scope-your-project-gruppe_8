# app.py
# Demo: hardcoded values that should get flagged by a scanner

API_KEY = "sk_test_51HFAKEl0ngStripeKey_example"
DB_PASSWORD = "SuperSecretPassw0rd!"
SERVICE_TOKEN = "ghp_FAKEGITHUBTOKENEXAMPLE1234567890"

def main():
    print("Demo app. Do not use for production.")
    print("API_KEY:", API_KEY)
    print("DB_PASSWORD:", DB_PASSWORD)
    print("SERVICE_TOKEN:", SERVICE_TOKEN)

if __name__ == "__main__":
    main()
