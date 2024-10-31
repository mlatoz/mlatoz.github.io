# Decision Tree Regression

## Importing the Dataset
dataset <- read.csv("Position_Salaries.csv")
dataset <- dataset[2:3]

## Fitting the Decision Tree Regression to the dataset
# install.packages("rpart") # nolint
library(rpart)

# Regression algorithm is used for prediction of continuous values such as salary based on various factors like level and experience # nolint

regressor <- rpart(formula = Salary ~ ., data = dataset, control = rpart.control(minsplit = 1)) # nolint
regressor <- rpart(formula = Salary ~ ., data = dataset, control = rpart.control(minsplit = 1)) # nolint

## Predicting a new result
y_pred <- predict(regressor, data.frame(Level = 6.5))
print(y_pred)

## Visualizing the Decision Tree Regression Results
library(ggplot2)
# plots <- ggplot() + # nolint
# geom_point(aes(x = dataset$Level, y = dataset$Salary), # nolint
# colour = "red") + # nolint
# geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)), # nolint
# colour = "blue") + ggtitle("Truth or Bluff (Decision Tree Regression)") + # nolint
# xlab("Level") + ylab("Salary") # nolint

# print(plots) # nolint

## Visualizing the Regression Model results (for higher resolution and smoother)
# x_grid <- seq(min(dataset$Level), max(dataset$Level), 0.1) # nolint
# plots <- ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = "red") + geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid), colour = "blue"))) + ggtitle("Truth or Bluff (Decision Tree Regression)") + xlab("Level") + ylab("Salary") # nolint

# print(plots) # nolint

x_grid <- seq(min(dataset$Level), max(dataset$Level), 0.01)
plots <- ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = "red") + geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid), colour = "blue"))) + ggtitle("Truth or Bluff (Decision Tree Regression)") + xlab("Level") + ylab("Salary") # nolint

print(plots)