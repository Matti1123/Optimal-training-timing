
import numpy as np
import matplotlib.pyplot as plt

# Zeitspanne definieren
time = np.linspace(0, 10, 500)  # 0 bis 10 Einheiten Zeit
baseline = 1  # Ausgangslevel der Leistungsfähigkeit

# Weitere Anpassung für das zweite Hoch
dip = -0.8 * np.exp(-0.5 * (time - 2)**2)  # Tieferer Leistungseinbruch
recovery = 0.25 * np.exp(-0.1 * (time - 5)**2)  # Erholung bis maximal 1.05
performance = baseline + dip + recovery  # Gesamtleistung

# Angepasste Kurve plotten
plt.figure(figsize=(10, 6))
plt.plot(time, performance, label="Leistung", color="blue")
plt.axhline(y=baseline, color='gray', linestyle='--', label="Baseline (Ausgangsleistung)")
plt.axvline(x=2, color='red', linestyle='--', label="Training")
plt.axvline(x=5, color='green', linestyle='--', label="Superkompensation")

# Diagramm anpassen
plt.title("Weiter angepasste Superkompensationskurve")
plt.xlabel("Zeit")
plt.ylabel("Leistung")
plt.legend()
plt.grid(True)
plt.show()

'''
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

# Zielpunkte
x_data = np.array([0, 12, 72])
y_data = np.array([1, 0.6, 1.04])

# Modifizierte Exponentialfunktion
def target_function(x, a, b, c, d, e, f):
    return a + (b - a) * np.exp(-c * x) + d * np.exp(-e * (x - f)**2)

# Asymptotischer Wert (a)
a = 0.95

# Curve fitting
initial_guess = [a, 1.0, 0.01, 0.1, 0.01, 50]  # Grobe Startwerte
params, _ = curve_fit(target_function, x_data, y_data, p0=initial_guess)

# Extrahierte Parameter
a_fit, b_fit, c_fit, d_fit, e_fit, f_fit = params

# Werte anzeigen
print(f"Fitted parameters: a={a_fit}, b={b_fit}, c={c_fit}, d={d_fit}, e={e_fit}, f={f_fit}")

# Kurve generieren
x_fit = np.linspace(0, 100, 500)
y_fit = target_function(x_fit, a_fit, b_fit, c_fit, d_fit, e_fit, f_fit)

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x_fit, y_fit, label="Modell", color="blue")
plt.scatter(x_data, y_data, label="Daten", color="red")
plt.title("Angepasste Superkompensationskurve")
plt.xlabel("Zeit")
plt.ylabel("Leistung")
plt.legend()
plt.grid(True)
plt.show()
'''