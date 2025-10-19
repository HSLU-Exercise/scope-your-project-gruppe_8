import numpy as np
import matplotlib.pyplot as plt

def Umsatz(t,x_0,r):
    Zustand = x_0
    Zeit = 0
    dt = 0.1
    while Zeit < t: #Kann auch nur kleiner Sein minimaler Rundungsunterschied, mit dt = 0.1 wird nur 0.1 mehr hinzugefügt bei dt = 1 wird zu viel hinzugefügt. Muss t<3 als ersatz verwendet werden.
        if 0 <= Zeit <= 7*24: #Bestimmt wie lage das Spendenkonto offen ist.
            Zustand += r
        Zeit += 1
    return Zustand

Umsatz(3,0,150)

t = np.linspace(-24,7*24+ 24, 1000) #Anfangswert, Schlusswerte, Anzahl werte
x = [Umsatz(Zeit,0,150) for Zeit in t] #Zeit for Zeit in r Umsatz als Funktion

fig = plt.figure()
ax = fig.add_subplot(1,1,1) #gibt die Funktion als Grafik aus
ax.plot(x,color = "blue",linewidth=3) #Gibt
ax.set_xlabel("Zeit [Stunden]")
ax.set_ylabel("Umsatz [Franken]")
ax.set_title("Umsatzfunktion")

plt.show()
