# Install necessary libraries if not already installed
# pip install tensorflow

# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from sklearn.model_selection import train_test_split
import numpy as np

# Generate example data (replace this with your own dataset)
def generate_sequence(length=10):
    return [np.random.rand() for _ in range(length)]

def generate_dataset(num_samples=1000, sequence_length=10):
    X, y = [], []
    for _ in range(num_samples):
        sequence = generate_sequence(sequence_length)
        X.append(sequence[:-1])  # Input sequence
        y.append(sequence[1:])   # Output sequence (shifted by one time step)
    return np.array(X), np.array(y)

# Generate dataset
X, y = generate_dataset()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the Recurrent Neural Network (RNN) model
model = Sequential()
model.add(SimpleRNN(units=32, input_shape=(X_train.shape[1], 1), activation='relu'))
model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
loss = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss:.4f}')