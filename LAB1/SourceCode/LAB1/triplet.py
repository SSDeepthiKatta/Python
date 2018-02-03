# LAB ASSIGNMENT -1
# created by SSDK

##QUESTION - 3

# Python program to find triplets in a given
# array whose sum is zero

# function to print triplets with 0 sum
def tripletsumzero(in_list, n):
    found = False
    # sort array elements
    in_list.sort()
    for i in range(0, n - 1):
        # initialize left and right
        left = i + 1
        right = n - 1
        x = in_list[i]
        while (left < right):
            if (x + in_list[left] + in_list[right] == 0):
                # print elements if their sum is zero
                print(x, in_list[left], in_list[right])
                left += 1
                right -= 1
                found = True
            # If sum < 0 then increment in left
            elif (x + in_list[left] + in_list[right] < 0):
                left += 1
            # if sum > 0 decrement in right
            else:
                right -= 1
    if (found == False):
        print(" No Triplet Found whose sum to zero")

#Source for initializing list of numbers
import sys
my_list = input('Enter your list: ')
my_list = [int(x) for x in my_list.split(',')]
n = len(my_list)
tripletsumzero(my_list, n)
