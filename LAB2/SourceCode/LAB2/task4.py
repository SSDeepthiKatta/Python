##LAB ASSIGNMENT - 2

##QUESTION 4

# Using Numpy create random vector of size 15 having only Integers in the range 0 -20.
# Write a program to find the most frequent item/value in the vector list.

import numpy as np
#random vector list of integers generated using numpy library
vector_list = np.random.randint(0, 20, 15)
print("Generated Random Vector List:")
print(vector_list) #list is printed
print("Most frequent value in the vector list:")
#np.bincount is used to count number of occurrences of each value in the list
#argmax gives the maximum of the bincount occurrences of the list
print(np.bincount(vector_list).argmax())