#LAB Assignment - 3
 # Question -3

#Write a program  Take an Inputfile.
#  Use the simple approach below to summarize a text file:
# -Read the file-Using Lemmatization, apply lemmatization on the words
# -Apply the bigram on the text
# -Calculate the word frequency (bi-gram frequency) of the words(bi-grams)
# -Choose top fivebi-gramsthat has been repeated most
# -Go through the original text that you had in the file
# -Find all the sentences with those most repeated bi-grams
# -Extract those sentences and concatenate
#-Enjoy the summarization
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import nltk
from nltk import ngrams
from operator import itemgetter

# Text file input is taken
with open('input.txt' , 'r') as f:
    lines = f.readlines()
print("_____________________________________________INPUT_________________________________________________")
print(lines)
file_read=''

#Multiple lines  into single string
for m in lines:
    file_read=file_read+m
print(file_read)
#tokenize word individually and sentence wise
f_r_w = word_tokenize(file_read)
f_r_s = sent_tokenize(file_read)

#-	Using Lemmatization, apply lemmatization on the remaining words
lemmatizer = WordNetLemmatizer()
f_r_l = []
for word in f_r_w:
    frl = lemmatizer.lemmatize(word.lower())
    f_r_l.append(frl)
print("\n\n")
print("______________________________________________________LEMMATIZATION_____________________________________________________")
print(f_r_l)


print("\n\n")
print("____________________________________________________BI-GRAMS_____________________________________________________________")
n = 2 #giving n value as 2 for getting bi-grams
gram=[]
bigrams = ngrams(f_r_l, n)
for grams in bigrams: #for every 2 grams are grouped into a set creating bi-grams
    gram.append(grams)
print(gram)

#getting parts of speech tags for each work
f_r_pos = pos_tag(f_r_l)
str1 = " ".join(str(x) for x,y in f_r_pos)
str1_word = word_tokenize(str1)
print("\n\n")
print("___________________________________Bi-Grams with Word frequency_______________________________________________________")
f_d = nltk.FreqDist(gram)
t_c = f_d.most_common() #most common bi-grams
t_c_f = f_d.most_common(5) #top most common five bi-grams
top=sorted(t_c,key=itemgetter(0))
print(top)
print("\n\n")
print('___________________________________Most Commonly Repeated top five Bi-grams______________________________________________')
print(t_c_f)

s = sent_tokenize(file_read)
f_s = []
for each in s: #for each sentence in the list of sentences
    for word,words in gram:  #bi-grams are taken
        for ((c,m), l) in t_c_f: #each bi-gram is compared with top five bi-grams
            if (word,words == c,m):
                f_s.append(each)  #if its a match then sentence is appended with the final sentence
print("\n\n")
print ("________________________________Top five sentences with commonly repeated Bi-grams______________________________________")
print(max(f_s,key=len))
