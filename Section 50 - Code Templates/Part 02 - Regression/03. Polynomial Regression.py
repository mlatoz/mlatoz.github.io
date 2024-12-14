# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate some example data
np.random.seed(42)
X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply polynomial features transformation
degree = 2  # Set the degree of the polynomial
poly_features = PolynomialFeatures(degree=degree, include_bias=False)
X_poly_train = poly_features.fit_transform(X_train)
X_poly_test = poly_features.transform(X_test)

# Create a Polynomial Regression model
poly_model = LinearRegression()

# Train the model on the polynomial features
poly_model.fit(X_poly_train, y_train)

# Make predictions on the test data
y_poly_pred = poly_model.predict(X_poly_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_poly_pred)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")

# Plot the original data and the polynomial regression curve
plt.scatter(X, y, label='Original Data')
X_plot = np.linspace(-3, 3, 100).reshape(-1, 1)
X_plot_poly = poly_features.transform(X_plot)
y_plot = poly_model.predict(X_plot_poly)
plt.plot(X_plot, y_plot, color='red', label=f'Polynomial Regression (Degree {degree})')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Polynomial Regression')
plt.legend()
plt.show()