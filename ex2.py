from nltk.corpus import stopwords
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer
text = "Artificial intelligence is transforming modern industries rapidly. Many companies are adopting machine learning techniques to improve efficiency and customer satisfaction. However, proper data handling and security measures are extremely important for successful implementation."
words = [w for w in word_tokenize(text.lower())
         if w.isalpha() and w not in stopwords.words('english')]
print("Words after Stop words removal:\n", words)
porter = PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()
regex = RegexpStemmer('ing$|ed$|ly$|s$')
print("\nPorter Stemmer :", [porter.stem(w) for w in words])
print("\nSnowball Stemmer:", [snowball.stem(w) for w in words])
print("\nLancaster Stemmer:", [lancaster.stem(w) for w in words])
print("\nRegexp Stemmer:", [regex.stem(w) for w in words])
