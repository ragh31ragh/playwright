from mako.util import FastEncodingBuffer

print("############Removing duplicates from list############")
##converting to list , but is does not preserve order
list1=[1,2,2,23,4,4,543,2,2,3,5,6,7,7]
b=set(list1)
print(b)
##converint to dictionary , it will preserve order

c=dict.fromkeys(list1)
print(c)
d = list(c)
print(d)
print(list1)

'''Create student class that takes name & marks of 3 subjects as arguments in constructor. 
Then create a method to print the average'''
class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def calc_average(self):
        average = (self.sub1 + self.sub2 + self.sub3) / 3
        return average

s1 = Student("rd",43,29,33)
print("Average")
print(s1.calc_average())

####Abstraction
###Hiding the implementation details of a class and only showing the essential features to the user.
## we have hided unwanted feature which is required to start the car s
class Car:
    def __init__(self):
        self.accl = False
        self.brk = False
        self.clutch = False

    def Start(self):
        self.accl = True
        self.brk = True
        self.clutch = True
        print ("Car Started")

c1 = Car()
c1.Start()

####Encapsulation
###Capsule of data and related function
'''Python Inheritance
Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

Types of Inheritance:
Single Inheritance: A child class inherits from a single parent class.
Multiple Inheritance: A child class inherits from more than one parent class.
Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
Hybrid Inheritance: A combination of two or more types of inheritance.'''

#SingleInheritance
class Dog:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(f"Dog's name : {self.name}")

class Labrador(Dog): #Single Inheritance
    def sound(self):
        print("labrador woofs")

#Multilevel Inheritance
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name}Guildes the way ")

#Multiple Inheritance
class Friendly :
    def greet(self):
        print("Friendly")

class GoldenRetriever(Dog,Friendly):#Multiple Inheritance
    def sound(self):
        print ("Golden Retriever Barks")

#Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.sound()
retriever.greet()