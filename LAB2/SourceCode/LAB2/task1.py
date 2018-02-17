#LAB ASSIGNMENT - 2

## QUESTION - 1

#Consider a shop UMKC with dictionary of all book items with their prices.
# Write a program to find the books from the dictionary in the range given by user.

dic_list={"Python" : "15", "Web" : "30", "C" : "20", "Java" : "40", "DeepLearning" : "25"}
print(dic_list) #priniting the list if dictionay items available
#intializing the range values
first=int(input("Enter the Initial Range: "))
last=int(input("Enter the Final Range: "))
print("You can purchase the books listed below:")
for name,cost in dic_list.items(): # for each book name and cost
    if int(cost) in range(first,last+1): #if the cost of book is in price range
        print('%s : %s' %(name, cost)) #the book name is printed