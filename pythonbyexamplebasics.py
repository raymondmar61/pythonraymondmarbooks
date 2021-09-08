#Python By Example By Nicholas Lacey
#Challenges 1-11:  The Basics
num1 = 9
num2 = 4
print(num1 / num2) #print 2.25
wholenumber = num1 // num2
print(wholenumber) #print 2
inputisaninteger = int(input("Enter an integer: "))
print(inputisaninteger)

#Challenges 12-19:  If Statements
notsecretnumber = 55
inputnumber = int(input("Enter a number which is not 55.  You may enter 100: "))
if inputnumber == 100:
    print("100 is the number you entered.")
elif inputnumber != notsecretnumber:
    print("You followed the instructions well.  BTW, it's elif, not else if")
else:
    print("You entered 55 the not secret number")

#Challenges 20-26:  Strings
#Escape character is the backslash \
multiplelinestring = """Use triple quotes to surround multiple
for multi-line strings
or multiple line strings.
Make sure end the last line with triple quotes.
Otherwise, Python inserts a line break below."""
print(multiplelinestring)
'''
Use triple quotes to surround multiple
for multi-line strings
or multiple line strings.
Make sure end the last line with triple quotes.
Otherwise, Python inserts a line break below.
'''
convertstringtotitle = "all lower case to become title"
print(convertstringtotitle.title()) #print All Lower Case To Become Title
convertstringtopropersentence = "capitalize the first word in the proper English sentence."
print(convertstringtopropersentence.capitalize()) #print Capitalize the first word in the proper english sentence.

#Challenges 27-34:  Maths
floatnumberinput = float(input("Enter a number: "))
print(floatnumberinput) #print 458.21897869
print(round(floatnumberinput, 3)) #print 458.219
print(10**2) #print 100

#Challenges 35-44:  For Loop
for i in range(1, 10):
    print(i, end=", ") #print 1, 2, 3, 4, 5, 6, 7, 8, 9,
for i in range(1, 10, 2):
    print(i, end=", ") #print 1, 3, 5, 7, 9,
for i in range(10, 1, -3):
    print(i, end=", ") #print 10, 7, 4,
for i in range(10, 0, -3):
    print(i, end=", ") #print 10, 7, 4, 1,
for i in "word":
    print(i, end=", ") #print w, o, r, d,

#Challenges 45-51:  While Loop
again == "yes"
while again == "yes":
    print("Hello")
    again = input("Do you want to loop again?  Type yes.")
total = 0
while total < 100:
    number = int(input("Enter a number: "))
    total = total + number
print("The grand total of numbers inputted is", str(total))
stopnumber = 0
while stopnumber != 43:
    stopnumber = int(input("Type 43 to stop the loop.  "))

#Challenges 52-59:  Random
import random
numberbetweenzeroandone = random.random()
print(numberbetweenzeroandone) #0.30127997120812766
randomintegerbetweenzeroandnine = random.randint(0, 9)
print(randomintegerbetweenzeroandnine) #print 2
onerandomintegersincrementsoffive = random.randrange(0, 100, 5)
print(onerandomintegersincrementsoffive) #print 50
bonussixrandomintegersincrementsoffive = [random.randrange(0, 100, 5) for x in range(0, 6)]
print(bonussixrandomintegersincrementsoffive) #print [85, 55, 85, 95, 90, 10]
chooseacolor = random.choice(["red", "yellow", "blue", "green"])
print(chooseacolor) #print "blue"

#Python By Example By Nicholas Lacey Challenges 69-79: Tuples, Lists And Dictionaries
fruittuplecantchange = ("apple", "bananna", "strawberry", "orange")
print(fruittuplecantchange.index("strawberry")) #print 2
print(fruittuplecantchange[2]) #print strawberry
namelist = ["John", "Tim", "Sam"]
del namelist[1]
namelist.append("Roger")
print(namelist) #print ['John', 'Sam', 'Roger']
namelist.sort()
print(namelist) #print ['John', 'Roger', 'Sam']
namelist.remove("John")
print(namelist) #print ["Roger', 'Sam']
colordictionary = {1: "red", 2: "blue", 3: "green"}
colordictionary[2] = "yellow"
print(colordictionary) #print {1: 'red', 2: 'yellow', 3: 'green'}
numberlist = [154, 634, 892, 345, 341, 43]
print(len(numberlist)) #print 6
print(numberlist[1:4]) #print [634, 892, 345]
number = 892
print(number in numberlist) #print True
number = 1
print(number in numberlist) #print False
numberlist.insert(0, 987)
print(numberlist) #print [987, 154, 634, 892, 345, 341, 43]
numberlist.remove(341)
print(numberlist) #print [987, 154, 634, 892, 345, 43]
numberlist.append(-390)
print(numberlist) #print [987, 154, 634, 892, 345, 43, -390]
numberlist.pop(3)
print(numberlist) #print [987, 154, 634, 345, 43, -390]

#Python By Example By Nicholas Lacey Challenges 80-87: More String Manipulation
message = "The quick brown fox jumped over the lazy dog."
print(message.isupper()) #print False
print(message.islower()) #print False
print(message.istitle()) #print False
uppercasemessage = message.upper() #print THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG.
print(uppercasemessage)
print(uppercasemessage.isupper()) #print False
print(uppercasemessage.lower()) #print the quick brown fox jumped over the lazy dog.
print(uppercasemessage.title()) #print The Quick Brown Fox Jumped Over The Lazy Dog.
