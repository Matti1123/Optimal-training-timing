import numpy as np
import matplotlib.pyplot as plt

# Parameter
p_star = 100  # Basisleistungsniveau
k1 = 1.0      # Gewichtung für Fitness
k2 = 1.5      # Gewichtung für Müdigkeit (größer, um Ermüdung stärker zu gewichten)
tau1 = 40.0   # Zeitkonstante für Fitness (längere Erholung)
tau2 = 10.0   # Zeitkonstante für Müdigkeit (schneller Abbau)

# Trainingsdaten: Zeitpunkt und Intensität
training_days = [1, 3, 7, 13, 16, 21, 24, 27, 32, 37, 40]  # Regelmäßige Trainingseinheiten
training_intensity = [1.0, 1.2, 0.8, 1.1, 0.9, 1.3, 1.0, 1.2, 0.9, 1.1, 1.0]  # Angepasste Intensität

# Simulationstage
n_days = 50
days = np.arange(1, n_days + 1)

# Nettoleistung berechnen
def calculate_performance(p_star, k1, k2, tau1, tau2, training_days, training_intensity, days):
    performance = np.zeros(len(days))
    fitness = np.zeros(len(days))
    fatigue = np.zeros(len(days))
    
    for n in range(len(days)):
        fitness[n] = sum(
            k1 * w_i * np.exp(-(n - (i - 1)) / tau1) if n >= (i - 1) else 0
            for i, w_i in zip(training_days, training_intensity)
        )
        fatigue[n] = sum(
            k2 * w_i * np.exp(-(n - (i - 1)) / tau2) if n >= (i - 1) else 0
            for i, w_i in zip(training_days, training_intensity)
        )
        performance[n] = p_star + fitness[n] - fatigue[n]
    return performance, fitness, fatigue

# Berechnen der Leistung, Fitness und Müdigkeit
performance, fitness, fatigue = calculate_performance(
    p_star, k1, k2, tau1, tau2, training_days, training_intensity, days
)

# Plot der Ergebnisse
plt.figure(figsize=(12, 6))
plt.plot(days, performance, label="Nettoleistung (p_n)", color="green", linewidth=2)
plt.plot(days, fitness, label="Fitness (F)", color="blue", linestyle="--")
plt.plot(days, fatigue, label="Müdigkeit (M)", color="red", linestyle="--")
plt.scatter(training_days, [p_star] * len(training_days), color="black", label="Trainingseinheiten", zorder=5)
plt.axhline(p_star, color="gray", linestyle="--", linewidth=0.8, label="Basisleistungsniveau (p*)")

# Diagramm beschriften
plt.title("Fatigue-Fitness-Modell: Nettoleistung, Fitness und Müdigkeit", fontsize=16)
plt.xlabel("Tage", fontsize=14)
plt.ylabel("Wert", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()

# Plot anzeigen
plt.show()
