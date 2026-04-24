# NLP Lab 9 Task
# Basic NLP operations

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = "This is a simple example showing running, played and better words."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stopword removal
stop_words = set(stopwords.words('english'))
filtered = [w for w in tokens if w.lower() not in stop_words]
print("After Stopword Removal:", filtered)

# Stemming
ps = PorterStemmer()
stemmed = [ps.stem(w) for w in filtered]
print("Stemmed Words:", stemmed)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(w) for w in filtered]
print("Lemmatized Words:", lemmatized)
