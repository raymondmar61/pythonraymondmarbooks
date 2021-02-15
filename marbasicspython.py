#Basics Python Combine All Lessons Learned One Stop Book One Stop Documentation
#Category:  *topic*
#Categories:  Boolean, Math, Strings, Lists, Tuples, Dictionaries, Sets, If Elif Else If then, try except, open file write file, Functions, Function Iterators, Lambda, import statement
#Classes at marbasicspythonclasses.py.
#Modules at marcommonmodulespython.py.  Math.
#YouTube and book tutorials:  thenewbostonallvideos, williamfisetallvideos, Python Crash Course take two

#Category:  Boolean
print(bool(1>3)) #print False
print(bool("a"<"v")) #print True
print(bool(1==1)) #print True
print(any([True, False, 0, 1 < 0])) #print True
print(any([False])) #print False
print(any([])) #print False
print(all([True, True])) #print True
print(all([True, 34<5])) #print False
print(True and True) #print True
print(True and False) #print False
print(False and False) #print False
print(True, True) #print True, True
print(True, False) #print True, False
print(False, False) #print False, False
firstnumber = 80
secondnumber = 55.70
resultfirst = isinstance(firstnumber, (int, float))
print(resultfirst) #print True
resultsecond = isinstance(secondnumber, (int, float))
print(resultsecond) #print True
#ValueError: too many values to unpack (expected 4)
#variable1, variable2, variable3, variable4 = "robert"
#print(variable1) #print robert
#print(variable2) #print robert
#print(variable3) #print robert
#print(variable4) #print robert
variable1, variable2, variable3, variable4 = "robert", "robert", "robert", "robert"
print(variable1) #print robert
print(variable2) #print robert
print(variable3) #print robert
print(variable4) #print robert
print(variable1 is variable4) #print True
variable1, variable2, variable3, variable4 = ["roberttimesfour"] * 4
print(variable1) #print roberttimesfour
print(variable2) #print roberttimesfour
print(variable3) #print roberttimesfour
print(variable4) #print roberttimesfour
print(type(variable4)) #print <class 'str'>
variable1, variable2, variable3, variable4 = "jake", "snake", "blake", "cake"
print(variable1) #print jake
print(variable2) #print snake
print(variable3) #print blake
print(variable4) #print cake
print(variable1 is variable4) #print False
[variable1, variable2, variable3, variable4] = ["jake", "snake", "blake", "cake"]
print(variable1) #print jake
print(variable2) #print snake
print(variable3) #print blake
print(variable4) #print cake
(variable1, variable2, variable3, variable4) = ("jaketuple", "snaketuple", "blaketuple", "caketuple")
print(variable1) #print jaketuple
print(variable2) #print snaketuple
print(variable3) #print blaketuple
print(variable4) #print caketuple
variable1 = variable2 = variable3 = variable4 = "robertfourequals"
print(variable1) #print robertfourequals
print(variable2) #print robertfourequals
print(variable3) #print robertfourequals
print(variable4) #print robertfourequals
xvariable = None
yvariable = None
print(xvariable) #print None
print(yvariable) #print None
xvariable = yvariable = "something"
print(xvariable) #print something
print(yvariable) #print something
a = b = c = [1, 3, 5]
print(a) #print [1, 3, 5]
print(b) #print [1, 3, 5]
print(c) #print [1, 3, 5]
print(a is b) #print True
print(b is c) #print True
print(c is b) #print True
b = 3333
print(b) #print 3333
print(a is b) #print False
print(b is c) #print False
print(c is b) #print False
a, b, c = 1, 3, 5
print(a) #print 1
print(b) #print 3
print(c) #print 5
print(a is b) #print False
print(b is c) #print False
print(c is b) #print False
b = 3333
print(b) #print 3333
print(a is b) #print False
a, b, c = ({"test": "a"}, {"test": "b"}, {"test": "c"})
print(a) #print {"test":"a"}
print(b) #print {"test":"b"}
print(c) #print {"test":"c"}
#A stackoverflow says don't do the following any other object
dontdothis = {}
dontdothistoo = {}
dontdothis = dontdothistoo = {} #same dictionary object assigned to dontdothis, dontdothistoo.  Should not do this.
#Anacoda removed my lamda--> fiveletters = lambda n: ["five letters" for _ in range(n)]
def fivelettersvariables(n):
    return ["five letters" for _ in range(n)]
v, w, z, y, z = fivelettersvariables(5)
print(v) #print five letters
print(z) #print five letters
#However . . . 
lista = listb = []
lista.append("x")
print(lista) #print x
print(listb) #print x
listc = listd = [[], []]
listc.append("xc")
print(listc) #print x
print(listd) #print x
liste, listf, listg = ([] for _ in range(0, 3)) #liste, listf, listg = [[] for _ in range(0, 3)] using lists also works
print(liste) #print []
print(listf) #print []
print(listg) #print []
liste.append("xe")
print(liste) #print ['xe']
print(listf) #print []
print(listg) #print []
listg.append("xg")
print(liste) #print ['xe']
print(listf) #print []
print(listg) #print ['xg']

#Category:  Math
print(18/5) #print 3.6
print(18//5) #print 3
print(18//5.0) #print 3.0
print(18/8) #print 2.25
print(18//8) #print 2
print(abs(-100)) #print 100
print(pow(4,2)) #print 16
print(4**2) #print 16
#eval evalulates a string like a math equation
foo = 34
bar = 3
print(eval("foo * bar")) #print 102.  34*3=102
isthenumberrounded = 80.654 #round numbers
print("%.3f" % isthenumberrounded) #print 80.654
print("%.2f" % isthenumberrounded) #print 80.65
print("%.1f" % isthenumberrounded) #print 80.7

#Category:  Strings
print(r"this story is \nokday d'kay") #print this story is \nokday d'kay. RM:  print as-is exact text
user = "Tuna McFish"
print(user[0]) #print T
print(user[1:4]) #print una
print(user[1:9:2]) #print uaMF
print(user[-1]) #print h
print(user[-1::-1]) #print hsiFcM anuT
helloworld = "Hello world!"
print(helloworld[::-1]) #print !dlrow olleH
fiveexcessesspace = "     PYTHON     "
print(fiveexcessesspace.rstrip()) #print      PYTHON
print(fiveexcessesspace.lstrip()) #print PYTHON     
print(fiveexcessesspace.strip()) #print PYTHON
print(fiveexcessesspace.lower()) #print      python    
splitstring = "do goat sheep boat"
print(splitstring.title()) #print Do Goat Sheep Boat
print(list(splitstring)) #print ['d', 'o', ' ', 'g', 'o', 'a', 't', ' ', 's', 'h', 'e', 'e', 'p', ' ', 'b', 'o', 'a', 't']
print(splitstring.split()) #print ['do', 'goat', 'sheep', 'boat']
print(splitstring.split(" ")) #print ['do goat sheep boat']
print(splitstring.split("\n")) #print ['do goat sheep boat']
print(" ".split(splitstring)) #print [' ']
print(splitstring.replace("boat","yoga")) #print do goat sheep yoga
splitstring = "do goat sheep boat"
print(splitstring.find("goat")) #print 3 which is the starting index number
print(splitstring.startswith("do")) #print True
print(splitstring.startswith("goat")) #print False
print(splitstring.endswith("t")) #print True
print(splitstring.endswith("boat")) #print True
wordis = "ABCiop"
print(wordis.lower()) #print abciop
print(wordis.upper()) #print ABCIOP
text = "We hope to one day become the world's leader in free, education resources.  We are constantly discovering and adding more free content to the website everyday.  There is already an enormous amount of resoruces online that can be accessed for free by anyone in the world, the main issue right now is that very little of it is organized or structured in any way.  We want to be the solution to that problem."
print(text)
splittext = text.split()
print(splittext) #print ['We', 'hope', 'to', 'one', 'day', 'become', 'the', "world's", 'leader', 'in', 'free,', 'education', 'resources.', 'We', 'are', 'constantly', 'discovering', 'and', 'adding', 'more', 'free', 'content', 'to', 'the', 'website', 'everyday.', 'There', 'is', 'already', 'an', 'enormous', 'amount', 'of', 'resoruces', 'online', 'that', 'can', 'be', 'accessed', 'for', 'free', 'by', 'anyone', 'in', 'the', 'world,', 'the', 'main', 'issue', 'right', 'now', 'is', 'that', 'very', 'little', 'of', 'it', 'is', 'organized', 'or', 'structured', 'in', 'any', 'way.', 'We', 'want', 'to', 'be', 'the', 'solution', 'to', 'that', 'problem.']
#inputcolors = str(input("Enter a list of colors separated by a space "))
inputcolors = "black white red"
print(inputcolors) #print black white red
print(inputcolors.split()) #print ['black', 'white', 'red']
splitinputcolors = inputcolors.split()
print(" ".join(splitinputcolors)) #print black white red
print(", ".join(splitinputcolors)) #print black, white, red
sortlistofstrings = "It is a nice day today, isn't it?"
sortlistofstrings.split()
print(sortlistofstrings) #print It is a nice day today, isn't it?
#sortlistofstrings.sort() #AttributeError: 'str' object has no attribute 'sort'
#print(sortlistofstrings) #print AttributeError: 'str' object has no attribute 'sort'
sortlistofstrings = "It is a nice day today, isn't it?".split()
print(sortlistofstrings) #print ['It', 'is', 'a', 'nice', 'day', 'today,', "isn't", 'it?']
sortlistofstrings.sort()
print(sortlistofstrings) #print ['It', 'a', 'day', 'is', "isn't", 'it?', 'nice', 'today,']
from collections import Counter
topwords = Counter(splittext)
topthree = topwords.most_common(3)
print(topthree) #print [('the', 5), ('to', 4), ('We', 3)]
astring = "The String"
anumber = 457
print("Standard novice plus sign to concatenate string variables.  My number is " +str(anumber)+ ".  My string is " +astring+".") #print Standard novice plus sign to concatenate string variables.  My number is 457.  My string is The String.
print("My number is %f.  My string is %s." %(anumber, astring)) #print My number is 457.000000.  My string is The String.
print("My number is %d.  My string is %s." %(anumber, astring)) #print My number is 457.  My string is The String.
print("Looking ahead .format().  My number is {}.  My string is {}." .format(anumber, astring)) #print Looking ahead .format().  My number is 457.  My string is The String.
astring2 = "The String2"
anumber2 = 457.56789
print("My number is %f.  My string is %s." %(anumber2, astring2)) #print My number is 457.567890.  My string is The String2.
print("My number is %d.  My string is %s." %(anumber2, astring2)) #print My number is 457.  My string is The String2.
print("Looking ahead .format().  My number is {}.  My string is {}." .format(anumber2, astring2)) #print Looking ahead .format().  My number is 457.56789.  My string is The String2.
print("Looking ahead .format().  My number is {:.2f}.  My string is {}." .format(anumber2, astring2)) #print Looking ahead .format().  My number is 457.57.  My string is The String2.
print("Looking ahead .format().  My number is {1:.2f}.  My string is {0}." .format(astring2, anumber2)) #print Looking ahead .format().  My number is 457.57.  My string is The String2.
escapecharacters = list("Hello World!")
print(escapecharacters) #print ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
print("\v".join(escapecharacters))
'''
H
 e
  l
   l
    o
      
      W
       o
        r
         l
          d
           !
'''
print("\t".join(escapecharacters)) #H	e	l	l	o	 	W	o	r	l	d!
print("\n".join(escapecharacters)) #H	e	l	l	o	 	W	o	r	l	d!
'''
H
e
l
l
o
 
W
o
r
l
d
!
'''
print("\h".join(escapecharacters)) #print H\he\hl\hl\ho\h \hW\ho\hr\hl\hd\h!
onelinestring = "Okay let's review the information again. "
onelinestring += "Practice, repeat, repetition."
print(onelinestring) #print Okay let's review the information again. Practice, repeat, repetition.
#a string is considered True if it's not empty.  If it's empty, then it's considered False.
itemslist = ["bread","chocolate","apple","peanuts"]
if itemslist:
	print("itemslist has items.  itemslist is True") #print itemslist has items.  itemslist is True
blankitemslist = []
if not blankitemslist:
	print("blankitemslist is empty.  blankitemslist is False.") #print blankitemslist is empty.  blankitemslist is False.
gerald = "This sentence is true"
while gerald:
	print("Keep printing the truth")
	gerald = input("Do you want the truth again?  If no, then press enter for gerald variable to be null and False")
#eval evalulates a string like a math equation
foo = 34
bar = 3
print(eval("foo * bar")) #print 102.  34*3=102
print("\n")

#Category:  Lists
print(list("logitech")) #print ['l', 'o', 'g', 'i', 't', 'e', 'c', 'h']
print(list("123456")) #print ['1', '2', '3', '4', '5', '6']
players = [29, 58, 66, 71, 87]
print(list(map(str, players))) #print ['29', '58', '66', '71', '87']
print(players[2]) #print 66
players[2] = 68
print(players[2]) #print 68
newplayers = [90, 91, 98]
players = newplayers + players
print(players) #print [90, 91, 98, 29, 58, 68, 71, 87]
players.append(120)
print(players) #print [90, 91, 98, 29, 58, 68, 71, 87, 120]
players[7:] = [-1, -2, -3]
print(players) #print [90, 91, 98, 29, 58, 68, 71, -1, -2, -3]
items = ["cat","dog","moon","shoe"]
print(min(items)) #print cat
print(max(items)) #print shoe
print(items[1]) #print dog
print(items.index("cat")) #print 0
items = ["cat","dog","moon","shoe"]
if items in ("cat","dog"):
	print("There are animals in the list.")
else:
	print("What's going on here.") #print What's going on here.
for eachitems in items:
	if eachitems in ("cat","dog"):
		print("There are animals in the list.")
	else:
		print("What's going on here.")
'''
There are animals in the list.
There are animals in the list.
What's going on here.
What's going on here.
'''
numbersxlist = [1, 2, 3]
print(numbersxlist)
numbersxlist.append(4)
print(numbersxlist)
#numbersxlist.append(5, 6) #TypeError: append() takes exactly one argument (2 given)
numbersxlist.append([5, 6])
print(numbersxlist) #print [1, 2, 3, 4, [5, 6]]
numbersxlist.pop()
print(numbersxlist) #print [1, 2, 3, 4]
#extend extends list by appending elements from the iterable; concatenates the first list with another list or another iterable not necessarily a list.  Iterates over its argument adding each element to the list and extending the length of the list.
numbersxlist.extend([5, 6])
print(numbersxlist) #print [1, 2, 3, 4, 5, 6]
numbersxlist.insert(3, 987)
print(numbersxlist) #print [1, 2, 3, 987, 4, 5, 6]
items[1] = "parrot"
print(items) #print ['cat', 'parrot', 'moon', 'shoe']
items.append("door")
print(items) #print ['cat', 'parrot', 'moon', 'shoe', 'door']
items.insert(0,"door beginning at index zero")
print(items) #print ['door beginning at index zero', 'cat', 'parrot', 'moon', 'shoe', 'door']
items.remove("door beginning at index zero")
print(items) #print ['cat', 'parrot', 'moon', 'shoe', 'door']
items.pop()  #.pop() removes the last item in a list
print(items) #print ['cat', 'parrot', 'moon', 'shoe']
savemooninvariable = items.pop(2)
print(items) #print ['cat', 'parrot', 'shoe']
print(savemooninvariable) #print moon
tryit = ['cat', 'parrot', 'shoe']
del tryit[2]
print(tryit) #print ['cat', 'parrot']
tryit.remove("parrot")
print(tryit) #print ['cat']
removespecificnumber = [43, 2983, 128794, 732897, 18374801, 583909873, 1003874, 9]
giveme18374801savehere = removespecificnumber.remove(18374801)
print(giveme18374801savehere) #None
duplicateitems = ["cat","dog","moon","shoe","cat","dog","cat"]
print(len(duplicateitems)) #print 7
print(duplicateitems.count("cat")) #print 3
print(duplicateitems.count("dog")) #print 2
print(sorted(duplicateitems)) #print ['cat', 'cat', 'cat', 'dog', 'dog', 'moon', 'shoe']
print(sorted(duplicateitems, reverse=True)) #print ['shoe', 'moon', 'dog', 'dog', 'cat', 'cat', 'cat']
duplicateitems.sort()
print(duplicateitems) #print ['cat', 'cat', 'cat', 'dog', 'dog', 'moon', 'shoe']
duplicateitems.sort(reverse = True)
print(duplicateitems) #print ['shoe', 'moon', 'dog', 'dog', 'cat', 'cat', 'cat']
duplicateitems.reverse()
print(duplicateitems) #print ['shoe', 'moon', 'dog', 'dog', 'cat', 'cat', 'cat']
duplicateitems = []
print(duplicateitems) #print []
backwarditems = ["mop","hop","cat","dog","moon","shoe","dog","cat"]
print(backwarditems) #print ['mop', 'hop', 'cat', 'dog', 'moon', 'shoe', 'dog', 'cat']
backwarditems.reverse()
print(backwarditems) #print ['cat', 'dog', 'shoe', 'moon', 'dog', 'cat', 'hop', 'mop']
mylist = [10,31,20]
mylist.sort() #listvariable.sort() doesn't return a sorted list.
print(mylist) #print [10, 20, 31]
sortabsolutevalue = [10, -5, 3, -2, 30, -20]
sortabsolutevalue.sort(key=abs)
print(sortabsolutevalue) #print [-2, 3, -5, 10, -20, 30]
sortcaseinsensitive = "This is a bunch of words in a Python string".split()
print(sortcaseinsensitive) #print ['This', 'is', 'a', 'bunch', 'of', 'words', 'in', 'a', 'Python', 'string']
sortcaseinsensitive.sort(key=str.lower)
print(sortcaseinsensitive) #print ['a', 'a', 'bunch', 'in', 'is', 'of', 'Python', 'string', 'This', 'words']
def functionsortbackwards(word):
	return word[::-1]
sortlastletteroftheword = "This is a bunch of words in a Python string".split()
sortlastletteroftheword.sort(key=functionsortbackwards)
print(sortlastletteroftheword) #print ['a', 'a', 'of', 'string', 'bunch', 'in', 'Python', 'words', 'is', 'This']
#sortlastletteroftheword.sort(key=lambda word: word[::-1]) #use lamboda
llist = ["candy","cookie","cracker","chips"]
print("-".join(llist)) #print candy-cookie-cracker-chips
print(" ".join(llist)) #print candy cookie cracker chips
pipelist = ["|||"]
fourpipelists = pipelist*4
print(fourpipelists) #print ['|||', '|||', '|||', '|||']
joinfourpipelists = "".join(fourpipelists)
print(joinfourpipelists) #print ||||||||||||
numberslist = [11,22,33,44,55,66,77,88]
print(numberslist) #print [11, 22, 33, 44, 55, 66, 77, 88]
print(numberslist[2:7]) #print [33, 44, 55, 66, 77]
print(numberslist[:4]) #print [11, 22, 33, 44]
print(numberslist[-1]) #print 88
print(numberslist[-3:]) #print [66, 77, 88] #a negative index returns an element a certain distance from the end of a list
print(numberslist[::-1]) #print [88, 77, 66, 55, 44, 33, 22, 11]
print(numberslist[::-3]) #print [88, 55, 22]
print(numberslist[2:5]) #print [33, 44, 55]
print(numberslist[0::2]) #print [11, 33, 55, 77]
print(numberslist[-1::-2]) #print [88, 66, 44, 22]
print(numberslist[-4::-2]) #print [55, 33, 11]
print(numberslist[0::-3]) #print [11]
print(numberslist[3::-3]) #print [44, 11]
print(numberslist[3::3]) #print [44, 77]
print(numberslist[5:9:-3]) #print []
print(numberslist[5:9:-1]) #print []
print(numberslist[1:4:-1]) #print []
print(list(range(1,11))) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(10,101,10))) #print [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
date, name, price = ["December 31, 2015","Bread Gloves",8.51]
print(name) #print Bread Gloves
randomnumbers = [1, 5676, 30943]
chrisfamilyguyfriends = ["Chandler", "Fonz", "Elmo"]
alistoflists = [randomnumbers, chrisfamilyguyfriends]
print(alistoflists) #print [[1, 5676, 30943], ['Chandler', 'Fonz', 'Elmo']]
singlea = [1, 2, 3, 4, 5]
doubleb = [10, 11, 12, 13, 14]
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachsinglea) #print 1\n 2\n 3\n 4\n 5
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachdoubleb) #print 10\n 11\n 12\n 13\n 14
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachsinglea, eachdoubleb) #print 1 10\n 2 11\n 3 12\n 4 13\n 5 14
singlea = [1, 2, 3, 4, 5]
doubleb = [10, 11, 12, 13, 14]
singleadoubleb = []
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
	singleadoubleb.append(eachsinglea+eachdoubleb)
print(singleadoubleb) #print [11, 13, 15, 17, 19]
listinformation1 = []
imagename = "three"
imageulr = "https"
listinformation1.append([imagename, imageulr])
print(listinformation1) #print [['three', 'https']]
imagename = "top"
imageulr = "https"
listinformation1.append([imagename, imageulr])
print(listinformation1) #print [['three', 'https'], ['top', 'https']]
for x in listinformation1:
    print(x[0], x[1])
    '''
    three https
    top https
    '''
tuplelist = [[1, "run"], [2, "shoe"], [3, "three"], [4, "four"]]
print(tuplelist) #print [[1, 'run'], [2, 'shoe'], [3, 'three'], [4, 'four']]
for eachtuplelist in tuplelist:
    print(eachtuplelist[0], eachtuplelist[1])
    '''
    1 run
    2 shoe
    3 three
    4 four
    '''
import heapq
grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(grades) #print [32, 43, 654, 34, 132, 66, 99, 532]
print(min(grades)) #print 32
print(max(grades)) #print 654
print(sum(grades)) #print 1592
print(heapq.nlargest(1, grades)) #print [654]
print(heapq.nlargest(3, grades)) #print [654, 532, 132]
print(heapq.nsmallest(2, grades)) #print [32, 34]
stocks = [{"Ticker": "AAPL", "Price": 201}, {"Ticker": "GOOG", "Price": 800}, {"Ticker": "F", "Price": 54}, {"Ticker": "MSFT", "Price": 313}, {"Ticker": "TUNA", "Price": 68}]
print(stocks) #print [{'Ticker': 'AAPL', 'Price': 201}, {'Ticker': 'GOOG', 'Price': 800}, {'Ticker': 'F', 'Price': 54}, {'Ticker': 'MSFT', 'Price': 313}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nsmallest(2, stocks, key=lambda stock:stock["Price"])) #print [{'Ticker': 'F', 'Price': 54}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nsmallest(2, stocks, key=lambda anyvariable:anyvariable["Price"])) #print [{'Ticker': 'F', 'Price': 54}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nlargest(2, stocks, key=lambda anyvariable:anyvariable["Ticker"])) #print [{'Ticker': 'TUNA', 'Price': 68}, {'Ticker': 'MSFT', 'Price': 313}]
numbers = list(range(0,10))
squares = []
for onenumber in numbers:
	squares.append(onenumber*onenumber)
print(squares) #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squareslistcomprehension = [onenumber*onenumber for onenumber in numbers]
print(squareslistcomprehension) #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#Reuven Lerner:  For loops perform an action a number of times; e.g. delete files, submit scrabble score for each word in a sentence, ping IP addresses, and copy a file to a server up to five times.  List comprehension get a list back for direct use as a list or input to create a different data structure; e.g. get usernames from Unix's, turning a configuration file a list of lists, and summing a bunch of hex numbers into integers. 
#enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
firstname = ["Bucky","Tom","Taylor"]
lastname = ["Roberts","Hanks","Swift"]
print(enumerate(firstname)) #print <enumerate object at 0x7f01d25b5708>
print(list(enumerate(firstname))) #print [(0, 'Bucky'), (1, 'Tom'), (2, 'Taylor')]
print(list(enumerate(lastname))) #print [(0, 'Roberts'), (1, 'Hanks'), (2, 'Swift')]
print(tuple(enumerate(firstname))) #print ((0, 'Bucky'), (1, 'Tom'), (2, 'Taylor'))
names = zip(firstname, lastname)
print(names) #print <zip object at 0x7f7c3a3eeb48>
for a, b in names:
	print(a,end=",")
	print(b,end=",")
	print(a, b)
'''
Bucky,Roberts,Bucky Roberts
Tom,Hanks,Tom Hanks
Taylor,Swift,Taylor Swift
'''
nameslistcomprehension = list(names)
print(nameslistcomprehension) #print []
nameslistcomprehension = list(zip(names))
print(nameslistcomprehension) #print []
nameslistcomprehension = list(zip(firstname, lastname))
print(nameslistcomprehension) #print [('Bucky', 'Roberts'), ('Tom', 'Hanks'), ('Taylor', 'Swift')]
print(list(zip(firstname, lastname))) #print [('Bucky', 'Roberts'), ('Tom', 'Hanks'), ('Taylor', 'Swift')]
print(list(zip(firstname, lastname))[1]) #print ('Tom', 'Hanks')
print(list(zip(firstname, lastname))[1][1]) #print Hanks
print(tuple(zip(firstname, lastname))) #print (('Bucky', 'Roberts'), ('Tom', 'Hanks'), ('Taylor', 'Swift'))
listsquared = [n**2 for n in range(1,7)] #list comprehension
print(listsquared) #print [1, 4, 9, 16, 25, 36]
print(len(listsquared)) #print 6
numbersa = [1, 5, 10, 79]
numbersb = [2, 3, 42, 79]
numbersab = zip(numbersa, numbersb)
for numbersa, numbersb in numbersab:
	if numbersa > numbersb:
		print(numbersa)
	elif numbersa < numbersb:
		print(numbersb)
	else:
		print(numbersa,"two equal numbers.")
"""
2
5
42
79 two equal numbers.
"""
players = [29, 58, 66, 71, 87]
for eachplayers in players[0:3]:
	print(eachplayers, end=" ") #print 29 58 66
for eachnumber in range(100,-51,-25):
	print(eachnumber, end=", ") #print 100, 75, 50, 25, 0, -25, -50,
bikes = "A trek is a bike"
if "trek" in bikes:
	print("Yes") #print Yes
if "surly" not in bikes:
	print("not in") #print not in
bikes = ["trek","bobby","alamo","surly"]
if "trek" in bikes:
	print("Yes") #print Yes
print("alamo" in bikes) #print True
#Sometimes it’s important to check all of the conditions of interest. Use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True.
requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
	print("Adding mushrooms") #print Adding mushrooms
if "pepperoni" in requested_toppings:
	print("Adding pepperoni")
if "extra cheese" in requested_toppings:
	print("Adding extra cheese") #print Adding extra cheese
requested_toppings = ["there is something here"]
if requested_toppings:
	print("Okay what do I do") #print Okay what do I do
ordinalnumbers = list(range(1,10))
for eachordinalnumbers in ordinalnumbers:
	if eachordinalnumbers == 1: #in (1) error message
		print(str(eachordinalnumbers)+"st")
	elif eachordinalnumbers in (2, 3):
		print(str(eachordinalnumbers)+"nd")
	else:
		print(str(eachordinalnumbers)+"th")
'''
1st
2nd
3nd
4th
5th
6th
7th
8th
9th
'''
randomnumbers = [5,8,9,1]
if randomnumbers in (5,9):
	print("There are fives and nines")
else:
	print("What's going on here.") #print What's going on here.
for eachrandomnumbers in randomnumbers:
	if eachrandomnumbers in (5,9):
		print("There are fives and nines")
	else:
		print("What's going on here.")
'''
There are fives and nines
What's going on here.
There are fives and nines
What's going on here.
'''
unconfirmedusers = ["Alice","Brian","Candace"]
confirmedusers = []
while unconfirmedusers:
	moveunconfirmeduserstoconfirmed = unconfirmedusers.pop()  #.pop() removes the last items in the list
	confirmedusers.append(moveunconfirmeduserstoconfirmed)
print("Confirmedusers list populated",confirmedusers) #print Confirmedusers list populated ['Candace', 'Brian', 'Alice']
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
while "cat" in pets:
	pets.remove("cat")
print("Cat is removed",pets) #print Cat is removed ['dog', 'dog', 'goldfish', 'rabbit']


#Category:  Tuples
print(tuple("My Python")) #print ('M', 'y', ' ', 'P', 'y', 't', 'h', 'o', 'n')
print(tuple((1,2,3))) #print (1, 2, 3)
print(tuple(["g","n","u"])) #print ('g', 'n', 'u')
print(tuple(list("GNU"))) #print ('G', 'N', 'U')
lettertuple = ("a","b","c")
print(lettertuple[2]) #print c
numbertuple = (1,2,3,4,5,6,7,8)
print(numbertuple[1:5]) #print (2, 3, 4, 5)
numbertuple = ()
print(numbertuple) #print ()
randomnumbers = (1, 5676, 30943)
chrisfamilyguyfriends = ("Chandler", "Fonz", "Elmo")
alistoftuples = [randomnumbers, chrisfamilyguyfriends]
print(alistoftuples) #print [(1, 5676, 30943), ('Chandler', 'Fonz', 'Elmo')]
atupleoftuples = (randomnumbers, chrisfamilyguyfriends)
print(atupleoftuples) #print ((1, 5676, 30943), ('Chandler', 'Fonz', 'Elmo'))
randomnumbers = (1, 5676, 30943)
chrisfamilyguyfriends = ("Chandler", "Fonz", "Elmo")
from itertools import product
alltuples = product(randomnumbers, chrisfamilyguyfriends)
print(alltuples) #print <itertools.product object at 0x7f602789fea0>
print(tuple(alltuples)) #print ((1, 'Chandler'), (1, 'Fonz'), (1, 'Elmo'), (5676, 'Chandler'), (5676, 'Fonz'), (5676, 'Elmo'), (30943, 'Chandler'), (30943, 'Fonz'), (30943, 'Elmo'))
print(list(alltuples)) #print []
alistoftuples = list(product(randomnumbers, chrisfamilyguyfriends))
print(alistoftuples) #print [(1, 'Chandler'), (1, 'Fonz'), (1, 'Elmo'), (5676, 'Chandler'), (5676, 'Fonz'), (5676, 'Elmo'), (30943, 'Chandler'), (30943, 'Fonz'), (30943, 'Elmo')]
numberletter = [("c",3),("a",1),("b",2)]
print(numberletter) #print [('c', 3), ('a', 1), ('b', 2)]
numberletter.sort()
print(numberletter) #print [('a', 1), ('b', 2), ('c', 3)]

#Category:  Dictionaries
menu = {}
menu["Chicken Alfredo"] = 14.50
print(menu) #print {'Chicken Alfredo': 14.5}
menu['Hamburger'] = 10.00 #add key: item to menu dictionary
menu['BBQ Chicken'] = 7.50 #add key: item to menu dictionary
menu['Ham Sandwich'] = 6.25 #add key: item to menu dictionary
print(len(menu)) #print 4
print(menu) #print {'Ham Sandwich': 6.25, 'Chicken Alfredo': 14.5, 'BBQ Chicken': 7.5, 'Hamburger': 10.0}
del menu["Chicken Alfredo"]
print(menu) #print {'Ham Sandwich': 6.25, 'BBQ Chicken': 7.5, 'Hamburger': 10.0}
medictionary = {"Name": "Raymond Mar", "Age": 46, "Board Games": True, "Attributes": ["strong", "high self-esteem", "self-trained genius"], "Favorite Color": "White"}
print(medictionary) #print {'Name': 'Raymond Mar', 'Age': 46, 'Board Games': True, 'Attributes': ['strong', 'high self-esteem', 'self-trained genius'], 'Favorite Color': 'White'}
#items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary
print(medictionary.items()) #print dict_items([('Name', 'Raymond Mar'), ('Age', 46), ('Board Games', True), ('Attributes', ['strong', 'high self-esteem', 'self-trained genius']), ('Favorite Color', 'White')])
print(medictionary.keys()) #print dict_keys(['Name', 'Age', 'Board Games', 'Attributes', 'Favorite Color'])
print(type(medictionary.keys())) #print <class 'dict_keys'>
print(medictionary.values()) #print dict_values(['Raymond Mar', 46, True, ['strong', 'high self-esteem', 'self-trained genius'], 'White'])
print(type(medictionary.values())) #print <class 'dict_values'>
print(list(medictionary.values())) #print ['Raymond Mar', 46, True, ['strong', 'high self-esteem', 'self-trained genius'], 'White']
print(type(list(medictionary.values()))) #print <class 'list'>
medictionarylist = list(medictionary.values())
print(medictionarylist[4]) #print White
for key in medictionary:
    print(key, medictionary[key])
    '''
    Name Raymond Mar
    Age 46
    Board Games True
    Attributes ['strong', 'high self-esteem', 'self-trained genius']
    Favorite Color White
    '''
classmatesdictionary = {"Tony":"cool but smells","Emma":"sits behind me","Lucy":"asks too many questions"}
print(classmatesdictionary) #print {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'Lucy': 'asks too many questions'}
print(classmatesdictionary["Emma"]) #print sits behind me
for keysonly in classmatesdictionary.keys():
	print(keysonly) #print Tony\n Emma\n Lucy
for valuesonly in classmatesdictionary.values():
	print(valuesonly) #print cool but smells\n sits behind me\n asks too many questions
for key, value in classmatesdictionary.items():
	print(key+" "+value,end="/") #print Tony cool but smells/Emma sits behind me/Lucy asks too many questions/
classmatesdictionary["Lucy"] = "I'm from Peanuts"
print(classmatesdictionary) #print {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'Lucy': "I'm from Peanuts"}
classmatesdictionary.update({"Lucy":"Psychiatric Help $0.05"})
print(classmatesdictionary) #print {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'Lucy': 'Psychiatric Help $0.05'}
classmatesdictionary["Zoe"] = "I'm the new person"
print(classmatesdictionary) #print {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'Lucy': "Psychiatric Help $0.05", 'Zoe': "I'm the new person"}
for sortedkeys in sorted(classmatesdictionary.keys()):
	print(sortedkeys,end=",") #print Emma,Lucy,Tony,Zoe,
dictionary = {"a": "apple", "b": "berry", "c": "cherry"}
for defaultgetkeyindictionary in dictionary:
    print("key " + defaultgetkeyindictionary) #print key a\n key b\n key c
for defaultgetkeyindictionary in dictionary:
    print("key " + defaultgetkeyindictionary)
    print("print the value " + dictionary[defaultgetkeyindictionary])
    '''
    key a
    print the value apple
    key b
    print the value berry
    key c
    print the value cherry
    '''
mydictionary = {"fish": ["c", "a", "r", "p"], "cash": -4483, "luck":"good"}
print(mydictionary["fish"]) #print ['c', 'a', 'r', 'p']
print(mydictionary["fish"][2]) #print r
mydictionary["inventory"] = ["rations","flashlight","sleeping bag"]
print(mydictionary) #print {'cash': -4483, 'fish': ['c', 'a', 'r', 'p'], 'luck': 'good', 'inventory': ['rations', 'flashlight', 'sleeping bag']}
mydictionary["fish"].sort() #sort key fish's list in dictionary mydictionary
print(mydictionary) #print {'luck': 'good', 'inventory': ['rations', 'flashlight', 'sleeping bag'], 'fish': ['a', 'c', 'p', 'r'], 'cash': -4483}
mydictionary["fish"].remove("p")
print(mydictionary) #print {'luck': 'good', 'inventory': ['rations', 'flashlight', 'sleeping bag'], 'fish': ['a', 'c', 'r'], 'cash': -4483}
pizzadictionarylist = {"crust":"thick", "toppings":["mushrooms","cheese","salami","pepperoni","bell peppers","meatballs","onions"]}
for eachpizzadictionarylisttoppings in pizzadictionarylist["toppings"]:
	print(eachpizzadictionarylisttoppings) #print mushrooms\n cheese\n salami\n pepperoni\n bell peppers\n meatballs\n onions
for eachvalues in pizzadictionarylist.values():
	print(eachvalues) #print thick\n ['mushrooms', 'cheese', 'salami', 'pepperoni', 'bell peppers', 'meatballs', 'onions']
for eachvalues in pizzadictionarylist.values():
	for eachvaluesindividual in eachvalues:
		print(eachvaluesindividual,end="\\") #print t\h\i\c\k\mushrooms\cheese\salami\pepperoni\bell peppers\meatballs\onions\
#nested dictionary
nesteddictionarycities = {"springdale": {"country": "usa","population": 3000,"fact": "zion national park",}, "anaheim": {"country": "usa","population": 50000,"fact": "disneyland"}, "london": {"country": "great britian","population": 500000, "fact": "london bridge"}}
for city, information in nesteddictionarycities.items():
	print("City: " +city)
	print("Country: " +information["country"]+ " population: " ,information["population"])
	print("fact: " +information["fact"])
'''
Country: usa population:  3000
fact: zion national park
City: anaheim
Country: usa population:  50000
fact: disneyland
City: london
Country: great britian population:  500000
fact: london bridge
'''
nameandhobby = {}
while True:
	name = input("What is your name? ")
	hobby = input("What is your hobby? ")
	nameandhobby[name] = hobby
	exit = input("Do you want to exit? Y or N? ")
	if exit == "Y":
		break
	else:
		continue
print(nameandhobby) #print {'Raymond': 'Read books', 'James': 'Video games', 'Michelle': 'Cooking'}
#order list order dictionary keep track of order
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"
print(favorite_languages) #print OrderedDict([('jen', 'python'), ('sarah', 'c'), ('edward', 'ruby'), ('phil', 'python')])
for name, language in favorite_languages.items():
	print(name+ "'s favorite language is " +language+ ".") #print jen's favorite language is python.\n sarah's favorite language is c.\n edward's favorite language is ruby.\n phil's favorite language is python.
stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN":306.21, "AAPL": 99.76}
print(stocks) #print {'GOOG': 520.54, 'FB': 76.45, 'YHOO': 39.28, 'AMZN': 306.21, 'AAPL': 99.76}
print(zip(stocks.values(), stocks.keys())) #print <zip object at 0x7f56392f8b48>
print(min(stocks)) #print AAPL
print(zip(stocks.keys(),stocks.values())) #print <zip object at 0x7f85f40ac648>
print(min(zip(stocks.values(), stocks.keys()))) #print (39.28, 'YHOO')
print(max(zip(stocks.keys(), stocks.values()))) #print ('YHOO', 39.28)
print(list(zip(stocks.keys(),stocks.values()))) #print [('GOOG', 520.54), ('FB', 76.45), ('YHOO', 39.28), ('AMZN', 306.21), ('AAPL', 99.76)]
print(sorted(zip(stocks.keys(),stocks.values()))) #print [('AAPL', 99.76), ('AMZN', 306.21), ('FB', 76.45), ('GOOG', 520.54), ('YHOO', 39.28)]
del(stocks["GOOG"])
print(stocks) #print {'FB': 76.45, 'YHOO': 39.28, 'AMZN': 306.21, 'AAPL': 99.76}
stocks.clear()
print(stocks) #print {}
users = [{"fname": "Bucky", "lname": "Roberts"},{"fname": "Tom", "lname": "Roberts"},{"fname": "Bernie", "lname": "Zunks"},{"fname": "Jenna", "lname": "Hayes"},{"fname": "Sally", "lname": "Jones"},{"fname": "Amanda", "lname": "Roberts"},{"fname": "Tom", "lname": "Williams"},{"fname": "Dean", "lname": "Hayes"},{"fname": "Bernie", "lname": "Barbie"},{"fname": "Tom", "lname": "Jones"}]
print(users) #print [{'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Tom', 'lname': 'Jones'}]
from operator import itemgetter
print(sorted(users, key=itemgetter("fname"))) #print [{'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}, {'fname': 'Tom', 'lname': 'Jones'}]
print(sorted(users, key=itemgetter("fname","lname"))) #print [{'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}]
#Individual dictionaries, variable dictionaries, assigned dictionaries
lloyd = {"name": "Lloyd", "homework": [0.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0]}
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
tyler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}
print(lloyd) #print {'name': 'Lloyd', 'homework': [0.0, 97.0, 75.0, 92.0], 'quizzes': [88.0, 40.0, 94.0], 'tests': [75.0, 90.0]}
students = [lloyd, alice, tyler]
print(students) #print [{'name': 'Lloyd', 'homework': [0.0, 97.0, 75.0, 92.0], 'quizzes': [88.0, 40.0, 94.0], 'tests': [75.0, 90.0]}, {'name': 'Alice', 'homework': [100.0, 92.0, 98.0, 100.0], 'quizzes': [82.0, 83.0, 91.0], 'tests': [89.0, 97.0]}, {'name': 'Tyler', 'homework': [0.0, 87.0, 75.0, 22.0], 'quizzes': [0.0, 75.0, 78.0], 'tests': [100.0, 100.0]}]
print(students[1]) #print {'name': 'Alice', 'homework': [100.0, 92.0, 98.0, 100.0], 'quizzes': [82.0, 83.0, 91.0], 'tests': [89.0, 97.0]}
print(students[1]["name"]) #print Alice
print(students[1]["quizzes"]) #print [82.0, 83.0, 91.0]
print(students[1]["quizzes"][2]) #print 91
print("\n")

#Category:  Sets
duplicatenumberslist = [1,1,1,2,3,4,4,4,5]
print(set(duplicatenumberslist)) #print {1, 2, 3, 4, 5}
print(list(set(duplicatenumberslist))) #print [1, 2, 3, 4, 5]
newset = set()
newset.add(5)
newset.add(1)
newset.add(2)
print(newset) #print {1, 2, 5}
newset.update([11,1,2,5,6,8])
print(newset) #print {1, 2, 5, 6, 8, 11}
setvariable = set()
print(setvariable) #print set()
setnumbers = set([10,20,30])
print(setnumbers) #print {10, 20, 30}
setnumbers = set([10,20,30,10,20,30,40])
print(setnumbers) #print {40, 10, 20, 30}
setletters = set("abc")
print(setletters) #print {'b', 'c', 'a'}
setletters = set("abcabcabc")
print(setletters) #print {'b', 'c', 'a'}
print("a" in setletters) #print True
setletterslist = set(["abc"])
print(setletterslist) #print {'abc'}
setlettersdictionary = set({"a","b","c","a","b","c","a","b","c",})
print(setlettersdictionary) #print {'a', 'b', 'c'}
setonetwothree = {1,2,3}
print(type(setonetwothree)) #print <class 'set'>
setonetwothree.add(4)
print(setonetwothree) #print {1, 2, 3, 4}
frozensetvariable = frozenset([10, 20,30,40,50])
print(frozensetvariable) #print frozenset({40, 10, 50, 20, 30})
#frozensetvariable.add(60) #return AttributeError: 'frozenset' object has no attribute 'add'
setupdatevariable = {1,2,3}
setupdatevariable.update([10, 20, 30])
print(setupdatevariable) #print {1, 2, 3, 10, 20, 30}
setupdatevariable.update([20, 30, 40, 50])
print(setupdatevariable) #print {1, 2, 3, 40, 10, 50, 20, 30}
setaddupdatevariable = {1,2,3}
setaddupdatevariable.add("abc")
print(setaddupdatevariable) #print {1, 2, 3, 'abc'}
setaddupdatevariable.update("abc")
print(setaddupdatevariable) #print {1, 2, 3, 'a', 'b', 'abc', 'c'}
setremovevariable = {1,2,3}
setremovevariable.remove(2)
print(setremovevariable) #print {1, 3}
setone = {1,2,3,4,1000}
settwo = {3,4,5,6,2222}
setonetwounion = setone | settwo
print(setonetwounion) #print {1, 2, 3, 4, 5, 6, 1000, 2222}
print(setone.union(settwo)) #print {1, 2, 3, 4, 5, 6, 1000, 2222}
setonetwointersect = setone & settwo
print(setonetwointersect) #print {3, 4}
print(setone.intersection(settwo)) #print {3, 4}
setonetwodifference = setone ^ settwo
print(setonetwodifference) #print {1, 2, 5, 6, 1000, 2222}
print(setone.symmetric_difference(settwo)) #print {1, 2, 5, 6, 1000, 2222}
print(setone < settwo) #print False is setone a subset of settwo
print({3,4} < settwo) #print True is {3,4} a subset of settwo
print(settwo > {3,4}) #print True is settwo a superset of {3,4}
usernumbers = "1 2 3 1 2 3 1 2 3 4"
usernumberslistcomprehensionsum = sum([int(eachusernumbers) for eachusernumbers in usernumbers.split()])
print(usernumberslistcomprehensionsum) #print 22
usernumberssetcomprehensionsum = sum({int(eachusernumbers) for eachusernumbers in usernumbers.split()})
print(usernumberssetcomprehensionsum) #print 10

#Category:  If Elif Else If then
name = "Bucky"
if name == "Bucky":
	print("Hey there Bucky") #print Hey there Bucky
elif name == "Lucky":
	print("You're lucky")
else:
	print("No name")
apples = 20
if apples > 3:
	print("First if statement independent greater than three apples.") #print First if statement independent greater than three apples.
if apples > 5:
	print("Second if statement independent greater than five apples.") #print Second if statement independent greater than five apples.
if apples > 50:
	print("Third if statement independent greater than fifty apples")
else:
	print("Third if statement independent greater than fifty apples else:  is like elif True:") #print Third if statement independent greater than fifty apples else:  is like elif True:
if 10 <= apples <=20:
	print("Fourth if statement independent between 10 and 20 apples inclusive.") #print Fourth if statement independent between 10 and 20 apples inclusive.
location = "home"
if location is "home" or location is "Vegas":
	print("I'm {}".format(location)) #print I'm home
number = 90
result = isinstance(number, int)
if result:
    print(number,"is an integer int.") #print 90 is an integer int.
else:
    print(number,"is not an inteer int.")

#Category:  Functions
def functionobjectnamedhello(name):
	return "The function object named hello returns {}".format(name)
print(functionobjectnamedhello("Python calls or invokes the object attached to functionobjectnamedhello")) #print The function object named hello returns Python calls or invokes the object attached to functionobjectnamedhello
def helloreuvenlerner(name):
	"This is the docstring.  If the first line of the function is a string, then the string is seen as the documentation for the function.  Technically, the docstring is stored in the function's __doc__attribute."
	return "Hello, {}".format(name)
print(helloreuvenlerner("Raymond")) #print Hello, Raymond
help(helloreuvenlerner) #return Help on function helloreuvenlerner in module __main__: helloreuvenlerner(name) This is the docstring.  If the first line of the function is a string, then the string is seen as the documentation for the function.  Technically, the docstring is stored in the function's __doc__attribute.  (END)
def helloreuvenlernerbetterdocstring(name):
	"""
	This is the better docstring.
	Write multiple lines.
	Docstring tells user what the function does, how to run the function, and what it returns.
	"""
	return "Hello, {}".format(name)
help(helloreuvenlernerbetterdocstring)  #return Help on function helloreuvenlernerbetterdocstring in module __main__: helloreuvenlernerbetterdocstring(name) This is the better docstring. Write multiple lines. Docstring tells user what the function does, how to run the function, and what it returns. (END)
def functionmultiplepasses(variable1, variable2):
	return "I make a rhyme "+variable1+" and " +variable2+"."
print(functionmultiplepasses("blue","clue")) #return I make a rhyme blue and clue.
def functionname(number=17):
	return number
print(functionname(150)) #print 150
print(functionname()) #print 17
def functionname2(name="Raymond", action="jump", braincells=500000000, item="glue"):
	print(name+" "+action+" "+item, braincells)
functionname2(action="run") #return Raymond run glue 500000000
functionname2(action="sleep", braincells=100000000) #return Raymond sleep glue 100000000
def anoptionalargument(hobby, show, location=""):
	return "%s hobby, %s show, location is %s" %(hobby,show,location)
print(anoptionalargument("cook","Breaking Bad","New Mexico")) #print cook hobby, Breaking Bad show, location is New Mexico
print(anoptionalargument("bake","Simpsons")) #print bake hobby, Simpsons show, location is 
def dropfirstlast(grades):
	first, *middle, last = grades #first index is saved in first, last index is saved in last, the rest are saved in *middle
	avg = sum(middle)/len(middle)
	return avg
print(dropfirstlast([65, 76, 98, 54, 21])) #print 76.0.  65 saved in first, 21 saved in last, averaged 76, 98, 54 is 76.0
print(dropfirstlast([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])) #print 69.375.  65 saved in first, 78 saved in last, averaged 76, 98, 54, 21, 54, 65, 99, 88 is 69.375.
def combinestrings(*strings):
	return "".join(strings)
print(combinestrings("Ed","Al","Winry","Riza","Roy","Mei Chang")) #print EdAlWinryRizaRoyMei Chang
def printcombinestrings(functionname, *args):
	return functionname(*args)
print(printcombinestrings(combinestrings,"red","green","blue","yellow")) #print redgreenblueyellow
def multiplevalues(anynumber, *words):
	print(anynumber)
	print(words)
multiplevalues(5,"yum","boo","black") #print 5\n ('yum', 'boo', 'black')
#Nested function
def averagefunction(numbers):
    sumnumbers = sum(numbers)
    average = (sumnumbers / len(numbers))
    return average
def notafunction():
    return [1, 35, 61, 92]
print(averagefunction(notafunction())) #print 47.25
#parent and child functions
def addnumbers(*numbers, ray="sunshine"):
	total = 0
	print(numbers)
	for eachnumbers in numbers:
		total+= eachnumbers
	return total, ray
print(addnumbers(3, 32)) #print (3, 32)\n (35, 'sunshine')
print(addnumbers(-30, 30, 32, ray="moon")) #print (-30, 30, 32)\n (32, 'moon')
players = [29, 58, 66, 71, 87]
print(addnumbers(*players)) #print (29, 58, 66, 71, 87)\n (311, 'sunshine')
def addnumbers2(ray2="sunshine", *numbers2):
	total2 = 0
	print(ray2)
	print(numbers2)
	print(type(numbers2))
	for eachnumbers in numbers2:
		total2 += eachnumbers
	return ray2 and total2
print(addnumbers2())
'''
sunshine
()
<class 'tuple'>
0
'''
print(addnumbers2("rainy",3,32))
'''
rainy
(3, 32)
<class 'tuple'>
35
'''
def callmyownfunction(number):
    print(number)
    if number == 5:
        print("You won")
    else:
        number = int(input("Enter a number between one and ten "))
        callmyownfunction(number)
firstinput = int(input("Enter a number between one and ten "))
callmyownfunction(firstinput)
def onegoodturn(n):
  return n + 1
def deservesanother(n):
  return onegoodturn(n) + 2
print(onegoodturn(10)) #return 11
print(deservesanother(10)) #return 13
def parentfunction(parentlist, givetochildlist):
	while parentlist:
		parenttochildlist = parentlist.pop()
		print(parenttochildlist+" is popped.") #print need is popped.\n I is popped.\n all is popped.
		givetochildlist.append(parenttochildlist)
	print("parentfunction givetochildlist list",givetochildlist)	
def childfunction(childlist):
	print("I now have the childlist",childlist)
list1 = ["all","I","need"]
list2 = []
parentfunction(list1, list2) #print parentfunction givetochildlist list ['need', 'I', 'all']
print(list2) #print ['need', 'I', 'all']
childfunction(list2) #print I now have the childlist ['need', 'I', 'all']
#double asterisks before the parameter **userinfo cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.  Function works no matter how many additional key-value pairs are provided in the function call.
def buildprofile(first, last, **userinfo):
	profile = {}
	profile["firstname"] = first
	profile["lastname"] = last
	for key, value in userinfo.items():
		profile[key] = value
	return profile
print(buildprofile("albert","einstein",location="princeton",field="physics")) #print {'location': 'princeton', 'field': 'physics', 'lastname': 'einstein', 'firstname': 'albert'}
print(buildprofile("Jackie","Chan",hobbies="books, karate, chow mein",favorite_color="red",car="audi")) #print {'lastname': 'Chan', 'firstname': 'Jackie', 'hobbies': 'books, karate, chow mein', 'car': 'audi', 'favorite_color': 'red'}
#parent and child functions
def peopleinformation(**peopleages):
	averageage = 0
	print(peopleages) #print {'susan': 88, 'ryan': 345, 'roxanne': 45
	for age in peopleages.values():
		averageage += age
	return averageage/len(peopleages)
print(peopleinformation(susan=88, ryan=345, roxanne=45)) #print 159.33333333333334
passdictionary = {'susan': 88, 'ryan': 345, 'roxanne': 45}
print(passdictionary) #print {'susan': 88, 'ryan': 345, 'roxanne': 45}
def peopleinformation2(peopleages2):
	averageage2 = 0
	print(peopleages2) #print {'susan': 88, 'ryan': 345, 'roxanne': 45}
	for age2 in peopleages2.values():
		averageage2 += age2
	return averageage2/len(peopleages2)
print(peopleinformation2(passdictionary)) #print 159.33333333333334
def commonstartendlists(list1, list2):
	startsmatch = list1[0] == list2[0]
	endsmatch = list1[-1] == list2[-1]
	return startsmatch and endsmatch
print(commonstartendlists([1,4,6,3],[1,57,3])) #print True
print(commonstartendlists([1,4,6,3],[1,57,9])) #print False
def commonstartendlistscomma(list1, list2):
	startsmatch = list1[0] == list2[0]
	endsmatch = list1[-1] == list2[-1]
	return startsmatch, endsmatch
print(commonstartendlistscomma([1,4,6,3],[1,57,3])) #print (True, True)
print(commonstartendlistscomma([1,4,6,3],[1,57,9])) #print (True, False)
#inefficient way to print largestnumber global variable
largestnumber2 = 0
def setlargestnumber2(list_):
	largest = 0
	for number in list_:
		if number > largest:
			largest = number
	largestnumber = largest
	return largestnumber	
largestnumber2 = setlargestnumber2([45,3,67,357,33])
print(largestnumber2) #print 357
#efficient way to print largestnumber global variable
largestnumber3 = 0
def setlargestnumber3(list_):
	global largestnumber3
	largest = 0
	for number in list_:
		if number > largest:
			largest = number
	largestnumber3 = largest
	print(largestnumber3)
setlargestnumber3([45,3,67,3357,33]) #return 3357
income = [10, 30, 75]
def doublemoney(dollars):
	return dollars*2
print(map(doublemoney, income)) #print <map object at 0x7fc2d7dcb278>
print(list(map(doublemoney, income))) #print [20, 60, 150]
#Recursion
def doublenorecursion(x):
	print("x variable {}".format(x))
	x -=1
	return x
doublenorecursion(4) #return x variable 4
print(doublenorecursion(4)) #return x variable 4\n 3
def doubleyesrecursion(x):
	print("x yes recursion variable {}".format(x))
	if x == 0:
		return "x is zero is the base case"
	return doubleyesrecursion(x-1)
doubleyesrecursion(4) #return x yes recursion variable 4\n x yes recursion variable 3\n x yes recursion variable 2\n x yes recursion variable 1\n x yes recursion variable 0
print(doubleyesrecursion(4)) #return x yes recursion variable 4\n x yes recursion variable 3\n x yes recursion variable 2\n x yes recursion variable 1\n x yes recursion variable 0\n x is zero is the base case
print("\n")
#Embed Function Calls
def addten(num):
	return num+10
def double(num):
	return num*2
def triple(num):
	return num*3
number = 3
tripled = triple(number)
print(tripled) #print 9
doubled = double(tripled)
print(doubled) #print 18
addedten = addten(doubled)
print(addedten) #print 28
number = 3
result = addten(double(triple(number)))
print(result) #print 28
def assignvariable():
	#print("Assigned variable to function")
	return "Assigned variable to function"
functionvariable = assignvariable()
print(functionvariable) #print Assigned variable to function
def addfunction():
	def addtwonumbers(a, b):
		return a+b
	return addtwonumbers
functionvariable = addfunction()
print(functionvariable(4,5)) #print 9
def doubleaddfunction():
	def addtwonumbers(a,b):
		def double(n):
			return n*2
		return double(a) + double(b)
	return addtwonumbers
functionvariable = doubleaddfunction()
print(functionvariable(4,5)) #print 18
def greaterthantenfilterlist(numberlist):
	return numberlist > 10
thenumberlist = [5,7,345,78,34,5]
print(filter(greaterthantenfilterlist, thenumberlist)) #print <filter object at 0x7f5bce4d7128>
print(list(filter(greaterthantenfilterlist, thenumberlist))) #print [345, 78, 34]
print(list(map(greaterthantenfilterlist,thenumberlist))) #print [False, False, True, True, True, False]
def beginswithletterfilterlist(wordlist, prefix="e"):
	return wordlist.startswith(prefix)
thewordlist = ["earth","unicycle","moose","beed","eradicate"]
#print(filter(beginswithletterfilterlist, thewordlist,"e")) #error message filter expected 2 arguments
print(filter(beginswithletterfilterlist, thewordlist)) #print <filter object at 0x7f7ca0627828>
print(list(filter(beginswithletterfilterlist, thewordlist))) #print ['earth', 'eradicate']
#Call functions from another file.  Also call classes from another file
from functionsfile import formattedname  #RM:  functionsfile is functionsfile.py file in the same directory
firstname = input("Enter your first name in lowercase? ")
lastname = input("Enter your last name in lowercase? ")
outputformattedname = formattedname(firstname, lastname)
print("{} is your name formatted.".format(outputformattedname)) #print Joe Johnson is your name formatted.
from functionsfile import AnonymousSurvey #RM:  functionsfile is functionsfile.py file in the same directory
question = "What computer languages do you know?"
survey = AnonymousSurvey(question)
survey.displayquestion()
while True:
    response = input("Language?  Press q to quit. ")
    if response == "q":
        break
    else:
        survey.saveresponse(response)
survey.showresponse() #return The list ['HTML', 'Python', 'SQL', 'CSS', 'JavaScript', 'DAX']\n Your languages are HTML, Python, SQL, CSS, JavaScript, DAX\n HTML, Python, SQL, CSS, JavaScript, DAX

#Category:  Function Iterators
numbers = [1, 2, 3, 4, 5]
def square(x):
	return x**2
print(map(square,numbers)) #print <map object at 0x7fa402f9f470>
print(list(map(square,numbers))) #print [1, 4, 9, 16, 25]
print(map(lambda x: x**2,numbers)) #print <map object at 0x7fd294e77470>
print(list(map(lambda x: x**2,numbers))) #print [1, 4, 9, 16, 25]
def uppercase(string):
	return string.upper()
letters = ["abc","def","ghi"]
print(list(map(uppercase,letters))) #print ['ABC', 'DEF', 'GHI']
firsta, firstd, firstg = list(map(uppercase, letters))
print(firsta) #print ABC
print(firstd) #print DEF
print(firstg) #print GHI
numbersfilter = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x>3,numbersfilter))) #print [4, 5, 6]
def greaterthanthree(x):
	return x > 3
print(list(filter(greaterthanthree,numbersfilter))) #print [4, 5, 6]
from functools import reduce #Guido van Rossum says 99% of the time an explicit for loop is more readable.
print(reduce(lambda x, y: x+y,numbersfilter)) #print 21
stringsentence = ["This","is","a","sentence"]
print(reduce(lambda x, y: x+" "+y,stringsentence)) #print This is a sentence
from random import shuffle
def jumble(word):
	anagram = list(word)
	shuffle(anagram)
	return "".join(anagram)
words = ["beetroot","carrots","potatoes"]
print(map(jumble,words)) #print <map object at 0x7fbc09ee02e8>
print(list(map(jumble,words))) #print ['etetboro', 'scrrtoa', 'oaptsoet']
#list comprehension
listcomprehension = [jumble(eachwords) for eachwords in words]
print(listcomprehension) #print ['rtooeteb', 'rstcaro', 'tespoato']
countries = ["","Argentina","","Brazil","Chile","","Colombia","","Ecuador","","","Venezuela"]
print(list(filter(None,countries))) #print ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Venezuela']
numberdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
averagedata = sum(numberdata)/len(numberdata)
print(averagedata) #print 2.183333333333333
numberdatagreaterthanaverage = list(filter(lambda x: x>averagedata,numberdata))
print(numberdatagreaterthanaverage) #print [2.7, 4.1, 4.3]
numberdatalessthanaverage = list(filter(lambda x: x<averagedata,numberdata))
print(numberdatalessthanaverage) #print [1.3, 0.8, -0.1]
abunchofnames = ["raymond1", "harry", "raymond2", "edward", "raymond3", "peach tree", "raymond4", "raymond5", "kenny rogers", "raymond6", "wolverine"]
extractraymonds = [eachabunchofnames for eachabunchofnames in abunchofnames if "raymond" in eachabunchofnames]
print(extractraymonds) #print ['raymond1', 'raymond2', 'raymond3', 'raymond4', 'raymond5', 'raymond6']
extractraymondselselove = [eachabunchofnames if "raymond" in eachabunchofnames else "love" for eachabunchofnames in abunchofnames]
print(extractraymondselselove) #print ['raymond1', 'love', 'raymond2', 'love', 'raymond3', 'love', 'raymond4', 'raymond5', 'love', 'raymond6', 'love']
value = 123
print(value, "is", "even." if value % 2 == 0 else "odd.") #print 123 is odd.
x = [1.5, 2.3, 4.4, 5.4, "n", 1.5, 5.1, "a"]
xnotstring = [element for element in x if not isinstance(element, str)]
print(xnotstring) #print [1.5, 2.3, 4.4, 5.4, 1.5, 5.1]
xallstringstob = ["b" if isinstance(element, str) else element for element in x]
print(xallstringstob) #print [1.5, 2.3, 4.4, 5.4, 'b', 1.5, 5.1, 'b']
list45 = [22, 13, 45, 50, 98, 69, 43, 44, 1]
add1add5 = [(eachlist45 + 1) if eachlist45 >= 45 else (eachlist45 + 5) for eachlist45 in list45]
print(add1add5) #print [27, 18, 46, 51, 99, 70, 48, 49, 6]

#Category open file write file
#To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to look in a specific location on your system.  Here are relative paths.  with open('text_files/filename.txt') as fileobject: on Linux and OS X.  with open('text_files\filename.txt') as fileobject: on Windows.
#"r" read mode, "w" write mode, "a" append mode, "r+" read and write mode, default is read mode.
filewrite = open("thenewbostontextfile.txt","w")
filewrite.write("Writing some stuff in my text file.\n")
filewrite.write("I like bacon.\n")
filewrite.close()
fileread = open("thenewbostontextfile.txt","r")
printtextfile = fileread.read()
print(printtextfile) #print Writing some stuff in my text file.\n I like bacon.
fileread.close()
#Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.
filenamevariable = "joejamesdata.txt"
with open(filenamevariable,"a") as appendnumbersvariable:
	appendnumbersvariable.write(str(55)) #number 55 is written at the end of filenamevariable.  It doesn't necessarily append 55 at a new line
	appendnumbersvariable.write("\n"+str(999)) #number 999 is written at a new line
import os
os.remove("thenewbostontextfile.txt")
filename = "createnewfile.txt"
createnewfile = open(filename,"w")
try:
	createnewfile.write("Write this sentence")
except BaseException:
	print("BaseException error")
finally:
	createnewfile.close()
os.remove(filename)
filename = "tempexample.txt"
examplefile = open(filename,"w")
try:
	examplefile.write("Blue goose on the loose\n")
	examplefile.write("Honeycomb cereal\n")
except Exception as aserror:
	print("Problem handling file.  Error was %s" % aserror)
finally:
	examplefile.close()
os.remove(filename)
filename = "openfilewritefile.txt"
with open(filename,"w") as variableforfilename:
	lineslist = ["Line 1 happy whale on parade!\n","Line 2 red bee dancing\n","Line 3 the great git in the sky\n"]
	variableforfilename.write(lineslist[0])
	variableforfilename.write(lineslist[1])
	variableforfilename.write(lineslist[2])
os.remove(filename)
with open(filename,"w") as betterwritetofilename:
	lineslist = ["Line 1 happy whale on parade!\n","Line 2 red bee dancing\n","Line 3 the great git in the sky\n"]
	betterwritetofilename.writelines(lineslist)
filenameread = open(filename,"r")
readtextfile = filenameread.read()
print(readtextfile)
'''
Line 1 happy whale on parade!
Line 2 red bee dancing
Line 3 the great git in the sky

'''
with open(filename,"r") as anotherwayreadfile:
	for anotherwayreadfilereadlines in anotherwayreadfile.readlines():
		print(anotherwayreadfilereadlines)
'''
Line 1 happy whale on parade!

Line 2 red bee dancing

Line 3 the great git in the sky

'''
#No need for readlines()
with open(filenamevariable) as fileobjectvariable:
	for eachfileobjectvariable in fileobjectvariable:
		print(eachfileobjectvariable)
with open(filename,"a") as appendexistingtextfile:
	appendexistingtextfile.write("Append the sentence\n")
#The blank line appears because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line. If you want to remove the extra blank line, you can use rstrip() in the print statement print(variablename.rstrip())
with open(filename,"r") as anotherwayreadfile2:
	readfunction = anotherwayreadfile2.read()
	print(readfunction)
'''
Line 1 happy whale on parade!
Line 2 red bee dancing
Line 3 the great git in the sky
Append the sentence

'''
os.remove(filename)
with open(filenamevariable,"r") as fileobjectvariable:
	readlinesinlist = fileobjectvariable.readlines()
print(readlinesinlist) #print ['column1,c2,c3,c4,c5,c6,c7,c8,c9,c10\n', '9,3,8,7,6,1,0,4,2,5\n', '1,7,4,9,2,6,8,3,5,0\n', '4,8,3,9,5,7,2,6,0,1\n', '1,7,4,2,5,9,6,8,0,3\n', '0,7,5,2,8,6,3,4,1,9\n', '5,9,1,4,7,0,3,6,8,2']
oneline = ""
for eachreadlinesinlist in readlinesinlist:
	print("rstrip "+eachreadlinesinlist.rstrip())
	oneline += eachreadlinesinlist.rstrip()
print(oneline) #print column1,c2,c3,c4,c5,c6,c7,c8,c9,c109,3,8,7,6,1,0,4,2,51,7,4,9,2,6,8,3,5,04,8,3,9,5,7,2,6,0,11,7,4,2,5,9,6,8,0,30,7,5,2,8,6,3,4,1,95,9,1,4,7,0,3,6,8,2
print("\n")
#Open a text file ignore blank lines
filename = "tempdelete.txt"
testlist = []
#https://codereview.stackexchange.com/questions/145126/open-a-text-file-and-remove-any-blank-lines
with open(filename, "r") as openfilename:
    for eachopenfilename in openfilename:
        lines = eachopenfilename.strip()
        if lines:
            testlist.append(lines)
print(testlist) #print ['csvalltutorials.py', 'csvfiles', 'developer_survey_2019', 'divclassitemcontainersample.html', 'downloadimages.py', ...]
#https://stackoverflow.com/questions/40647881/skipping-blank-lines-in-read-file-python
filename = "tempdelete.txt"
testlist = []
file = open(filename)
lines = [line for line in file if line.strip()]
file.close()
print(lines)  #print ['csvalltutorials.py\n', 'csvfiles\n', 'developer_survey_2019\n', 'divclassitemcontainersample.html\n', ...]
filename = "tempdelete.txt"
testlist = []
with open(filename) as file:
    for line in file:
        if line.strip():
            testlist.append(line)
print(testlist)  #print ['csvalltutorials.py\n', 'csvfiles\n', 'developer_survey_2019\n', 'divclassitemcontainersample.html\n', ...]
linkslist = ["apple", "bananna", "orange", "bread", "apple", "strawberry", "grape", "apple", "bananna"]
with open("tempdeletelinks.txt", "w") as testwritelinks:
    for eachlinkslist in linkslist:
        testwritelinks.write(eachlinkslist)
        testwritelinks.write("\n")
'''
tempdeletelinks.txt
apple
bananna
orange
bread
apple
strawberry
grape
apple
bananna
'''
newlinkslist = []
with open("tempdeletelinks.txt", "r") as testreadlinks:
    for eachtestreadlinks in testreadlinks:
        eachline = eachtestreadlinks.strip()
        if eachline not in newlinkslist:
            newlinkslist.append(eachline)
print(newlinkslist) #print ['apple', 'bananna', 'orange', 'bread', 'strawberry', 'grape']
filename = "stringintextfile.txt"
prelist = ["apple", "orange", "bananna", "grape", "kiwi", "apple", "melon", "strawberry", "orange", "mango"]
for eachprelist in prelist:
    print(eachprelist)
    with open(filename, "r") as filenameobjectvariable:
        readcheckininfilename = filenameobjectvariable.read()
    if eachprelist in readcheckininfilename:
        print("true")
    else:
        with open(filename, "a") as checkifinfilename:
            checkifinfilename.write(eachprelist + "\n")
        print("false")
filename = "testlinks.txt"
os.remove(filename)
createnewfile = open(filename, "w")
createnewfile.close()

abunchofnames = ["raymond1", "harry", "raymond2", "edward", "raymond3", "peach tree", "raymond4", "raymond5", "kenny rogers", "raymond6", "wolverine"]
for eachabunchofnames in abunchofnames:
    with open(filename, "a") as abunchofnameswritefile:
        abunchofnameswritefile.write(eachabunchofnames)
        abunchofnameswritefile.write("\n")
newabunchofnames = ["harry", "kenny rogers"]
with open(filename, "r") as abunchofnamesreadfile:
    for eachabuncofnamesreadfile in abunchofnamesreadfile:
        eachline = eachabuncofnamesreadfile.strip()
        if eachline in newabunchofnames:
            print(eachline + " is in the list.")
        else:
            print(eachline + " is not in the list.")
            newabunchofnames.append(eachline)
'''
raymond1 is not in the list.
harry is in the list.
raymond2 is not in the list.
edward is not in the list.
raymond3 is not in the list.
peach tree is not in the list.
raymond4 is not in the list.
raymond5 is not in the list.
kenny rogers is in the list.
raymond6 is not in the list.
wolverine is not in the list.
'''
print(newabunchofnames) #print ['harry', 'kenny rogers', 'raymond1', 'raymond2', 'edward', 'raymond3', 'peach tree', 'raymond4', 'raymond5', 'raymond6', 'wolverine']
#generate 20 random numbers between 1 and 21 inclusive
counter = 0
abunchofnumbers = []
while counter < 20:
    number = random.randint(1, 21)
    abunchofnumbers.append(number)
    counter += 1
print(abunchofnumbers) #print [20, 9, 11, 13, 18, 15, 16, 7, 12, 19, 6, 5, 7, 20, 18, 2, 3, 9, 13, 12]
#write the 20 random numbers as a string in filename variable
for eachabunchofnumbers in abunchofnumbers:
    with open(filename, "a") as abunchofnumbersfile:
        abunchofnumbersfile.write(str(eachabunchofnumbers)) #write() only takes a single string argument
        abunchofnumbersfile.write("\n")
#read the 20 random numbers as a string; add any of the 20 random numbers as a string to a list newabunchofnumbers
newabunchofnumbers = []
with open(filename, "r") as abunchofnumbersfile:
    for eachabuncofnamesreadfile in abunchofnumbersfile:
        eachline = eachabuncofnamesreadfile.strip()
        if eachline in newabunchofnumbers:
            print(eachline, " is in the list.")
        else:
            print(eachline, " is not in the list.")
            newabunchofnumbers.append(eachline)
'''
20  is not in the list.
9  is not in the list.
11  is not in the list.
13  is not in the list.
18  is not in the list.
15  is not in the list.
16  is not in the list.
7  is not in the list.
12  is not in the list.
19  is not in the list.
6  is not in the list.
5  is not in the list.
7  is in the list.
20  is in the list.
18  is in the list.
...
'''
print(newabunchofnumbers) #print ['20', '9', '11', '13', '18', '15', '16', '7', '12', '19', '6', '5', '2', '3']
#convert the numbers as a string to numbers as an integer
tointegersnewabunchofnumbers = list(map(int, newabunchofnumbers))
print(tointegersnewabunchofnumbers) #print [20, 9, 11, 13, 18, 15, 16, 7, 12, 19, 6, 5, 2, 3]

#Category:  try except
filename = "alices.txt"
try:
	with open(filename,"r") as fileobject:
		contents = fileobject.read()
except FileNotFoundError:
	print(filename+" file doesn't exist.")
else:
	print(contents)
try:
	number = int("I'm a string")
	#number = (5/0)
	#number = 50/100
except ValueError:
	print(r"number = int(\"I'm a string\") is a ValueError") #print number = int(\"I'm a string\") is a ValueError
except ZeroDivisionError:
	print("number = (5/0) can't divide by zero is a ZeroDivisionError")
except:
	print("The number = 50/100 is valid code.  No error messages in except:.")
finally:
	print("The finally is printed no matter if the code works or doesn't work.  Finally always activates.") #print The finally is printed no matter if the code works or doesn't work.  Finally always activates.
age = 199
if age > 135:
	raise Exception("You're supposed to be dead.  You're older than 135 years old.") #user created an custom error message using raise Exception().  error message appered because age = 199 is greater than age > 135.
'''
Traceback (most recent call last):
  File "yywork.py", line 15, in <module>
    raise Exception("You're supposed to be dead.  You're older than 135 years old.") #user created an custom error message using raise Exception().  error message appered because age = 199 is greater than age > 135.
Exception: You're supposed to be dead.  You're older than 135 years old.
'''

#Category:  Lambda
def square(x):
	return x*x
print(square(99)) #print 9801
squarelambda = lambda x: x*x
print(squarelambda(99)) #print 9801
def sumrgb(r, g, b):
	return r+g+b
print(sumrgb(45,56,87)) #print 188
sumrgblambda = lambda r, g, b: r+g+b
print(sumrgblambda(45,56,87)) #print 188
def typetwostrings(yes, no):
	#return yes+" today is a good day "+no+".  Have a good day."
	return "{} today is a good day {}.  Have a good day.".format(yes,no)
print(typetwostrings("hi","beering")) #print hi today is a good day beering.  Have a good day.
typetwostringslambda = lambda yes, no: "{} today is a good day {}.  Have a good day.".format(yes,no)
print(typetwostringslambda("hi","beering")) #print hi today is a good day beering.  Have a good day.
removeduplicateslambda = lambda givemeduplicates:  list(set(givemeduplicates))
print(removeduplicateslambda("roooot")) #print["r","o","t"]
print(removeduplicateslambda(["roooot"])) #print ['roooot']
print(removeduplicateslambda(["roooot","roooot"])) #print ['roooot']
def square(x):
	return x*x
print(square(99)) #print 9801
squarelambda = lambda x: x*x
print(squarelambda(99)) #print 9801
def sumrgb(r, g, b):
	return r+g+b
print(sumrgb(45,56,87)) #print 188
sumrgblambda = lambda r, g, b: r+g+b
print(sumrgblambda(45,56,87)) #print 188
def typetwostrings(yes, no):
	#return yes+" today is a good day "+no+".  Have a good day."
	return "{} today is a good day {}.  Have a good day.".format(yes,no)
print(typetwostrings("hi","beering")) #print hi today is a good day beering.  Have a good day.
typetwostringslambda = lambda yes, no: "{} today is a good day {}.  Have a good day.".format(yes,no)
print(typetwostringslambda("hi","beering")) #print hi today is a good day beering.  Have a good day.
removeduplicateslambda = lambda givemeduplicates:  list(set(givemeduplicates))
print(removeduplicateslambda("roooot")) #print["r","o","t"]
print(removeduplicateslambda(["roooot"])) #print ['roooot']
print(removeduplicateslambda(["roooot","roooot"])) #print ['roooot']
def evenslist(numberslist):
	evenslist = []
	for eachnumberslist in numberslist:
		if eachnumberslist % 2 == 0:
			evenslist.append(eachnumberslist)
	return evenslist
print(evenslist(range(0,51))) #print [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
def evenslistlambda(numberslist):
	isevenlambda = lambda number: number % 2 == 0
	evenslist = []
	for eachnumberlist in numberslist:
		if isevenlambda(eachnumberlist):
			evenslist.append(eachnumberlist)
	return evenslist
print(evenslistlambda(range(0,51))) #print [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
isevenlambda = lambda number: number % 2 == 0
evenslambda = lambda numberslist: list(filter(isevenlambda, numberslist))
print(evenslambda(range(0,51))) #print [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
answer = lambda x: x*7
print(answer(5)) #print 35
#Lambda separates creating a new function object and assigning a name to the function object; e.g. def functionobjectnamedhello(name).

#iterator manual counter
for n in range(0,10):
	print(n,end=", ") #print 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
generateanumber = iter(range(0,10))
print(generateanumber) #print <range_iterator object at 0x7f676de74870>
print(next(generateanumber)) #print 0
print(next(generateanumber)) #print 1
print(next(generateanumber)) #print 2
letters = "abcdefghijkl"
print(letters[next(generateanumber)]) #print d
print(letters[next(generateanumber)]) #print e
print(letters[next(generateanumber)]) #print f
print(next(generateanumber)) #print 6
print(letters[next(generateanumber)]) #print h
print(next(generateanumber)) #print 8
print(letters[next(generateanumber)]) #print j
#print(next(generateanumber)) #return StopIteration

love = "check"
print("{}".format(love))

#Category:  import statement
#import mymod
#import is a statement.  import is not a function.  import has no return value like def and class.
#mymod is the name of the module to be loaded and the name of the variable we define.  The global variable "x" defined in mymod is available afterwards as mymod.x.
#The import statement is defining a variable mymod.  We can't pass mymod as a string.
#from X import Y
#import foobar
#from foorbar import hello, x
#from mymod import *  <--Reuven says don't do this in production.  Okay in development.