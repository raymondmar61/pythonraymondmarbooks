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
