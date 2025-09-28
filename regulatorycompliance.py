# Regulatory Compliance Skript
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

def print_compliance_checklist():
	checklist = [
		"Datenschutzrichtlinie (Privacy Policy) vorhanden",
		"Impressum/Kontaktinformationen vorhanden",
		"Einwilligung zur Datenverarbeitung eingeholt",
		"Dokumentation der Datenflüsse vorhanden",
		"Zugriffskontrollen und Rollen dokumentiert",
		"Aufbewahrungsfristen für Daten definiert",
		"Mechanismen zur Datenlöschung implementiert",
		"Sicherheitsvorfälle werden dokumentiert und gemeldet",
		"Regelmäßige Compliance-Schulungen durchgeführt"
	]
	logger.log("Regulatory Compliance Checkliste:")
	for idx, item in enumerate(checklist, 1):
		logger.log(f"{idx}. {item}")

def interactive_compliance_checklist():
	checklist = [
		"Datenschutzrichtlinie (Privacy Policy) vorhanden",
		"Impressum/Kontaktinformationen vorhanden",
		"Einwilligung zur Datenverarbeitung eingeholt",
		"Dokumentation der Datenflüsse vorhanden",
		"Zugriffskontrollen und Rollen dokumentiert",
		"Aufbewahrungsfristen für Daten definiert",
		"Mechanismen zur Datenlöschung implementiert",
		"Sicherheitsvorfälle werden dokumentiert und gemeldet",
		"Regelmäßige Compliance-Schulungen durchgeführt"
	]
	logger.log("\nInteraktive Compliance-Checkliste: Bitte beantworten Sie mit 'j' (ja) oder 'n' (nein)")
	results = []
	for idx, item in enumerate(checklist, 1):
		answer = input(f"{idx}. {item} [j/n]: ").strip().lower()
		checked = "✔" if answer == "j" else "✘"
		results.append(f"{checked} {item}")
	logger.log("\nErgebnisse der Checkliste:")
	for line in results:
		logger.log(line)

def check_documents():
	docs = ["privacy_policy.txt", "impressum.txt", "data_flow_diagram.png"]
	logger.log("\nPrüfe auf wichtige Compliance-Dokumente...")
	for doc in docs:
		if os.path.exists(doc):
			logger.log(f"OK: {doc} gefunden.")
		else:
			logger.log(f"Fehlt: {doc} nicht gefunden.")
def check_consent_documented():
	# Beispiel: Suche nach Einwilligungsdokumenten
	consent_files = ["consent.txt", "einwilligung.txt"]
	logger.log("\nPrüfe auf dokumentierte Einwilligungen...")
	found = False
	for file in consent_files:
		if os.path.exists(file):
			logger.log(f"OK: Einwilligung dokumentiert in {file}.")
			found = True
	if not found:
		logger.log("Warnung: Keine dokumentierte Einwilligung gefunden!")

def search_gdpr_terms(directory):
	terms = ["DSGVO", "GDPR", "Datenschutz", "privacy", "data protection"]
	logger.log("\nSuche nach DSGVO-relevanten Begriffen im Projekt...")
	for root, _, files in os.walk(directory):
		for file in files:
			if file.endswith(('.py', '.md', '.txt')):
				path = os.path.join(root, file)
				with open(path, "r", encoding="utf-8") as f:
					content = f.read()
					for term in terms:
						if term in content:
							logger.log(f"Begriff '{term}' gefunden in {path}")

if __name__ == "__main__":
	logger = ReportLogger("compliance_report.txt")
	print_compliance_checklist()
	check_documents()
	check_consent_documented()
	search_gdpr_terms(".")
	interactive_compliance_checklist()
	logger.save()
	print("\nBericht gespeichert als compliance_report.txt")
