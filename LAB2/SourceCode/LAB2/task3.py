##LAB ASSIGNMENT - 2

## QUESTION - 3


# AIRLINE BOOKING RESERVATION SYSTEM #

class Booking:         #class to book ticket
    def __init__(self, e, b):  #initializing constructor
        self.economy_class = e
        self.business_class = b

    def get_Economy_class(self): # function to book economy class seat
        print("Airlines Class:" + str(self.economy_class))

    def get_Business_class(self): #funtion to book business class seat
        print("Airlines Class:" + str(self.business_class))

class Airline:            # class to book a flight ticket
    def __init__(self, num, name):       # _init_ constructor intializing value
        self.flight_number = num
        self.flight_name = name

    def get_flight_number(self):
        print("Airlines Number: " + str(self.flight_number))

    def get_flight_name(self):
        print("Airlines Name: " + str(self.flight_name))


class Seat:              # class to book a seat for the ticket
    def __init__(self, n, p):  #init constructor initializing seat number and seat letter
        self.seat_number = n
        self.seat_letter = p

    def get_seat_number(self):
        print("Reserved Seat Number: " + str(self.seat_number))

    def get_seat_letter(self):
        print("Reserved Seat Letter: " + str(self.seat_letter))


class Person:     # Class person gets the details of the traveller
    count = 0

    def __init__(self, a, b, c, d, e):   #init constructor
        self.first_name = a    #getting persons first and last name
        self.last_name = b       #along with age and ID
        self.age = c
        self.ID = d
        self.SSN = e

        Person.count += 1 #count is incremented for each traveller
     #functions are created to get travellers details
    def get_first_name(self):
        print("Traveler's First Name:" + str(self.first_name))

    def get_last_name(self):
        print("Traveler's Last Name:" + str(self.last_name))

    def get_age(self):
        print("Traveler's Age:" + str(self.age))

    def get_ID(self):
        print("Traveler's Ticket ID:" + str(self.ID))

    def __get_SSN(self):  #using private data member
        print("Traveler's SSN:" + str(self.SSN))

#objects are created for Person Class
person1 = Person("Samyu", "Khanna", "22", "1234", "987654321")
#Printing details of objects created
print("--From the Person class--")
person1.get_first_name()
person1.get_last_name()
person1.get_age()
person1.get_ID()

# Using Multiple Inheritance..
# Passenger class created with inheriting all the above four classes
class Passenger(Person, Seat, Booking, Airline):
    def __init__(self, f, l, a, id, ssn, fn, fno, sn, sno, e, b):  #init constructor
        Person.__init__(self, f, l, a, id, ssn)
        Airline.__init__(self, fn, fno)
        Seat.__init__(self, sn, sno)
        Booking.__init__(self, e, b)  #calling the super class constructor

#
print("--After using Multiple Inheritance,From Passenger class--")
person2 = Passenger("Sydney", "Sheldon", "42", "1435", "123456789", "3435", "Delta", "15", "K", "Economy","Business")
person2.get_first_name()
person2.get_last_name()
person2.get_age()
#person2.__get_SSN()
person2.get_seat_number()
person2.get_seat_letter()
person2.get_Economy_class()
person2.get_flight_name()
person2.get_flight_number()
person2.get_ID()
