import datetime
import feedparser
from dateutil import parser
import json
import os

def select_country_news_option():
    print("Select Country News Option:")
    print("[1] Global News")
    print("[2] General News")
    print("[3] India")
    print("[4] Pakistan")
    print("[5] China")
    print("[6] Sri Lanka")
    option = input("Enter your choice: ")
    return option

def select_sector_specific_option():
    print("Select Sector Specific News Option:")
    print("[1] Technology")
    print("[2] Military")
    print("[3] Government & Politics")
    print("[4] Entertainment & Sports")
    option = input("Enter your choice: ")
    return option

def process_rss_feeds(option, rss_feed_file):
    feedRSSFile = open(rss_feed_file)
    feedRSSLineEach = feedRSSFile.readlines()
    feedValue = 0
    all_articles = []  # List to store all articles for JSON export

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

        # Prepare JSON data
        all_articles.extend(filteredArticle)

        # Open the text file for writing
        with open(f"../DataSources/RSSFEED_LOGFILES/{option}-{feedValue}.json", "w", encoding="utf-8") as json_file:
            json.dump(filteredArticle, json_file, indent=4)

        feedValue += 1

    # Export all articles to a single JSON file
    with open(f"../DataSources/RSSFEED_LOGFILES/{option}-AllNews.json", "w", encoding="utf-8") as json_file:
        json.dump(all_articles, json_file, indent=4)


def main():
    print("Welcome to RSS Feed Aggregator")
    print("[1] Country News")
    print("[2] Sector Specific News")
    category_option = input("Enter your choice: ")

    if category_option == '1':
        country_option = select_country_news_option()
        if country_option == '1':
            process_rss_feeds("Global", "../DataSources/Country-Specific/RSSFEED_GLOBAL_GENERALSOURCE.txt")
        elif country_option == '2':
            process_rss_feeds("General", "../DataSources/Country-Specific/RSSFEED_GENERALNEWS_SOURCE.txt")
        elif country_option == '3':
            process_rss_feeds("India", "../DataSources/Country-Specific/RSSFEED_INDIA_GENERALSOURCE.txt")
        elif country_option == '4':
            process_rss_feeds("Pakistan", "../DataSources/Country-Specific/RSSFEED_PAKISTAN_GENERALSOURCE.txt")
        elif country_option == '5':
            process_rss_feeds("China", "../DataSources/Country-Specific/RSSFEED_CHINA_GENERALSOURCE.txt")
        elif country_option == '6':
            process_rss_feeds("SriLanka", "../DataSources/Country-Specific/RSSFEED_SRILANKA_GENERALSOURCE.txt")
        else:
            print("Invalid option selected")

    elif category_option == '2':
        sector_option = select_sector_specific_option()
        if sector_option == '1':
            process_rss_feeds("Technology", "../DataSources/Sector-Specific/RSSFEED_TECHNOLOGY_GENERALSOURCE.txt")
        elif sector_option == '2':
            process_rss_feeds("Military", "../DataSources/Sector-Specific/RSSFEED_MILITARY_GENERALSOURCE.txt")
        elif sector_option == '3':
            process_rss_feeds("Government-Politics", "../DataSources/Sector-Specific/RSSFEED_GOVERNMENT_POLITICS_GENERALSOURCE.txt")
        elif sector_option == '4':
            process_rss_feeds("Entertainment-Sports", "../DataSources/Sector-Specific/RSSFEED_ENTERTAINMENT_SPORTS_GENERALSOURCE.txt")
        else:
            print("Invalid option selected")

    else:
        print("Invalid category selected")

if __name__ == "__main__":
    main()
