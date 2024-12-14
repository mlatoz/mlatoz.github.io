# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate some example data (you can replace this with your own dataset)
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Create a K-Means model
kmeans_model = KMeans(n_clusters=4, random_state=42)  # You can adjust the number of clusters (n_clusters) parameter

# Fit the model to the data
kmeans_model.fit(X)

# Get the cluster labels and centroids
labels = kmeans_model.labels_
centroids = kmeans_model.cluster_centers_

# Visualize the clustering
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, linewidths=2, color='red', label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.legend()
plt.show()