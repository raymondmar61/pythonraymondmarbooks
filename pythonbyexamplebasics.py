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

#Python By Example By Nicholas Lacey Challenges 96-103: 2D Lists And Dictionaries
twodimensionlistgrades = [[45, 37, 54], [62, 58, 59], [49, 47, 60], [78, 83, 62]]
print(twodimensionlistgrades) #print [[45, 37, 54], [62, 58, 59], [49, 47, 60], [78, 83, 62]]
print(twodimensionlistgrades[1]) #print [62, 58, 59]
grades = [{"Ma": 45, "En": 37, "Fr": 54}, {"Ma": 62, "En": 58, "Fr": 59}, {"Ma": 49, "En": 47, "Fr": 60}, {"Ma": 78, "En": 83, "Fr": 62}]
print(grades) #print [{'Ma': 45, 'En': 37, 'Fr': 54}, {'Ma': 62, 'En': 58, 'Fr': 59}, {'Ma': 49, 'En': 47, 'Fr': 60}, {'Ma': 78, 'En': 83, 'Fr': 62}]
print(grades[0]["En"]) #print 37
gradesstudents = {"Susan": {"Ma": 45, "En": 37, "Fr": 54}, "Peter": {"Ma": 62, "En": 58, "Fr": 59}, "George": {"Ma": 49, "En": 47, "Fr": 60}, "Mary": {"Ma": 78, "En": 83, "Fr": 62}}
print(gradesstudents) #print gradesstudents
print(gradesstudents["Susan"]["En"]) #print 37
print(gradesstudents["Peter"]["En"]) #print 58
twodimensionlistsimplearray = [[2, 5, 8], [3, 7, 4], [1, 6, 9]]
print(twodimensionlistsimplearray) #print [[2, 5, 8], [3, 7, 4], [1, 6, 9]]
print(twodimensionlistsimplearray[1]) #print [3, 7, 4]
print(twodimensionlistsimplearray[1][2]) #print 4
twodimensionlistsimplearray.append(33)
print(twodimensionlistsimplearray) #print [[2, 5, 8], [3, 7, 4], [1, 6, 9], 33]
dictionarydataset = {"row1": {"col1": 54, "col2": 82, "col3": 91}, "row2": {"col1": 75, "col2": 29, "col3": 80}}
print(dictionarydataset) #print {'row1': {'col1': 54, 'col2': 82, 'col3': 91}, 'row2': {'col1': 75, 'col2': 29, 'col3': 80}}
print(dictionarydataset["row1"]) #print {'col1': 54, 'col2': 82, 'col3': 91}
print(dictionarydataset["row2"]["col2"]) #print 29
for eachnumber in dictionarydataset:
    print(dictionarydataset[eachnumber]["col2"])
    '''
    82
    29
    '''
dictionarydataset["row2"]["col2"] = 929 #change row2 and col2 to 929
print(dictionarydataset) #print {'row1': {'col1': 54, 'col2': 82, 'col3': 91}, 'row2': {'col1': 75, 'col2': 929, 'col3': 80}}
gradesstudents["New student Becky"] = {"Ma": 66, "En": 77, "Fr": 88}
print(gradesstudents) #print {'Susan': {'Ma': 45, 'En': 37, 'Fr': 54}, 'Peter': {'Ma': 62, 'En': 58, 'Fr': 59}, 'George': {'Ma': 49, 'En': 47, 'Fr': 60}, 'Mary': {'Ma': 78, 'En': 83, 'Fr': 62}, 'New student Becky': {'Ma': 66, 'En': 77, 'Fr': 88}}
for eachname in gradesstudents:
    print(gradesstudents[eachname])
    '''
    {'Ma': 45, 'En': 37, 'Fr': 54}
    {'Ma': 62, 'En': 58, 'Fr': 59}
    {'Ma': 49, 'En': 47, 'Fr': 60}
    {'Ma': 78, 'En': 83, 'Fr': 62}
    {'Ma': 66, 'En': 77, 'Fr': 88}
    '''
for eachname in gradesstudents:
    print(eachname, gradesstudents[eachname])
    '''
    Susan {'Ma': 45, 'En': 37, 'Fr': 54}
    Peter {'Ma': 62, 'En': 58, 'Fr': 59}
    George {'Ma': 49, 'En': 47, 'Fr': 60}
    Mary {'Ma': 78, 'En': 83, 'Fr': 62}
    New student Becky {'Ma': 66, 'En': 77, 'Fr': 88}
    '''
for eachnameengrades in gradesstudents:
    print(eachnameengrades, gradesstudents[eachnameengrades]["En"])
    '''
    Susan 37
    Peter 58
    George 47
    Mary 83
    New student Becky 77
    '''
del gradesstudents["New student Becky"]
print(gradesstudents) #print {'Susan': {'Ma': 45, 'En': 37, 'Fr': 54}, 'Peter': {'Ma': 62, 'En': 58, 'Fr': 59}, 'George': {'Ma': 49, 'En': 47, 'Fr': 60}, 'Mary': {'Ma': 78, 'En': 83, 'Fr': 62}}
fourrowsthreecolumns2dlist = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]  #not dictionary with row headers and column headers
print(fourrowsthreecolumns2dlist) #print [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
selectrow = 2
selectcolumn = 1
print(fourrowsthreecolumns2dlist[selectrow][selectcolumn]) #print 6
print(fourrowsthreecolumns2dlist[selectrow]) #print [1, 6, 9]
fourrowsfourcolumnsdictionary = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694}, "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612}, "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859}, "John": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
print(fourrowsfourcolumnsdictionary) #print {'John': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}, 'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612}, 'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859}}
salesname = "John"
salesregion = "N"
print(fourrowsfourcolumnsdictionary[salesname][salesregion]) #print 3904
