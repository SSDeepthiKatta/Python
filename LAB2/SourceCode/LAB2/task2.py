## LAB ASSIGNMENT - 2

## QUESTION -2

##With any given number n,
# In any mobile , there is contact list.
# Create a list of contacts and then prompt the user to do the following:
#  a)Display contact by name
#  b)Display contact by number
#  c)Edit contact by name
#  d)Exit
#  Based on the above scenario, Write a single program to perform the above the operations.
#  Each time an operation is performed on the list, the contact list should be displayed


contact_list = [{"name":"satya", "number":1234567890, "email":"satya@gmail.com"},
                {"name":"sandy", "number":2345678901, "email":"sandy@gmail.com"},
                {"name":"rocky","number":3456789012,"email":"rocky@gmail.com"}]

while True:
    print('''   Would you like to:
                1.) Display contact by Name 
                2.) Display contact by Number
                3.) Edit a Contact by Name
                4.) Quit''')

    sel = input("Select an option: ") # for selecting a option in the given list

    if sel == "1": #if selection is 1 then display contact details by name
     name = input("Enter Name: ") #enter a name to search
     for i in contact_list: # for loop to find name is present in contact list
      if name in i.values():
       print("Contact details of the entered name:")
       print(i) #details are printed

    elif sel == "2": #if selection is 2 then display conatct details by number
        num = int(input("Enter Contact: ")) #enter a number to search
        for j in contact_list:# for loop to find number is present in contact list
            if num in j.values():
                print("Details of the entered number:")
                print(j)

    elif sel == "3":
        in_name = input("Enter name to edit its contact: ")
        for k in contact_list: #for loop to search for entered name
            if in_name in k.values():
                print(k) #displaying entered name details
                newnum = int(input("Enter New Number: "))
                k["number"] = newnum #new number is assigned to the contact
                print("Contact Modified!")
                #print(k)
                print("Contact list with modified contact:")
            print(k) #printing contact list after modifying the contact

    elif sel == "4":
        print("Program Quit!")
        break
    else:
     print("Invalid Input! Try again.") #if selected is in not among 4 given options
     break
