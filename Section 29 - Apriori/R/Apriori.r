# Apriori in R

## Data Preprocessing
# print(install.packages("arules")) # nolint
library(arules)

dataset <- read.csv("Market_Basket_Optimisation.csv", header = FALSE)
# View(dataset) # nolint

dataset <- read.transactions("Market_Basket_Optimisation.csv", sep = ",", rm.duplicates = TRUE) # nolint
# View(dataset) # nolint
print(summary(dataset)) # nolint

# itemFrequencyPlot(dataset, topN = 100) # nolint

## Training Apriori on the Dataset
rules <- apriori(data = dataset, parameter = list(support = 0.003, confidence = 0.2)) # nolint
print(rules) # nolint

## Visualising the results
inspect(sort(rules, by = "lift")[1:10])