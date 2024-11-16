import numpy as np
import matplotlib.pyplot as plt

# Definiere die Punkte
points = np.array([[0, 1], [6, 0.6], [48, 0.8], [68, 1.],[72, 1.04],[82, 1.],[140, 0.98]])

# Erstellen der Linien zwischen den Punkten
x_values = np.linspace(0, 140, 500)  # Erzeuge 500 Punkte zwischen 0 und 72
y_values = np.interp(x_values, points[:, 0], points[:, 1])  # Interpolierte y-Werte

# Plot der Linien
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Stückweise lineare Kurve')

# Markiere die Punkte
plt.scatter(points[:, 0], points[:, 1], color='red', label='Datenpunkte')

# Titel und Achsenbeschriftungen
plt.title('Stückweise lineare Kurve')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.show()
