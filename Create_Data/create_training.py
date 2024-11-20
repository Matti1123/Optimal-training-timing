import pandas as pd
import random

# Original CSV laden
df = pd.read_csv('Data_Set\DatenAusInterpolatedPoints.csv')

# Die Reihe 260 (mit +/- 60) extrahieren
base_row = 260
min_row = max(0, base_row - 60)
max_row = min(len(df), base_row + 60)

# Initialer Wert für die neue CSV
new_data = []
new_data.append([0, 80])  # Beginn bei 0h und 80kg

# Zufällige Auswahl von Trainingsdaten für die nächsten Stunden
for i in range(1, 100):  # Hier definierst du die Anzahl der Zeilen (z.B. 100 Zeilen)
    random_row = random.randint(min_row, max_row)
    training_time = df.iloc[random_row]['Trainingszeit']  # Angenommen, die Zeit ist in der Spalte 'Trainingszeit'
    performance = df.iloc[random_row]['Leistung']  # Angenommen, die Leistung ist in der Spalte 'Leistung'
    
    # Berechnung des Gewichtfaktors
    factor = performance / 100
    
    # Berechnung des neuen Gewichts
    prev_weight = new_data[-1][1]
    new_weight = prev_weight * factor
    
    # Neue Zeile hinzufügen
    new_data.append([training_time, new_weight])

# Neue CSV erstellen
new_df = pd.DataFrame(new_data, columns=['Trainingszeit', 'Gewicht'])
new_df.to_csv('training_ip.csv', index=False)

print("Neue CSV 'training_ip.csv' wurde erstellt.")
