import numpy as np
import matplotlib.pyplot as plt

# 1. Kurvenabschnitt: Sinusfunktion (0 bis 48 Stunden)
x1 = np.linspace(0, 48, 140) 
y1 = -0.4 * np.sin(0.05 * x1) + 1  

# 2. Kurvenabschnitt: Parabel (48 bis 72 Stunden)
x2 = np.linspace(48, 72, 100)  
y2 = -(2756581 / 18768000000) * x2**2 + (143338793 / 4692000000) * x2 - (15568201 / 39100000)  # Parabel

# 3. Kurvenabschnitt: Exponentialfunktion (72 bis 140 Stunden)
x3 = np.linspace(72, 140, 200)  
a = 53.577  
b = 0.1
c = 1  
y3 = a * np.exp(-b * x3) + c  

# Plot der drei Abschnitte
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Sinus (0-48 Stunden)", color="blue")
plt.plot(x2, y2, label="Parabel (48-72 Stunden)", color="red")
plt.plot(x3, y3, label="Exponentialfunktion (72-140 Stunden)", color="green")

# Achsen und Titel
plt.axhline(y=1, color="gray", linestyle="--", label="Grenzwert: 1")
plt.xlabel("Zeit (Stunden)")
plt.ylabel("Leistung (relativ)")
plt.title("Superkompensation als zusammengesetzte Funktion über Zeit")
plt.legend()
plt.grid()
plt.show()

