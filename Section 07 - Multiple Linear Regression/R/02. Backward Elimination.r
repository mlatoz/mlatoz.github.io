# Multiple Linear Regression in R - Backward Elimination - Homework

## Importing the dataset
dataset <- read.csv("50_Startups.csv")

## Encoding Categorical Data
dataset$State <- factor(dataset$State,
levels = c("New York", "California", "Florida"), labels = c(1, 2, 3))

library(caTools)
set.seed(123)
split <- sample.split(dataset$Profit, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

regressor <- lm(formula = Profit ~ ., data = training_set)

## Predicting the Test set results
y_pred <- predict(regressor, newdata = test_set)

## Building the optimal model using Backward Elimination
regressor <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend
+ State, data = dataset)
# print(summary(regressor)) # nolint

regressor <- lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend
, data = dataset)
# print(summary(regressor)) # nolint

regressor <- lm(formula = Profit ~ R.D.Spend + Marketing.Spend
, data = dataset)
# print(summary(regressor)) # nolint

regressor <- lm(formula = Profit ~ R.D.Spend, data = dataset)
print(summary(regressor))

# View(dataset) # nolint