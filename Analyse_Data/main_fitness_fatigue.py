import numpy as np
import matplotlib.pyplot as plt

from fitness_fatigue import fitness_fatigue

def populate_training_entries_random(w, max_ones=100, max_step=24, min_step=1,train_gain=0.05):
    index = 0
    count = 0
    while count < max_ones and index < len(w):
        w[index] = 1   # Setze eine 1 an der aktuellen Position
        count += 1
        step = np.random.randint(min_step, max_step) if max_step > min_step else min_step  # Zufälliger Abstand zwischen 1 und 28
        index += step  # Bewege den Index um den zufälligen Schritt weiter
    return w

# Trainingseinheiten-Liste erstellen
w1 = np.zeros(750)

# call function
w1 = populate_training_entries_random(w1, max_ones=100, max_step=20, min_step=20)
w2 = np.zeros(750)

# call function
w2 = populate_training_entries_random(w2, max_ones=100, max_step=40, min_step=40)
w = np.concatenate((w1, w2), axis=0)


# w = np.zeros(100)
# w[0] = 1
p_star = 100
n = np.arange(len(w))


fitness,fatigue,performance = fitness_fatigue(p_star = p_star,w = w)


# Plot der Ergebnisse
plt.plot(n, p_star + fitness, label="Fitness (F)", color="blue", linestyle="--")
plt.plot(n, p_star - fatigue, label="Müdigkeit (M)", color="red", linestyle="--")
plt.plot(n, performance, label="Performance (p_n)", color="green", linewidth=2)
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
