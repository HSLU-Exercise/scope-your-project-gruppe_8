# Sicheres Beispiel
import getpass

# Passwort wird sicher abgefragt
user_password = getpass.getpass("Enter password: ")
print("User logged in")
# kein eval, kein hardcodiertes Passwort
