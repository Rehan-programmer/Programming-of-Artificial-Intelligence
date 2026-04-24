from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Random Joke API App"

@app.route('/joke')
def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "setup": data["setup"],
            "punchline": data["punchline"]
        })
    else:
        return jsonify({"error": "Failed to fetch joke"})

if __name__ == '__main__':
    app.run(debug=True)
