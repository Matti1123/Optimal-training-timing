import pandas as pd

import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data_Set/training_ip.csv')

# Plot the data
plt.figure(figsize=(10, 6))
for column in data.columns[1:]:  # Assuming the first column is an index or non-numeric
    plt.plot(data.iloc[:, 0], data[column], label=column)

plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Training Data Plot')
plt.legend()
plt.grid(True)
plt.show()
'Data_Set/training_ip.png'
plt.savefig('Data_Set/training_ip.png')