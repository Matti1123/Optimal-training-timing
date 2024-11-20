import pandas as pd

import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data_Set\DatenAusInterpolatedPoints.csv')

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['Zeit[h]'], data['Leistung[%]'], marker='o', linestyle='-')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Data from DatenAusInterpolatedPoints')
plt.grid(True)
plt.show()

