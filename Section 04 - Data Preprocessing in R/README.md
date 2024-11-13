# Data Preprocessing in R

## Code

```r
# Data Preprocessing in R

## Importing the Dataset
dataset <- read.csv("Data.csv")


## Taking Care of Missing Data
### Filling the missing values of Age
dataset$Age <- ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age) # nolint

### Filling the missing values of Salary
dataset$Salary <- ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary) # nolint


## Encoding Categorical Data

### ECD for Country
dataset$Country <- factor(dataset$Country, levels = c('France', 'Spain', 'Germany'), labels = c(1, 2, 3)) # nolint

### ECD for Purchased
dataset$Purchased <- factor(dataset$Purchased, levels = c('No', 'Yes'), labels = c(0, 1)) # nolint


## Splitting the dataset into the Training set and Test set
library(caTools)
set.seed(123) # setting seed for reproducibility of results
split <- sample.split(dataset$Purchased, SplitRatio = 0.8)
View(split)

training_set <- subset(dataset, split == TRUE)
# View(training_set) # nolint

test_set <- subset(dataset, split == FALSE)
# View(test_set) # nolint


## Feature Scaling
training_set[, 2:3] <- scale(training_set[, 2:3])
test_set[, 2:3] <- scale(test_set[, 2:3])

View(training_set)
View(test_set)


View(dataset)
```

## Download Resources
* <a href="Data Preprocessing in R.r" download>R Code</a>
* <a href="Data.csv" download>Dataset</a>
<hr>

<a href="../Section 03 - Data Preprocessing in Python">«Previous</a> | <a href="../Section 05 - Part 02 - Regression">Next»</a>
