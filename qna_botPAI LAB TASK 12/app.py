from flask import Flask, render_template, request
import pandas as pd
import faiss
from model import search

app = Flask(__name__)

df = pd.read_csv('data/sample.csv')
index = faiss.read_index('index.faiss')

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        results = search(query, df, index)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
