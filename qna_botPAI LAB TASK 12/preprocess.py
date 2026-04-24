import pandas as pd
import re

def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'[^A-Za-z\s]', '', text)
        return text.lower()
    return ''

def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna()
    df['clean'] = df['text'].apply(clean_text)
    return df
