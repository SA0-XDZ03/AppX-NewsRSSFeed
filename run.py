from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Read data from articles.json
    with open('./RSSFEED_LOGS/articles.json', 'r') as json_file:
        articles = json.load(json_file)
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)

