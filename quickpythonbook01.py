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

#The Quick Python Book by Naomi Ceder Chapter 04 The Absolute Basics
xvariableassign5value = 5
x = 3
y = 5
zexpression = (x + y) / 2
xstringescapecharacter = "Steve Jobs said,\t \"Stay hungry, stay foolish\"."
print(xstringescapecharacter) #print Steve Jobs said,    "Stay hungry, stay foolish".
print(5 / 2) #print 2.5. floating point.
print(type(5 / 2)) #print <class 'float'>
print(5 / 2.0) #print 2.5. floating point.
print(type(5 / 2.0)) #print <class 'float'>
print(5 // 2) #print 2.  integer.
print(type(5 // 2)) #print <class 'int'>
#Built-in number related functions:  abs, divmod, float, hex, int, max, min, oct, pow, round.
print(divmod(5, 3)) #print (1,2).  5/3 is 1 remainder 2.
print(divmod(11, 3)) #print (3,2).  11/3 is 3 remainder 2.
print(divmod(11, 3)[1]) #print 2
#Need math module for some advanced numeric functions such as trigonometry and hyberbolic.  Noted functions:  ceil, e, exp, floor, log, log10, pow, sqrt.
import math
#print(help(math.exp)) #print Return e raised to the power of x.
print(math.exp(5)) #print 148.4131591025766
#print(help(math.pow)) #print Return x**y (x to the power of y)
print(math.pow(7, 4)) #print 2401.0
print(math.sqrt(81)) #print 9.0

#The Quick Python Book by Naomi Ceder Chapter 05 Lists, Tuples, And Sets
#Lists and tuples are sequence types.
listvariablevarietyofelements = [2, "two", [1, 2, 3]]
print(listvariablevarietyofelements) #print [2, 'two', [1, 2, 3]]
print(len(listvariablevarietyofelements)) #print 3
listindexing = ["first", "second", "third", "fourth"]
print(listindexing)
print(listindexing[0]) #print first
print(listindexing[2]) #print third
print(listindexing[-1]) #print fourth
print(listindexing[-2]) #print third
#List slicing or sublist list[indexnumber1 inclusive: indexnumber2 exclusive]
print(listindexing[1:-1]) #print ['second', 'third']
print(listindexing[0:3]) #print ['first', 'second', 'third']
print(listindexing[-2:-1]) #print ['third']
print(listindexing[:3]) #print ['first', 'second', 'third']
print(listindexing[2:]) #print ['third', 'fourth']
print(listindexing[2::-1]) #print ['third', 'second', 'first']
print(listindexing[2::-2]) #print ['third', 'first']
modifylist = [1, 2, 3, 4]
print(modifylist) #print [1, 2, 3, 4]
modifylist[1] = "two"
print(modifylist) #print [1, 'two', 3, 4]
modifylist = [1, 2, 3, 4]
print(modifylist) #print [1, 2, 3, 4]
modifylist[len(modifylist):] = [5, 6, 7]
print(modifylist) #print [1, 2, 3, 4, 5, 6, 7]
modifylist[:0] = [-1, 0]
print(modifylist) #print [-1, 0, 1, 2, 3, 4, 5, 6, 7]
modifylist[1:-1] = []
print(modifylist) #print [-1, 7]
appendlist = [1, 2, 3]
print(appendlist) #print [1, 2, 3]
appendlist.append("four")
print(appendlist) #print [1, 2, 3, 'four']
appendlist = [1, 2, 3, 4]
print(appendlist) #print [1, 2, 3, 4]
y = [5, 6, 7]
appendlist.append(y)
print(appendlist) #print [1, 2, 3, 4, [5, 6, 7]]
extendlist = [1, 2, 3, 4]
print(extendlist) #print [1, 2, 3, 4]
y = [5, 6, 7]
extendlist.extend(y)
print(extendlist) #print [1, 2, 3, 4, 5, 6, 7]
insertlist = [1, 2, 3]
print(insertlist) #print [1, 2, 3]
insertlist.insert(2, "second index hello")
print(insertlist) #print[ 1, 2, 'second index hello', 3]
insertlist.insert(0, "zero index start")
print(insertlist) #print ['zero index start', 1, 2, 'second index hello', 3]
insertlist.insert(-1, "second to last index hello")
print(insertlist) #print ['zero index start', 1, 2, 'second index hello', 'second to last index hello', 3]
deletelist = ["a", 2, "c", 7, 9, 11]
print(deletelist) #print ['a', 2, 'c', 7, 9, 11]
del deletelist[1]
print(deletelist) #print ['a', 'c', 7, 9, 11]
del deletelist[:2]
print(deletelist) #print [7, 9, 11]
removelist = [1, 2, 3, 4, 3, 5]
print(removelist) #print [1, 2, 3, 4, 3, 5]
removelist.remove(3)
print(removelist) #print [1, 2, 4, 3, 5]
removelist.remove(3)
print(removelist) #print [1, 2, 4, 5]
reverselist = [1, 3, 5, 6, 7]
print(reverselist) #print [1, 3, 5, 6, 7]
reverselist.reverse()
print(reverselist) #print [7, 6, 5, 3, 1]
sortlistinplace = [3, 8, 4, 0, 2, 1]
print(sortlistinplace) #print [3, 8, 4, 0, 2, 1]
sortlistinplace.sort()
print(sortlistinplace) #print [0, 1, 2, 3, 4, 8]
sortlistinplace.sort(reverse=True)
print(sortlistinplace) #print [8, 4, 3, 2, 1, 0]
sortlistinplacestrings = ["Life", "Is", "Enchanting"]
print(sortlistinplacestrings) #print ['Life', 'Is', 'Enchanting']
sortlistinplacestrings.sort()
print(sortlistinplacestrings) #print ['Enchanting', 'Is', 'Life']
#The sort() method returns an error if the list contains both strings and numbers.
#Write function sort a string of lists by number of characters in each word.
def comparenumberofcharacters(inputlist):
    return len(inputlist)


wordlist = ["Python", "is", "better", "than", "C"]
print(wordlist) #print ['Python', 'is', 'better', 'than', 'C']
wordlist.sort()
print(wordlist) #print ['C', 'Python', 'better', 'is', 'than'].  RM:  Upper case letters are first, lower case letters are second.
wordlist = ["Python", "is", "better", "than", "C"]
print(wordlist) #print ['Python', 'is', 'better', 'than', 'C']
print(comparenumberofcharacters(wordlist)) #print 5
wordlist.sort(key=comparenumberofcharacters) #wordlist.sort(key=5) return TypeError: 'int' object is not callable
print(wordlist) #print ['C', 'is', 'than', 'Python', 'better']
wordlist = ["Python", "is", "better", "than", "C"]
print(wordlist) #print ['Python', 'is', 'better', 'than', 'C']
wordlist.sort(key=len)
print(wordlist) #print ['C', 'is', 'than', 'Python', 'better']
tuplenumbers = (4, 3, 1, 2)
print(tuplenumbers) #print (4, 3, 1, 2)
sortedtuplenumbers = sorted(tuplenumbers)
print(sortedtuplenumbers) #print [1, 2, 3, 4]
print(type(sortedtuplenumbers)) #print <class 'list'>
#Sort the second element or index number one in the sublists
from operator import itemgetter #https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
sortlistwithinalist = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
print(sortlistwithinalist) #print [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
sortlistwithinalist.sort(key=itemgetter(1))
print(sortlistwithinalist) #print [[4, 0, 1], [2, 1, 3], [1, 2, 3]]
print(3 in [1, 3, 4, 5])
print(3 not in [1, 3, 4, 5])
concatenatelists = [1, 2, 3] + [4, 5]
print(concatenatelists)
multiplylistelements = ["fournones"] * 4 #RM:  replicates list
print(multiplylistelements) #print ['fournones', 'fournones', 'fournones', 'fournones']
multiplylistelements = [3, 1, 6] * 3
print(multiplylistelements) #print [3, 1, 6, 3, 1, 6, 3, 1, 6]
print(min(multiplylistelements)) #print 1
print(max(multiplylistelements)) #print 6
findindexposition = [1, 3, "five", 7, -2]
print(findindexposition.index(7)) #print 3
print(findindexposition.index("five")) #print 2
countelementsinalist = [1, 2, 2, 3, 5, 2, 5]
print(countelementsinalist.count(2)) #print 3
print(countelementsinalist.count(3)) #print 1
print(countelementsinalist.count(4)) #print 0
print(sum(countelementsinalist)) #print 20
slicenestedlist = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
print(slicenestedlist) #print [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
print(slicenestedlist[0]) #print [0, 1, 2]
print(slicenestedlist[0][1]) #print 1
print(slicenestedlist[2]) #print [20, 21, 22]
print(slicenestedlist[2][2]) #print 22
#Tuples are very similar to lists which can’t be modified; they can only be created
tuplebasics = ("a", "b", "c")
print(tuplebasics) #print ('a', 'b', 'c')
print(tuplebasics[1:]) #print ('b', 'c')
print(len(tuplebasics)) #print 3
print(max(tuplebasics)) #print c
print(min(tuplebasics)) #print a
print(5 in tuplebasics) #print False
print(tuplebasics + tuplebasics) #print ('a', 'b', 'c', 'a', 'b', 'c')
print(tuplebasics * 3) #print ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')
oneelementtupleneedscomma = (7,)
print(oneelementtupleneedscomma) #print (7,)
(one, two, three, four) = (1, 2, 3, 4)
print(one) #print 1
print(two) #print 2
[a, b] = [1, 2]
[c, d] = 3, 4
[e, f] = (5, 6)
(g, h) = 7, 8
i, j = [9, 10]
k, l = (11, 12)
print(a) #print 1
print([b, c, d]) #print [2, 3, 4]
print((e, f, g)) #print (5, 6, 7)
print(h, i, j, k, l) #print 8 9 10 11 12
#Convert list to tuple, convert tuple to list, convert string to list
print(list((1, 2, 3, 4))) #print [1, 2, 3, 4]
print(tuple([1, 2, 3, 4])) #print (1, 2, 3, 4)
print(list("stringtolist")) #print ['s', 't', 'r', 'i', 'n', 'g', 't', 'o', 'l', 'i', 's', 't']
#A set is an unordered collection of objects used when membership and uniqueness are main things
setlist = set([1, 2, 3, 1, 3, 5])
print(setlist) #print {1, 2, 3, 5}
setlist.add(6)
print(setlist) #print {1, 2, 3, 5, 6}
setlist.remove(5)
print(setlist) #print {1, 2, 3, 6}
print(1 in setlist) #print True
setlistappend = set([1, 7, 8, 9])
print(setlist | setlistappend) #print {1, 2, 3, 6, 7, 8, 9}
print(setlist & setlistappend) #print {1}
print(setlist ^ setlistappend) #print {2, 3, 6, 7, 8, 9}
