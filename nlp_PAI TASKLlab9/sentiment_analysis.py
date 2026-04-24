# Sentiment Analysis Example

from textblob import TextBlob

text = "This product is excellent!"
blob = TextBlob(text)

print("Sentiment:", blob.sentiment)
