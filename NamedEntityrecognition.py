import nltk
from nltk.tokenize import word_tokenize,PunktSentenceTokenizer

text_file = open(".\login2.txt","r")
text=text_file.read()

word=nltk.word_tokenize(text)

custom_sen=PunktSentenceTokenizer(text)
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

process()
