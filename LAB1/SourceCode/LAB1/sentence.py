# LAB ASSIGNMENT -1
# created by SSDK

##QUESTION - 2

# Python Function which accepts sentence from the user and prints
# middle words of the sentence
# longest word of sentence
# reverses all words in sentence individually

def revlongmiddleSen(Sen):

 words = Sen.split(" ")

 Str_len = len(words)
 middle = float(Str_len) / 2
 # print(middle)
 if Str_len % 2 == 0:
     print("Middle words in given sentence:", [words[int(middle)], words[int(middle - 1)]])
 else:
     print("Middle words in given sentence:", [words[int(middle - .5)]])

 pivot = 0
 long_str = ""
 for itr in words:
     if (len(itr) > pivot):
         long_str = itr
         pivot = len(itr)
 print("Longest word in given sentence is: " + long_str)

 #takes each word in the list and prints it in reversed order using {::-1}
 #whereas join is used to combined all the reversed words to make a sentence
 rev = " ".join([word[::-1] for word in words])
 print("Reveresed Sentence is:" + rev)

 return #end of Python revlongmiddleSen function

# Source - Inialization
import sys
Sen = input("Enter a sentence: ")
revlongmiddleSen(Sen)



