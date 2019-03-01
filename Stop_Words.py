import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text_file = open(".\login2.txt","r")
text=text_file.read()

filtered_sent=[]
stop_words= set(stopwords.words("english"))

word=nltk.word_tokenize(text)
for w in word:
    if w not in stop_words:
        filtered_sent.append(w)

print(filtered_sent)
