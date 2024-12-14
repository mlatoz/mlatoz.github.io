# Install necessary libraries if not already installed
# pip install scikit-learn matplotlib

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler

# Load example data (replace this with your own dataset)
digits = load_digits()
X = digits.data
y = digits.target

# Standardize the data
X_std = StandardScaler().fit_transform(X)

# Apply PCA
n_components = 2  # Number of principal components
pca = PCA(n_components=n_components)
principal_components = pca.fit_transform(X_std)

# Create a DataFrame for visualization (optional)
import pandas as pd
principal_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
principal_df['Target'] = y

# Visualize the results
plt.figure(figsize=(10, 8))
plt.scatter(principal_components[:, 0], principal_components[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.title('PCA of Digits Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()