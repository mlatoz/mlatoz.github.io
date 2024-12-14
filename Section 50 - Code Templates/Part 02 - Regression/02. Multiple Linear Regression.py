# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load your dataset (replace 'your_dataset.csv' with your actual file)
# Example: df = pd.read_csv('your_dataset.csv')
# Ensure that your dataset includes multiple independent variables (features) and the target variable (dependent variable).

# For demonstration, let's generate a synthetic dataset:
np.random.seed(42)
X = 2 * np.random.rand(100, 3)  # 3 features
y = 4 + 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Multiple Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")

# Print the coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Note: Make sure to replace the column names and dataset with your own data.

# You can also perform feature scaling, feature engineering, or other preprocessing steps based on your dataset.