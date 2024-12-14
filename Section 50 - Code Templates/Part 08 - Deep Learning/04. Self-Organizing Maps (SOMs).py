# Install necessary libraries if not already installed
# pip install minisom

# Import necessary libraries
from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

# Generate example data (replace this with your own dataset)
np.random.seed(42)
data = np.random.random((100, 10))  # 100 samples with 10 features each

# Normalize the data
data = (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))

# Define SOM parameters
som_size = (10, 10)  # Size of the SOM grid
input_len = data.shape[1]  # Number of features in the input data
sigma = 1.0  # Initial spread of the neighborhood function
learning_rate = 0.5  # Initial learning rate

# Create and train the Self-Organizing Map
som = MiniSom(som_size[0], som_size[1], input_len, sigma=sigma, learning_rate=learning_rate)
som.random_weights_init(data)
som.train_random(data, 1000)  # Adjust the number of epochs as needed

# Visualize the SOM
plt.figure(figsize=(8, 8))
plt.pcolor(som.distance_map().T, cmap='bone_r')  # Distance map as background
plt.colorbar()

# Mark the position of the neurons in the SOM grid
for i, j in np.ndindex(som_size):
    plt.text(i + 0.5, j + 0.5, f'{i},{j}', color='black', ha='center', va='center')

# Mark the position of data points on the map
for d in data:
    winner = som.winner(d)
    plt.plot(winner[0] + 0.5, winner[1] + 0.5, 'o', markerfacecolor='None', markeredgecolor='r', markersize=10, markeredgewidth=2)

plt.title('Self-Organizing Map')
plt.show()