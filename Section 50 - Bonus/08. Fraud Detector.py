# https://chat.openai.com/share/f6b956da-fadf-40d3-88e8-91e71c9bbda9

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc, roc_curve, classification_report

# Load your dataset here, and make sure it has a 'Class' column indicating fraud (1) or non-fraud (0)

# Preprocessing: Standardize the features
scaler = StandardScaler()
data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
data['Time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))

# Split the data into train and test sets
X_train, X_test = train_test_split(data, test_size=0.2, random_state=42)

# Define the autoencoder model
input_dim = X_train.shape[1]

model = keras.Sequential([
    keras.layers.Input(shape=(input_dim,)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(input_dim, activation='sigmoid')
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the autoencoder
model.fit(X_train, X_train, epochs=50, batch_size=256, shuffle=True, validation_data=(X_test, X_test))

# Use the trained autoencoder for prediction
X_pred = model.predict(X_test)

# Calculate the reconstruction error (MSE) for each sample
mse = np.mean(np.power(X_test - X_pred, 2), axis=1)

# Set a threshold for anomaly detection (you can fine-tune this)
threshold = 2.5

# Classify data points as normal (0) or anomaly (1) based on the threshold
y_pred = [1 if error > threshold else 0 for error in mse]

# Evaluate the model's performance
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Plot precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_test, mse)
auc_score = auc(recall, precision)

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.plot(recall, precision, 'b', label='AUC = %0.2f' % auc_score)
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='lower right')
plt.show()