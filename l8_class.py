#8. Classes
#==================================

#class ClassName(object):
#    --snip--

#One of the popular approach to solve a programming problem is by creating objects. 
#This is known as Object-Oriented Programming (OOP).
#An object has two characteristics:

#		attributes
#		behavior

#A class is a blueprint for the object.
#We can think of class as an sketch of a parrot with labels. It contains all the details about the name, 
#colors, size etc. Based on these descriptions, we can study about the parrot. Here, parrot is an object.

class Calculation:

    def display(self):
        print("I am from person class")

    def add(self,a,b):
        z= a+b
        print("Addition is : {}".format(z))

    def sub(self,a,b):
        z= a-b
        return z

    def mul(self,a,b):
        z= a*b
        return z

    def div(self,a,b):
        z= a/b
        return z


class Person:

    #class instance attribute
    def __init__(self):
        print("I am from Person Class")
        self.name="Not Defined"
        self.age=0

    # def __init__(self, n,a):
    #     print("I am from Person Class")
    #     self.name=n
    #     self.age=a

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self,yourname):
        self.name = yourname

    def setAge(self, yourage):
        self.age = yourage

    def shoW(self):
        print("I am {} and {} years".format(self.name, self.age))

p = Calculation()
p.display()
p.add(3,6)
t=p.sub(7,2)

print("Subtraction is : {}".format(t))
print("Multiplication is : {}".format(p.mul(7,2)))
print("Division is : {}".format(p.div(7,2)))

pp = Person()

pp.setName("AAA")
pp.setAge(77)

pp.shoW()

"""
per = Person("Test",33)

nm = input("Enter Your Name :")
ag = int(input("Enter Your Age :"))
per.setName(nm)
per.setAge(ag)

print(per.getName())
print(per.getAge())
per.shoW()

"""
