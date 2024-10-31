# Polynomial Regression in R

## Importing the dataset
dataset <- read.csv("Position_Salaries.csv")
dataset <- dataset[2:3]

## Fitting Linear Regression to the dataset
lin_reg <- lm(formula = Salary ~ ., data = dataset)
# print(summary(lin_reg)) # nolint

## Fitting Polynomial Regression the dataset
dataset$Level2 <- dataset$Level^2
dataset$Level3 <- dataset$Level^3
dataset$Level4 <- dataset$Level^4
poly_reg <- lm(formula = Salary ~ ., data = dataset)
# print(summary(poly_reg)) # nolint

## Visualizing the Linear Regression results
library(ggplot2)
plot <- ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = "red") + geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)), colour = "blue") + ggtitle("Truth or Bluff (Linear Regression)") + xlab("Level") + ylab("Salary") # nolint

# print(plot) # nolint


## Visualizing the Polynomial Regression results
plot <- ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = "red") + geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)), colour = "blue") + ggtitle("Truth or Bluff (Polynomial Regression)") + xlab("Level") + ylab("Salary") # nolint

# print(plot) # nolint

## Predicting a new result with Linear Regression
y_pred <- predict(lin_reg, data.frame(Level = 6.5))
print("Prediction with Linear Regression:")
print(y_pred) # nolint

## Predicting a new result with Polynomial Regression
y_pred <- predict(poly_reg, data.frame(Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3, Level4 = 6.5^4)) # nolint
print("Prediction with Polynomial Regression:")
print(y_pred)