import nltk
from nltk.tokenize import sent_tokenize, word_tokenize,PunktSentenceTokenizer

text_file = open(".\login2.txt","r")
text=text_file.read()

word=nltk.word_tokenize(text)
print(word)

print("\n \n \n")

sent = nltk.sent_tokenize(text)
print(sent)


print("\n \n \n")


cust = custom_sen=PunktSentenceTokenizer(text)
tokenized = custom_sen.tokenize("hello. how can i login. where is otp?")
print(tokenized)

