import datetime
import feedparser
from dateutil import parser

# Open RSS Feed File
feedRSSFile = open('RSSFEED_TEMPSOURCE.txt')
feedRSSLineEach = feedRSSFile.readlines()
feedValue = 0
for eachLine in feedRSSLineEach:
    print("Now Checking: " + eachLine)
    # Parse the RSS feed
    feedRSS = feedparser.parse(eachLine)
    # Set the target date
    targetDate = datetime.datetime.now()
    filenameTargetDate = str(datetime.date.today())
    # Initialize a list to store valid articles
    filteredArticle = []

    # Check if the 'published' attribute is present in the feed entries
    if 'entries' in feedRSS:
        for article in feedRSS.entries:
            # Check if 'published' attribute is present in the current article
            if hasattr(article, 'published'):
                # Filter the articles by date
                if parser.parse(article.published).date() == targetDate.date():
                    filteredArticle.append(article)

    # Open the text file for writing
    with open("../RSSFEED_LOG/FEED" + str(feedValue) + ".txt", "w", encoding="utf-8") as file:
        # Write the filtered articles to the text file
        for article in filteredArticle:
            file.write("Title: " + article.title + "\n")
            file.write("Link: " + article.link + "\n")
            file.write("Description: " + article.description + "\n")
            file.write("Published: " + article.published + "\n\n")
        feedValue += 1
