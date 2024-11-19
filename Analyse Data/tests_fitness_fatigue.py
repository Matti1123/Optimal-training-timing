import numpy as np
import matplotlib.pyplot as plt

# Parameter
p_star = 100  # Basisleistungsniveau
k1 = 1.0      # Gewichtung für Fitness
k2 = 1.5      # Gewichtung für Müdigkeit (größer, um Ermüdung stärker zu gewichten)
tau1 = 40.0   # Zeitkonstante für Fitness (längere Erholung)
tau2 = 10.0   # Zeitkonstante für Müdigkeit (schneller Abbau)

n = np.arange(1, 50 + 1)
w = np.random.randint(0, 2, 50)
print(w)

y1_fitness = k1 * np.array([sum(w[i] * np.exp(-(n_j-i)/tau1) for i in range(len(w))) for n_j in n])
y2_fatigue = k2 * np.array([sum(w[i] * np.exp(-(n_j-i)/tau2) for i in range(len(w))) for n_j in n])
y3_performance = p_star + y1_fitness - y2_fatigue

plt.plot(n, y1_fitness, label="Fitness (F)", color="blue", linestyle="--")
plt.plot(n, y2_fatigue, label="Müdigkeit (M)", color="red", linestyle="--")
plt.plot(n, y3_performance, label="Nettoleistung (p_n)", color="green", linewidth=2)
plt.xlabel("Tage")
plt.ylabel("Wert")
plt.legend()
plt.show()