# Kombiniertes Skript: Security Best Practices und automatische Prüfung
import os

class ReportLogger:
	def __init__(self, filename):
		self.filename = filename
		self.lines = []
	def log(self, message):
		print(message)
		self.lines.append(message)
	def save(self):
		with open(self.filename, "w", encoding="utf-8") as f:
			for line in self.lines:
				f.write(line + "\n")

def print_security_best_practices():
	best_practices = [
		"Verwende starke Passwörter und sichere Authentifizierung.",
		"Halte Software und Abhängigkeiten aktuell.",
		"Vermeide die Speicherung von sensiblen Daten im Code.",
		"Nutze Verschlüsselung für vertrauliche Daten.",
		"Setze Zugriffsrechte und Rollen sinnvoll ein.",
		"Überprüfe Eingaben auf Validität (Input Validation).",
		"Führe regelmäßige Backups durch.",
		"Nutze sichere Netzwerkverbindungen (HTTPS, SSH)."
	]
	logger.log("Security Best Practices:")
	for idx, practice in enumerate(best_practices, 1):
		logger.log(f"{idx}. {practice}")

def interactive_checklist():
	best_practices = [
		"Verwende starke Passwörter und sichere Authentifizierung.",
		"Halte Software und Abhängigkeiten aktuell.",
		"Vermeide die Speicherung von sensiblen Daten im Code.",
		"Nutze Verschlüsselung für vertrauliche Daten.",
		"Setze Zugriffsrechte und Rollen sinnvoll ein.",
		"Überprüfe Eingaben auf Validität (Input Validation).",
		"Führe regelmäßige Backups durch.",
		"Nutze sichere Netzwerkverbindungen (HTTPS, SSH)."
	]
	logger.log("\nInteraktive Checkliste: Bitte beantworten Sie mit 'j' (ja) oder 'n' (nein)")
	results = []
	for idx, practice in enumerate(best_practices, 1):
		answer = input(f"{idx}. {practice} [j/n]: ").strip().lower()
		checked = "✔" if answer == "j" else "✘"
		results.append(f"{checked} {practice}")
	logger.log("\nErgebnisse der Checkliste:")
	for line in results:
		logger.log(line)

def scan_for_sensitive_keywords(directory, keywords):
	logger.log("\nPrüfe auf sensible Schlüsselwörter im Code...")
	for root, _, files in os.walk(directory):
		for file in files:
			if file.endswith(".py"):
				path = os.path.join(root, file)
				with open(path, "r", encoding="utf-8") as f:
					content = f.read()
					for keyword in keywords:
						if keyword in content:
							logger.log(f"Warnung: '{keyword}' gefunden in {path}")

def keyword_statistics(directory, keywords):
	logger.log("\nCode-Statistik zu sensiblen Schlüsselwörtern:")
	stats = {kw: {"count": 0, "files": set()} for kw in keywords}
	for root, _, files in os.walk(directory):
		for file in files:
			if file.endswith(".py"):
				path = os.path.join(root, file)
				with open(path, "r", encoding="utf-8") as f:
					content = f.read()
					for kw in keywords:
						occurrences = content.count(kw)
						if occurrences > 0:
							stats[kw]["count"] += occurrences
							stats[kw]["files"].add(path)
	for kw, data in stats.items():
		logger.log(f"'{kw}': {data['count']} Vorkommen in {len(data['files'])} Datei(en)")
		if data['files']:
			logger.log(f"  Dateien: {', '.join(data['files'])}")

def scan_for_unsafe_imports(directory):
	logger.log("\nPrüfe auf unsichere Imports und Funktionen...")
	unsafe_patterns = ["os.system", "eval(", "exec("]
	for root, _, files in os.walk(directory):
		for file in files:
			if file.endswith(".py"):
				path = os.path.join(root, file)
				with open(path, "r", encoding="utf-8") as f:
					content = f.read()
					for pattern in unsafe_patterns:
						if pattern in content:
							logger.log(f"Warnung: Unsichere Funktion '{pattern}' gefunden in {path}")

def scan_for_unencrypted_connections(directory):
	logger.log("\nPrüfe auf unverschlüsselte Verbindungen (http statt https)...")
	for root, _, files in os.walk(directory):
		for file in files:
			if file.endswith(".py"):
				path = os.path.join(root, file)
				with open(path, "r", encoding="utf-8") as f:
					content = f.read()
					if "http://" in content:
						logger.log(f"Warnung: Unverschlüsselte Verbindung (http://) gefunden in {path}")

def check_outdated_requirements(requirements_path):
	logger.log("\nPrüfe requirements.txt auf veraltete Pakete...")
	try:
		import pkg_resources
		with open(requirements_path, "r", encoding="utf-8") as req_file:
			for line in req_file:
				line = line.strip()
				if not line or line.startswith('#'):
					continue
				if '==' in line:
					pkg, version = line.split('==')
				else:
					pkg = line
					version = None
				try:
					dist = pkg_resources.get_distribution(pkg)
					installed_version = dist.version
					if version and installed_version != version:
						logger.log(f"Warnung: {pkg} installiert: {installed_version}, gefordert: {version}")
				except Exception:
					logger.log(f"Hinweis: Paket {pkg} ist nicht installiert.")
	except ImportError:
		logger.log("Das Modul pkg_resources ist nicht verfügbar. Bitte installieren Sie setuptools.")

def check_sensitive_file_permissions(files):
	import stat
	logger.log("\nPrüfe Dateiberechtigungen für sensible Dateien...")
	for file in files:
		if os.path.exists(file):
			mode = os.stat(file).st_mode
			if mode & stat.S_IROTH:
				logger.log(f"Warnung: {file} ist für andere lesbar!")
			else:
				logger.log(f"OK: {file} ist nicht für andere lesbar.")
		else:
			logger.log(f"Hinweis: {file} existiert nicht.")

if __name__ == "__main__":
	logger = ReportLogger("security_report.txt")
	print_security_best_practices()
	keywords = ["password", "secret", "api_key", "token"]
	scan_for_sensitive_keywords(".", keywords)
	scan_for_unsafe_imports(".")
	scan_for_unencrypted_connections(".")
	check_outdated_requirements("Dependabot/requirements.txt")
	sensitive_files = [".env", "config.env", "settings.env"]
	check_sensitive_file_permissions(sensitive_files)
	keyword_statistics(".", keywords)
	interactive_checklist()
	logger.save()
	print("\nBericht gespeichert als security_report.txt")
