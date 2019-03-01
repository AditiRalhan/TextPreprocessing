import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps= PorterStemmer()

text_file = open(".\login2.txt","r")
text=text_file.read()

word=nltk.word_tokenize(text)

for w in word:
    print(w,"   ",ps.stem(w))
