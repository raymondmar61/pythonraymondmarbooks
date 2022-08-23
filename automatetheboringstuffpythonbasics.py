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

#Automate The Boring Stuff With Python By Al Sweigart Chapter 06 Manipulating Strings
print(r"Raw string begins the print statement with a lower case r.") #print Raw string begins the print statement with a lower case r.
print(r"Raw strings are helpful when a string contains many backslashes for escape characters.") #print raw string begins the print statement with a lower case r.
print("""Dear person,

    If you want a multiline string, then being and end with three double quotes.

Easy to understand.""")
'''
Dear person,

    If you want a multiline string, then being and end with three double quotes.

Easy to understand.
'''
indexslicereview = "Hello world!"
print(indexslicereview[0]) #print H
print(indexslicereview[4]) #print o
print(indexslicereview[-1]) #print !
print(indexslicereview[0:5]) #print Hello
print(indexslicereview[:5]) #print Hello
print(indexslicereview[6:]) #print world!
print("" in "spam") #print True
print(" " in "spam") #print False
commonstringmethods = "Hello world!"
print(commonstringmethods.upper()) #print HELLO WORLD!
print(commonstringmethods.lower()) #print hello world!
print(commonstringmethods.lower().isupper()) #print False
print(commonstringmethods.lower().islower()) #print True
checkstringlettersnoblanks = commonstringmethods.isalpha()
print(checkstringlettersnoblanks) #print False
checkstringlettersnumbersnoblanks = commonstringmethods.isalnum()
print(checkstringlettersnumbersnoblanks) #print False
checkstringnumbersnoblanks = commonstringmethods.isdecimal()
print(checkstringlettersnumbersnoblanks) #print False
checkstringspacestabslinesnoblanks = "     ".isspace()
print(checkstringspacestabslinesnoblanks) #print True
checkstringtitlecase = commonstringmethods.istitle()
print(checkstringtitlecase) #print False
checkstringtitlecase = "This Is Title Case With Blanks Numbers 123 Exclamation!".istitle()
print(checkstringtitlecase) #print True
startswithendswith = "Starts with is the sentence ends with."
print(startswithendswith.startswith("Starts with")) #print True
print(startswithendswith.endswith("ends with")) #print False
print(startswithendswith.endswith("ends with.")) #print True
joinlistwithcomma = ["cats", "rats", "bats"]
print(", ".join(joinlistwithcomma)) #print cats, rats, bats
joinlistsimon = ["My", "Name", "Is", "Simon"]
print(" ".join(joinlistsimon)) #print My Name Is Simon
print("I am behind of each list item".join(joinlistsimon)) #print MyI am behind of each list itemNameI am behind of each list itemIsI am behind of each list itemSimon
splitstringtoalist = "Split the string to a list".split() #default split is wherever whitespace character such as a space, tab, or newline.  Any delimiter string can be passed to specify the split.
print(splitstringtoalist) #print ['Split', 'the', 'string', 'to', 'a', 'list']
splitstringtoalistbyABC = "SplitABCtheABCstringABCtoABCaABClist".split("ABC")
print(splitstringtoalistbyABC) #print ['Split', 'the', 'string', 'to', 'a', 'list']
splitstringbytremovest = "Split the string to a list".split("t")
print(splitstringbytremovest) #print ['Spli', ' ', 'he s', 'ring ', 'o a lis', '']
#rjust() and ljust() methods return a padded version which insert spaces to justify the ntext length
print("No right justify ten spaces on the left because string is more than ten characters long.".rjust(10)) #print No right justify ten spaces on the left because string is more than ten characters long.
print("Yes right justify 012 spaces on the left because string is more than 089 characters long.".rjust(100)) #print            Yes right justify 012 spaces on the left because string is more than 089 characters long.
print("Hello".rjust(10)) #print '     Hello'
print("Hello World".rjust(10)) #print Hello World
print("Hello".ljust(10)) #print 'Hello     '
print("Hello World".ljust(10)) #print Hello World
print("Four".rjust(10)) #print '      Four'
print("Four".ljust(10)) #print 'Four      '
print("Add asterisk on the left to total 50 characters".rjust(50, "*")) #print ***Add asterisk on the left to total 50 characters
print("Add hyphen on the right to total 60 characters".ljust(60, "-")) #print Add hyphen on the right to total 60 characters--------------
print("CENTERME total 40 characters".center(40)) #print '      CENTERME total 40 characters      '
print("centerme total 50 characters with =".center(50, "=")) #print =======centerme total 50 characters with =========
def picnic(item, leftwidth, rightwidth):
    print("PICNIC ITEMS".center(leftwidth + rightwidth, "-"))
    for key, value in item.items():
        print(key.ljust(leftwidth, ".") + str(value).rjust(rightwidth))


picnicdictionary = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}
picnic(picnicdictionary, 12, 5)
'''
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
'''
picnic(picnicdictionary, 20, 6)
'''
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
'''
removewhitespace = "     String has white space before and after          "
print(removewhitespace) #print '     String has white space before and after          '
print(removewhitespace.strip()) #print String has white space before and after
print(removewhitespace.lstrip()) #print 'String has white space before and after          '
print(removewhitespace.rstrip()) #print '     String has white space before and after'
removelettersampSbeginningend = "SpamSpamBaconSpamEggsSpamSpam"
print(removelettersampSbeginningend.strip("ampS")) #print BaconSpamEggs.  strip("ampS") removes a, m, p, and S from the left side and the right side of removelettersampSbeginningend.  The order of the characters don't matter.  strip("ampS"), strip("mapS"), and strip("Spam") returns BaconSpamEggs
#pyperclip module has copy() and paste() functions which sends text to and receive text from the computer's clipboard.  Send the output of your program to the clipboard makes it easy to paste it when calling pyperclip.paste().
# import pyperclip
# # pyperclip.copy("Copy the string to pyperclip")
# # print(pyperclip.paste()) #print Copy the string to pyperclip
# print(pyperclip.paste()) #print String has white space before and after.  RM:  If I commented the two lines above and ctrl+c String has white space before and after, then pyperclip.paste() prints String has white space before and after
tabledata = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]

numberoflists = len(tabledata)
print(numberoflists) #print 3
numberofdata = len(tabledata[0])
print(numberofdata) #print 4
longestitemlength = 0
joinitems = []
for y in range(0, numberofdata):
    newinnerlist = []
    rowitemlength = 0
    for x in range(0, numberoflists):
        print(tabledata[x][y]) #print apples
        item = tabledata[x][y]
        newinnerlist.append(item)
        itemlength = len(item)
        rowitemlength += itemlength
        if rowitemlength > longestitemlength:
            longestitemlength = rowitemlength
            print(longestitemlength) #print 6
    joinitems.append(newinnerlist)
print(joinitems) #print [['apples', 'Alice', 'dogs'], ['oranges', 'Bob', 'cats'], ['cherries', 'Carol', 'moose'], ['banana', 'David', 'goose']]
longestitemlength = longestitemlength + numberoflists - 1
print(longestitemlength) #print 20
for eachjoinitems in joinitems:
    print(" ".join(eachjoinitems).rjust(longestitemlength))
    '''
       apples Alice dogs
        oranges Bob cats
    cherries Carol moose
      banana David goose
    '''

#Automate The Boring Stuff With Python By Al Sweigart Chapter 08 Reading And Writing Files
import os
#Join file paths or file pathways
os.path.join("home", "mar", "python")
print(os.path.join("home", "mar", "python")) #print home/mar/python
filepath = os.path.join("home", "mar", "python")
selectedpythonfiles = ["automatetheboringstuffpythonbasics.py", "mastermind147.py", "sqldatabase.py", "yytest.py"]
for eachselectedpythonfiles in selectedpythonfiles:
    print(os.path.join(filepath, eachselectedpythonfiles))
    '''
    home/mar/python/automatetheboringstuffpythonbasics.py
    home/mar/python/mastermind147.py
    home/mar/python/sqldatabase.py
    home/mar/python/yytest.py
    '''
currentworkingdirectory = os.getcwd() #cwd current working directory
print(currentworkingdirectory) #print /home/mar/python
for eachselectedpythonfiles in selectedpythonfiles:
    print(os.path.join(currentworkingdirectory, eachselectedpythonfiles))
    '''
    /home/mar/python/automatetheboringstuffpythonbasics.py
    /home/mar/python/mastermind147.py
    /home/mar/python/sqldatabase.py
    /home/mar/python/yytest.py
    '''
changedirectory = os.chdir("/media/sf_UbuntuShare2004") #change current working directory
print(changedirectory) #print None
print(os.chdir("/media/sf_UbuntuShare2004")) #print None.  RM:  Python changed path
printabsolutepath = os.path.abspath(".")
print(printabsolutepath) #print /media/sf_UbuntuShare2004
#createnewfolder = os.makedirs(currentworkingdirectory + "/tempdelete") #create new working directory tempdelete in /home/mar/python for /home/mar/python/tempdelete
print(os.chdir("/home/mar/python")) #print None.  Change path to Python to continue learning
absolutepath = os.path.abspath(".") #Returns a string of the absolute path.  Convert a relative path to an absolute path.
print(absolutepath) #print /home/mar/python
absolutepathwithsubfolder = ("./tempdelete")
print(absolutepathwithsubfolder) #print ./tempdelete
confirmabsolutepath = os.path.isabs(".") #returns True if absolute path and False if relative path
print(confirmabsolutepath) #print False
confirmabsolutepath = os.path.isabs("..")
print(confirmabsolutepath) #print False
confirmrelativepath = os.path.relpath("/home/python", "~") #returns a string of a relative path from the start path to path.  If start path is not provided, the current working directory is used as the start path.
print(confirmrelativepath) #print ../../../python
confirmrelativepath = os.path.relpath("/home/", "~")
print(confirmrelativepath) #print ../../..
confirmrelativepath = os.path.relpath("/home", "~")
print(confirmrelativepath) #print ../../..
confirmrelativepath = os.path.relpath("/", "~")
print(confirmrelativepath) #print ../../../..
confirmrelativepath = os.path.relpath("/home/python", "/home/")
print(confirmrelativepath) #print python
confirmrelativepath = os.path.relpath("/home/python", "/home")
print(confirmrelativepath) #print python
fullpathworkingdirectory = "/home/mar/python"
beforelastslash = os.path.dirname(fullpathworkingdirectory)
print(beforelastslash) #print /home/mar
afterlastslash = os.path.basename(fullpathworkingdirectory)
print(afterlastslash) #print python
separatepathfilename = "/home/mar/python/yytest.py"
print(os.path.split(separatepathfilename)) #print ('/home/mar/python', 'yytest.py')
print(os.path.dirname(separatepathfilename), os.path.basename(separatepathfilename)) #print /home/mar/python yytest.py
print((os.path.dirname(separatepathfilename), os.path.basename(separatepathfilename))) #print ('/home/mar/python', 'yytest.py')
print(os.path.sep) #print /
print(fullpathworkingdirectory.split(os.path.sep)) #print ['', 'home', 'mar', 'python'].  Use split string method for the fullpathworkingdirectory variable for os.path.sep to split by /
# filesizeinbytes = os.path.getsize("~/python/automatetheboringstuffpythonbasics.py")
# print(filesizeinbytes) #print FileNotFoundError: [Errno 2] No such file or directory: '~/python/automatetheboringstuffpythonbasics.py'
filesizeinbytes = os.path.getsize("/home/mar/python/automatetheboringstuffpythonbasics.py")
print(filesizeinbytes) #print 23509
fileslistindorectory = os.listdir("/home/mar/python")
print(fileslistindorectory) #print ['twitterdownloadtweetsfinalv1.2.py', 'coffeesqllitedatabase.py', 'myphotoalbum.html', . . . ,'mfgcompanysqlite.py', 'sqllitebackendbeginnersdatabase.py']
print(os.path.exists("/home")) #print True
print(os.path.exists("/home/mar")) #print True
print(os.path.exists("/home/mar/python")) #print True
print(os.path.isdir("/home")) #print True
print(os.path.isdir("/home/mar")) #print True
print(os.path.isdir("/home/mar/python")) #print True
print(os.path.isfile("/home/mar/python/automatetheboringstuffpythonbasics.py")) #print True
print(os.path.exists("/home/mar/python/automatetheboringstuffpythonbasics.py")) #print True
print(os.path.isdir("/home/mar/python/automatetheboringstuffpythonbasics.py")) #print False
print(os.path.isfile("/home/mar/python")) #print False
#There are three steps to read or to write Python files.  1 Call the open() function to return a file object.  2 Call the read() or write() method on the file object.  3 Call the close() method to close the file on the file object.
opentextfileobject = open(fullpathworkingdirectory + "/temphello.txt", "r") #open() returns a file object saved to opentextfileobject variable.  A file object represents a file on your computer or another type of value in Python like lists and dictionaries.
readtextfileobject = opentextfileobject.read()
print(readtextfileobject) #print Hello world!
opentextfileobject.close()
sonnetfileobject = open("sonnet29.txt")
readsonnetfileobject = sonnetfileobject.readlines() #readlines method returns a list of sting values from the file.  One string for each line.
print(readsonnetfileobject) #print ['Not sonnet29 in the book.\n', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\n', 'tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\n', 'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\n', 'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\n', 'cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\n', 'proident, sunt in culpa qui officia deserunt mollit anim id est laborum.']
sonnetfileobject.close()
writetobaconfileobject = open("bacon.txt", "w")
writetobaconfileobject.write("Hello world!\n")
writetobaconfileobject.close()
addtextbaconfileobject = open("bacon.txt", "a")
addtextbaconfileobject.write("Bacon is not a vegetable.\n")
addtextbaconfileobject.close()
readbaconfileobject = open("bacon.txt", "r")
printreadbaconfileobject = readbaconfileobject.read()
print(printreadbaconfileobject) #print Hello world!\n Bacon is not a vegetable.\n
readbaconfileobject.close()

#Automate The Boring Stuff With Python By Al Sweigart Chapter 09 Organizing Files
import shutil
import os
import zipfile

shutil.copy("temp.txt", "/home/mar") #copy temp.txt file in the python directory /home/mar/python to /home/mar
shutil.copy("temp.txt", "/home/mar/renametempfilename.txt") #copy temp.txt file in the python directory /home/mar/python to /home/mar rename temp.txt file to renametempfilename.txt
shutil.copytree("/home/mar/python", "/home/mar/createnewdirectory/") #copy python directory to a new directory name createnewdirectory
shutil.move("temptext.txt", "/home/mar/Downloads") #move temptext.txt file to Downloads folder
shutil.move("temptext.txt", "/home/mar/Downloads/renamemovedtemptext.txt") #move temptext.txt file to Downloads folder and rename text file from temptext.txt to renamemovedtemptext.txt
os.unlink("deletetemptextfile.txt") #delete deletetemptextfile.txt at present directory permanently
os.unlink("/home/mar/python/deletetemptextfile.txt") #delete deletetemptextfile.txt at /home/mar/python/ permanently
os.rmdir("deletedirectory") #delete the empty folder deletedirectory in present directory permanently
shutil.rmtree("/home/mar/python/deleteunempydirectory/") #delete the folder deleteunempydirectory with files and folders in present directory permanently
for forloopdeletefiles in os.listdir():
    if forloopdeletefiles.endswith(".txt"):
        print("Check filenames before permanent delete os.unlink(forloopdeletefiles): " + forloopdeletefiles)
        #os.unlink(forloopdeletefiles)
#Directory tree or files and folders
for foldername, subfolder, filename in os.walk("/home/mar/python/"):
    print("Folder in python directory " + foldername)
    for eachsubfolder in subfolder:
        print("Subfolder " + eachsubfolder + " in " + foldername)
    for eachfilename in filename:
        print("Filename " + eachfilename + " in " + foldername)
        '''
        Folder in python directory /home/mar/python/
        Subfolder myphotoalbum in /home/mar/python/
        Subfolder journal in /home/mar/python/
        Subfolder __pycache__ in /home/mar/python/
        Filename twitterdownloadtweetsfinalv1.2.py in /home/mar/python/
        Filename coffeesqllitedatabase.py in /home/mar/python/
        Filename myphotoalbum.html in /home/mar/python/
        Filename mastermind147.py in /home/mar/python/
        Filename artgallery150.py in /home/mar/python/
        Filename piecesofart.txt in /home/mar/python/
        Filename encrypttextfile.txt in /home/mar/python/
        ...
        Folder in python directory /home/mar/python/myphotoalbum
        Subfolder myphotoalbum in /home/mar/python/myphotoalbum
        Filename sanmateojapanesegardens.jpg in /home/mar/python/myphotoalbum
        Filename joaquinmillerlookoutpoint.jpg in /home/mar/python/myphotoalbum
        Filename caacademy1.jpg in /home/mar/python/myphotoalbum
        Filename zionnarrowsbottomup.jpg in /home/mar/python/myphotoalbum
        Filename bernalheights.jpg in /home/mar/python/myphotoalbum
        Filename baseballvintage.jpg in /home/mar/python/myphotoalbum
        ...
        '''
#Zip files
viewfilesinzipfolderobject = zipfile.ZipFile("kevincookiecompanygittutorial.zip")
print(viewfilesinzipfolderobject.namelist()) #print ['Employee Salaries.txt', 'index.htm', 'KCC Logo.png', 'secret recipe.htm']
afileinzipfileinformation = viewfilesinzipfolderobject.getinfo("index.htm")
print(afileinzipfileinformation) #print <ZipInfo filename='index.htm' file_size=505>
print(afileinzipfileinformation.file_size) #print 505 #RM:  number in bytes
print(afileinzipfileinformation.compress_size) #print 505 #RM:  number in bytes
viewfilesinzipfolderobject.extract("index.htm", "/home/mar") #extract() method extracts a file to destination which is extract index.htm to /home/mar directory
viewfilesinzipfolderobject.extractall("/home/mar/python/extractzipfilefolder") #extractall() method extracts all files and folders in zip file to extractzipfilefolder folder
viewfilesinzipfolderobject.close()
createzipfile = zipfile.ZipFile("zipfile.zip", "w")
createzipfile.write("personlog.txt", compress_type=zipfile.ZIP_DEFLATED)
createzipfile.close()
# If you want to add files to an existing zip file, use "a" append mode as the second argument
createzipfileforloop = zipfile.ZipFile("zipfilealltextfiles.zip", "w")
for forlooptextfiles in os.listdir():
    if forlooptextfiles.endswith(".txt"):
        createzipfileforloop.write(forlooptextfiles, compress_type=zipfile.ZIP_DEFLATED)
createzipfileforloop.close()

#Automate The Boring Stuff With Python By Al Sweigart Chapter 13 Working With PDF and Word Documents
#PyPDF2 extracts text which returns as a Python string.
#Can't get PyPDF2 to work.  Google search there are better substitutes.  PyPDF2 and PyPDF4 installed.
import PyPDF2
pdffileobject = open("magnummaniamaddogsandenglishmen.pdf", "rb")
pdfreader = PyPDF2.PdfFileReader(pdffileobject)
print(pdfreader.numPages) #print 3
page1pdffile = pdfreader.getPage(0)
page1pdffile.extractText()
print(page1pdffile.extractText()) #print *nothing*
page2pdffile = pdfreader.getPage(1)
page2pdffile.extractText()
print(page2pdffile) #print {'/Type': '/Page', '/Resources': {'/ProcSet': ['/PDF', '/Text', '/ImageB', '/ImageC', '/ImageI'], '/ExtGState': {'/G3': IndirectObject(3, 0)}, '/Font': {'/F4': IndirectObject(4, 0), '/F10': IndirectObject(10, 0), '/F11': IndirectObject(11, 0)}}, '/MediaBox': [0, 0, 612, 792], '/Annots': [IndirectObject(43, 0), IndirectObject(44, 0), IndirectObject(45, 0), IndirectObject(46, 0), IndirectObject(47, 0), IndirectObject(48, 0), IndirectObject(49, 0)], '/Contents': IndirectObject(50, 0), '/StructParents': 1, '/Parent': IndirectObject(55, 0)}
print(type(page2pdffile.extractText())) #print <class 'str'>
print(type(page2pdffile)) #print <class 'PyPDF2._page.PageObject'>
page = pdfreader.pages[0]
print(page.extractText()) #print *nothing*
print(pdfreader.getDocumentInfo()) #print {'/Creator': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36', '/Producer': 'Skia/PDF m96', '/CreationDate': "D:20220101091634+00'00'", '/ModDate': "D:20220101091634+00'00'"}
pdffileobject.close()

#Automate The Boring Stuff With Python By Al Sweigart Chapter 15 Keeping Time, Scheduling Tasks, And Launching Programs
#The built-in time module reads the computer's system clock which is set to a date, time, and timezone.  time.time() and time.sleep() are the most useful functions.
import time
print(time.time()) #print 1660940220.9355557.  time.time() returns the number of seconds since 12:00am on Jan 1, 1970 which is called an epoch timestamp.
recordtimestarttime = time.time()
print("What is the difference between start time recordtimestarttime and recordtimeendtime?")
recordtimeendtime = time.time()
print("The answer is", recordtimeendtime - recordtimestarttime) #print The answer is 3.5762786865234375e-06
def pauseprogram(numberofsecondssleep):
    for i in range(1, numberofsecondssleep + 1):
        time.sleep(i)
        print("time.sleep() function blocks or don't return and release the program to execute another code.  Pause second number", i)
    return "pauseprogram function completed"


seconds = 1
print(pauseprogram(seconds))
'''
time.sleep() function blocks or don't return and release the program to execute another code.  Pause second number 1
time.sleep() function blocks or don't return and release the program to execute another code.  Pause second number 2
time.sleep() function blocks or don't return and release the program to execute another code.  Pause second number 3
time.sleep() function blocks or don't return and release the program to execute another code.  Pause second number 4
time.sleep() function blocks or don't return and release the program to execute another code.  Pause second number 5
'''
import datetime
print(datetime.datetime.now()) #print 2022-08-19 13:30:32.012225
dt = datetime.datetime.now()
print("datetime year", dt.year) #print datetime year 2022
print("datetime month number no leading zero", dt.month) #print datetime month number no leading zero 8
print("datetime day number", dt.day) #print datetime day number 19
print("datetime hour 24 hour", dt.hour) #print datetime hour 24 hour 13
print("datetime minute", dt.minute) #print datetime minute 30
print("datetime second", dt.second) #print datetime second 32
numberofsecondssinceepochtimestamp = 1000000 #epoch timestamp is Jan 1, 1970 at 12:00am
print(datetime.datetime.fromtimestamp(numberofsecondssinceepochtimestamp)) #print 1970-01-12 05:46:40.  Jan 12, 1970 at 5:46am at 40 seconds is the date and time 1,000,000 seconds passed since Jan 1, 1970 at 12:00am.
print(datetime.datetime.fromtimestamp(time.time())) #print 2022-08-19 13:36:41.765676.  time.time() returns the number of seconds since 12:00am on Jan 1, 1970 which is called an epoch timestamp.  fromtimestamp returns the datetime from time.time().  datetime.datetime.now() and datetime.datetime.fromtimestamp(time.time()) return the same result.
halloween2022 = datetime.datetime(2022, 10, 31, 0, 0, 0)
presidentsday2023 = datetime.datetime(2023, 2, 13, 0, 0, 0)
oct312022 = datetime.datetime(2022, 10, 31, 0, 0, 0)
print(halloween2022 == oct312022) #print True
print(halloween2022 > presidentsday2023) #print False
print(presidentsday2023 > halloween2022) #print True
print(presidentsday2023 != oct312022) #print True
#The datetime.timedelta() function takes keyword arguments weeks, days, hours, minutes, seconds, milliseconds, and microseconds. There is no month or year keyword argument because "a month" or "a year" is a variable amount of time depending on the particular month or year. A timedelta object has the total duration represented in days, seconds, and microseconds. These numbers are stored in the days, seconds, and microseconds attributes, respectively. The total_seconds() method will return the duration in number of seconds alone. Passing a timedelta object to str() will return a nicely formatted, human-readable string representation of the object.
giventimereturntimeduration = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8) #RM:  delta is the better variable.  I used giventimereturntimeduration to quickly explain timedelta.
print("Number of days", giventimereturntimeduration.days) #print Number of days 11
print("Number of seconds from hours, minutes and seconds", giventimereturntimeduration.seconds)  #Number of seconds from hours, minutes and seconds 36548.  10 hours, 9 minutes, are 8 seconds total 36548 seconds.
print("Number of microseconds", giventimereturntimeduration.microseconds)  #Number of microseconds 0
print("Total number of seconds days, hours, minutes, seconds", giventimereturntimeduration.total_seconds()) #print Total number of seconds days, hours, minutes, seconds 986948.0
print("Return giventimereturntimeduration as a string " + str(giventimereturntimeduration)) #print Return giventimereturntimeduration as a string 11 days, 10:09:08
todaysdate = datetime.datetime.now()
onethousanddays = datetime.timedelta(days=1000)
onethousanddayslater = todaysdate + onethousanddays
print(onethousanddayslater) #print 2025-05-15 13:56:59.237881.  One thounsand days later is May 15, 2025
#Pause program, delay, sleep
initialnumber = 1
while initialnumber < 6:
    print("Wait one second")
    time.sleep(0)
    print(initialnumber)
    initialnumber += 1
    '''
    Wait one second
    1
    Wait one second
    2
    Wait one second
    3
    Wait one second
    4
    Wait one second
    5
    '''
#strftime() as in string str, f format, time is time.
presentdaytimeobject = datetime.datetime.now()
print(presentdaytimeobject) #print 2022-08-22 22:15:22.104291
print(presentdaytimeobject.strftime("%Y")) #print 2022
print(presentdaytimeobject.strftime("%y")) #print 22.  Year without century or two digit year.
print(presentdaytimeobject.strftime("%m")) #print 08.  Month as decimal number.
print(presentdaytimeobject.strftime("%B")) #print August
print(presentdaytimeobject.strftime("%b")) #print Aug
print(presentdaytimeobject.strftime("%d")) #print 22.  Day of the month.
print(presentdaytimeobject.strftime("%j")) #print 234.  Numbered day of the year.  Aug 22 is the 234th day of the 2022 year.
print(presentdaytimeobject.strftime("%w")) #print 1.  Numbered day of the week.  Sun is 0.  Sat is 6.
print(presentdaytimeobject.strftime("%A")) #print Monday
print(presentdaytimeobject.strftime("%a")) #print Mon
print(presentdaytimeobject.strftime("%H")) #print 22.  24-hour clock
print(presentdaytimeobject.strftime("%I")) #print 10.  12-hour clock.
print(presentdaytimeobject.strftime("%M")) #print 15.  Minute.
print(presentdaytimeobject.strftime("%S")) #print 22  Second.
print(presentdaytimeobject.strftime("%p")) #print PM  AM or PM.
print(presentdaytimeobject.strftime("%%")) #print %.  A percentage.
print(presentdaytimeobject.strftime("%b %d, %Y")) #print Aug 22, 2022
print(presentdaytimeobject.strftime("Today is %B %y, %Y.")) #print Today is August 22, 2022.
#datetime.datetime.strptime() to convert a date in string format to a datetime object.  strptime() as in string str, p parse, time is time.
print(datetime.datetime.strptime("Aug 22, 22", "%b %d, %y")) #print 2022-08-22 00:00:00
print(datetime.datetime.strptime("Today is Mon Aug 22, 2022.", "Today is %a %b %d, %Y.")) #print 2022-08-22 00:00:00
#Multithreading
#A singlethreaded program has one finger.  A multithreaded program has multiple fingers.  Each finger moves to the next line of code.  The fingers can be at different places in the program and execute different lines of code at the same time.  You can execute the delayed or scheduled code in a separate thread using Python's threading module.  The separate thread pauses for the time.sleep calls for example.  Mean while, the program does other work in the original thread.
import threading
import time

yesthreadstartime = time.time()
print("Start program yesthread() function")
def yesthread():
    time.sleep(5)
    yesthreadcompletedtime = time.time()
    print("Wake up yesthread() function.  Time elapsed", yesthreadcompletedtime - yesthreadstartime)


threadobject = threading.Thread(target=yesthread)
threadobject.start()
print("End program yesthread() function")
yesthreadendtime = time.time()
print("Time elapsed yesthread() function", yesthreadendtime - yesthreadstartime)
print("\n")
nothreadstartime = time.time()
print("Start program nothread() function")
def nothread():
    time.sleep(5)
    nothreadcompletedtime = time.time()
    print("Wake up nothread() function.  Time elapsed", nothreadcompletedtime - nothreadstartime)


nothread()
print("End program nothread() function")
nothreadendtime = time.time()
print("Time elapsed nothread() function", nothreadendtime - nothreadstartime)
#RM:  No more experimenting.
#Create a thread object by calling the threading.Thread() function.
print("Start real program")
def takeanap():
    time.sleep(5)
    print("Wake up from takeanap() function")


createthreadobject = threading.Thread(target=takeanap) #keyword argument target=takeanap() call the function takeanap() in the new thread.  You want to pass the takeanap function itself as the argument instead of call takeanap() function and pass its return value.
createthreadobject.start() #create a new thread and start executing the target function in the new thread
print("End real program")
'''
Start program yesthread() function
End program yesthread() function
Time elapsed yesthread() function 0.00018739700317382812


Start program nothread() function
Wake up nothread() function.  Time elapsed 5.002316236495972
End program nothread() function
Time elapsed nothread() function 5.002425193786621
Start real program
End real program
Wake up yesthread() function.  Time elapsed 5.003744840621948
Wake up from takeanap() function
'''
#If print('End of program.') is the last line of the program, you might think that it should be the last thing printed. The reason Wake up! comes after it is that when threadObj.start() is called, the target function for threadObj is run in a new thread of execution. Think of it as a second finger appearing at the start of the takeANap() function. The main thread continues to print('End of program.'). Meanwhile, the new thread that has been executing the time.sleep(5) call, pauses for 5 seconds. After it wakes from its 5-second nap, it prints 'Wake up!' and then returns from the takeANap() function. Chronologically, 'Wake up!' is the last thing printed by the program.
#Two threads. RM:  technically three threads because of threadobject = threading.Thread(target=yesthread).  The first is the original thread that began at the start of the program and ends after print('End of program.'). The second thread is created when threadObj.start() is called, begins at the start of the takeANap() function, and ends after takeANap() returns.
#A Python program will not terminate until all its threads have terminated. When you ran threadDemo.py, even though the original thread had terminated, the second thread was still executing the time.sleep(5) call.

def threenumbersonestring(n1, n2, n3, string32):
    print(n1)
    print(n2)
    print(n3)
    print(string32)


createthreadobject31 = threading.Thread(target=threenumbersonestring, args=[111, 345, 9899, "I am a string", ])
createthreadobject31.start()
'''
Start program yesthread() function
End program yesthread() function
Time elapsed yesthread() function 0.00021219253540039062


Start program nothread() function
Wake up nothread() function.  Time elapsed 5.037243843078613
End program nothread() function
Time elapsed nothread() function 5.0375330448150635
Start real program
Wake up yesthread() function.  Time elapsed 5.037549257278442
End real program
111
345
9899
I am a string
Wake up from takeanap() function

'''
