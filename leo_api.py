from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # 👈 Enables cross-origin access

@app.route('/start')
def start_assistant():
    subprocess.Popen(['python', 'Leo.py'])
    return jsonify({"message": "LEO assistant started!"})

@app.route('/news')
def get_news():
    import requests
    url = 'https://newsapi.org/v2/top-headlines'
    params = {'apiKey': 'YOUR_API_KEY', 'country': 'in'}
    response = requests.get(url, params=params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=5000)
