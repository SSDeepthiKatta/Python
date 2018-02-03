# LAB ASSIGNMENT -1
# created by SSDK

##QUESTION - 4

#Python code to print the list of students
#who are common in both the classes
#list who are not common in both Python and Web Classes

def common(list1, list2): #function to print common students list
    result = []
    for element in list1: #iterates throught Pythonn class for each student
    # if same stdent appears in Web class from Python class,then if loop is iterated.
        if element in list2:
            result.append(element)
    print("List of students common in both classes: ", result)
    return result

def not_common(list1, list2): #function to print not common in both classes
    result1 = []
    #searches for students who are in Python class but not in Web class
    for element in list1:
        if element not in list2:
            result1.append(element)

    #searches for students who are in Web class but not in Python class
    for element in list2:
        if element not in list1:
            result1.append(element)
    print("List of students not common in both classes: ", result1)

    return result1

#Source - initializing Stduent's list
Python = "Ryan", "Jack", "Oliver", "William"
print("Students in Python class", Python)
Web = "Bob", "Jack", "William", "Adam"
print("Students in Web class", Web)
#functions to print list of studennts common and not common in both classes
common(Python,Web)
not_common(Python,Web)