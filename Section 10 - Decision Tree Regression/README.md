# Decision Tree Regression

* `Decision Tree Regression` is a supervised learning algorithm used for regression tasks. Unlike its counterpart, Decision Tree Classification, which *predicts class labels*, Decision Tree Regression *predicts continuous output values by partitioning the input space into regions* and *assigning a constant value (typically the mean or median) to each region*.

* Here are some key points about Decision Tree Regression:
    1. <b><i>Tree structure:</b></i> Decision Tree Regression builds a tree-like model where each internal node represents a decision based on a feature, and each leaf node represents the predicted output value. The tree is constructed by recursively splitting the data based on features to minimize the variance or the mean squared error of the target variable.

    2. <b><i>Splitting criteria:</b></i> The algorithm uses different splitting criteria, such as Mean Squared Error (MSE) or Mean Absolute Error (MAE), to determine the best feature and value to split the data at each node.

    3. <b><i>Greedy algorithm:</b></i> Decision Tree Regression uses a greedy approach to build the tree. At each step, it chooses the best feature and value to split the data, without considering future implications. This can sometimes lead to suboptimal trees.

    4. <b><i>Overfitting:</b></i> Decision trees are prone to overfitting, especially when the tree becomes deep and complex. Overfitting occurs when the tree captures noise and outliers in the training data, leading to poor generalization on unseen data.

    5. <b><i>Pruning:</b></i> To combat overfitting, pruning techniques can be applied. Pruning involves removing branches from the tree that do not contribute significantly to reducing the error on the validation data. This results in a more generalized model.

    6. <b><i>Interpretability:</b></i> Decision trees are highly interpretable models, as their decisions can be easily visualized and understood. Each path from the root to a leaf represents a decision rule.

    7. <b><i>Handling non-linear relationships:</b></i> Decision trees can model non-linear relationships between features and the target variable effectively. By recursively splitting the data, they can approximate complex relationships in the data.

    8. <b><i>Ensemble methods:</b></i> To improve performance and robustness, ensemble methods like Random Forest and Gradient Boosting can be used with decision trees. These methods combine multiple decision trees to make more accurate predictions and reduce overfitting.

    9. <b><i>Missing values:</b></i> Decision Tree Regression can handle missing values in the data without the need for imputation. It can make use of the available features to make predictions even when some values are missing.

    10. <b><i>Feature scaling:</b></i> Decision Tree Regression is not sensitive to the scale of features, making it unnecessary to perform feature scaling before training the model.

    11. <b><i>Evaluation:</b></i> Common evaluation metrics for Decision Tree Regression include Mean Squared Error (MSE), Mean Absolute Error (MAE), R-squared (R2), and others, depending on the specific problem and requirements.

* Decision Tree Regression is a versatile algorithm that can be used for both simple and complex regression tasks. However, careful tuning and pruning are essential to prevent overfitting and improve the model's performance.
<hr>

`Good`
- Can solve non-linear problems.
- Can work on high-dimensional data with excellent accuracy.
- Easy to visualize and explain.

`Bad`
- Overfitting. Might be resolved by random forest.
- A small change in the data can lead to a large change in the structure of the optimal decision tree.
- Calculations can get very complex.
<hr>