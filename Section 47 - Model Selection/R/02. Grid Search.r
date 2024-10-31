# Grid Search in R

## Importing the dataset
dataset <- read.csv("Social_Network_Ads.csv")
dataset <- dataset[, 3:5]

## Encoding the target feature as factor
dataset$Purchased <- factor(dataset$Purchased, levels = c(0, 1))

## Splitting the dataset into the Training set and Test set
# install.packages('caTools') # nolint
library(caTools)
set.seed(123)
split <- sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

## Feature Scaling
training_set[-3] <- scale(training_set[-3])
test_set[-3] <- scale(test_set[-3])

## Fitting Kernel SVM to the Training set
library(e1071)
classifier <- svm(formula = Purchased ~ ., data = training_set, type = "C-Classification", kernel = "radial") # nolint

## Predicting the Test set results
y_pred <- predict(classifier, newdata = test_set[-3])

## Making the Confusion Matrix
cm <- table(test_set_pca[, 3], y_pred)
print(cm)

## Applying k-Fold Cross Validation
# install.packages("caret") # nolint
library(caret)
folds <- createFolds(training_set$Purchased, k = 10)
cv <- lapply(folds, function(x) {
    training_fold <- training_set[-x, ]
    test_fold <- test_set[x, ]
    classifier <- svm(formula = Purchased ~ ., data = training_fold, type = "C-Classification", kernel = "radial") # nolint
    y_pred <- predict(classfier, newdata = test_fold[-3])
    cm <- table(test_fold[, 3], y_pred)
    accuracy <- (cm[1, 1] + cm[2, 2]) / (cm[1, 1] + cm[2, 2] + cm[1, 2] + cm[2, 1]) # nolint
    return(accuracy)
})
accuracy <- mean(as.numeric(cv))

## Applying Grid Search to find the best parameters
library(caret)
classifier <- train(form = Purchased ~ ., data = training_set, method = "svmRadial") # nolint
print(classifier)
print(classifier$bestTune)

## Visualising the Training set results
library(ElemStatLearn)
set <- training_set_pca
X1 <- seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01) # nolint
X2 <- seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01) # nolint
grid_set <- expand.grid(X1, X2)
colnames(grid_set) <- c("V1", "V2")
prob_set <- predict(classifier, type = "response", newdata = grid_set)
y_grid <- ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = "Logistic Regression (Training set)",
     xlab = "PC1", ylab = "PC2",
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = ".", col = ifelse(y_grid == 1, "springgreen3", "tomato"))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, "green4", "red3"))

## Visualising the Test set results
library(ElemStatLearn)
set <- test_set_pca
X1 <- seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01) # nolint
X2 <- seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01) # nolint
grid_set <- expand.grid(X1, X2)
colnames(grid_set) <- c("V1", "V2")
prob_set <- predict(classifier, type = "response", newdata = grid_set)
y_grid <- ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = "Logistic Regression (Test set)",
     xlab = "Age", ylab = "Estimated Salary",
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = ".", col = ifelse(y_grid == 1, "springgreen3", "tomato"))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, "green4", "red3"))