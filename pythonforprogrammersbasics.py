#Python For Programmers by Paul Deitel Chapter 03 Control Statements
grade = 77
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C") #print C
elif grade >= 60:
    print("D")
else:
    print("F")
product = 3
while product <= 50:
    print(product)
    '''
    3
    9
    27
    '''
    product = product * 3
print(product) #print 81
for eachcharacter in "Programming":
    print(eachcharacter, end="") #print Programming
print("\b")
print("Use a line break after a print(, end=\"\")")
print(10, 20, 30) #print 10 20 30
print(10, 20, 30, sep=", ") #print 10, 20, 30
formattedstringvariable = 81.7
print(f"Class average is {formattedstringvariable}.") #print Class average is 81.7.
print(f"Class average is {formattedstringvariable:.2f}.") #print Class average is 81.70.
fieldwidth10with2totheright = 1050
print(f"Compound interest {fieldwidth10with2totheright:10.2f}") #print Compound interest    1050.00.  RM:  exclude the space from the total count 10
print(f"Compound interest right align {fieldwidth10with2totheright:>10.2f}") #print Compound interest right align ***1050.00
print(f"Compound interest left align {fieldwidth10with2totheright:<10.2f}") #print Compound interest left align 1050.00***
from statistics import mean, median, mode
grades = [85, 93, 45, 89, 85]
print(mean(grades)) #print 79.4
print(median(grades)) #print 85
print(mode(grades)) #print 85

#Python For Programmers by Paul Deitel Chapter 04 Functions
def square(number):
    "Calculate the square of a number.  Custom function docstring input here."
    return number**2


print(square(7)) #print 49
print(square(2.5)) #print 6.25
#https://stackoverflow.com/questions/713138/getting-the-docstring-from-a-function
print(square.__doc__) #print Calculate the square of a number.  Custom function docstring input here.
#print(help(square)) #opens the help in CommandPrompt
def maximum(inputparameter1, inputparameter2, inputparameter3):
    maxvalue = inputparameter1
    if inputparameter2 > maxvalue:
        maxvalue = inputparameter2
    if inputparameter3 > maxvalue:
        maxvalue = inputparameter3
    return maxvalue


print(maximum(12, 27, 36)) #print 36
print(maximum(12.3, 45.6, 9.7)) #print 45.6
print(maximum("yellow", "red", "orange")) #print yellow
import random
#guarantee reproducibility of a random sequence such as debugging.  Use the random.seed function.
#randrange generates pseudorandom numbers based on an international calculation which begins with a numeric value known as a seed.  It can be helpful to use the same sequence of random numbers to debug logical errors.  Use the random module seed function to seed the random number generator.  It forces randrange to begin calculating its pseudorandom numbers sequence from the seed you specify.
#Applications requiring secure random numbers such as cryptography, use the secrets module instead of the random module.
for numbersbetweenoneandten in range(5):
    print("A random number between one and ten", random.randrange(1, 10), end=" ") #print A random number between one and ten 1 A random number between one and ten 5 A random number between one and ten 7 A random number between one and ten 2 A random number between one and ten 1
print("\n")

seednumber = 32
random.seed(seednumber) #Define a seed to make random numbers predictable or the same random numbers appear every time
for samerandomnumbers in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 2 2 3 6 2 4 1 6 1
print("\b")
for differentrandomnumbers1 in range(10): #RM:  the differentrandomnumbers*number* generates different values because it continues the pseudorandom number sequence which started at samerandomnumbers
    print(random.randrange(1, 7), end=" ") #print 1 3 5 3 1 5 6 4 3 5
print("\b")
for differentrandomnumbers2 in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 5 2 5 1 4 6 2 3 2
print("\b")
random.seed(seednumber) #start again random.seed(seednumber)
for samerandomnumbers in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 2 2 3 6 2 4 1 6 1
print("\b")
for differentrandomnumbers3 in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 3 5 3 1 5 6 4 3 5
print("\b")
for differentrandomnumbers4 in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 5 2 5 1 4 6 2 3 2
print("\n")

random.seed() #deactivate random.seed or stop random.seed

def displaydice(diceresults):
    die1, die2 = diceresults
    print("The player rolled a", die1, "and a", die2, "totaling", sum(diceresults))

def rolldice():
    die1 = random.randrange(1, 6)
    die2 = random.randrange(1, 6)
    return (die1, die2) #die results returned as a tuple


def firstroll():
    dievalue = rolldice()
    print("Coming out", dievalue)
    displaydice(dievalue)
    sumdievalue = sum(dievalue)
    print("Craps sum =", sumdievalue)
    if sumdievalue in (7, 11):
        return print("Winner")
    elif sumdievalue in (2, 3, 12):
        return print("Loser")
    return sumdievalue


point = firstroll()
print(type(point))
print("Point", point)
if point != None:
    gamestatus = "continue"
    while gamestatus == "continue":
        dievalue = rolldice()
        displaydice(dievalue)
        sumdievalue = sum(dievalue)
        if sumdievalue == 7:
            print("Loser")
            break
        elif sumdievalue == point:
            print("Winner")
            break
        else:
            sumdievalue = sum(rolldice())
'''
Yes first roll crap out
Coming out (1, 1)
The player rolled a 1 and a 1 totaling 2
Craps sum = 2
Loser
<class 'NoneType'>
Point None

No first roll crap out
Coming out (5, 1)
The player rolled a 5 and a 1 totaling 6
Craps sum = 6
<class 'int'>
Point 6
The player rolled a 5 and a 5 totaling 10
The player rolled a 1 and a 2 totaling 3
The player rolled a 3 and a 2 totaling 5
The player rolled a 1 and a 4 totaling 5
The player rolled a 3 and a 4 totaling 7
Loser

No first roll crap out
Coming out (5, 4)
The player rolled a 5 and a 4 totaling 9
Craps sum = 9
<class 'int'>
Point 9
The player rolled a 2 and a 3 totaling 5
The player rolled a 3 and a 3 totaling 6
The player rolled a 3 and a 2 totaling 5
The player rolled a 1 and a 4 totaling 5
The player rolled a 5 and a 1 totaling 6
The player rolled a 2 and a 1 totaling 3
The player rolled a 1 and a 3 totaling 4
The player rolled a 1 and a 4 totaling 5
The player rolled a 4 and a 5 totaling 9
Winner
'''
def functiondefaultvalues(length=2, width=3):
    "Calculate the area of a rectangle.  Default is length 2 and width 3."
    return length * width


print(functiondefaultvalues.__doc__) #print Calculate the area of a rectangle.  Default is length 2 and width 3.
print(functiondefaultvalues(7, 3)) #print 21
print(functiondefaultvalues(width=5, length=2)) #print 10
print(functiondefaultvalues) #print <function functiondefaultvalues at 0x7fa30e1441f0>
print(functiondefaultvalues()) #print 6
print(functiondefaultvalues(width=3.5)) #print 7.0
print(functiondefaultvalues(1.5)) #print 4.5
def multiplearguments(*numbers):
    return sum(numbers), (sum(numbers) / len(numbers))


print(multiplearguments(78, 33, 22, 98)) #print (231, 57.75)
print(multiplearguments(78, 33, 22, 98)[0]) #print 231
print(multiplearguments(78, 33, 22, 98)[1]) #print 57.75
print(type(multiplearguments(78, 33, 22, 98)[1])) #print <class 'float'>
methodexercise = "Hello"
print(methodexercise.lower()) #print hello
print(methodexercise.upper()) #print HELLO

globalvariablex = 7
def accessglobalvariable():
    print("globalvariablex printed from accessglobalvariable function", globalvariablex)


accessglobalvariable() #return globalvariablex printed from accessglobalvariable function 7
def modifyglobalvariable():
    globalvariablex = 3.5
    print("globalvariablex printed from modifyglobalvariable function", globalvariablex)


modifyglobalvariable() #return globalvariablex printed from modifyglobalvariable function 3.5
print(globalvariablex) #print 7
def changeglobalvariable():
    global globalvariablex
    globalvariablex = 178939
    print("globalvariablex printed from changeglobalvariable function", globalvariablex)


changeglobalvariable() #return globalvariablex printed from changeglobalvariable function 178939
print(globalvariablex) #print 178939

#Recursion
#A factorial of a positive integer n written n! pronounced "n factorial."  n * (n-1) *(n-2) . . . 1.  1! equals 1.  0! defined as 1.
factorial = 1
for forloopfactorial in range(5, 0, -1):
    print(factorial, forloopfactorial)
    '''
    1 5
    5 4
    20 3
    60 2
    120 1
    '''
    factorial = factorial * forloopfactorial
print(factorial) #print 120
#A recursive function is capable of solving only the simplest case or base case.  If you call the function with a base case, the function returns a result immediately.  If you call the function with a more complex problem, it divides the problem into two pieces.  The first piece is the function knows how to do.  The second piece is the function doesn't know how to do.  The second piece must be a slightly simpler or smaller version of the original problem.  The function calls a fresh copy of its own function to work on the smaller problem; the new problem resembles the original problem referred to as a recursive call and recursion step.
#The recursion step executes while the original function call is still active.  It can result in many more recursive calls as the function divides each new subproblem into two conceptual pieces.  Each time the function calls itself with a simpler version of the original problem, the sequence of smaller and smaller problems must converge on a base case for the recursion to terminate.  The function returns a result of the previous copy of the function when the function recognizes the base case.
#factorialfunction below explanation.  If number <=1 is True, factorialfunction returns 1 and no further recursion is necessary.  If number is greater than 1, the second return statement is the product of number and a recursive call to factorialfunction which evalulates factorialfunction(number-1).
def factorialfunction(number):
    if number <= 1:
        print("Prepare to return number=1")
        return 1 #base case
    print(number, (number - 1), (number * factorialfunction(number - 1)))
    return number * factorialfunction(number - 1) #recursive call


for i in range(6):
    print(f"{i}!={factorialfunction(i)}")
    print("\n")
'''
Prepare to return number=1
0!=1

Prepare to return number=1
1!=1

Prepare to return number=1
2 1 2
Prepare to return number=1
2!=2

Prepare to return number=1
2 1 2
Prepare to return number=1
3 2 6
Prepare to return number=1
2 1 2
Prepare to return number=1
3!=6

Prepare to return number=1
2 1 2
Prepare to return number=1
3 2 6
Prepare to return number=1
2 1 2
Prepare to return number=1
4 3 24
Prepare to return number=1
2 1 2
Prepare to return number=1
3 2 6
Prepare to return number=1
2 1 2
Prepare to return number=1
4!=24

Prepare to return number=1
2 1 2
Prepare to return number=1
3 2 6
Prepare to return number=1
2 1 2
Prepare to return number=1
4 3 24
Prepare to return number=1
2 1 2
Prepare to return number=1
3 2 6
Prepare to return number=1
2 1 2
Prepare to return number=1
5 4 120
Prepare to return number=1
2 1 2
Prepare to return number=1
3 2 6
Prepare to return number=1
2 1 2
Prepare to return number=1
4 3 24
Prepare to return number=1
2 1 2
Prepare to return number=1
3 2 6
Prepare to return number=1
2 1 2
Prepare to return number=1
5!=120
'''

import math
#RM:  some of the function are standard Python no need to use the math module
roundup = math.ceil(9.2)
print(roundup) #print 10
roundup = math.ceil(-9.8)
print(roundup) #print -9
rounddown = math.floor(9.2)
print(rounddown) #print 9
rounddown = math.floor(-9.8)
print(rounddown) #print -10
exponent = pow(2, 4)
print(exponent) #print 16
squareroot = math.sqrt(9)
print(squareroot)
absolutevalue = abs(-5.1)
print(absolutevalue) #print 5.1
absolutevalue = abs(-700)
print(absolutevalue) #print 700
absolutevaluealwaysfloat = math.fabs(-5.1)
print(absolutevaluealwaysfloat) #print 5.1
absolutevaluealwaysfloat = math.fabs(-700)
print(absolutevaluealwaysfloat) #print 700.0
remainder = 10 % 5
print(remainder) #print 0
remainderalwaysfloat = math.remainder(10, 5)
print(remainderalwaysfloat) #print 0.0
remainderalwaysfloat = math.fmod(10, 5)
print(remainderalwaysfloat) #print 0.0
import statistics as stats
useasclausereferencemodule = [85, 93, 45, 87, 93]
print(stats.mean(useasclausereferencemodule)) #print 80.6
#Avoid wildcard imports from modulename import *; for example, from math import *
print(7 is 7) #print True
print(7 == 7) #print True
print(stats.mean(useasclausereferencemodule) is 80.6) #print False
print(stats.mean(useasclausereferencemodule) == 80.6) #print True
print(stats.mean(useasclausereferencemodule) is stats.mean(useasclausereferencemodule)) #print False

#Python For Programmers by Paul Deitel Chapter 05 Sequences:  Lists And Tuples
integerlist = [-45, 6, 0, 72, 1543]
print(integerlist) #print [-45, 6, 0, 72, 1543]
print(integerlist[0]) #print -45
print(integerlist[-5]) #print -45
print(integerlist[4]) #print 1543
integerlist[-1] = 17
print(integerlist) #print [-45, 6, 0, 72, 17]
lista = [10, 20, 30, 100]
listb = [40, 50]
combinelist = lista + listb #concatenate lists
print(combinelist) #print [10, 20, 30, 100, 40, 50]
print(lista > listb) #print False.  Book said True because lista has four elements.  listb has two elements.
studenttuple = ()
studenttuple = "John", "Green", 3.3
print(studenttuple) #print ('John', 'Green', 3.3)
colors = ["red", "orange", "yellow"]
print(list(enumerate(colors))) #print [(0, 'red'), (1, 'orange'), (2, 'yellow')]
print(tuple(enumerate(colors))) #print ((0, 'red'), (1, 'orange'), (2, 'yellow'))
for index, value in list(enumerate(colors)):
    print(index, value)
    '''
    0 red
    1 orange
    2 yellow
    '''
primitivebarchart = [19, 3, 15, 7, 11]
for index, value in enumerate(primitivebarchart):
    print(index, value, ("*" * value))
    '''
    0 19 *******************
    1 3 ***
    2 15 ***************
    3 7 *******
    4 11 ***********
    '''
slicelistnumbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(slicelistnumbers[2:6]) #print [5, 7, 11, 13]
print(slicelistnumbers[:6]) #print [2, 3, 5, 7, 11, 13]
print(slicelistnumbers[6:]) #print [17, 19]
print(slicelistnumbers[::2]) #print [2, 5, 11, 17]
print(slicelistnumbers[::-1]) #print [19, 17, 13, 11, 7, 5, 3, 2]
print(slicelistnumbers[-3::-2]) #print [13, 7, 3]
slicelistnumbers[0:3] = ["two", "three", "five"]
print(slicelistnumbers) #print ['two', 'three', 'five', 7, 11, 13, 17, 19]
slicelistnumbers[0:3] = []
print(slicelistnumbers) #print [7, 11, 13, 17, 19]
slicetoreplacelistnumbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(slicetoreplacelistnumbers) #print [2, 3, 5, 7, 11, 13, 17, 19]
slicetoreplacelistnumbers[::2] = [100, 100, 100, 100]
print(slicetoreplacelistnumbers) #print [100, 3, 100, 7, 100, 13, 100, 19]
replaceonehundred = [2, 3, 5, 7, 11, 13, 17, 19, 21]
print(replaceonehundred) #print [2, 3, 5, 7, 11, 13, 17, 19, 21]
print(len(replaceonehundred)) #print 9
import math
counter = math.ceil(len(replaceonehundred) / 2) #round up
print(counter) #print 5
blanklist = [100 for i in range(0, counter)]
print(blanklist) #print [100, 100, 100, 100, 100]
replaceonehundred[::2] = blanklist
print(replaceonehundred) #print [100, 3, 100, 7, 100, 13, 100, 19, 100]
#Delete elements delete items from a list
removenumbers = list(range(0, 10))
print(removenumbers) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del(removenumbers[-1])
print(removenumbers) #print [0, 1, 2, 3, 4, 5, 6, 7, 8]
del removenumbers[0:2]
print(removenumbers) #print [2, 3, 4, 5, 6, 7, 8]
del removenumbers[::2]
print(removenumbers) #print [3, 5, 7]
del removenumbers[:]
print(removenumbers) #print []
sortnumbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(sortnumbers) #print [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(sortnumbers.sort()) #print None
sortmethod = sortnumbers.sort() #The .sort method must be stand alone.  No assigned variable.  No inside a print function.
print(sortmethod) #print None
sortedfunction = sorted(sortnumbers)
print(sortedfunction) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sortlettersinstring = "fadgchjebi"
print(sorted(sortlettersinstring, reverse=True)) #print ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
searchlistelement = ["dog", "cat", "bird", "butterfly", "squarrel", "lady bug", "fish", "cat", "squarrel", "parrot", "snake"]
print(searchlistelement.index("bird")) #print 2.  Print index number return index.
print(searchlistelement.index("cat", 3)) #print 7.  Start search for cat at index number 3.
print(searchlistelement.index("squarrel", 0, 5)) #print 4.  Start search for squarrel at index number 0 and end at index 4.
searchlistelement.insert(1, "elephant")
print(searchlistelement) #print ['dog', 'elephant', 'cat', 'bird', 'butterfly', 'squarrel', 'lady bug', 'fish', 'cat', 'squarrel', 'parrot', 'snake']
searchlistelement.append("last animal hamster")
print(searchlistelement) #print ['dog', 'elephant', 'cat', 'bird', 'butterfly', 'squarrel', 'lady bug', 'fish', 'cat', 'squarrel', 'parrot', 'snake', 'last animal hamster']
searchlistelement.extend(["more items", "added as a list"])
print(searchlistelement) #print ['dog', 'elephant', 'cat', 'bird', 'butterfly', 'squarrel', 'lady bug', 'fish', 'cat', 'squarrel', 'parrot', 'snake', 'last animal hamster', 'more items', 'added as a list']
searchlistelement.remove("cat") #.remove deletes the first element in the list starting from the beginning.
print(searchlistelement) #print ['dog', 'elephant', 'bird', 'butterfly', 'squarrel', 'lady bug', 'fish', 'cat', 'squarrel', 'parrot', 'snake', 'last animal hamster', 'more items', 'added as a list']
searchlistelement.clear() #delete all elements in list
quickstringtolist = []
letters = "abcdefghijklmn"
quickstringtolist.extend(letters)
print(quickstringtolist) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
quickstringtolist.reverse()
print(quickstringtolist) #print ['n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
letters = "abcdefghijklmn"
reversedfunction = reversed(letters)
print(reversedfunction) #print <reversed object at 0x7fa649495b50>
reversedletters = [eachletters for eachletters in reversed(letters)]
print(reversedletters) #print ['n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
countelementsinalist = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
for i in range(1, 6):
    print(f"{i} appears {countelementsinalist.count(i)} times.")
    '''
    1 appears 3 times.
    2 appears 5 times.
    3 appears 8 times.
    4 appears 2 times.
    5 appears 2 times.
    '''
searchlistelement = ["dog", "cat", "bird", "butterfly", "squarrel", "lady bug", "fish", "cat", "squarrel", "parrot", "snake"]
copysearchlistelement = searchlistelement.copy()
print(copysearchlistelement) #print ['dog', 'cat', 'bird', 'butterfly', 'squarrel', 'lady bug', 'fish', 'cat', 'squarrel', 'parrot', 'snake']
pushappendpop = []
pushappendpop.append("red") #insert element end of list
print(pushappendpop) #print ['red']
pushappendpop.append("green")
print(pushappendpop) #print ['red', 'green']
pushappendpop.pop() #delete element end of list
print(pushappendpop) #print ['red']
#Lambda to define a function inline.  A lambda expression is an anonymous function without a name.  lambda parameterlist: expression
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
oddnumbers = list(filter(lambda x: x % 2 != 0, numbers))
print(oddnumbers) #print [3, 7, 1, 9, 5]
exponents = list(map(lambda x: x**2, numbers))
print(exponents) #print [100, 9, 49, 1, 81, 16, 4, 64, 25, 36]
exponentslistcomprehension = [eachnumbers**2 for eachnumbers in numbers]
print(exponentslistcomprehension) #print [100, 9, 49, 1, 81, 16, 4, 64, 25, 36]
oddnumbersexponentslistcomprehension = [eachnumbers**2 for eachnumbers in numbers if eachnumbers % 2 != 0]
print(oddnumbersexponentslistcomprehension) #print [9, 49, 1, 81, 25]

#Python For Programmers by Paul Deitel Chapter 06 Dictionaries And Sets
dayspermonth = {"January": 31, "February": 28, "March": 31}
print(dayspermonth) #print {'January': 31, 'February': 28, 'March': 31}
print(len(dayspermonth)) #print 3
for keymonth, valuedays in dayspermonth.items():
    print(keymonth, valuedays)
    '''
    January 31
    February 28
    March 31
    '''
dayspermonth["February"] = 38
print(dayspermonth["February"]) #print 38
dayspermonth["AddApril"] = 31
print(dayspermonth) #print {'January': 31, 'February': 38, 'March': 31, 'AddApril': 31}
del dayspermonth["February"]
print(dayspermonth) #print {'January': 31, 'March': 31, 'AddApril': 31}
print("May" in dayspermonth) #print False
months = {"January": 1, "February": 2, "March": 3}
print(months) #print {'January': 1, 'February': 2, 'March': 3}
savekeysasvariable = months.keys()
print(savekeysasvariable) #print dict_keys(['January', 'February', 'March'])
for eachkey in savekeysasvariable:
    print(eachkey)
    '''
    January
    February
    March
    '''
months["Add December"] = 12
print(months) #print {'January': 1, 'February': 2, 'March': 3, 'Add December': 12}
dictionarylistkeys = list(months.keys())
print(dictionarylistkeys) #print ['January', 'February', 'March', 'Add December']
dictionarylistitems = list(months.items())
print(dictionarylistitems) #print [('January', 1), ('February', 2), ('March', 3), ('Add December', 12)]
print(type(dictionarylistitems)) #print <class 'list'>
print(dictionarylistitems[1]) #print ('February', 2)
print(dictionarylistitems[1][1]) #print 2
countrycodes = {}
countrycodes.update({"South Africa": "ra"}) #insert key value in dictionary countrycodes
print(countrycodes) #print {'South Africa': 'ra'}
countrycodes.update({"Australia": "ar"})
print(countrycodes) #print {'South Africa': 'ra', 'Australia': 'ar'}
countrycodes.update({"Australia": "au"}) #correct value replace value
print(countrycodes) #print {'South Africa': 'ra', 'Australia': 'au'}
dictionarycomprehension = {monthnumber: monthname for monthname, monthnumber in months.items()}
print(dictionarycomprehension) #print {1: 'January', 2: 'February', 3: 'March', 12: 'Add December'}
#A set is an unordered collection of unique values.  Sets may contain only immutable objects such as strings, integers, floats, and tuples which contain immutable elements.  Sets are mutable.  Elements can be added or be removed.
colorsset = {"red", "orange", "yellow", "green", "red", "blue", "blue"}
print(colorsset) #print {'orange', 'green', 'blue', 'red', 'yellow'}
print(len(colorsset)) #print 5
duplicatenumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
print(set(duplicatenumbers)) #print {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print({1, 3, 5} == {3, 5, 1}) #print True
print({1, 3, 5} != {3, 5, 1}) #print False
print({1, 3, 5} < {3, 5, 1}) #print False.  #The less than < operator tests all the elements in the left are in the right.  A proper subset.
print({1, 3, 5} < {7, 3, 5, 1}) #print True
print({1, 3, 5} < {1, 3, 5, 7}) #print True
print({1, 3, 5} <= {3, 5, 1}) #print True.  #The less than or equal to <= operator tests all the elements in the left are in the right and the sets might be equal.  An improper subset.
print({1, 3} <= {3, 5, 1}) #print True.
print({1, 3, 5}.issubset({3, 5, 1})) #print True.  #Use method issubset().  The less than or equal to <= operator tests all the elements in the left are in the right and the sets might be equal.  An improper subset.
print({1, 3}.issubset({3, 5, 1})) #print True.
print({1, 3, 5} > {3, 5, 1}) #print False.  #The greater than > operator tests all the elements in the right are in the left and the left has more elements.  A proper superubset.
print({1, 3, 5, 7} > {3, 5, 1}) #print True.  #The greater than > operator tests all the elements in the right are in the left and the left has more elements.  A proper supersubset.
print({1, 3, 5} >= {3, 5, 1}) #print True.  #The greater than or equal to >= operator tests all the elements in the right are in the left and the sets might be equal.  An improper superset.
print({1, 3, 5, 7} >= {3, 1}) #print True
print({1, 3} >= {3, 1, 7}) #print False
print({1, 3, 5}.issuperset({3, 5, 1})) #print True.  #Use method isupserset().  The greater than or equal to >= operator tests all the elements in the right are in the left and the sets might be equal.  An improper superset.
print({1, 3, 5, 7}.issuperset({3, 2})) #print False
#The union of two sets is a set consisting of all unique elements for both sets.  The binary set operators must be be sets.
print({1, 3, 5} | {2, 3, 4}) #print {1, 2, 3, 4, 5}
print({1, 3, 5}.union({2, 3, 4})) #print {1, 2, 3, 4, 5}
#The intersection of two sets is a set consisting of all the unqiue elements the two sets have in common.
print({1, 3, 5} & {2, 3, 4}) #print {3}
print({1, 3, 5}.intersection({2, 3, 4})) #print {3}
#The difference between two sets is a set consisting of the elements in the left which are not in the right.
print({1, 3, 5} - {2, 3, 4}) #print {1, 5}
print({1, 3, 5}.difference({2, 3, 4})) #print {1, 5}
#The symmetric difference between two sets is a set consisting of the elments of both sets not in common which each other.
print({1, 3, 5} ^ {2, 3, 4}) #print {1, 2, 4, 5}
print({1, 3, 5}.symmetric_difference({2, 3, 4})) #print {1, 2, 4, 5}
#The disjoint returns True or False if both sets don't have any common elements
print({1, 3, 5}.isdisjoint({2, 4, 6})) #print True
print({1, 3, 5}.isdisjoint({4, 6, 1})) #print False
numbersset = {1, 3, 5, 2, 3, 4}
print(numbersset) #print {1, 2, 3, 4, 5}
numbersset.update(range(10))
print(numbersset) #print {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numbersset.add(17)
print(numbersset) #print {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 17}
numbersset.remove(3)
print(numbersset) #print {0, 1, 2, 4, 5, 6, 7, 8, 9, 17}
setcomprehension = {eachnumbersset for eachnumbersset in numbersset if eachnumbersset % 2 == 0}
print(setcomprehension) #print {0, 2, 4, 6, 8}
#The Law Of Large Numbers.  The more number data generated gets closer to the expected average.