import numpy as np
import matplotlib.pyplot as plt

# Parameter
p_star = 80  # Basisleistungsniveau
k1 = 1       # Gewichtung für Fitness
k2 = 2       # Gewichtung für Müdigkeit (größer, um Ermüdung stärker zu gewichten)
tau1 = 42.0  # Zeitkonstante für Fitness (längere Erholung)
tau2 = 7     # Zeitkonstante für Müdigkeit (schneller Abbau)

n = np.arange(0, 100)
w = np.zeros(100)  # Trainingseinheiten
w[0] = 1
w[10] = 1
w[20] = 1
w[30] = 1

# Fitness, Müdigkeit und Performance berechnen
y1_fitness = k1 * np.array([sum(w[i] * np.exp(-(n_j - i) / tau1) for i in range(n_j)) for n_j in n])
y2_fatigue = k2 * np.array([sum(w[i] * np.exp(-(n_j - i) / tau2) for i in range(n_j)) for n_j in n])
y3_performance = p_star + y1_fitness - y2_fatigue

# Maximalwert der Performance und zugehöriger x-Wert
max_index = np.argmax(y3_performance)  # Index des Maximums
max_value = y3_performance[max_index]  # Maximalwert

# Plot der Ergebnisse
plt.plot(n, p_star + y1_fitness, label="Fitness (F)", color="blue", linestyle="--")
plt.plot(n, p_star - y2_fatigue, label="Müdigkeit (M)", color="red", linestyle="--")
plt.plot(n, y3_performance, label="Performance (p_n)", color="green", linewidth=2)
plt.axhline(p_star, label="Baseline (p*)", color="yellow", linestyle="--")

# Markierung des Maximums
plt.scatter(max_index, max_value, color="purple", label=f"Max. Leistung (p_n) bei Tag {max_index}: {max_value:.2f}")
plt.text(max_index, max_value + 2, f"({max_index}, {max_value:.2f})", color="purple")

# Diagrammbeschriftung
plt.xlabel("Zeit in Tagen")
plt.ylabel("Leistung")
plt.title("Fatigue-Fitness-Modell: Nettoleistung, Fitness und Müdigkeit")
#plt.savefig("\Analyse_Data")
plt.legend()
plt.grid(True)

# Diagramm anzeigen
plt.show()

# Maximalwert ausgeben
print(f"Maximale Leistung: {max_value:.2f} bei Tag {max_index}")
