#Automate The Boring Stuff With Python By Al Sweigart Chapter 01 Python Basics
print("Alice" + "Bob") #print AliceBob
print("Alice" * 5) #print AliceAliceAliceAliceAlice
variables = "Variables is one word consisting of letters, numbers, and the underscore.  It can't begin with a number."
print(variables) #print Variables is one word consisting of letters, numbers, and the underscore.  It can't begin with a number.
print(42 == "42") #print False
print(42 == 42.0) #print True
print(42.0 == 0042.0000) #print True

#Automate The Boring Stuff With Python By Al Sweigart Chapter 02 Flow Control
spam = True
print(spam) #print True
print(2 != 3) #print True
name = "Mary"
password = "swordfish"
if name == "Mary":
    if password == "swordfish":
        print("Access granted.") #print Access granted.
    else:
        print("Wrong password")
name = "Mary"
password = "halibit"
if name == "Mary":
    if password == "swordfish":
        print("Access granted.")
    else:
        print("Wrong password") #print Wrong password
name = "Alice"
age = 10
if name == "Alice":
    print("Hi, Alice") #print Hi, Alice
elif age < 12:
    print("You are not Alice")
name = "Julie"
age = 10
if name == "Alice":
    print("Hi, Alice")
elif age < 12:
    print("You are not Alice") #print You are not Alice
name = "Alice"
age = 10000
if name == "Alice":
    print("Hi, Alice") #print Hi, Alice
elif age < 12:
    print("You are not Alice")
elif age > 2000:
    print("Alice is not an undead, immortal vampire")
name = "Beth"
age = 10000
if name == "Alice":
    print("Hi, Alice") #print Hi, Alice
elif age < 12:
    print("You are not Alice")
elif age > 2000:
    print("Alice is not an undead, immortal vampire") #print Alice is not an undead, immortal vampire
while True:
    name = input("Who are you?  Enter Joe to proceed; otherwise, while loop goes back to the top of while loop ")
    if name != "Joe":
        continue
    password = input("What is the password?  It's a fish ")
    if password == "swordfish":
        print("Exiting while loop.  Break")
        break
print("Exit while loop")
import sys
while True:
    response = input("Terminate a program or exit calling sys.exit() function.  Type exit to exit. ")
    if response == "exit":
        sys.exit()
    else:
        continue

#Automate The Boring Stuff With Python By Al Sweigart Chapter 03 Functions
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"


r = random.randint(1, 9)
fortune = getAnswer(r)
print(r) #print 2
print(fortune) #print It is decidedly so

#local variables and global variables
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0


spam() #return 99

def bacon2():
    ham = 101
    eggs = 0
def spam2():
    eggs = 99
    bacon2()
    print(eggs)


spam2() #return 99

def spam3():
    eggs = "spam3 function eggs local variable"
    print(eggs)
def bacon3():
    eggs = "bacon3 function eggs local variable"
    print(eggs)
    spam3()
    print(eggs)


eggs = "eggs global variable"
bacon3()
'''
bacon3 function eggs local variable
spam3 function eggs local variable
bacon3 function eggs local variable
'''
print(eggs) #print eggs global variable

def spam4():
    global eggs
    eggs = "spam4 function eggs global variable"


eggs = "eggs global variable"
spam4()
print(eggs) #print spam4 function eggs global variable
