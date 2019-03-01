import nltk
from nltk.stem import WordNetLemmatizer

text_file = open(".\login2.txt","r")
text=text_file.read()

word=nltk.word_tokenize(text)

lemmatizer = WordNetLemmatizer()

for w in word:
    print(w,lemmatizer.lemmatize(w))
            
       
        
       
