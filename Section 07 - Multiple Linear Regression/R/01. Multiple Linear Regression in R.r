# Multiple Linear Regression in R

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

## Fitting Multiple Linear Regression to the Training set
# regressor <- lm(formula = Profit ~ R.D.Spend + Administration +
# Marketing.Spend + State)

# The Another method to add all the independent variables is using "."
regressor <- lm(formula = Profit ~ ., data = training_set)

# print(summary(regressor)) # nolint

# Predicting the Profit
## Predicting the Test set results
y_pred <- predict(regressor, newdata = test_set)
print(y_pred)

# View(dataset) # nolint