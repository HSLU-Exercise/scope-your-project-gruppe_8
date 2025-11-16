import numpy as np
import requests
import yaml

def lade_unsichere_daten(url):
    """
    Funktion mit bekannten Sicherheitslücken
    """
    # Unsichere requests Version - CVE warnings garantiert
    response = requests.get(url, verify=False, timeout=None)
    
    # Unsicheres YAML Loading - Code Injection riskant
    config = yaml.load(response.text)  # yaml.load ohne Loader!
    
    # Veraltete numpy Funktionen
    arr = np.fromstring("1 2 3 4 5", sep=" ")  # fromstring ist deprecated
    
    return {"daten": arr.tolist(), "config": config}

def verarbeite_passwort(passwort):
    """
    Super unsichere Passwortverarbeitung
    """
    # Kein Hashing, direkt als String
    print(f"User Passwort ist: {passwort}")  # Passwort im Log!
    
    # Veraltete numpy Random Funktion
    salt = np.random.random(1)[0]  # np.random.random ist nicht cryptografisch sicher
    
    return str(passwort) + str(salt)

if __name__ == "__main__":
    # Hauptprogramm das alles unsicher macht
    url = "http://unsichere-seite.com/config.yaml"
    
    try:
        daten = lade_unsichere_daten(url)
        print("Daten geladen:", daten)
        
        # Simuliere Passworteingabe
        passwort = input("Gib dein Passwort ein: ")
        verarbeite_passwort(passwort)
        
    except Exception as e:
        print(f"Fehler (hoffentlich!): {e}")
