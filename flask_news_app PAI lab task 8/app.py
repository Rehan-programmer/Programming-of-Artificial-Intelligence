from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "demo"  # replace with real key if needed

@app.route('/', methods=['GET', 'POST'])
def home():
    articles = []
    if request.method == 'POST':
        topic = request.form.get('topic')
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])[:5]
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
