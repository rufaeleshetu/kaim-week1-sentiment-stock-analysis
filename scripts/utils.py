import pandas as pd
from textblob import TextBlob

def load_csv(path):
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        return None
    except Exception as e:
        print(f"❌ Failed to load {path}: {e}")
        return None

def get_sentiment(text):
    try:
        return TextBlob(text.strip().lower()).sentiment.polarity
    except Exception as e:
        print(f"❌ Sentiment error: {e}")
        return 0