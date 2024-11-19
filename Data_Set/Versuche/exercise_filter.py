import pandas as pd

def filter_exercises(file_path, exercise_name):
    """
    Filtert eine CSV-Datei nach einem bestimmten Übungsnamen und gibt Datum, Übung und Gewicht zurück.

    :param file_path: Pfad zur CSV-Datei
    :param exercise_name: Name der Übung, nach der gefiltert werden soll
    :return: Gefilterte DataFrame mit Datum, Übung und Gewicht
    """
    try:
        # CSV-Datei laden
        data = pd.read_csv(file_path)
        
        # Filtern nach dem Übungsnamen (case-insensitive)
        filtered_data = data[data['Exercise Name'].str.contains(exercise_name, case=False, na=False)]
        
        # Nur relevante Spalten behalten (Datum, Übung, Gewicht)
        result = filtered_data[['Date', 'Exercise Name', 'Weight']].reset_index(drop=True)
        
        return result
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None

# Aufruf
result = filter_exercises("Versuche\weightlifting_721_workouts.csv", "Lat Pulldown")
print(result)

result.to_csv("Data_Set/filtered_exercises.csv", index=False)
