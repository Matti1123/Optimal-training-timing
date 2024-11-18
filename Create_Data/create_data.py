import numpy as np
import matplotlib.pyplot as plt

# 1. Kurvenabschnitt: Sinusfunktion (0 bis 48 Stunden)
x1 = np.linspace(0, 48, 140)  # x-Werte für den Sinus
y1 = -0.4 * np.sin(0.05 * x1) + 1  # Sinusfunktion

# 2. Kurvenabschnitt: Parabel (48 bis 72 Stunden)
x2 = np.linspace(48, 72, 100)  # x-Werte für die Parabel
y2 = -(71 / 469200) * x2**2 + (1847 / 58650) * x2 - (866 / 1955)  # Parabel

# 3. Kurvenabschnitt: Exponentialfunktion (72 bis 140 Stunden)
x3 = np.linspace(72, 140, 200)  # x-Werte für die Exponentialfunktion
a = 53.577  # Aus der vorherigen Berechnung
b = 0.1
c = 1  # Der Grenzwert
y3 = a * np.exp(-b * x3) + c  # Exponentialfunktion

# Plot der drei Abschnitte
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Sinus (0-48 Stunden)", color="blue")
plt.plot(x2, y2, label="Parabel (48-72 Stunden)", color="green")
plt.plot(x3, y3, label="Exponentialfunktion (72-140 Stunden)", color="red")

# Achsen und Titel
plt.axhline(y=1, color="gray", linestyle="--", label="Grenzwert: 1")
plt.xlabel("Zeit (Stunden)")
plt.ylabel("Funktion f(x)")
plt.title("Zusammengesetzte Funktion über Zeit")
plt.legend()
plt.grid()
plt.show()

