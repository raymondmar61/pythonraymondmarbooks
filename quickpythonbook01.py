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

#The Quick Python Book by Naomi Ceder Chapter 06 Strings
sliceastring = "Hello"
print(sliceastring[0]) #print H
print(sliceastring[-1]) #print o
print(sliceastring[1:]) #ello
stripastring = "Goodbye\n"
print(stripastring[:-1]) #print Goodbye
concatenateplussign = "Hello " + "World"
print(concatenateplussign) #print Hello World
duplicatemultiplysign = "multiplytwice" * 2
print(duplicatemultiplysign) #print multiplytwicemultiplytwice
print("override print function no newline\n", end="") #print override print function no newline use end parameter of "" end="" for the print function to not append the newline
joinmethod = ["join", "puts", "spaces", "between", "elements"]
print(" ".join(joinmethod)) #print join puts spaces between elements
print("::".join(joinmethod)) #print join::puts::spaces::between::elements
splitmethod = "You\t\t can have tabs\t\n \t and newlines " "mixed in"
print(splitmethod)
'''
You      can have tabs  
     and newlines mixed in
'''
print(splitmethod.split()) #print ['You', 'can', 'have', 'tabs', 'and', 'newlines', 'mixed', 'in']
splitmethod = "Mississippi split by ss"
print(splitmethod.split("ss")) #print ['Mi', 'i', 'ippi split by ', '']
#Specify how many splits in the second argument.  If you specify n splits, split goes along the input string until it performs n splits which generates a list with n+1 substrings as elements or until it runs out of string.
howmanysplits = "abcd"
print(howmanysplits) #print abcd
print(howmanysplits.split()) #print ['abcd']
#print(howmanysplits.split("", 1)) #print ValueError: empty separator
howmanysplits = "a b c d"
print(howmanysplits) #print a b c d
print(howmanysplits.split()) #print ['a', 'b', 'c', 'd']
print(howmanysplits.split(" ", 1)) #print ['a', 'b c d']
print(howmanysplits.split(" ", 2)) #print ['a', 'b', 'c d']
print(howmanysplits.split(" ", 9)) #print ['a', 'b', 'c', 'd']
#A first argument is required when specifying the number of splits in the second argument.  To split on whitespace runs using the second argument, type None as the first argument.
print(howmanysplits.split(None, 1)) #print ['a', 'b c d']
print(howmanysplits.split(None, 2)) #print ['a', 'b', 'c d']
print(howmanysplits.split(None, 9)) #print ['a', 'b', 'c', 'd']
removewhitespace = "  Hello,       World\t\t"
print(removewhitespace) #print **Hello,       World********
print(removewhitespace.strip()) #print Hello,       World
print(removewhitespace.lstrip()) #print Hello,       World******
print(removewhitespace.rstrip()) #print **Hello,       World
specifycharactersremove = "www.python.org"
print(specifycharactersremove.strip("w")) #print .python.org
print(specifycharactersremove.strip("org")) #print www.python.
print(specifycharactersremove.strip("worg")) #print .python.
print(specifycharactersremove.strip("gorw")) #print .python. #Strip removes any and all characters no matter the order.  RM:  it doesn't work all the time.
print(specifycharactersremove.strip("gorwt")) #print .python.
print(specifycharactersremove.strip("gorwt.")) #print python
print(specifycharactersremove.strip("gorth")) #print www.python.
print(specifycharactersremove.strip("gorth.")) #print www.python
searchinstring = "Mississippi"
print(searchinstring.find("ss")) #print 2
print(searchinstring.find("zz")) #print -1
print(searchinstring.find("ss", 3)) #print 5.  Begin search at the third index position
print(searchinstring.find("ss", 1, 4)) #print 2.  Begin search at the first index position and end at the fourth index position
print(searchinstring.rfind("ss")) #print 5.  Start the search at the end of the string which returns the position of the first character of the last occurrence with respect to the start of the string.  There is no lfind method.
print(searchinstring.startswith("Miss")) #print True
print(searchinstring.startswith("Mist")) #print False
print(searchinstring.endswith("pi")) #print True
print(searchinstring.endswith(("i", "u", "check all strings in tuple"))) #print True.  If the parameter with startswith or endswith is a tuple of strings, both methods check for all the strings in the tuple which returns True if any of them is found.
countcharacters = "Mississippi"
print(countcharacters.count("ss")) #print 2
replacecharacters = "Mississippi"
print(replacecharacters.replace("ss", "+++")) #print Mi+++i+++ippi
changecase = "MiSSiSSippi valley"
print(changecase) #print MiSSiSSippi valley
print(changecase.lower()) #print mississippi valley
print(changecase.upper()) #print MISSISSIPPI VALLEY
print(changecase.capitalize()) #print Mississippi valley.  Capitalize capitalizes the first character of a string.
print(changecase.title()) #print Mississippi Valley
print(changecase.swapcase()) #print mIssIssIPPI VALLEY
splitmethod = "You\t\t can have tabs\t\n \t and newlines " "mixed in"
print(splitmethod.expandtabs(1)) #expandtabs replaces tab characters with the specified number of spaces
'''
You   can have tabs 
   and newlines mixed in
'''
checkstringtext = "stringcheck"
checkstringintegers = "123"
print(checkstringtext.isdigit()) #print False
print(checkstringtext.isalpha()) #print True
print(checkstringintegers.isalpha()) #print False
checkstringtextuppercase = "M"
print(checkstringtextuppercase.isupper()) #print True
print(checkstringtextuppercase.islower()) #print False
checkstringtext = "string check there are spaces returns False"
print(checkstringtext.isalpha()) #print False
#Use the format method to combine a format string containing replacement fields with curly braces {} with replacement values taken from the parameters given to the format command.  Use double curly braces for the literal { or }.  Quick format is "contain string with {}." end with .format(strings for the curlybraces)
formatmethod = "{0} is the {1} of {2}".format("Ambrosia", "food", "the gods")
print(formatmethod) #print Ambrosia is the food of the gods
print("{food} is the food of {user}".format(food="Ambrosia", user="the gods")) #print Ambrosia is the food of the gods
print("{0} is the food of {user[1]}".format("Ambrosia", user=["men", "the gods", "others"])) #print Ambrosia is the food of the gods
print("{0:10} is the food of gods".format("Ambrosia")) #print Ambrosia   is the food of gods.  Ambrosia90 is the food of gods.  10 spaces start at 0 pad with spaces.
print("{0:{2}} is the food of gods".format("Ambrosia", 55, 10)) #print Ambrosia   is the food of gods.  Ambrosia90 is the food of gods.  10 spaces start at 0 pad with spaces using the third parameter or the second index parameter.
print("{food:{width}} is the food of gods".format(food="Ambrosia", width=10)) #print Ambrosia   is the food of gods.  Ambrosia90 is the food of gods.
print("{0:>10} is the food of gods".format("Ambrosia")) #print **Ambrosia is the food of gods.  >10 forces right justify of the field and pads with spaces
print("{0:&>10} is the food of gods".format("Ambrosia")) #print &&Ambrosia is the food of gods.  &>10 forces right justify of the field and pads with ampersands instead of spaces
#String modulus operator.  The left side of the percentage sign is the string.  The right side of the percentage sign is the tuple containing the values to substitute the %s string formatting sequences.
print("%s is the %s of %s" % ("Ambrosia", "food", "the gods")) #print Ambrosia is the food of the gods
print("%s is the %s of %s" % ("Nectar", "drink", "gods")) #print Nectar is the drink of gods
print("%s is the %s of %s" % ("Brussels Sprouts", "food", "foolish")) #print Brussels Sprouts is the food of foolish
#Use %f for floats
print("Pi is %f" % (3.14159)) #print Pi is 3.141590
print("Pi is %.2f" % (3.14159)) #print Pi is 3.14
print("Pi is %6.2f" % (3.14159)) #print Pi is **3.14
print("Pi is %-6f for geometry circles" % (3.14159)) #print Pi is 3.141590 for geometry circles
print("Pi is %-6.2f" % (3.14159)) #print Pi is 3.14**
dictionarymodules = {"e": 2.718, "pi": 3.14159}
print("%(pi).2f - %(pi).4f - %(e).2f" % dictionarymodules)
dictionarymodulesstring = {"e": "letter e", "pi": "letters pi"}
print("%(pi).s %(e).s" % dictionarymodulesstring) #print *null*
print("Include several arguments", "or", "several strings", "are printed on the same line", "separated by spaces and ending with a new line") #print Include several arguments or several strings are printed on the same line separated by spaces and ending with a new line
print("Include several arguments", "or", "several strings", "are printed on the same line", "separated by a vertical line and ending with a new line", sep="|") #print Include several arguments|or|several strings|are printed on the same line|separated by a vertical line and ending with a new line
print("Use print function", "to create a file", "to write everything on the print statement", file=open("printfunctionoutput.txt", "w")) #created text file printfunctionoutput.txt with the sentence Use print function to create a file to write everything on the print statement\n
from os import remove
remove("printfunctionoutput.txt")
value = 42
stringinterpolation = f"The answer is {value}"
print(stringinterpolation) #print The answer is 42
pi = 3.1415
print(f"pi is {pi:{10}.{2}}") #print pi is *******3.1
value = "grapes"
print(f"String interpolation value variable {value}.") #print String interpolation value variable grapes.

#The Quick Python Book by Naomi Ceder Chapter 07 Dictionaries
emptydictionary = {}
emptydictionary[0] = "Hello"
print(emptydictionary) #print {0: 'Hello'}
emptydictionary[1] = "Goodbye"
print(emptydictionary) #print {0: 'Hello', 1: 'Goodbye'}
emptydictionary["two"] = 2
emptydictionary["pi"] = 3.15
print(emptydictionary) #print {0: 'Hello', 1: 'Goodbye', 'two': 2, 'pi': 3.15}
print(emptydictionary["two"] * emptydictionary["pi"]) #print 6.3
englishtofrench = {"red": "rouge", "blue": "bleu", "green": "vert"}
print(englishtofrench) #print {'red': 'rouge', 'blue': 'bleu', 'green': 'vert'}
print(len(englishtofrench)) #print 3
listdictionarykeys = list(englishtofrench.keys())
print(listdictionarykeys) #print ['red', 'blue', 'green']
listdictionaryvalues = list(englishtofrench.values())
print(listdictionaryvalues) #print ['rouge', 'bleu', 'vert']
listdictionarykeysvalues = list(englishtofrench.items())
print(listdictionarykeysvalues) #print [('red', 'rouge'), ('blue', 'bleu'), ('green', 'vert')]
print(englishtofrench.get("blue", "Didn't find blue")) #print bleu
print(englishtofrench.get("chartresue", "Didn't find chartresue")) #print Didn't find chartresue
print(englishtofrench.setdefault("chartresue", "Didn't find chartresue use setdefault to add to englishtofrench dictionary")) #print Didn't find chartresue
print(englishtofrench) #print {'red': 'rouge', 'blue': 'bleu', 'green': 'vert', 'chartresue': "Didn't find chartresue use setdefault to add to englishtofrench dictionary"}
copydictionary = englishtofrench.copy()
print(copydictionary) #print {'red': 'rouge', 'blue': 'bleu', 'green': 'vert', 'chartresue': "Didn't find chartresue use setdefault to add to englishtofrench dictionary"}
updatedictionary = {"white": "blanc", "black": "black?", "red": "rouge", "blue": "override initial blue"}
copydictionary.update(updatedictionary)
print(copydictionary) #print {'red': 'rouge', 'blue': 'override initial blue', 'green': 'vert', 'chartresue': "Didn't find chartresue use setdefault to add to englishtofrench dictionary", 'white': 'blanc', 'black': 'black?'}.  RM:  The updates from the update dictionary or second dictionary overrides matching key-value pairs in the first dictionary.  Same values are not duplicated.
del(copydictionary["chartresue"]) #delete entry, remove entry
print(copydictionary) #print {'red': 'rouge', 'blue': 'override initial blue', 'green': 'vert', ''white': 'blanc', 'black': 'black?'}
print("white" in copydictionary) #print True

#The Quick Python Book by Naomi Ceder Chapter 08 Control Flow
whileloopcondition = 0
while whileloopcondition < 5:
    print("body.  whileloopcondition is a Boolean expression True or False", whileloopcondition)
    whileloopcondition += 1
else:
    print("post while loop code.  Some programmers omit the else because the else statement is optional.", whileloopcondition)
'''
body.  whileloopcondition is a Boolean expression True or False 0
body.  whileloopcondition is a Boolean expression True or False 1
body.  whileloopcondition is a Boolean expression True or False 2
body.  whileloopcondition is a Boolean expression True or False 3
body.  whileloopcondition is a Boolean expression True or False 4
post while loop code.  Some programmers omit the else because the else statement is optional. 5
'''
#while loop two special statements break and continue.  Break terminates the while loop.  Continue causes the remainder of the body to be skipped over.
condition1 = False
condition2 = True
if condition1:
    print("body1")
elif condition2:
    print("body2") #print body2
else:
    print("body")
#if-elif-else statement special statement pass.  Pass performs no action.  Pass is a placeholder statement.
#Case statement use functions and dictionaries
def casea():
    print("casea process")
def caseb():
    print("caseb process")
def casec():
    print("casec process")


casedictionary = {"a": casea, "b": caseb, "c": casec} #RM:  the case function nanes in the casedictionary are not strings
selectcasefunction = "a"
casedictionary[selectcasefunction]() #return casea process

objectyieldsequenceofvalues = [1, 2, 3, 4]
for x in objectyieldsequenceofvalues:
    print(x)
    '''
    1
    2
    3
    4
    '''
else:
    print("The else statement in a for loop is optional.  Break statement and Continue statement are valid in for loops.")
print(list(range(3, 7))) #print [3, 4, 5, 6]
print(list(range(2, 10))) #print [2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 3))) #print []
print(list(range(5, 3, -1))) #print [5, 4]
print(list(range(0, 10, 2))) #print [0, 2, 4, 6, 8]
print(list(range(5, 0, -1))) #print [5, 4, 3, 2, 1]
tupleunpacking = [(1, 2), (3, 7), (9, 5)]
for eachtuple in tupleunpacking:
    print(eachtuple[0] * eachtuple[1])
    '''
    2
    21
    45
    '''
for lefttuple, righttuple in tupleunpacking:
    print(lefttuple * righttuple)
    '''
    2
    21
    45
    '''
#Enumerate function assigns a number with an item in a list.  It returns a tuple of (index position of item,item) in a list.
enumeratelist = [1, 3, -7, 4, 9, -5, 4]
print(enumeratelist) #print [1, 3, -7, 4, 9, -5, 4]
print(enumerate(enumeratelist)) # print <enumerate object at 0x7fed1832a040>
print(list(enumerate(enumeratelist))) #print [(0, 1), (1, 3), (2, -7), (3, 4), (4, 9), (5, -5), (6, 4)]
for index, item in enumerate(enumeratelist):
    print("index position", index, ".  Item is", item, ".")
    '''
    index position 0 .  Item is 1 .
    index position 1 .  Item is 3 .
    index position 2 .  Item is -7 .
    index position 3 .  Item is 4 .
    index position 4 .  Item is 9 .
    index position 5 .  Item is -5 .
    index position 6 .  Item is 4 .
    '''
#Zip function combine two or more iterables.  Zip function combines lists into tuples.  Combine lists to tuples.
firstnumber = [1, 2, 3, 4]
secondstring = ["a", "b", "c"]
combinenumberstringlists = zip(firstnumber, secondstring)
print(list(combinenumberstringlists)) #print [(1, 'a'), (2, 'b'), (3, 'c')
#A list comprehension or comprehension is a list or dictionary as a one line for loop to create a new list or dictionary from a sequence.  newlist = [expression1 for variable in oldlist if expression2].  newdictionary = {expression1:expression2 for variable in list if expression 3}
numberslist = [1, 2, 3, 4]
numberslistsquared = [eachnumberslist * eachnumberslist for eachnumberslist in numberslist]
print(numberslistsquared) #print [1, 4, 9, 16]
numberslistsquaredif = [eachnumberslist * eachnumberslist for eachnumberslist in numberslist if eachnumberslist > 2]
print(numberslistsquaredif) #print [9, 16]
keylist = ["football", "baseball", "basketball", "hockey"]
valuelist = ["49ers", "Giants", "Warriors", "Sharks"]
combinekeylistvaluelist = zip(keylist, valuelist)
print(combinekeylistvaluelist) #print <zip object at 0x7fef9acf0980>
combinekeylistvaluelist = list(zip(keylist, valuelist))
print(combinekeylistvaluelist) #print [('football', '49ers'), ('baseball', 'Giants'), ('basketball', 'Warriors'), ('hockey', 'Sharks')]
bayareasportsdictionary = {key: value for key, value in combinekeylistvaluelist}
print(bayareasportsdictionary) #print {'football': '49ers', 'baseball': 'Giants', 'basketball': 'Warriors', 'hockey': 'Sharks'}
#Python has a Boolean object which can be set to either True or False.  Any expression with a Boolean operation returns True or False.
print(bool(0)) #print False
print(bool(1)) #print True
print(bool(-94531)) #print True
print(bool("")) #print False
print(bool("here is a string")) #print True
print(bool([])) #print False
print(bool(["the", "list", "has", "string", "objects"])) #print True
print(bool({})) #print False
print(bool(set())) #print False
print(bool(None)) #print False
#If an and expression has one false element, the expression is False and the False value is returned.  If an and expression is all True, the expression is True and the last value is returned.  If an or expression has one false element, the expression is True and the True value is returned.  If an or expression is all True, the expression is True and the first value is returned.
print([] and [5]) #print []
print([2] and [3, 4]) #print [3, 4]
print([] or [5]) #print [5]
print([2] or [3, 4]) #print [2]

#The Quick Python Book by Naomi Ceder Chapter 09 Functions
def basicfunction(parameter1, parameter2):
    """Optional documentation string or docstring"""
    print("function body parameter1 " + parameter1)
    print(f"function body parameter2 {parameter2}.")


basicfunction("parameter1apple", "parameter2orange")
'''
function body parameter1 parameter1apple
function body parameter2 parameter2orange.
'''
print(basicfunction.__doc__) #print Optional documentation string or docstring.  Print function definition function description.
def factorial(n):
    """Return the factorial of a given number."""
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r


print(factorial.__doc__) #print Return the factorial of a given number.
print(factorial(4)) #print 24
def power(x, defaultvaluelastonesy=2):
    r = 1
    while defaultvaluelastonesy > 0:
        r = r * x
        defaultvaluelastonesy = defaultvaluelastonesy - 1
    return r


print(power(3, 2)) #print 9
print(power(3)) #print 9
print(power(defaultvaluelastonesy=2, x=3)) #print 9
def foodlist(fruit=False, meat=False, grain=False):
    if not fruit:
        fruit = "No fruit"
    if not meat:
        meat = "No meat"
    if not grain:
        grain = "No grain"
    return fruit, meat, grain


print(foodlist()) #print ('No fruit', 'No meat', 'No grain')
print(foodlist("apple", grain="rice")) #print ('apple', 'No meat', 'rice')
def variablenumberarguments(*lotsofnumbers):
    if len(lotsofnumbers) == 0:
        return None
    else:
        maximumnumber = lotsofnumbers[0]
        for eachlotsofnumbers in lotsofnumbers[1:]:
            if eachlotsofnumbers > maximumnumber:
                maximumnumber = eachlotsofnumbers
        return maximumnumber


print(variablenumberarguments(3, 2, 8)) #print 8
print(variablenumberarguments(1, 5, 9, -2, 2)) #print 9
#Global variables
def globalvariables():
    global aglobalvariable
    aglobalvariable = 1
    blocalvariable = 2
    return aglobalvariable, blocalvariable


aglobalvariable = "one"
blocalvariable = "two"
print(aglobalvariable) #print one
print(blocalvariable) #print two
print(globalvariables()) #print (1,2)
print(aglobalvariable) #print 1
print(blocalvariable) #print two
#Assign functions to variables.  Function a variable assigned.
def addten(inputnumber):
    return inputnumber + 10


variableassignedfunction = addten
print(variableassignedfunction(25)) #print 35
functionindictionary = {"add30": addten, "add55": addten, "add200": addten}
print(functionindictionary["add30"](30)) #print 40
print(functionindictionary["add55"](55)) #print 65
print(functionindictionary["add200"](200)) #print 210
#Define short functions using the lambda expression.  lambda parameter1, parameter2, . . .: expression.  Lambda expressions are anonymous little functions defined inline.  A small function needs to be passed to another function such as the key function used by a list's sort method.
parameter1 = 5
parameter2 = 6
simplelambda = lambda parameter1, parameter2: parameter1*parameter2
print(simplelambda) #print <function simplelambda at 0x7f62fe328280>
print(simplelambda(parameter1,parameter2)) #print 30
lambdaindictionary = {"add30": lambda inputnumber: inputnumber + 30, "add50": lambda inputnumber: inputnumber + 50, "subtract10": lambda inputnumber: inputnumber - 10, "subtractwhat": lambda inputnumber, subtractnumber: inputnumber - subtractnumber}
print(lambdaindictionary["add30"](75)) #print 105
print(lambdaindictionary["subtract10"](75)) #print 65
print(lambdaindictionary["subtractwhat"](100, 30)) #print 70
#Decorators are functions passing as arguments to other functions and passed back as return values from other functions.  A decorator wraps one function inside another with a one-line addition.  A decorator involves two parts which are define the function being wrapped or decorated and use an @ followed by the decorator immediately before the wrapped function is defined
def decorate(functionname):
    print("In decorate function, decorating.  Print the function name being wrapped when the function is defined", functionname.__name__)

    def wrapperfunction(*arguments):
        print("Executing", functionname.__name__)
        return functionname(*arguments)
    return wrapperfunction #Return the wrapped function
@decorate #myfunctionbelowatdecorate is decorated using @decorate
def myfunctionbelowatdecorate(parameter):
    print(parameter)


myfunctionbelowatdecorate("hello")
'''
In decorate function, decorating.  Print the function name being wrapped when the function is defined myfunctionbelowatdecorate
Executing myfunctionbelowatdecorate
hello
'''