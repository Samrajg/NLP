import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

# Sample data
posts = [
    "I like this new phone's battery life",
    "This update is bad and disappointing",
    "Amazing camera quality",
    "The app loading time is too much",
    "The phone is very nice and I love it"
]

# Preprocessing setup
nltk.download('stopwords')
st_words = set(stopwords.words('english'))

ug, bg, tg = [], [], []

# N-gram Generation
for post in posts:
    post_clean = post.lower()
    post_clean = re.sub(r'[^a-z\s]', '', post_clean)
    words = [w for w in post_clean.split() if w not in st_words]
    
    ug.extend(words)
    bg.extend(zip(words, words[1:]))
    tg.extend(zip(words, words[1:], words[2:]))

# Counting frequencies
ugc = Counter(ug)
bgc = Counter(bg)
tgc = Counter(tg)

# Output N-grams
print("Top Unigrams :", ugc.most_common(3))
print("Top Bigrams :", bgc.most_common(3))
print("Top Trigrams :", tgc.most_common(3))

# Sentiment Analysis
print("\nSentiment Analysis:")
for post in posts:
    blob = TextBlob(post)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "Neutral"
        
    print(f"{sentiment}")
    print(f"post: '{post}' polarity: {polarity}")