# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Generate some example data
np.random.seed(42)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (important for SVR)
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_train_scaled = scaler_X.fit_transform(X_train)
y_train_scaled = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()

X_test_scaled = scaler_X.transform(X_test)
y_test_scaled = scaler_y.transform(y_test.reshape(-1, 1)).ravel()

# Create a Support Vector Regression model
svr_model = SVR(kernel='rbf', C=1.0, epsilon=0.2)

# Train the model on the training data
svr_model.fit(X_train_scaled, y_train_scaled)

# Make predictions on the test data
y_pred_scaled = svr_model.predict(X_test_scaled)

# Transform predictions back to original scale
y_pred = scaler_y.inverse_transform(y_pred_scaled)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")

# Plot the original data and the SVR predictions
plt.scatter(X, y, label='Original Data')
plt.plot(X_test, y_pred, color='red', label='SVR Predictions')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Support Vector Regression')
plt.legend()
plt.show()