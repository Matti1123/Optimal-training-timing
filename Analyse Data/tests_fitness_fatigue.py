import numpy as np
import matplotlib.pyplot as plt

# Parameter
p_star = 100  # Basisleistungsniveau
k1 = 30     # Gewichtung für Fitness
k2 = 40      # Gewichtung für Müdigkeit (größer, um Ermüdung stärker zu gewichten)
tau1 = 40.0   # Zeitkonstante für Fitness (längere Erholung)
tau2 = 10.0   # Zeitkonstante für Müdigkeit (schneller Abbau)

n = np.arange(0, 50)
#w = np.random.randint(0, 2, 50)
w = np.zeros(50)
w[0] = 1
w[20] = 1
#print(w)
y1_fitness = k1 * np.array([sum(w[i] * np.exp(-(n_j-i)/tau1) for i in range(n_j)) for n_j in n])
y2_fatigue = k2 * np.array([sum(w[i] * np.exp(-(n_j-i)/tau2) for i in range(n_j)) for n_j in n])
y3_performance = p_star + y1_fitness - y2_fatigue

plt.plot(n, p_star+y1_fitness, label="Fitness (F)", color="blue", linestyle="--")
plt.plot(n, p_star-y2_fatigue, label="Müdigkeit (M)", color="red", linestyle="--")
plt.plot(n, y3_performance, label="Performance (p_n)", color="green", linewidth=2)
plt.plot(n, p_star +y1_fitness -y1_fitness, label="Baseline", color="yellow", linestyle="--")
plt.xlabel("Tage")
plt.ylabel("Wert")
plt.legend()
plt.savefig("C:\\Users\\flets\\OneDrive\\Documents\\Semester_3\\Optimal_training_timing\\Analyse Data\\graph1.jpg")
plt.show()
