import pandas as pd
import random
from datetime import datetime, timedelta

# Start- und Enddatum festlegen (letzte zwei Jahre)
start_date = datetime.now() - timedelta(days=2*365)
end_date = datetime.now()

# Parameter für die Gewichtsdaten
min_weight = 60  # Startgewicht in kg
target_weight = 140  # Zielgewicht am Ende
total_entries = 400  # Anzahl der Einträge
frequency_per_week = random.choice([2, 3])  # 2-3 Mal pro Woche

# Liste zur Speicherung der Daten
data = []

# Berechnung des linearen Gewichtsanstiegs pro Eintrag
linear_increase = (target_weight - min_weight) / total_entries

# Generierung der Daten
current_date = start_date
current_weight = min_weight
for i in range(total_entries):
    # Leichte Schwankungen um den linearen Anstieg
    weight_change = linear_increase + random.uniform(-0.5, 0.5)
    current_weight = current_weight + weight_change
    
    # Kontrollieren, dass das Gewicht nicht vorzeitig zu hoch wird
    if i < total_entries - 20 and current_weight > target_weight - 2:
        current_weight = target_weight - 2
    
    # Zufällige Uhrzeit generieren (zwischen 6:00 und 20:00 Uhr)
    training_hour = random.randint(6, 20)
    training_minute = random.choice([0, 15, 30, 45])  # Viertelstunden
    training_time = f"{training_hour:02d}:{training_minute:02d}"
    
    # Eintrag hinzufügen
    data.append({
        "Date": current_date.strftime("%Y-%m-%d"),
        "Time": training_time,
        "Exercise Name": "Squats",
        "Weight": round(current_weight, 1)  # Gewicht auf eine Dezimalstelle runden
    })
    
    # Zum nächsten Datum springen (2-3 Mal pro Woche)
    days_to_add = random.choice([2, 3, 4])
    current_date += timedelta(days=days_to_add)
    
    # Ende des Datumsbereichs prüfen
    if current_date > end_date:
        break

# Sicherstellen, dass der letzte Wert genau das Zielgewicht erreicht
data[-1]["Weight"] = target_weight

# DataFrame erstellen
df = pd.DataFrame(data)

# DataFrame als CSV speichern
file_path = "squat_progress_steady_increase.csv"
df.to_csv(file_path, index=False)

print(f"Die Datei mit {len(df)} Einträgen wurde unter {file_path} gespeichert!")
