import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
nltk.data.path.append('/media/safak/Data/NLTK/')

def absTokenizer1(regex, abstracts):
    """
    above abstractTokenizer returns all the word but sentence structured.
    """
    stopWords = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(regex)
    tokened = [tokenizer.tokenize(abstract) for abstract in abstracts]
    #return [item for sublist in (tokenizer.tokenize(abstract) for abstract in abstracts) for item in sublist if item not in stopWords ]
    print('Abstracts are tokenized...')
    return tokened
