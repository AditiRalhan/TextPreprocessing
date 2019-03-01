import nltk
from nltk.tokenize import sent_tokenize, word_tokenize,PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

##stop_words= set(stopwords.words("english"))

##ps= PorterStemmer()

text_file = open("D:\Aditi\login.txt","r")
text=text_file.read()

word=nltk.word_tokenize(text)

lemmatizer = WordNetLemmatizer()

for w in word:
    print(w,lemmatizer.lemmatize(w))


""" custom_sen=PunktSentenceTokenizer(text)
tokenized = custom_sen.tokenize("hello. how can i login. where is otp?")

def process():
    try:
        for w in tokenized:
            word=nltk.word_tokenize(w)
            tagged=nltk.pos_tag(word)

            namedEnt = nltk.ne_chunk(tagged)
            namedEnt.draw()
            print(tagged)
            
    except Exception as e:
        print(str(e))

        """
    
        
""" filtered_sent=[]

for w in word:
    if w not in stop_words:
        filtered_sent.append(w)

print(filtered_sent)
print('\n')

for w in filtered_sent:
    print(ps.stem(w))

process() """

text_file.close()

