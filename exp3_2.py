import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

# Sample data
posts = [
    "I love this new phone battery life is amazing",
    "This update is very bad and disappointing",
    "Amazing camera and great performance",
    "The app is slow and interface is bad",
    "I love the camera quality and battery performance"
]

# Preprocessing setup
nltk.download('stopwords')
st_words = set(stopwords.words('english'))

ug, bg, tg = [], [], []

# Character N-gram Generation
for post in posts:
    post_clean = post.lower()
    post_clean = re.sub(r'[^a-z\s]', '', post_clean)
    words = [w for w in post_clean.split() if w not in st_words]
    
    for word in words:
        # Unigrams (Individual characters)
        ug.extend(list(word))
        
        # Bigrams (Pairs of characters)
        bg.extend([word[i:i+2] for i in range(len(word)-1)])
        
        # Trigrams (Triplets of characters)
        tg.extend([word[i:i+3] for i in range(len(word)-2)])

# Counting frequencies
ugc = Counter(ug)
bgc = Counter(bg)
tgc = Counter(tg)

# Output N-grams
print("Top Unigrams :", ugc.most_common(3))
print("Top Bigrams :", bgc.most_common(3))
print("Top Trigrams :", tgc.most_common(3))

# Sentiment Analysis
from textblob import TextBlob
print("\nSentiment Analysis:")
for post in posts:
    blob = TextBlob(post)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
        
    print(f"{sentiment}")
    print(f"post: '{post}' polarity: {polarity}")