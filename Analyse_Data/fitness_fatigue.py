import numpy as np
def fitness_fatigue(p_star:float = 100,k1:float = 1,k2:float = 2,tau1:float = 42,tau2:float=7,w:np.array = np.zeros(100))->tuple[np.array]:
    """
    Berechnet die Fitness, Müdigkeit und Performance eines Athleten
    Args:
        p_star (float): Basisleistungsniveau
        k1 (float): Gewichtung für Fitness
        k2 (float): Gewichtung für Müdigkeit
        tau1 (float): Zeitkonstante für Fitness
        tau2 (float): Zeitkonstante für Müdigkeit
        w (np.array): Belastungsvektor
    Returns:
        y1_fitness (np.array): Fitness
        y2_fatigue (np.array): Müdigkeit
        y3_performance (np.array): Performance
        """
    n = np.arange(len(w))

    # Fitness, Müdigkeit und Performance berechnen
    y1_fitness = k1 * np.array([sum(w[i] * np.exp(-(n_j - i) / tau1) for i in range(n_j)) for n_j in n])
    y2_fatigue = k2 * np.array([sum(w[i] * np.exp(-(n_j - i) / tau2) for i in range(n_j)) for n_j in n])
    y3_performance = p_star + y1_fitness - y2_fatigue

    return y1_fitness,y2_fatigue,y3_performance


# max_index = np.argmax(y3_performance)  # Index des Maximums
# max_value = y3_performance[max_index]  # Maximalwert
# # Plot der Ergebnisse
# plt.plot(n, p_star + y1_fitness, label="Fitness (F)", color="blue", linestyle="--")
# plt.plot(n, p_star - y2_fatigue, label="Müdigkeit (M)", color="red", linestyle="--")
# plt.plot(n, y3_performance, label="Performance (p_n)", color="green", linewidth=2)
# plt.axhline(p_star, label="Baseline (p*)", color="yellow", linestyle="--")

# # Markierung des Maximums
# """plt.scatter(max_index, max_value, color="purple", label=f"Max. Leistung (p_n) bei Tag {max_index}: {max_value:.2f}")
# print(max_index, max_value + 2, f"({max_index}, {max_value:.2f})")"""

# # Diagrammbeschriftung
# plt.xlabel("Zeit in Tagen")
# plt.ylabel("Leistung")
# plt.title("Fatigue-Fitness-Modell: Nettoleistung, Fitness und Müdigkeit")
# #plt.savefig("Analyse_Data\tests_fitness_fatigue.py")
# plt.legend()
# plt.grid(True)

# # Diagramm anzeigen
# plt.show()

# # Maximalwert ausgeben
# print(f"Maximale Leistung: {max_value:.2f} bei Tag {max_index}")
