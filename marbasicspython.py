#Basics Python Combine All Lessons Learned One Stop Book One Stop Documentation
#Category:  *topic*
#Categories:  Strings, Lists, Tuples, Dictionaries, try except, open file write file
#thenewbostonallvideos
#williamfisetallvideos

print(18/5) #print 3.6
print(18//5) #print 3
print(18//5.0) #print 3.0
print(18/8) #print 2.25
print(18//8) #print 2

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
splitstring = "do goat sheep boat"
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
print("\n")

#Category:  Lists
players = [29, 58, 66, 71, 87]
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
print(items[1]) #print dog
print(items.index("cat")) #print 0
items[1] = "parrot"
print(items) #print ['cat', 'parrot', 'moon', 'shoe']
items.append("door")
print(items) #print ['cat', 'parrot', 'moon', 'shoe', 'door']
items.insert(0,"door beginning at index zero")
print(items) #print ['door beginning at index zero', 'cat', 'parrot', 'moon', 'shoe', 'door']
items.remove("door beginning at index zero")
print(items) #print ['cat', 'parrot', 'moon', 'shoe', 'door']
items.pop()
print(items) #print ['cat', 'parrot', 'moon', 'shoe']
items.pop(2)
print(items) #print ['cat', 'parrot', 'shoe']
tryit = ['cat', 'parrot', 'shoe']
del tryit[2]
print(tryit) #print ['cat', 'parrot']
tryit.remove("parrot")
print(tryit) #print ['cat']
duplicateitems = ["cat","dog","moon","shoe","cat","dog","cat"]
print(duplicateitems.count("cat")) #print 3
print(duplicateitems.count("dog")) #print 2
duplicateitems.sort()
print(duplicateitems) #print ['cat', 'cat', 'cat', 'dog', 'dog', 'moon', 'shoe']
duplicateitems.reverse()
print(duplicateitems) #print ['shoe', 'moon', 'dog', 'dog', 'cat', 'cat', 'cat']
duplicateitems = []
print(duplicateitems) #print []
backwarditems = ["mop","hop","cat","dog","moon","shoe","dog","cat"]
print(backwarditems) #print ['mop', 'hop', 'cat', 'dog', 'moon', 'shoe', 'dog', 'cat']
backwarditems.reverse()
print(backwarditems) #print ['cat', 'dog', 'shoe', 'moon', 'dog', 'cat', 'hop', 'mop']
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
print(numberslist[::-1]) #print [88, 77, 66, 55, 44, 33, 22, 11]
print(numberslist[2:5]) #print [33, 44, 55]
print(numberslist[0::2]) #print [11, 33, 55, 77]
print(numberslist[-1]) #print 88
print(numberslist[-1::-2]) #print [88, 66, 44, 22]
print(list(range(1,11))) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(10,101,10))) #print [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
date, name, price = ["December 31, 2015","Bread Gloves",8.51]
print(name) #print Bread Gloves
singlea = [1, 2, 3, 4, 5]
doubleb = [10, 11, 12, 13, 14]
singleadoubleb = []
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
	singleadoubleb.append(eachsinglea+eachdoubleb)
print(singleadoubleb) #print [11, 13, 15, 17, 19]
import heapq
grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(grades) #print [32, 43, 654, 34, 132, 66, 99, 532]
print(heapq.nlargest(1, grades)) #print [654]
print(heapq.nlargest(3, grades)) #print [654, 532, 132]
print(heapq.nsmallest(2, grades)) #print [32, 34]
stocks = [{"Ticker": "AAPL", "Price": 201}, {"Ticker": "GOOG", "Price": 800}, {"Ticker": "F", "Price": 54}, {"Ticker": "MSFT", "Price": 313}, {"Ticker": "TUNA", "Price": 68}]
print(stocks) #print [{'Ticker': 'AAPL', 'Price': 201}, {'Ticker': 'GOOG', 'Price': 800}, {'Ticker': 'F', 'Price': 54}, {'Ticker': 'MSFT', 'Price': 313}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nsmallest(2, stocks, key=lambda stock:stock["Price"])) #print [{'Ticker': 'F', 'Price': 54}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nsmallest(2, stocks, key=lambda anyvariable:anyvariable["Price"])) #print [{'Ticker': 'F', 'Price': 54}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nlargest(2, stocks, key=lambda anyvariable:anyvariable["Ticker"])) #print [{'Ticker': 'TUNA', 'Price': 68}, {'Ticker': 'MSFT', 'Price': 313}]
firstname = ["Bucky","Tom","Taylor"]
lastname = ["Roberts","Hanks","Swift"]
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
list1 = [n for n in range(1,7)]
print(list1) #print [1, 2, 3, 4, 5, 6]
print(len(list1)) #print 6
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

#Category:  Tuples
lettertuple = ("a","b","c")
print(lettertuple[2]) #print c
numbertuple = (1,2,3,4,5,6,7,8)
print(numbertuple[1:5]) #print (2, 3, 4, 5)
numbertuple = ()
print(numbertuple) #print ()

#Category:  Dictionaries
stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN":306.21, "AAPL": 99.76}
print(stocks) #print {'GOOG': 520.54, 'FB': 76.45, 'YHOO': 39.28, 'AMZN': 306.21, 'AAPL': 99.76}
print(zip(stocks.values(), stocks.keys())) #print <zip object at 0x7f56392f8b48>
print(min(stocks)) #print AAPL
print(zip(stocks.keys(),stocks.values())) #print <zip object at 0x7f85f40ac648>
print(min(zip(stocks.values(), stocks.keys()))) #print (39.28, 'YHOO')
print(max(zip(stocks.keys(), stocks.values()))) #print ('YHOO', 39.28)
print(list(zip(stocks.keys(),stocks.values()))) #print [('GOOG', 520.54), ('FB', 76.45), ('YHOO', 39.28), ('AMZN', 306.21), ('AAPL', 99.76)]
print(sorted(zip(stocks.keys(),stocks.values()))) #print [('AAPL', 99.76), ('AMZN', 306.21), ('FB', 76.45), ('GOOG', 520.54), ('YHOO', 39.28)]
users = [{"fname": "Bucky", "lname": "Roberts"},{"fname": "Tom", "lname": "Roberts"},{"fname": "Bernie", "lname": "Zunks"},{"fname": "Jenna", "lname": "Hayes"},{"fname": "Sally", "lname": "Jones"},{"fname": "Amanda", "lname": "Roberts"},{"fname": "Tom", "lname": "Williams"},{"fname": "Dean", "lname": "Hayes"},{"fname": "Bernie", "lname": "Barbie"},{"fname": "Tom", "lname": "Jones"}]
print(users) #print [{'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Tom', 'lname': 'Jones'}]
from operator import itemgetter
print(sorted(users, key=itemgetter("fname"))) #print [{'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}, {'fname': 'Tom', 'lname': 'Jones'}]
print(sorted(users, key=itemgetter("fname","lname"))) #print [{'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}]
classmatesdictionary = {"Tony":"cool but smells","Emma":"sits behind me","Lucy":"asks too many questions"}
print(classmatesdictionary) #print {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'Lucy': 'asks too many questions'}
print(classmatesdictionary["Emma"]) #print sits behind me
for key, value in classmatesdictionary.items():
	print(key+" "+value,end="/") #print Tony cool but smells/Emma sits behind me/Lucy asks too many questions/
print("")
classmatesdictionary["Lucy"] = "I'm from Peanuts"
print(classmatesdictionary) #print {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'Lucy': "I'm from Peanuts"}
groceryset = {"cereal","milk","starcrunch","beer","duct tape","lotion","beer"}
print(groceryset) #print {'duct tape', 'milk', 'lotion', 'starcrunch', 'beer', 'cereal'}
if "milk" in groceryset:
	print("Yes I have milk") #print Yes I have milk
for eachgroceryset in groceryset:
	print(eachgroceryset,end=",") #print duct tape,milk,lotion,starcrunch,beer,cereal,
print("\n")
print("\n")

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


print("")
print("\n")

print("\n")



def functionname(number=17):
	return number
print(functionname(150)) #print 150
print(functionname()) #print 17
def functionname2(name="Raymond", action="jump", braincells=500000000, item="glue"):
	print(name+" "+action+" "+item, braincells)
functionname2(action="run") #return Raymond run glue 500000000
functionname2(action="sleep", braincells=100000000) #return Raymond sleep glue 100000000
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
def dropfirstlast(grades):
	first, *middle, last = grades #first index is saved in first, last index is saved in last, the rest are saved in *middle
	avg = sum(middle)/len(middle)
	return avg
print(dropfirstlast([65, 76, 98, 54, 21])) #print 76.0.  65 saved in first, 21 saved in last, averaged 76, 98, 54 is 76.0
print(dropfirstlast([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])) #print 69.375.  65 saved in first, 78 saved in last, averaged 76, 98, 54, 21, 54, 65, 99, 88 is 69.375.
income = [10, 30, 75]
def doublemoney(dollars):
	return dollars*2
print(map(doublemoney, income)) #print <map object at 0x7fc2d7dcb278>
print(list(map(doublemoney, income))) #print [20, 60, 150]
print("\n")

#Category open file write file
filewrite = open("thenewbostontextfile.txt","w")
filewrite.write("Writing some stuff in my text file.\n")
filewrite.write("I like bacon.\n")
filewrite.close()
fileread = open("thenewbostontextfile.txt","r")
printtextfile = fileread.read()
print(printtextfile) #print Writing some stuff in my text file.\n I like bacon.
fileread.close()
import os
os.remove("thenewbostontextfile.txt")
print("\n")


#Category:  try except
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
	print("The finally is printed not matter if the code works or doesn't work.  Finally always activates.") #print The finally is printed not matter if the code works or doesn't work.  Finally always activates.

answer = lambda x: x*7
print(answer(5)) #print 35

love = "check"
print("{}".format(love))

