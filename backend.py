from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes and origins

@app.route('/news.all.get')
def get_news_all_articles():
    with open('news_data.json', 'r') as file:
        data = json.load(file)
    return json.dumps(data)

if __name__ == "__main__":
    app.run(port=8080)
