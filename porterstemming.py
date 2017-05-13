import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


#SORTING
files=["doc1.txt","doc2.txt","doc3.txt","doc4.txt","doc5.txt","doc6.txt","doc7.txt","doc8.txt","doc9.txt","doc10.txt","doc11.txt","doc12.txt","doc13.txt","doc14.txt","doc15.txt","doc16.txt","doc17.txt","doc18.txt","doc19.txt","doc20.txt","doc21.txt","doc22.txt","doc23.txt","doc24.txt","doc25.txt","doc26.txt","doc27.txt","doc28.txt","doc29.txt","doc30.txt"]
for filea in files:
    a=open(filea,'r').read()
    x=a.split(" ")
    print (x)

    stemmer=PorterStemmer()
    print (x.sort())
    
english_stops = set(stopwords.words('english'))
words=x
abcx=[word for word in words if word not in english_stops]
print (abcx)

for i in abcx:
    print (stemmer.stem(i))

