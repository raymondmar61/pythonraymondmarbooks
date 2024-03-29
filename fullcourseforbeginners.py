#Learn Python - Full Course for Beginners [Tutorial] [rfscVS0vtbw] https://www.youtube.com/watch?v=rfscVS0vtbw
print("Hello World") #print Hello World
stringvariable = "a container which stores data values"
print("The explanation of a variable is " + stringvariable + ".") #print The explanation of a variable is A container which stores data values.
numericalvariable = 99
print("Use a comma for a number or numerical variable", numericalvariable, ".") #print Use a comma for a number or numerical variable 99 .
booleanvariable = True
print("Also use a comma for True or False booleans", booleanvariable) #print Use True or False for booleans True
print("An escape character is a backslash \". I want the one double quote.") #print An escape character is a backslash ". I want the one double quote.
phrase = "Giraffe Academy"
print(phrase) #print Giraffe Academy
print(phrase.lower()) #print giraffe academy
print(phrase.upper()) #print GIRAFFE ACADEMY
print(phrase.isupper()) #print False
print(phrase.upper().isupper()) #print True
print(len(phrase)) #print 15
print(phrase[0]) #print G
print(phrase[3]) #print a
print(phrase.index("G")) #print 0 #Find index position of a string
print(phrase.index("a")) #print 3
print(phrase.index("Acad")) #print 8
print(phrase.replace("Giraffe", "Elephant")) #print Elephant Academy
print(2.0987)
print(10 % 3) #print 1.  Modulo operator returns the remainder
number = -5
print(abs(number)) #print 5
print(pow(3, 2)) #print 9
print(max(4, 6, number)) #print 6
print(min(4, 6, number)) #print -5
print(round(3.2)) #print 3
print(round(3.7)) #print 4
import math #RM:  Save time import the math module with the asterisk from math import *.  I choose import math to emphasize the math module for these methods.
print(math.floor(3.2)) #print 3
print(math.ceil(3.2)) #print 4
print(math.floor(3.7)) #print 3
print(math.ceil(3.7)) #print 4
print(math.sqrt(36)) #print 6
# userinputname = input("Input prompt Enter your name: ")
# userinputage = int(input("Input prompt Enter your age: "))
# print("Hello " + userinputname + "!  You're", userinputage) #print Hello userinputname!  You're 25
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
datatypeslist = ["Kevin", 2, True]
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
print(datatypeslist) #print ['Kevin', 2, True]
print(friendslist[2]) #print Jim
print(friendslist[-1]) #print Toby
print(friendslist[1]) #print Karen
print(friendslist[-2]) #print Oscar
print(friendslist[1:]) #print ['Karen', 'Jim', 'Oscar', 'Toby']
print(friendslist[1:3]) #print ['Karen', 'Jim']
friendslist[1] = "Change from Karen to Mike"
print(friendslist) #print ['Kevin', 'Change from Karen to Mike', 'Jim', 'Oscar', 'Toby']
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
luckynumbers = [4, 8, 15, 16, 23, 42]
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
friendslist.extend(luckynumbers) #append lists
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friendslist.append("Creed")
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 'Creed']
friendslist.insert(1, "Add at index one Kelly")
print(friendslist) #print ['Kevin', 'Add at index one Kelly', 'Karen', 'Jim', 'Oscar', 'Toby', 'Creed']
friendslist.remove("Jim")
print(friendslist) #print ['Kevin', 'Add at index one Kelly', 'Karen', 'Oscar', 'Toby', 'Creed']
friendslist.clear()
print(friendslist) #print []
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friendslist.pop() #delete the item on the furthest right of a list or last itme in a list
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar']
print(friendslist.index("Kevin")) #print 0
friendslist = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friendslist.count("Jim")) #print 2
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friendslist.sort()
print(friendslist) #print ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']
friendslist.reverse()
print(friendslist) #print ['Toby', 'Oscar', 'Kevin', 'Karen', 'Jim']
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
copyfriendslist = friendslist.copy()
print(copyfriendslist) #print ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#A tuple is immutable.  A tuple can't be changed.  A good example is coordinates in an cartisan coordinate graph.
coordinates = (4, 5)
print(coordinates) #print (4, 5)
print(coordinates[0]) #print 4
tupleslist = [(4, 5), (6, 7), (80, 34)]
print(tupleslist[2]) #print (80, 34)
print(tupleslist[2][1]) #print 34

#Functions
def functionnamesayhi(parametervariable, parameterage):
    print("Hello User " + parametervariable + ", you are " + str(age))


personname = "Mike"
age = 35
functionnamesayhi(personname, age) #return Hello User Mike, you are 35.  Calling function to execute function.  Calls function.
personname = "Steve"
age = 70
functionnamesayhi(personname, age) #return Hello User Steve, you are 70
def cube(number):
    return number * number * number
    print("The print statement is not printed below the return keyword.  return breaks out of the function.")


print(cube(3)) #print 27
resultvariable = cube(4)
print(resultvariable) #print 64

#If statements
ismale = False
istall = False
if ismale or istall:
    print("Execute when the if is True.  You are a male or tall or both.")
else:
    print("Execute when the condition above is False.  You are neither male nor tall.") #print Execute when the condition above is False.  You are neither male nor tall.
ismale = True
istall = True
if ismale and istall:
    print("Execute when the if is True.  You are a tall male.") #print Execute when the if is True.  You are a tall male.
else:
    print("Execute when the condition above is False.  You are either not male or tall or both.")
ismale = False
istall = True
if ismale and istall:
    print("Execute when the if is True.  You are a tall male.")
elif ismale and not(istall):
    print("You are a short male.")
elif not ismale and (istall):
    print("You are a tall female.") #print You are a tall female.
else:
    print("You are a short female.")
def maximumnumber(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(maximumnumber(3, 40, 5)) #print 40

num1 = 6
# num1 = float(input("Enter first number: "))
operator = "*"
# operator = input("Enter operator +, -, *, /: ")
num2 = 5.23
# num2 = float(input("Enter second number: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2) #print 31.380000000000003
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

#Dictionary
monthconversion = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June", "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}
print(monthconversion) #print {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April', 'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August', 'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'}
print(monthconversion["Nov"]) #print November
print(monthconversion.get("Dec")) #print December
print(monthconversion.get("Luv")) #print None
print(monthconversion.get("Luv", "Default valid not a valid Key")) #print Default valid not a valid Key

#While loop
counteri = 1
while counteri <= 10:
    print("Condition variable counteri is true", counteri)
    '''
    Condition variable counteri is true 1
    Condition variable counteri is true 2
    Condition variable counteri is true 3
    Condition variable counteri is true 4
    Condition variable counteri is true 5
    Condition variable counteri is true 6
    Condition variable counteri is true 7
    Condition variable counteri is true 8
    Condition variable counteri is true 9
    Condition variable counteri is true 10
    '''
    counteri += 1
print("counteri is 11.  Exit while loop.  While loop counteri completed.") #print counteri is 11.  Exit while loop.  While loop counteri completed.
# secretword = "giraffe"
# guess = ""
# guesscount = 0
# guesslimit = 3
# outofguesses = False
# while guess != secretword and outofguesses is False:
#     if guesscount < guesslimit:
#         print("Cheat.  The secret word is " + secretword)
#         guess = input("Enter guess: ")
#         #guess = secretword #cheat to immediately exit while loop
#         guesscount += 1
#     else:
#         outofguesses = True
# if outofguesses:
#     print("You lose!  Exit while loop.")
# else:
#     print("You win!  Exit while loop.")
secretword = "giraffe"
guess = ""
guesscount = 0
guesslimit = 3
while guess != secretword:
    if guesscount == guesslimit:
        print("You lose!  Exit while loop.")
        break
    else:
        print("Cheat.  The secret word is " + secretword)
        guess = input("Enter guess: ")
        #guess = secretword #cheat to immediately exit while loop
        if guess == secretword:
            print("You win!  Exit while loop.")
            break
        guesscount += 1
for differentvaluevariable in "letter in string":
    print(differentvaluevariable) #print l\n e\n t\n t\n e\n r\n \n i\n n\n \n s\n t\n r\n i\n n\n g
arrayvariable = ["Jim", "Karen", "Kevin"]
for friend in arrayvariable:
    print(friend)
    '''
    Jim
    Karen
    Kevin
    '''
for index in range(3, 10):
    print(index) #print 3\n 4\n 5\n 6\n 7\n 8\n 9
for arrayvariableindex in range(len(arrayvariable)):
    print(arrayvariable[arrayvariableindex])
    '''
    Jim
    Karen
    Kevin
    '''
print(2**3) #print 8 RM:  exponents
def raisetopower(basenumber, powernumber):
    result = 1
    for index in range(powernumber):
        result = result * basenumber
    return result


print(raisetopower(2, 3)) #print 8
print(raisetopower(3, 2)) #print 9
print(raisetopower(3, 4)) #print 81
twodimensionlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]
print(twodimensionlist[0][0]) #print 1
print(twodimensionlist[2][1]) #print 8
for row in twodimensionlist:
    print(row)
    '''
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    [0]
    '''
    for column in row:
        print(column)
        '''
        1
        2
        3
        4
        5
        6
        7
        8
        9
        0
        '''
#Giraffe language.  All vowels is the letter g.  For example, dog is dgg, cat is cgt.
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


#print(translate(input("Enter a phrase: "))) #dog prints dgg
print(translate("To be or not to be")) #print Tg bg gr ngt tg bg
print(translate("On")) #print Gn
number = int(input("Enter an integer number: "))
print(number) #print 4

number = "String input"
try:
    print(int(number))
except ValueError:
    print("ValueError print statement") #print ValueError print statement

try:
    number = int(input("Enter an integer number: "))
    print("Valid input " + str(number)) #print Valid input 4.  RM:  I can't get any of the excepts to be printed.  invalid literal for int() with base 10: 'were' is returned.
except ZeroDivisionError as saveerrorasvariable:
    print("Divided by zero")
except ValueError as saveerrorasvariable:
    print(saveerrorasvariable)
except:
    print("What the heck.  The default except must be last.")
variablerepresentfile = open("/home/mar/python/employees.txt", "r")
print(variablerepresentfile.readable()) #print True
print(variablerepresentfile.read())
'''
Jim - Salesman
Dwight - Salesman
Pam - Receptionist
Michael - Manager
Oscar - Accountant
'''
print(variablerepresentfile.readline()) #print Jim - Salesman.  RM:  readline() works if no read().
print(variablerepresentfile.readline()) #print Dwight - Salesman.  RM:  readline() works if no read().
print(variablerepresentfile.readline()) #print Pam - Receptionist.  RM:  readline() works if no read().
print(variablerepresentfile.readlines()) #print ['Jim - Salesman\n', 'Dwight - Salesman\n', 'Pam - Receptionist\n', 'Michael - Manager\n', 'Oscar - Accountant'].  RM:  readline() works if no read().
for x in variablerepresentfile:
    print(x)
    '''
    Jim - Salesman

    Dwight - Salesman

    Pam - Receptionist

    Michael - Manager

    Oscar - Accountant
    '''
for xreadlines in variablerepresentfile.readlines():  #readline() works if no read().
    print(xreadlines)
    '''
    Jim - Salesman

    Dwight - Salesman

    Pam - Receptionist

    Michael - Manager

    Oscar - Accountant
    '''
variablerepresentfile.close()

with open("/home/mar/python/employees.txt", "r") as anothervariablepresentfile:
    print(anothervariablepresentfile) #print <_io.TextIOWrapper name='/home/mar/python/employees.txt' mode='r' encoding='UTF-8'>
    for x in anothervariablepresentfile:
        print(x)
        '''
        Jim - Salesman

        Dwight - Salesman

        Pam - Receptionist

        Michael - Manager

        Oscar - Accountant
        '''
variablerepresentfile = open("/home/mar/python/employees.txt", "a")
variablerepresentfile.write("\nToby - Human Resources")
variablerepresentfile.write("\nKelly - Customer Service")
variablerepresentfile.close()
'''
usefultools.py module Python file

import random
feetinmile = 5280
metersinkilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]
def getfileextension(filename):
    return filename[filename.index(".") + 1:]
def rolldice(number):
    return random.randint(1, number)
'''
#Modules webpage module webpage docs.python.org/3/py-modindex.html.  Modules with a lib reference is an external module saved to the lib directory.  Modules without a lib reference are built-in to Python.  /usr/local/lib/python3.8/dist-packages? for my Ubuntu.  No.  /home/mar/.local/lib/python3.8/site-packages.  Yes.  Module location module files modules file modules folder modules directory.

import usefultools
print(usefultools.feetinmile) #print 5280
print(usefultools.beatles) #print ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr']
print(usefultools.beatles[1]) #print Paul McCartney
print(usefultools.getfileextension("text.txt")) #print txt
print(usefultools.rolldice(10)) #print 10
class Student:
    def __init__(self, name, major, gpa, isonprobation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isonprobation = isonprobation


student1 = Student("Jim", "Business", 3.1, False)
print(student1) #print <__main__.Student object at 0x7fa1597334c0>
print(student1.name) #print Jim
print(student1.gpa) #print 3.1
student2 = Student("Pam", "Art", 2.5, True)
print(student2) #print <__main__.Student object at 0x7fb275227850>
print(student2.name) #print Pam
print(student2.gpa) #print 2.5
questionprompts = ["What color are applies?\n(a) Red or Green\n(b) Purple\n(c) Orange\n\n", "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n", "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"]
for eachquestion in questionprompts:
    print(eachquestion)
    '''
    What color are applies?
    (a) Red or Green
    (b) Purple
    (c) Orange


    What color are Bananas?
    (a) Teal
    (b) Magenta
    (c) Yellow


    What color are strawberries?
    (a) Yellow
    (b) Red
    (c) Blue
    '''

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questionsandanswers = [Question(questionprompts[0], "a"), Question(questionprompts[1], "c"), Question(questionprompts[2], "b")]
def quiz(inputquestions):
    #print(inputquestions) #print ['What color are applies?\n(a) Red or Green\n(b) Purple\n(c) Orange\n\n', 'What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n', 'What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n']
    score = 0
    for eachinputquestions in inputquestions:
        print("eachinputquestions.prompt " + eachinputquestions.prompt)
        print("eachinputquestions.answer " + eachinputquestions.answer)
        useranswer = input(eachinputquestions.prompt)
        if useranswer == eachinputquestions.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questionprompts)) + " correct")


quiz(questionsandanswers)
'''
eachinputquestions.prompt What color are applies?
(a) Red or Green
(b) Purple
(c) Orange


eachinputquestions.answer a
What color are applies?
(a) Red or Green
(b) Purple
(c) Orange

a
eachinputquestions.prompt What color are Bananas?
(a) Teal
(b) Magenta
(c) Yellow


eachinputquestions.answer c
What color are Bananas?
(a) Teal
(b) Magenta
(c) Yellow

b
eachinputquestions.prompt What color are strawberries?
(a) Yellow
(b) Red
(c) Blue


eachinputquestions.answer b
What color are strawberries?
(a) Yellow
(b) Red
(c) Blue

c
You got 1/3 correct
'''
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def honorroll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    def favoritehobby(self, hobby):
        print(self.name + "'s favorite hobby is " + hobby + ".")


student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)
print(student1.honorroll()) #print False
print(student2.honorroll()) #print True
student1.favoritehobby("cooking") #return Oscar's favorite hobby is cooking.
student2.favoritehobby("sewing") #return Phyllis's favorite hobby is sewing.

class Chef:
    def makechicken(self):
        print("The chef makes a chicken")
    def makesalad(self):
        print("The chef makes a salad")
    def makespecialdish(self):
        print("The chef makes bbq ribs")

#class inheritance.  Chinesechef class uses Chef class functions.
class Chinesechef(Chef):
    def makefriedrice(self):
        print("The chef makes fried rice")
    def makespecialdish(self):
        print("The chef makes orange chicken")


mychef = Chef()
mychef.makechicken() #return The chef makes a chicken
mychef.makespecialdish() #return The chef makes bbq ribs
mychinesechef = Chinesechef()
mychinesechef.makespecialdish() #return The chef makes orange chicken
mychinesechef.makesalad() #return The chef makes a salad
mychinesechef.makechicken() #return The chef makes a chicken
