import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Beispiel-Daten: Liste von Abhängigkeiten mit Versionen und Sicherheitsstatus
data = {
    'package': ['requests', 'urllib3', 'cryptography'],
    'version': ['2.19.1', '1.24.3', '2.8'],
    'vulnerable': [True, True, True],  # Simuliert, ob eine Sicherheitslücke existiert
    'severity': [8.0, 7.5, 6.5]  # Fiktive Schweregradwerte (0-10)
}

# Erzeuge ein Pandas DataFrame
df = pd.DataFrame(data)

# Füge eine Spalte für empfohlene sichere Versionen hinzu
df['recommended_version'] = ['2.31.0', '2.2.1', '42.0.5']  # Fiktive sichere Versionen

# Drucke die Tabelle zur Übersicht
print("Abhängigkeitsübersicht:")
print(df)

# Berechne statistische Zusammenfassungen mit numpy
mean_severity = np.mean(df['severity'])
max_severity = np.max(df['severity'])
print(f"\nStatistik: Durchschnittlicher Schweregrad = {mean_severity:.1f}, Höchster Schweregrad = {max_severity:.1f}")

# Erstelle ein Balkendiagramm mit matplotlib
plt.figure(figsize=(10, 6))
bars = plt.bar(df['package'], df['severity'], color=['red' if v else 'green' for v in df['vulnerable']])
plt.xlabel('Paket')
plt.ylabel('Schweregrad der Sicherheitslücke')
plt.title('Sicherheitsanalyse der Abhängigkeiten')
plt.ylim(0, 10)

# Füge Werte über den Balken hinzu
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}',
             ha='center', va='bottom')

# Zeige das Diagramm
plt.show()

# Optional: Speichere die Daten in eine CSV-Datei
df.to_csv('dependencies_analysis.csv', index=False)
print("Daten wurden in 'dependencies_analysis.csv' gespeichert.")
