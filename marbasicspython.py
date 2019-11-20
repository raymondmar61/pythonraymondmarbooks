#Basics Python Combine All Lessons Learned One Stop Book One Stop Documentation
#thenewbostonallvideos

print(18/5) #print 3.6
print(18//5) #print 3
print(18//5.0) #print 3.0
print(18/8) #print 2.25
print(18//8) #print 2
print(r"this story is \nokday d'kay") #print this story is \nokday d'kay. RM:  print as-is exact text
user = "Tuna McFish"
print(user[0]) #print T
print(user[1:4]) #print una
print(user[1:9:2]) #print uaMF
print(user[-1]) #print h
print(user[-1::-1]) #print hsiFcM an
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
income = [10, 30, 75]
def doublemoney(dollars):
	return dollars*2
print(map(doublemoney, income)) #print <map object at 0x7fc2d7dcb278>
print(list(map(doublemoney, income))) #print [20, 60, 150]
print("\n")

name = "Bucky"
if name == "Bucky":
	print("Hey there Bucky") #print Hey there Bucky
elif name == "Lucky":
	print("You're lucky")
else:
	print("No name")
players = [29, 58, 66, 71, 87]
for eachplayers in players[0:3]:
	print(eachplayers, end=" ") #print 29 58 66
for eachnumber in range(100,-51,-25):
	print(eachnumber, end=", ") #print 100, 75, 50, 25, 0, -25, -50,
print("")
print("\n")

groceryset = {"cereal","milk","starcrunch","beer","duct tape","lotion","beer"}
print(groceryset) #print {'duct tape', 'milk', 'lotion', 'starcrunch', 'beer', 'cereal'}
if "milk" in groceryset:
	print("Yes I have milk") #print Yes I have milk
for eachgroceryset in groceryset:
	print(eachgroceryset,end=",") #print duct tape,milk,lotion,starcrunch,beer,cereal,
print("\n")

text = "We hope to one day become the world's leader in free, education resources.  We are constantly discovering and adding more free content to the website everyday.  There is already an enormous amount of resoruces online that can be accessed for free by anyone in the world, the main issue right now is that very little of it is organized or structured in any way.  We want to be the solution to that problem."
print(text)
splittext = text.split()
print(splittext) #print ['We', 'hope', 'to', 'one', 'day', 'become', 'the', "world's", 'leader', 'in', 'free,', 'education', 'resources.', 'We', 'are', 'constantly', 'discovering', 'and', 'adding', 'more', 'free', 'content', 'to', 'the', 'website', 'everyday.', 'There', 'is', 'already', 'an', 'enormous', 'amount', 'of', 'resoruces', 'online', 'that', 'can', 'be', 'accessed', 'for', 'free', 'by', 'anyone', 'in', 'the', 'world,', 'the', 'main', 'issue', 'right', 'now', 'is', 'that', 'very', 'little', 'of', 'it', 'is', 'organized', 'or', 'structured', 'in', 'any', 'way.', 'We', 'want', 'to', 'be', 'the', 'solution', 'to', 'that', 'problem.']
from collections import Counter
topwords = Counter(splittext)
topthree = topwords.most_common(3)
print(topthree) #print [('the', 5), ('to', 4), ('We', 3)]
print("\n")

classmatesdictionary = {"Tony":"cool but smells","Emma":"sits behind me","Lucy":"asks too many questions"}
print(classmatesdictionary) #print {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'Lucy': 'asks too many questions'}
print(classmatesdictionary["Emma"]) #print sits behind me
for key, value in classmatesdictionary.items():
	print(key+" "+value,end="/") #print Tony cool but smells/Emma sits behind me/Lucy asks too many questions/
print("")
classmatesdictionary["Lucy"] = "I'm from Peanuts"
print(classmatesdictionary) #print {'Tony': 'cool but smells', 'Emma': 'sits behind me', 'Lucy': "I'm from Peanuts"}
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
print("\n")

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












