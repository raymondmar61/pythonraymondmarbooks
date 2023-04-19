#The Quick Python Book by Naomi Ceder Chapter 03 The Quick Python Overview
integernumbertype = 10 #int
floatnumbertype = 6.91 #float
complexnumbertype = 3 + 2j #complex
booleannumbertype = True #bool
print(5 / 2) #print 2.5
print(5 // 2) #print 2.  Division truncation divide truncate.
print(5 % 2) #print 1
#Built-in functions are called using a standard function calling syntax.  The functions in library modules are available using the import statement.  The module's functions are called using the attribute notation modulename.function(arguments); for example, math.ceil(3.49).
import math
librarymodulemath = math.ceil(3.49)
print(librarymodulemath) #print 4
print(int(booleannumbertype)) #print 1
print(not booleannumbertype) #print False
#List.  Index from the front or the left use positive indexes starting with 0 as the first element.  Index from the back or the right use negative indexes starting with -1 as the first element.  A list slice is [inclusive starting:exclusive ending].  An [:exclusive ending] starts at its beginning.  An [inclusive starting:] ends at its ending.
listintroduction = ["first", "second", "third", "fourth"] #list
print(listintroduction[0]) #print first
print(listintroduction[2]) #print third
print(listintroduction[-1]) #print fourth
print(listintroduction[-2]) #print third
print(listintroduction[:3]) #print ['first', 'second', 'third']
print(listintroduction[0:3]) #print ['first', 'second', 'third']
print(listintroduction[1:3]) #print ['second', 'third']
print(listintroduction[1:-1]) #print ['second', 'third']
print(listintroduction[1:0]) #print []
print(listintroduction[-2:]) #print ['third', 'fourth']
print(listintroduction[-2:-1]) #print ['third']
print(len(listintroduction)) #print 4
print(listintroduction[::-1]) #print ['fourth', 'third', 'second', 'first']
#Tuples are immutable lists which can't be modified.  There are two tuple methods which are count and index.
tupleintroduction = (1, 2, 3, 4, 5, 6, 7, 8, 12) #tuple
#Dictionary.  Dictionaries data type provides associative array functionality implement by using hash tables.
dictionaryintroduction = {1: "one", 2: "two"} #dict
print(dictionaryintroduction.keys()) #print dict_keys([1, 2])
print(list(dictionaryintroduction.keys())) #print [1, 2]
print(tupleintroduction[1]) #print 2
#Sets are unordered collection of objects.  Uniqueness is important.
setintroduction = set([1, 2, 3, 1, 3, 5]) #set
print(setintroduction) #print {1, 2, 3, 5}
print(1 in setintroduction) #print True
print(4 in setintroduction) #print False
#Conditional if else if elif else
x = 5
if x < 5:
    y = -1
    z = 5
elif x > 5:
    y = 1
    z = 11
else:
    y = 0
    z = 10
print(x, y, z) #print 5 0 10
#While loop is executed as long as the condition is true.
u, v, x, y = 0, 0, 100, 30
while x > y:
    u = u + y
    x = x - y
    if x < y + 2:
        v = v + x
        x = 0
    else:
        v = v + y + 2
        x = x - y - 2
print(u, v) #print 60 40
#For loop iterate any iterable such as a list or tuple in a sequence.
forloopitemlist = [3, "string1", 23, 14.0, "string2", 49, 64, 70]
for eachforloopitemlist in forloopitemlist:
    print(str(eachforloopitemlist), end=" ") #print 3 string1 23 14.0 string2 49 64 70
print("\n")
#Functions
def function1(x, y, z):
    value = x + 2 * y + z**2
    if value > 0:
        return x + 2 * y + z**2
    else:
        return 0


print(function1(3, 4, 2)) #print 15
def function2(x, z, y=1):
    value = x + 2 * y + z**2
    if value > 0:
        return x + 2 * y + z**2
    else:
        return 0


print(function2(3, 4)) #print 21
print(function2(z=4, x=3)) #print 21
#Exceptions or errors can be caught using try, except, else, finally statements.
falsenumber = "2350"
try:
    print(falsenumber + 75)
except TypeError:
    print("falsenumber is a string.  The error is TypeError.  Convert to integer to add 75.")
    print(int(falsenumber) + 75)
else:
    print("I can't identify the error.")
finally:
    print("Always print the finally.")
'''
falsenumber is a string.  The error is TypeError.  Convert to integer to add 75.
2425
Always print the finally.
'''
#Object Oriented Programming OOP.  Class example.  The instance initializer method or constructor is always __init__.  Instance variables are created and initialized at __init__.  Methods are like functions in classes defined using the def keyword.  The first argument in any method is self.  Self is set to the instance which invoked the method.
class Shape:
    """Class definition Shape class"""
    def __init__(self, x=1, y=1, r=1):
        self.x = x
        self.y = y
        self.radius = r
    def addnumbers(self):
        return(self.x + self.y)
class Circle(Shape):
    """Circle Class inherits from Shape"""
    pi = 3.14159
    # def __init__(self, r):
    #     self.radius = r
    def area(self):
        """Circle method calculate the area of the circle"""
        return (self.radius * self.radius * self.pi) + self.x + self.y


basicuseclass = Shape(1, 2)
print(basicuseclass.addnumbers()) #print 3
circlearea1 = Circle(1, 2, 5)
print(circlearea1) #print <__main__.Circle object at 0x7fae0b64bca0>
print(circlearea1.radius) #print 5
print(circlearea1.x + circlearea1.y) #print 3
print(circlearea1.radius**2) #print 25
print(circlearea1.area()) #print 81.53975
