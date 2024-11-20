import numpy as np
import matplotlib.pyplot as plt

# Parameter für das Fitness-Fatigue-Modell
P0 = 1.0  # Ausgangsleistung
k1 = 0.9  # Gewicht für Fitness
k2 = 1.2  # Gewicht für Fatigue
tau_F = 42  # Zeitkonstante für Fitness (in Tagen)
tau_D = 7   # Zeitkonstante für Fatigue (in Tagen)

# Trainingsbelastung (Beispieldaten: [Tag, Belastung])
training_sessions = np.array([
    [0, 1.0],
    [5, 0.8],
    [10, 1.2],
    [15, 1.0],
    [20, 1.5],
])

# Zeitachse (in Tagen)
t = np.linspace(0, 50, 500)  # Von Tag 0 bis 50

# Fitness- und Fatigue-Funktionen
def fitness_effect(t, sessions, tau_F):
    return np.sum([T * np.exp(-(t - t_i) / tau_F) * (t >= t_i) for t_i, T in sessions], axis=0)

def fatigue_effect(t, sessions, tau_D):
    return np.sum([T * np.exp(-(t - t_i) / tau_D) * (t >= t_i) for t_i, T in sessions], axis=0)

# Fitness und Fatigue berechnen
F_t = fitness_effect(t, training_sessions, tau_F)
D_t = fatigue_effect(t, training_sessions, tau_D)

# Leistung berechnen
P_t = P0 + k1 * F_t - k2 * D_t

# Plot erstellen
plt.figure(figsize=(12, 6))
plt.plot(t, P_t, label="Leistung (P(t))", color="blue", linewidth=2)
plt.plot(t, F_t, label="Fitness (F(t))", color="green", linestyle="--")
plt.plot(t, D_t, label="Fatigue (D(t))", color="red", linestyle="--")

# Trainingstage markieren
for t_i, T in training_sessions:
    plt.axvline(x=t_i, color="gray", linestyle=":", alpha=0.7)

plt.title("Fitness-Fatigue-Modell")
plt.xlabel("Zeit (Tage)")
plt.ylabel("Leistung")
plt.legend()
plt.grid(True)
plt.show()
