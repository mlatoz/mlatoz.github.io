# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load a sample dataset for binary classification (you can replace this with your own dataset)
# Example: X, y = load_your_dataset()
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier
decision_tree_model = DecisionTreeClassifier(max_depth=3)  # You can adjust the max_depth parameter

# Train the model on the training data
decision_tree_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = decision_tree_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(classification_rep)

# Plot the decision tree for visualization (requires 'graphviz' and 'pydotplus' libraries)
# Uncomment the following lines if you have these libraries installed
# from sklearn.tree import export_graphviz
# import graphviz
# dot_data = export_graphviz(decision_tree_model, out_file=None, feature_names=iris.feature_names,
#                            class_names=iris.target_names, filled=True, rounded=True, special_characters=True)
# graph = graphviz.Source(dot_data)
# graph.render("iris_decision_tree", view=True)