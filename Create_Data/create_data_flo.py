import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import pandas as pd

# Datenpunkte
data = np.array([[0, 1], [5, 0.8], [16, 0.6], [30, 0.7], [40, 0.8], [50, 0.9], [60, 1.0],
                 [66, 1.03], [72, 1.04], [77, 1.03], [82, 1.02], [110, 1.005], [140, 1]])
x_data, y_data = data[:, 0], data[:, 1]

# Spline-Interpolation für eine glatte Kurve
x_smooth = np.linspace(x_data.min(), x_data.max(), 500)  # Glatte Werte für x
spline = make_interp_spline(x_data, y_data, k=2) 
y_smooth = spline(x_smooth)

# Plot erstellen
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth, label="Interpolierte Kurve", color="blue")
plt.scatter(x_data, y_data, color="red", label="Datenpunkte")
plt.axhline(y=1, color='gray', linestyle='--', label="Ursprungsniveau")
plt.title("Superkompensationskurve")
plt.xlabel("Zeit")
plt.ylabel("Leistung")
plt.legend()
plt.grid(True)
plt.show()

# Leistung zu jedem Zeitpunkt in % berechnen und in einer Tabelle speichern

performance_percent = y_smooth *100  # Leistung in Prozent

# Ergebnisse in einer Tabelle speichern
results = pd.DataFrame({'Zeit[h]': x_smooth, 'Leistung[%]': performance_percent})
print(results)
results.to_csv('Data_Set\DatenAusInterpolatedPoints.csv', index=False)



# Zufällige Punkte zwischen 0 und 140 generieren
random_points = np.sort(np.random.uniform(0, 140, 10))

# Entsprechende y-Werte aus y_smooth finden
corresponding_y_values = np.interp(random_points, x_smooth, y_smooth)

# Ergebnisse anzeigen
for x, y in zip(random_points, corresponding_y_values):
    print(f"Zeit: {x:.2f}, Leistung: {y:.4f}")

'''
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


'''
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
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