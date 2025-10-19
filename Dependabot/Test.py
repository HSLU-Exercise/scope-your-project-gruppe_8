import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Umsatz(t, x_0, r):
    Zustand = x_0
    Zeit = 0
    dt = 0.1
    while Zeit < t:
        if 0 <= Zeit <= 7*24:
            Zustand += r * dt
        Zeit += dt
    return Zustand

# Daten für den Plot
t = np.linspace(0, 7*24 + 24, 1000)
x = [Umsatz(Zeit, 0, 150) for Zeit in t]

# Erstelle einen DataFrame mit pandas
df = pd.DataFrame({'Zeit [Stunden]': t, 'Umsatz [Franken]': x})

# Plot mit matplotlib
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(df['Zeit [Stunden]'], df['Umsatz [Franken]'], color="blue", linewidth=3)
ax.set_xlabel("Zeit [Stunden]")
ax.set_ylabel("Umsatz [Franken]")
ax.set_title("Umsatzfunktion")
plt.grid(True)
plt.show()

# Optional: Speichere die Daten in eine CSV-Datei
df.to_csv('umsatz_daten.csv', index=False)
print("Daten wurden in 'umsatz_daten.csv' gespeichert.")
