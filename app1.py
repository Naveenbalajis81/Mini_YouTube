from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing search query"}), 400

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q={query}&maxResults=10&videoEmbeddable=true&key={YOUTUBE_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "YouTube API request failed"}), 500

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
