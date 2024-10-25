import re
from autocorrect import Speller
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
import string
nltk.download("stopwords")
nltk.download('punkt')
nltk.download("wordnet")

def remove_html_tags(text):
    html_pattern = r'<.*?>'
    without_html = re.sub(pattern=html_pattern, repl=' ', string=text)
    return without_html

def convert_to_lower(text):
    return text.lower()

def remove_urls(text):
    url_pattern = r'https?://\S+|www\.\S+'
    without_urls = re.sub(pattern=url_pattern, repl=' ', string=text)
    return without_urls

def spell_checker(text):
    spellChecker = Speller(lang="en")
    correct_words = []
    for word in nltk.word_tokenize(text):
        correct_word = spellChecker(word)
        correct_words.append(correct_word)
    correct_spell_text = " ".join(correct_words)
    return correct_spell_text


def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def remove_stopwords(text):
    removed = []
    stop_words = list(stopwords.words("english"))
    tokens = word_tokenize(text)
    for i in range(len(tokens)):
        if tokens[i] not in stop_words:
            removed.append(tokens[i])
    return " ".join(removed)


def lemmatizing(text):
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    for i in range(len(tokens)):
        lemma_word = lemmatizer.lemmatize(tokens[i])
        tokens[i] = lemma_word
    return " ".join(tokens)



def clean(text):
    cleaned_text=convert_to_lower(text)
    cleaned_text=remove_html_tags(cleaned_text)
    cleaned_text=remove_urls(cleaned_text)
    cleaned_text=remove_punctuation(cleaned_text)
    cleaned_text=remove_stopwords(cleaned_text)
    cleaned_text=lemmatizing(cleaned_text)
    cleaned_text= spell_checker(cleaned_text)
    return  cleaned_text
    