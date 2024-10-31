# Support Vector Regression in R

## Importing the dataset
dataset <- read.csv("Position_Salaries.csv")
dataset <- dataset[2:3]


## Fitting the SVR to the dataset
# install.packages("e1071") # nolint
library(e1071)
regressor <- svm(formula = Salary ~ ., data = dataset, type = "eps-regression")


## Predicting a new result
y_pred <- predict(regressor, data.frame(Level = 6.5))
print(y_pred)


## Visualizing the SVR results
library(ggplot2)
print(ggplot() + geom_point(aes(x = dataset$Level, y = dataset$Salary),
colour = "red") + geom_line(aes(x = dataset$Level,
y = predict(regressor, newdata = dataset)), colour = "blue") +
ggtitle("Truth or Bluff (SVR)") + xlab("Level") + ylab("Salary"))