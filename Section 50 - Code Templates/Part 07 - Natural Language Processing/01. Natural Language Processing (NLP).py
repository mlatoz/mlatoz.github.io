# Install necessary libraries if not already installed
# pip install nltk

# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import string

# Download NLTK resources (run this once)
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')

# Example text data (replace this with your own text data)
text_data = "Natural Language Processing (NLP) is a fascinating field of study."

# Text preprocessing
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    return tokens

# Sentiment analysis using VADER sentiment analyzer
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Perform text preprocessing
processed_tokens = preprocess_text(text_data)
print("Processed Tokens:", processed_tokens)

# Perform sentiment analysis
sentiment = analyze_sentiment(text_data)
print("Sentiment:", sentiment)