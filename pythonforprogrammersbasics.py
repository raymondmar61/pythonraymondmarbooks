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
