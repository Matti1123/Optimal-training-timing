import matplotlib.pyplot as plt
import numpy as np

# Zeitspanne definieren
time = np.linspace(0, 10, 500)  # 0 bis 10 Einheiten Zeit
baseline = 1  # Ausgangslevel der Leistungsfähigkeit

# Superkompensationsverlauf modellieren
performance = np.piecewise(
    time,
    [time < 2, (time >= 2) & (time <= 5), time > 5],
    [lambda t: baseline - 0.5 * (t - 2)**2,  # Abfall während der Belastung (Parabel)
     lambda t: baseline - 0.2 * (t - 2)**2,  # Erholung zurück zum Ausgangsniveau
     lambda t: baseline + 0.3 * (t - 5) - 0.1 * (t - 5)**2]  # Superkompensation
)

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(time, performance, label="Leistungsfähigkeit", color="blue", linewidth=2)
plt.axhline(y=baseline, color="gray", linestyle="--", label="Baseline (Ausgangsniveau)")

# Markierungen für Schlüsselphasen
plt.axvline(x=2, color="red", linestyle="--", label="Trainingszeitpunkt")
plt.axvline(x=5, color="green", linestyle="--", label="Optimaler Trainingszeitpunkt")

# Beschriftungen
plt.title("Superkompensation: Verlauf der Leistungsfähigkeit", fontsize=14)
plt.xlabel("Zeit", fontsize=12)
plt.ylabel("Leistungsfähigkeit", fontsize=12)
plt.legend()
plt.grid(True)

# Diagramm anzeigen
plt.show()
