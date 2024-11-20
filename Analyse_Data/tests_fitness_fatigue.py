import numpy as np
import matplotlib.pyplot as plt

# Parameter
p_star = 80  # Basisleistungsniveau
k1 = 1       # Gewichtung für Fitness
k2 = 2       # Gewichtung für Müdigkeit (größer, um Ermüdung stärker zu gewichten)
tau1 = 42  # Zeitkonstante für Fitness (längere Erholung)
tau2 = 7     # Zeitkonstante für Müdigkeit (schneller Abbau)

<<<<<<< HEAD
n = np.arange(0, 30)
w = np.zeros(30)  # Trainingseinheiten
w[0] = 1
<<<<<<< HEAD
w[48] = 1
w[96] = 1
w[150] = 1
w[190] = 1
=======
w[3] = 1
w[6] = 1
w[12] = 1
w[15] = 0.8
>>>>>>> 500ad79a130f97d55deb74ed2e0d648ddc6e73fb
=======

n = np.arange(0, 100)
w = np.zeros(100)  # Trainingseinheiten
# hier eine liste die die bei null startet mit 100 elementen und immer zeitabstände von 1-14 tagen hat
# Trainingseinheiten

def generate_training_schedule(intervals, length=100):
    w = np.zeros(length)
    for interval in intervals:
        for i in range(interval, length, interval):
            w[i] = 1
    return w

# Beispiel: Trainingseinheiten alle 10 Tage
intervals = [np.random.randint(1, 15)]
w = generate_training_schedule(intervals)
>>>>>>> 7b073da05bf95cdb7f9e8427e827f36fb3dea8de

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
"""plt.scatter(max_index, max_value, color="purple", label=f"Max. Leistung (p_n) bei Tag {max_index}: {max_value:.2f}")
print(max_index, max_value + 2, f"({max_index}, {max_value:.2f})")"""

# Diagrammbeschriftung
plt.xlabel("Zeit in Tagen")
plt.ylabel("Leistung")
plt.title("Fatigue-Fitness-Modell: Nettoleistung, Fitness und Müdigkeit")
#plt.savefig("Analyse_Data\tests_fitness_fatigue.py")
plt.legend()
plt.grid(True)

# Diagramm anzeigen
plt.show()

# Maximalwert ausgeben
print(f"Maximale Leistung: {max_value:.2f} bei Tag {max_index}")
