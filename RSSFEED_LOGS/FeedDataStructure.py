import glob
import re
import json

def read_log_files():
    log_files = glob.glob('FEED*.txt')
    all_articles = []
    for file_path in log_files:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            article = {}
            for line in lines:
                line = line.strip()
                if line.startswith('Title:'):
                    article['title'] = line.split(': ', 1)[1] if len(line.split(': ', 1)) > 1 else ''
                elif line.startswith('Link:'):
                    article['link'] = line.split(': ', 1)[1] if len(line.split(': ', 1)) > 1 else ''
                elif line.startswith('Description:'):
                    article['description'] = line.split(': ', 1)[1] if len(line.split(': ', 1)) > 1 else ''
                elif line.startswith('Published:'):
                    article['published'] = line.split(': ', 1)[1] if len(line.split(': ', 1)) > 1 else ''
                    all_articles.append(article.copy())
    return all_articles

def main():
    all_articles = read_log_files()

    # Export the data structure as a JSON file
    with open('articles.json', 'w') as json_file:
        json.dump(all_articles, json_file, indent=4)

if __name__ == "__main__":
    main()

