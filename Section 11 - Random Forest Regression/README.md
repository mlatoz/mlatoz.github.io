# Random Forest Regression

* Random Forest Regression is an ensemble learning method based on Decision Trees. It is used for regression tasks, where the goal is to predict continuous output values based on input features. Random Forest Regression builds multiple decision trees and combines their predictions to improve accuracy and reduce overfitting.

* Here are some key points about Random Forest Regression:
    1. <b><i>Ensemble method:</i></b> Random Forest Regression is an ensemble learning technique that combines the predictions of multiple decision trees. Each decision tree is trained on a different subset of the data and features.

    2. <b><i>Bagging:</i></b> The ensemble is created using a process called bagging (Bootstrap Aggregating). Bagging involves sampling the data with replacement to create multiple subsets (bootstrap samples). Each decision tree is trained on one of these bootstrap samples.

    3. <b><i>Random feature selection:</i></b> In addition to sampling the data, Random Forest Regression also randomly selects a subset of features at each node during the construction of each decision tree. This introduces further diversity among the trees and helps in reducing correlation.

    4. <b><i>Prediction aggregation:</i></b> When making predictions, each decision tree in the forest provides a prediction, and the final output is obtained by aggregating these predictions, typically using the mean (for regression tasks) of all the tree outputs.

    5. <b><i>Handling overfitting:</i></b> Random Forest Regression is less prone to overfitting compared to single decision trees. The ensemble nature of Random Forest helps in capturing the underlying patterns in the data while reducing the impact of noisy data and outliers.

    6. <b><i>Robustness:</i></b> Random Forest Regression is more robust to outliers and noise in the data due to the aggregation of predictions from multiple trees. Outliers are less likely to have a significant impact on the final prediction.

    7. <b><i>Feature importance:</i></b> Random Forest provides a measure of feature importance, which indicates the extent to which each feature contributes to the prediction. This information can be helpful in feature selection and understanding the data.

    8. <b><i>Parallelization:</i></b> The training and prediction processes in Random Forest can be parallelized easily, allowing for efficient processing of large datasets.

    9. <b><i>Hyperparameters:</i></b> Random Forest has hyperparameters that need to be tuned for optimal performance, such as the number of trees in the forest, the maximum depth of each tree, and the number of features to consider for each split.

    10. <b><i>Interpretability:</i></b> Although individual decision trees in the Random Forest are interpretable, the ensemble as a whole is less interpretable compared to a single decision tree.

    11. <b><i>Evaluation:</i></b> Common evaluation metrics for Random Forest Regression include Mean Squared Error (MSE), Mean Absolute Error (MAE), R-squared (R2), and others, depending on the specific problem and requirements.

* Random Forest Regression is a powerful and popular algorithm for regression tasks, especially when dealing with complex datasets. Its ability to handle non-linearity, feature interactions, and outliers makes it a go-to choice for many real-world regression problems. However, it may require careful tuning of hyperparameters to achieve the best performance.
<hr>

## Random Forest Intuition

**STEP 1:** Pick a random *K* data points from the Training set.

**STEP 2:** Build the Decision Tree associated to these *K* data points.

**STEP 3:** Choose the number *Ntree* of trees you want to build and repeat STEPS 1 & 2.

**STEP 4:** For a new data point, make each one of your *Ntree* trees predict the value of *Y* to for the data point in question, and assign the new data point the average across all of the predicted *Y* values.
<hr>

## Python Code Template

```python
    # Import necessary libraries
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    
    # Generate some example data
    np.random.seed(42)
    X = np.sort(5 * np.random.rand(100, 1), axis=0)
    y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create a Random Forest Regression model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)  # You can adjust the n_estimators parameter
    
    # Train the model on the training data
    rf_model.fit(X_train, y_train)
    
    # Make predictions on the test data
    y_pred = rf_model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    print(f"Root Mean Squared Error: {rmse}")
    
    # Plot the original data and the Random Forest predictions
    plt.scatter(X, y, label='Original Data')
    X_plot = np.linspace(0, 5, 100).reshape(-1, 1)
    y_plot = rf_model.predict(X_plot)
    plt.plot(X_plot, y_plot, color='red', label='Random Forest Predictions')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Random Forest Regression')
    plt.legend()
    plt.show()
```
<hr>

## Download Resources
* <a href="Python/Random Forest Regression.ipynb" download>Python Notebook</a>
* <a href="R/Random Forest Regression.r" download>Random Forest Regression | R Code</a>
* <a href="Python/Position_Salaries.csv" download>Dataset</a>
<hr>

<a href="../Section 10 - Decision Tree Regression">«Previous</a> | <a href="../Section 12 - Evaluating Regression Models Performance">Next»</a>
