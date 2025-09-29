# Audit Trail Maintenance Beispielskript
import csv
import os
from datetime import datetime, timedelta

import hashlib

AUDIT_FILE = "audit_trail.csv"

def add_audit_entry(user, action, details):
	now = datetime.now().isoformat()
	# Hash für Integritätsprüfung
	hash_value = hashlib.sha256(f"{now}{user}{action}{details}".encode()).hexdigest()
	entry = [now, user, action, details, hash_value]
	with open(AUDIT_FILE, "a", newline='', encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(entry)

def show_audit_trail():
	print("\nAudit Trail Einträge:")
	if not os.path.exists(AUDIT_FILE):
		print("Keine Audit-Trail-Datei vorhanden.")
		return
	with open(AUDIT_FILE, "r", encoding="utf-8") as f:
		reader = csv.reader(f)
		for row in reader:
			print(row)

def cleanup_old_entries(days=30):
	print(f"\nBereinige Einträge älter als {days} Tage...")
	if not os.path.exists(AUDIT_FILE):
		print("Keine Audit-Trail-Datei vorhanden.")
		return
	cutoff = datetime.now() - timedelta(days=days)
	new_entries = []
	with open(AUDIT_FILE, "r", encoding="utf-8") as f:
		reader = csv.reader(f)
		for row in reader:
			entry_time = datetime.fromisoformat(row[0])
			if entry_time >= cutoff:
				new_entries.append(row)
	with open(AUDIT_FILE, "w", newline='', encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerows(new_entries)
	print(f"{len(new_entries)} Einträge sind noch vorhanden.")

def export_audit_trail(filename="audit_trail_export.txt"):
	print(f"\nExportiere Audit Trail nach {filename} ...")
	if not os.path.exists(AUDIT_FILE):
		print("Keine Audit-Trail-Datei vorhanden.")
		return
	with open(AUDIT_FILE, "r", encoding="utf-8") as f_in, open(filename, "w", encoding="utf-8") as f_out:
		for line in f_in:
			f_out.write(line)
	print("Export abgeschlossen.")

def filter_by_user(user):
	print(f"\nFilter: Einträge für Benutzer '{user}':")
	if not os.path.exists(AUDIT_FILE):
		print("Keine Audit-Trail-Datei vorhanden.")
		return
	with open(AUDIT_FILE, "r", encoding="utf-8") as f:
		reader = csv.reader(f)
		for row in reader:
			if row[1] == user:
				print(row)

def search_by_action(action):
	print(f"\nSuche: Einträge mit Aktion '{action}':")
	if not os.path.exists(AUDIT_FILE):
		print("Keine Audit-Trail-Datei vorhanden.")
		return
	with open(AUDIT_FILE, "r", encoding="utf-8") as f:
		reader = csv.reader(f)
		for row in reader:
			if row[2] == action:
				print(row)

def audit_statistics():
	print("\nAudit Trail Statistik:")
	if not os.path.exists(AUDIT_FILE):
		print("Keine Audit-Trail-Datei vorhanden.")
		return
	user_count = {}
	action_count = {}
	with open(AUDIT_FILE, "r", encoding="utf-8") as f:
		reader = csv.reader(f)
		for row in reader:
			user = row[1]
			action = row[2]
			user_count[user] = user_count.get(user, 0) + 1
			action_count[action] = action_count.get(action, 0) + 1
	print("Aktionen pro Benutzer:")
	for user, count in user_count.items():
		print(f"  {user}: {count}")
	print("Aktionen gesamt:")
	for action, count in action_count.items():
		print(f"  {action}: {count}")

def check_integrity():
	print("\nIntegritätsprüfung der Audit-Trail-Einträge:")
	if not os.path.exists(AUDIT_FILE):
		print("Keine Audit-Trail-Datei vorhanden.")
		return
	with open(AUDIT_FILE, "r", encoding="utf-8") as f:
		reader = csv.reader(f)
		for row in reader:
			if len(row) < 5:
				print(f"Warnung: Eintrag unvollständig: {row}")
				continue
			timestamp, user, action, details, hash_value = row
			expected_hash = hashlib.sha256(f"{timestamp}{user}{action}{details}".encode()).hexdigest()
			if hash_value != expected_hash:
				print(f"Warnung: Manipulation erkannt bei Eintrag: {row}")

if __name__ == "__main__":
	# Beispiel: Neue Einträge anlegen
	add_audit_entry("alice", "login", "Erfolgreicher Login")
	add_audit_entry("bob", "delete", "Datensatz 123 gelöscht")
	# Audit Trail anzeigen
	show_audit_trail()
	# Alte Einträge bereinigen (älter als 30 Tage)
	cleanup_old_entries(days=30)

	# Export
	export_audit_trail()
	# Filter nach Benutzer
	filter_by_user("alice")
	# Suche nach Aktion
	search_by_action("delete")
	# Statistik
	audit_statistics()
	# Integritätsprüfung
	check_integrity()
