# Natural Language Processing (NLP) in R

## Importing the dataset
dataset <- read.delim("Restaurant_Reviews.tsv", quote = "", stringsAsFactors = FALSE) # nolint
# View(dataset) # nolint

## Cleaning the texts
# install.packages("tm") # nolint
library(tm)

corpus <- VCorpus(VectorSource(dataset$Review))
# print(as.character(corpus[[1]])) # nolint

# The capital "W" in the statement will become small "w"
corpus <- tm_map(corpus, content_transformer(tolower))
# print(as.character(corpus[[1]])) # nolint
# print(as.character(corpus[[841]])) # nolint

# It will remove the number in the statement
corpus <- tm_map(corpus, removeNumbers)
# print(as.character(corpus[[841]])) # nolint

# To remove punctuation
corpus <- tm_map(corpus, removePunctuation)
# print(as.character(corpus[[1]])) # nolint

# To remove words
# install.packages("SnowballC") # nolint
library(SnowballC)

corpus <- tm_map(corpus, removeWords, stopwords())
# It will delete "this" word from the statement
# print(as.character(corpus[[1]])) # nolint

corpus <- tm_map(corpus, stemDocument)
# print(as.character(corpus[[1]])) # nolint

# Stripping White Space
corpus <- tm_map(corpus, stripWhitespace)
# print(as.character(corpus[[841]])) # nolint

## Creating the Bag of Words Model
dtm <- DocumentTermMatrix(corpus)
# print(dtm) # nolint
dtm <- removeSparseTerms(dtm, 0.999)
# print("") # nolint
# print(dtm) # nolint
dataset <- as.data.frame(as.matrix(dtm))
# View(dataset) # nolint
dataset_original <- read.delim("Restaurant_Reviews.tsv", quote = "", stringsAsFactors = FALSE) # nolint
dataset$Liked <- dataset_original$Liked

## Encoding the target feature as factor
dataset$Liked <- factor(dataset$Liked, levels = c(0, 1))

## Splitting the dataset into the Training set and Test set
# install . packages('caTools')
library(caTools)
set.seed(123)
split <- sample.split(dataset$Liked, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

## Fitting Random Forest Classification to the Training set
# install . packages("randomForest")
library(randomForest)
classifier <- randomForest(x = training_set[-692], y = training_set$Liked, ntree = 10) # nolint

## Predicting the Test set results
y_pred <- predict(classifier, newdata = test_set[-692])

## Making the Confusion Matrix
cm <- table(test_set[, 692], y_pred)
print(cm)