import pandas as pd
import random

# Original CSV laden
df = pd.read_csv('Data_Set\DatenAusInterpolatedPoints.csv')

# Die Reihe 260 (mit +/- 90) extrahieren
base_row = 260
min_row = max(0, base_row - 90)
max_row = min(len(df), base_row + 90)

# Initialer Wert für die neue CSV
new_data = []
new_data.append([0, 80])  # Beginn bei 0h und 80kg
training_timeadded = 0

# Zufällige Auswahl von Trainingsdaten für die nächsten Stunden
for i in range(1, 100):  # Anzahl der Zeilen
    random_row = random.randint(min_row, max_row)
    training_time = df.iloc[random_row]['Zeit[h]']  
    performance = df.iloc[random_row]['Leistung[%]'] 
    
    # Berechnung des Gewichtfaktors
    factor = performance / 100
    
    # Berechnung des neuen Gewichts
    prev_weight = new_data[-1][1]
    new_weight = prev_weight * factor
    training_timeadded = training_timeadded + training_time 
    
    # Neue Zeile hinzufügen
    new_data.append([training_timeadded, new_weight])

# Neue CSV erstellen
new_df = pd.DataFrame(new_data, columns=['Trainingszeit', 'Gewicht'])
new_df.to_csv('Data_Set/training_ip.csv', index=False)

print("Neue CSV 'training_ip.csv' wurde erstellt.")
