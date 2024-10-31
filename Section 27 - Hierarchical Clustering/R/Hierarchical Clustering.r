# Hierarchical Clustering in R

## Importing the Dataset
dataset <- read.csv("Mall_Customers.csv")
# View(dataset) # nolint

X <- dataset[4:5]
# View(X) # nolint

## Using the dendrogram to find the optimal number of clusters
dendrogram <- hclust(dist(X, method = "euclidean"), method = "ward.D")
plot(dendrogram, main = paste("Dendogram"), xlab = "Customers", ylab = "Euclidean Distances") # nolint

## Fitting Hierarchical Clustering to the Mall_Customers Dataset
hc <- hclust(dist(X, method = "euclidean"), method = "ward.D")
y_hc <- cutree(hc, 5)
print(y_hc)

## Visualizing the Clusters
library(cluster)
clusplot(X, y_hc, lines = 0, shade = TRUE, color = TRUE, labels = 2, plotchar = FALSE, span = TRUE, main = paste("Clusters of Customers"), xlab = "Annual Income", ylab = "Spending Score") # nolint