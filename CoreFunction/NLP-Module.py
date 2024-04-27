import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Load articles from JSON file
with open('../RSSFEED_LOGFILES/Articles.json', 'r') as json_file:
    articles = json.load(json_file)

# Initialize lists to store sentiments of individual articles
article_sentiments = []
overall_sentiment = {'positive': 0, 'negative': 0, 'neutral': 0}

# Analyze sentiment for each article
for article in articles:
    title = article['title']
    description = article['description']
    
    # Combine title and description for sentiment analysis
    text = title + ' ' + description
    
    # Perform sentiment analysis
    scores = sid.polarity_scores(text)
    
    # Interpret sentiment scores
    if scores['compound'] >= 0.05:
        sentiment = "Positive"
        overall_sentiment['positive'] += 1
    elif scores['compound'] <= -0.05:
        sentiment = "Negative"
        overall_sentiment['negative'] += 1
    else:
        sentiment = "Neutral"
        overall_sentiment['neutral'] += 1
    
    article_sentiments.append({'title': title, 'sentiment': sentiment})

# Print sentiment for each article
for article_sentiment in article_sentiments:
    print(f"Article: {article_sentiment['title']}")
    print(f"Sentiment: {article_sentiment['sentiment']}\n")

# Calculate overall sentiment
total_articles = len(articles)
overall_sentiment_percentage = {
    'positive': overall_sentiment['positive'] / total_articles * 100,
    'negative': overall_sentiment['negative'] / total_articles * 100,
    'neutral': overall_sentiment['neutral'] / total_articles * 100
}

print("Overall Sentiment:")
print(f"Positive: {overall_sentiment_percentage['positive']:.2f}%")
print(f"Negative: {overall_sentiment_percentage['negative']:.2f}%")
print(f"Neutral: {overall_sentiment_percentage['neutral']:.2f}%")

