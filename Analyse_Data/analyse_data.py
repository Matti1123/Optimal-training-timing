import pandas as pd

data = pd.read_csv('Data_Set/training_ip.csv')


def calculate_weight_increases(data):
    weight_increases = []
    for i in range(1, len(data)):  # Start bei 1, da vorheriger WErt benötigt word
        increase = data['Gewicht'][i] - data['Gewicht'][i - 1]
        weight_increases.append(increase)
    return weight_increases

weight_increases = calculate_weight_increases(data)
#print("Gewichtszunahmen:", weight_increases)
#print(f'Maximaler Anstieg: {max(weight_increases)} kg')

def calculate_time_between_Trainings(data):
    time_between_trainings = []
    for i in range(1, len(data)):
        time = data['Trainingszeit'][i] - data['Trainingszeit'][i - 1]
        time_between_trainings.append(time)
    return time_between_trainings

#print("Zeit zwischen Trainings:", calculate_time_between_Trainings(data))

def Zunahme_und_Zeit(data):
    combined_data = pd.DataFrame({
    'Gewichtszunahme': calculate_weight_increases(data),
    'Zeit zwischen Trainings': calculate_time_between_Trainings(data)
    })
    return combined_data
    
print(Zunahme_und_Zeit(data))

def best_moment_to_train(data):
    best_moment = data['Gewichtszunahme'].idxmax()
    time_between_trainings = data['Zeit zwischen Trainings'][best_moment]
    return time_between_trainings

print(f'Bestes Training: {best_moment_to_train(Zunahme_und_Zeit(data))} Stunden nach dem letzten Training')
