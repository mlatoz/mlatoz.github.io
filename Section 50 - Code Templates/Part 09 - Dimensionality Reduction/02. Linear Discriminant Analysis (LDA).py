# Install necessary libraries if not already installed
# pip install scikit-learn matplotlib

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load example data (replace this with your own dataset)
iris = load_iris()
X = iris.data
y = iris.target

# Standardize the data
X_std = StandardScaler().fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.2, random_state=42)

# Apply LDA
n_components = 2  # Number of components
lda = LinearDiscriminantAnalysis(n_components=n_components)
X_lda = lda.fit_transform(X_train, y_train)

# Visualize the results
plt.figure(figsize=(10, 8))
for target, color in zip(range(len(iris.target_names)), ['r', 'g', 'b']):
    plt.scatter(X_lda[y_train == target, 0], X_lda[y_train == target, 1], color=color, label=iris.target_names[target])

plt.title('LDA of Iris Dataset')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.legend()
plt.show()