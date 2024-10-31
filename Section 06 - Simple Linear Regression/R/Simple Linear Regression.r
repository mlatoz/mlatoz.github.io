# Step 1
## Importing the dataset
dataset <- read.csv("Salary_Data.csv")

## Splitting the dataset into the Training set and Test set
library(caTools)
set.seed(123)
split <- sample.split(dataset$Salary, SplitRatio = 2 / 3)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)
# View(dataset) # nolint
# View(training_set) # nolint
# View(test_set) # nolint


# Step 2
## Fitting Simple Linear Regression to the Training set
# * In the below code "~" means Proportion
# * Means here the "Salary is proportional to YearsExperience"
regressor <- lm(formula = Salary ~ YearsExperience, data = training_set)
# print(summary(regressor)) # nolint


# Step 3
## Predicting the Test set results
y_pred <- predict(regressor, newdata = test_set)
# View(y_pred) # nolint


# Step 4
## Visualizing the Training set results
library(ggplot2)
print(ggplot() + geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary), colour = "red") + geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)), colour = "blue") + ggtitle("Salary V/S Experience (Training set)") + xlab("Years of Experience") + ylab("Salary")) # nolint