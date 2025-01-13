import numpy as np
import string
import re
import nltk
import spacy
from nltk.corpus import stopwords
#nltk.download('stopwords')
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
#nltk.download('wordnet')
from spellchecker import SpellChecker

def upper_to_lower(text):
    return text.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('','',string.punctuation))

stop_words=set(stopwords.words('english'))
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop_words])

cnt=Counter()
freq_words=set([w for (w,wc) in cnt.most_common(10)])
def remove_freqwords(text):
    return " ".join([word for word in str(text).split() if word not in freq_words])

n_rarewords=10
rarewords = set([w for (w, wc) in cnt.most_common()[:-n_rarewords-1:-1]])
def remove_rarewords(text):
    return " ".join([word for word in str(text).split() if word not in rarewords])

st=PorterStemmer()
def stemming(text):
    return " ".join([st.stem(word) for word in text.split()])

lematizer=WordNetLemmatizer()
def lematization(text):
    return " ".join([lematizer.lemmatize(word) for word in text.split()])

def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'',text)

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)

spell = SpellChecker()
def correct_spellings(text):
    if not text:
        return ""
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    for word in text.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)
