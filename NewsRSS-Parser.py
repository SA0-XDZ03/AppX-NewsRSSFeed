from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define the directory containing your text files
text_files_directory = "RSSFEED_LOG"

# Function to read the content of text files
def read_text_files():
    file_contents = []
    for filename in os.listdir(text_files_directory):
        if filename.endswith(".txt"):
            with open(os.path.join(text_files_directory, filename), "r", encoding="utf-8") as file:
                content = file.read()
                file_contents.append(content)
    return file_contents

@app.route("/", methods=["GET", "POST"])
def index():
    # Read the content of text files
    content_list = read_text_files()

    if request.method == "POST":
        search_query = request.form.get("search_query", "").strip()
        if search_query:
            # Filter text files based on the search query
            content_list = [content for content in content_list if search_query in content]

    return render_template("index.html", content_list=content_list)

    # Route to serve MapsOpen.js
    @app.route('/')
    def serve_maps_open_js():
        return send_from_directory("MapsOpen.js")

if __name__ == "__main__":
    app.run(debug=True)
