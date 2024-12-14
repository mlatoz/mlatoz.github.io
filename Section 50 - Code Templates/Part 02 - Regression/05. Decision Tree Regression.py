# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some example data
np.random.seed(42)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Regression model
dt_model = DecisionTreeRegressor(max_depth=3)  # You can adjust the max_depth parameter

# Train the model on the training data
dt_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = dt_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")

# Plot the original data and the Decision Tree predictions
plt.scatter(X, y, label='Original Data')
X_plot = np.linspace(0, 5, 100).reshape(-1, 1)
y_plot = dt_model.predict(X_plot)
plt.plot(X_plot, y_plot, color='red', label='Decision Tree Predictions')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Decision Tree Regression')
plt.legend()
plt.show()