import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
text = "He killed two people"

# Perform sentiment analysis
scores = sid.polarity_scores(text)

# Interpret sentiment scores
if scores['compound'] >= 0.05:
    sentiment = "Positive"
elif scores['compound'] <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Sentiment:", sentiment)

