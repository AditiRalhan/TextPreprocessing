import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


text_file = open(".\login2.txt","r")
text=text_file.read()

stop_words= set(stopwords.words("english"))

filtered_sent=[]

word=nltk.word_tokenize(text)

synonyms=[]
antonyms=[]

lemmatizer = WordNetLemmatizer()

for w in word:
    if w not in stop_words:
        filtered_sent.append(lemmatizer.lemmatize(w))

for w in filtered_sent:
    for syn in wordnet.synsets(w):
        synonyms=[]
        antonyms=[]
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                 antonyms.append(l.antonyms()[0].name())
        print("\n","Word: ",w)
        print(set(synonyms))
        print("An  ")
        print(set(antonyms))
            
                 
  

    



