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

#Automate The Boring Stuff With Python By Al Sweigart Chapter 04 Lists
animallist = ["cat", "bat", "rat", "elephant"]
print(animallist) #print ['cat', 'bat', 'rat', 'elephant']
print(animallist[0]) #print cat
print(animallist[3]) #print elephant
print(animallist[-1]) #print elephant
print(animallist[-3]) #print bat
print("The " + animallist[1] + " ate the " + animallist[0]) #print The bat ate the cat
print("The " + animallist[-3] + " ate the " + animallist[-4]) #print The bat ate the cat
print(animallist[0:4]) #print ['cat', 'bat', 'rat', 'elephant']
print(animallist[:]) #print ['cat', 'bat', 'rat', 'elephant']
print(animallist[0:]) #print ['cat', 'bat', 'rat', 'elephant']
print(animallist[1:3]) #print ['bat', 'rat']
print(animallist[:2]) #print ['cat', 'bat']
print(animallist[0:-1]) #print ['cat', bat', 'rat']
print(len(animallist)) #print 4
animallist = ["cat", "bat", "rat", "elephant"]
animallist[1] = "aardvark"
print(animallist) #print ['cat', 'aardvark', 'rat', 'elephant']
animallist[-1] = "parrot"
print(animallist) #print ['cat', 'aardvark', 'rat', 'parrot']
animalnumberlist = [["cat", "bat"], [10, 20, 30, 40, 50]]
print(animalnumberlist[1]) #print [10, 20, 30, 40, 50]
print(animalnumberlist[1][2]) #print 30
concatenatelist = [1, 2, 3] + ["a", "b", "c"]
print(concatenatelist) #print [1, 2, 3, 'a', 'b', 'c']
replicatelist = ["x", "y", "z"] * 3
print(replicatelist) #print ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']
animallist = ["cat", "bat", "rat", "elephant"]
del(animallist[2])
print(animallist) #print ['cat', 'bat', 'elephant']
# catnames = []
# userinputcatname = input("Enter a cat name ")
# catnames = catnames + [userinputcatname]
# print(catnames) #print ['pooka']
# catnames2 = []
# userinputcatname = input("Enter a cat name ")
# catnames2.append(userinputcatname)
# print(catnames2) #print ['akoop']
animallist = ["cat", "bat", "rat", "elephant"]
for eachanimallist in animallist:
    print(eachanimallist)
    '''
    cat
    bat
    rat
    elephant
    '''
for i in range(0, len(animallist)):
    print(i, "is the index number for " + animallist[i])
    '''
    0 is the index number for cat
    1 is the index number for bat
    2 is the index number for rat
    3 is the index number for elephant
    '''
print("cat" in animallist) #print True
print("dog" in animallist) #print False
print("dog" not in animallist) #print True
multipleassignments = ["blue", "red", "black", "white"]
ocean, danger, night, paint = multipleassignments
print(multipleassignments)
print(ocean) #print blue
print(night) #print black
#A method is like a function.  A method is "called on" a value.  The method part comes after the value separated by a period.
animallist = ["cat", "bat", "rat", "elephant"]
print(animallist.index("cat")) #print 0
print(animallist.index("elephant")) #print 3
animallist.append("bear")
print(animallist) #print ['cat', 'bat', 'rat', 'elephant', 'bear']
animallist.insert(2, "eagle")
print(animallist) #print ['cat', 'bat', 'eagle', 'rat', 'elephant', 'bear']
animallist.remove("bat") #If an item appears multiple times, the remove method removes the first instance.
print(animallist) #print ['cat', 'eagle', 'rat', 'elephant', 'bear']
animallist = ["cat", "bat", "rat", "elephant"]
animallist.sort()
print(animallist) #print ['bat', 'cat', 'elephant', 'rat']
animallist = ["cat", "bat", "rat", "elephant"]
animallist.sort(reverse=True)
print(animallist) #print ['rat', 'elephant', 'cat', 'bat']
#sort uses ASCIIbetical order.  Uppercase letters are before lowercase letters.
uppercaselowercase = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
uppercaselowercase.sort()
print(uppercaselowercase) #print ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
#sort regular order pass str.lower in the key argument
uppercaselowercase = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
uppercaselowercase.sort(key=str.lower)
print(uppercaselowercase) #print ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']
stringasalist = "Zophie"
print(stringasalist[0]) #print Z
print(stringasalist[-2]) #print i
print(stringasalist[:4]) #print Zoph
print(stringasalist[-4:]) #print phie
print(stringasalist[-4:-1]) #print phi
print(stringasalist[-4:0]) #print *null*
print("Zo" in stringasalist) #print True
print("a" in stringasalist) #print False
for letter in stringasalist:
    print(letter)
    '''
    Z
    o
    p
    h
    i
    e
    '''
mutableastring = "Zophie a cat"
print(mutableastring[0:6] + " the " + mutableastring[9:12]) #print Zophie the cat
print(mutableastring[0:6] + " the " + mutableastring[-3:]) #print Zophie the cat
eggtuple = ("hello", 42, 0.5)
print(eggtuple) #print ('hello', 42, 0.5)
print(eggtuple[0]) #print hello
print(eggtuple[1:3]) #print (42, 0.5)
print(len(eggtuple)) #print 3
animallist = ["cat", "bat", "rat", "elephant"]
print(tuple(animallist)) #print ('cat', 'bat', 'rat', 'elephant')
eggtuple = ("hello", 42, 0.5)
print(list(eggtuple)) #print ['hello', 42, 0.5]
print(list(mutableastring)) #print ['Z', 'o', 'p', 'h', 'i', 'e', ' ', 'a', ' ', 'c', 'a', 't']
import copy
letterslist = ["a", "b", "c", "d"]
print(letterslist) #print ['a', 'b', 'c', 'd']
cheeseletterslist = copy.copy(letterslist) #copy.copy makes a duplicate copy of a mutable value such as a list or dictionary
print(cheeseletterslist) #print ['a', 'b', 'c', 'd']
cheeseletterslist[1] = "cheese"
print(cheeseletterslist) #print ['a', 'cheese', 'c', 'd']
print(letterslist) #print ['a', 'b', 'c', 'd']
def commacodefunction(inputlist):
    answer = ""
    for indexnumber in range(len(inputlist)):
        if indexnumber == len(inputlist) - 1:
            answer = answer + "and " + inputlist[indexnumber]
        else:
            answer = answer + inputlist[indexnumber] + ", "
    return answer


commacode = ["apples", "bananas", "tofu", "cats"]
print(commacodefunction(commacode)) #print apples, bananas, tofu, and cats
grid = [['.', '.', '.', '.', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['O', 'O', 'O', 'O', 'O', '.'], ['.', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', '.'], ['O', 'O', 'O', 'O', '.', '.'], ['.', 'O', 'O', '.', '.', '.'], ['.', '.', '.', '.', '.', '.']]
for eachgrid in grid:
    print("".join(eachgrid)) #RM:  incorrect.  Want the grid to print vertically, not horizontally.
    '''
    ......
    .OO...
    OOOO..
    OOOOO.
    .OOOOO
    OOOOO.
    OOOO..
    .OO...
    ......
    '''
for x in range(0, len(grid[0])):
    for y in range(0, len(grid)):
        print(grid[y][x], end="")
    print("")
    '''
    ..OO.OO..
    .OOOOOOO.
    .OOOOOOO.
    ..OOOOO..
    ...OOO...
    ....O....
    '''

#Automate The Boring Stuff With Python By Al Sweigart Chapter 05 Dictionaries And Structuring Data
mycat = {"size": "fat", "color": "gray", "disposition": "loud"}
print(mycat) #print {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(mycat["color"]) #print gray
numberdictionary = {12345: "lock combination", 42: "Jackie Robinson"}
print(numberdictionary) #print {12345: 'lock combination', 42: 'Jackie Robinson'}
print(numberdictionary[12345]) #print lock combination
listordermatters1 = ["cats", "dogs", "moose"]
listordermatters2 = ["dogs", "moose", "cats"]
print(listordermatters1 == listordermatters2) #print False
dictionaryordernotmatters1 = {"name": "Zophie", "species": "cat", "age": 8}
dictionaryordernotmatters2 = {"species": "cat", "age": 8, "name": "Zophie"}
print(dictionaryordernotmatters1 == dictionaryordernotmatters2) #print True
birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}
print(birthdays) #print {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
birthdays["add Ron"] = "add date May 4"
print(birthdays) #print {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', 'add Ron': 'add date May 4'}
for loopvalues in birthdays.values():
    print(loopvalues)
    '''
    Apr 1
    Dec 12
    Mar 4
    add date May 4
    '''
for loopkeys in birthdays.keys():
    print(loopkeys)
    '''
    Alice
    Bob
    Carol
    add Ron
    '''
for loopkeysvalues in birthdays.items():
    print(loopkeysvalues)
    '''
    ('Alice', 'Apr 1')
    ('Bob', 'Dec 12')
    ('Carol', 'Mar 4')
    ('add Ron', 'add date May 4')
    '''
birthdayskeyslist = list(birthdays.keys())
print(birthdayskeyslist) #print ['Alice', 'Bob', 'Carol', 'add Ron']
birthdayvalueslist = list(birthdays.values())
print(birthdayvalueslist) #print ['Apr 1', 'Dec 12', 'Mar 4', 'add date May 4']
print("Alice" in birthdays.keys()) #print True
print("Dec 25" in birthdays.values()) #print False
print("get() method get value for Alice's birthday " + str(birthdays.get("Alice", "default value if there's no Alice birthday")) + ".") #print get() method get value for Alice's birthday Apr 1.
print("get() method get value for Sam's birthday " + str(birthdays.get("Sam", "default value if there's no Sam Birthday")) + ".") #print get() method get value for Sam's birthday default value if there's no Sam Birthday.
missingvalue = {"name": "Pooka", "age": 5}
print(missingvalue) #print {'name': 'Pooka', 'age': 5}
missingvalue.setdefault("color", "add key and default value if key and value doesn't exist")
print(missingvalue) #print {'name': 'Pooka', 'age': 5, 'color': "add key and default value if key and value doesn't exist"}
missingvalue.setdefault("color", "I want to change the default value.  I actually can't change because color key is already in missingvalue dictionary")
print(missingvalue) #print {'name': 'Pooka', 'age': 5, 'color': "add key and default value if key and value doesn't exist"}
message = "It was a bright cold day in April, and the clocks were striking thirteen."
countletters = {}
for eachcharacter in message:
    countletters.setdefault(eachcharacter, 0) #if eachcharacter not in countletters, then set eachcharacter key to 0 value
    countletters[eachcharacter] = countletters[eachcharacter] + 1
print(countletters) #print {'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}
import pprint
pprint.pprint(countletters)
'''
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
'''
print(type(pprint.pprint(countletters))) #print <class 'NoneType'>
print(pprint.pformat(countletters))
'''
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
'''
print(type(pprint.pformat(countletters))) #print <class 'str'>
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
def displayinventory(inventory):
    print("Inventory:")
    itemsum = 0
    for key, value in inventory.items():
        print(value, key)
        itemsum = itemsum + value
    print("Total number of items:", itemsum)


displayinventory(stuff)
'''
Inventory:
1 rope
6 torch
42 gold coin
1 dagger
12 arrow
Total number of items: 62
'''
def addtoinventory(inventory, addtoinventory):
    for eachaddtoinventory in addtoinventory:
        print(eachaddtoinventory)
        inventory.setdefault(eachaddtoinventory, 0) #if eachcharacter not in countletters, then set eachcharacter key to 0 value
        inventory[eachaddtoinventory] = inventory[eachaddtoinventory] + 1
    print(inventory)
    return(inventory)
    '''
    gold coin
    dagger
    gold coin
    gold coin
    ruby
    {'gold coin': 45, 'rope': 1, 'dagger': 1, 'ruby': 1}
    '''


presentinventory = {"gold coin": 42, "rope": 1}
dragonloot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
presentinventory = addtoinventory(presentinventory, dragonloot)
print(presentinventory) #print {'gold coin': 45, 'rope': 1, 'dagger': 1, 'ruby': 1}
displayinventory(presentinventory)
'''
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
'''
