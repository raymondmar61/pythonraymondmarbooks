#If, elseif which is elif, else
flowcontrol = "elif is elseif in Python"
if flowcontrol == "use double equal signs for comparison":
    print("Remember colon at the end of the if statement")
elif flowcontrol == "elif is elseif in Python":
    print("Type elif for else if") #print Type elif for else if
elif flowcontrol == "type if statements by logic":
    print("If statements stop at the first true.")
else:
    print("All ifs and elfis are false the else statement is printed.")
apples = 20
if apples > 3:
    print("First if statement independent greater than three apples at 3.") #print First if statement independent greater than three apples at 3.
if apples > 5:
    print("Second if statement independent greater than three apples at 5.") #print Second if statement independent greater than three apples at 5.
if apples > 50:
    print("Third if statement independent greater than fifty applies at 50.")
else:
    print("Third if statement independent greater than fifty applies at 50 with an else less than or equal to fifty applies.") #print Third if statement independent greater than fifty applies at 50 with an else less than or equal to fifty applies.
if 10 <= apples <= 20:
    print("If statement between if statement greater than equal less than equal") #print If statement between if statement greater than equal less than equal
grade = 77
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C") #print C
elif grade >= 60:
    print("D")
else:
    print("If statement exits at the first True")
truevariable = True
if truevariable:
    print("The truevariable is True.  Print the sentence.") #print The truevariable is True.  Print the sentence.
truesentence = "Anything between the quotes"
if truesentence:
    print("The truesentence is True.  Print the sentence.") #print The truevariable is True.  Print the sentence.
andortrue = True
andorfalse = False
if andortrue and andorfalse:
    print("if and Execute when both conditions are true.  True and True is True.")
else:
    print("if and Execute when the conditions are false.  True and False or False and True is False.") #print if and Execute when the conditions are false.  True and False or False and True is False.
if andortrue or andorfalse:
    print("if or Execute when either condition is true.  True or False, or False or True, is True.") #print if or Execute when either condition is true.  True or False, or False or True, is True.
else:
    print("if or Execute when either condition is false.  False or False is False.")
if not(andortrue) or andorfalse:
    print("if or Execute when either condition is true.  True or False, or False or True, is True.")
else:
    print("if or Execute when either condition is false.  False or False is False.") #print if or Execute when either condition is false.  False or False is False.
numberintuple = 7
if numberintuple in (7, 11):
    print("Winner") #print Winner
elif numberintuple in (2, 3, 12):
    print("Loser")
else:
    print("Point number established")
name = "Mary"
password = "swordfish"
if name == "Mary":
    if password == "swordfish":
        print("Name and password correct") #print Name and password correct
    else:
        print("Name or password incorrect")
else:
    print("Name incorrect")
name = "Barry"
password = "swordfish"
if name == "Mary":
    if password == "swordfish":
        print("Name and password correct")
    else:
        print("Name or password incorrect")
else:
    print("Name incorrect") #print Name incorrect
name = "Mary"
password = "nested ifs nested if statements"
if name == "Mary":
    if password == "swordfish":
        print("Name and password correct")
    else:
        print("Name or password incorrect") #print Name or password incorrect
else:
    print("Name incorrect")
secretnumber = 55
inputnumber = int(input("Convert to int() after input() or outside input(): "))
if inputnumber == secretnumber:
    print("You guessed the secret number")
    print("A second print statement")
    secretnumber = 65
    print("I change the secret number")
    print("Multiple actions contained in if statement")
print(secretnumber)
'''
Convert to int() after input() or outside input(): 55
You guessed the secret number
A second print statement
I change the secret number
Multiple actions contained in if statement
65
'''
#yytest.py:30: SyntaxWarning: "is" with a literal. Did you mean "=="? if location is "home" or location is "Vegas":
# location = "home"
# if location is "home" or location is "Vegas":
#     print(f"If statment with ors and iss {location}.") #print If statment with ors and iss home.
#     print("If statment with ors and iss {}.".format(location)) #print If statment with ors and iss home.
integernumber = 90
checkdatatypefunciton = isinstance(integernumber, int)
print(checkdatatypefunciton)
if checkdatatypefunciton:
    print(integernumber, "is an integer int by checking data type") #print 90 is an integer int by checking data type
else:
    print(integernumber, "is not an integer int by checking data type")
if type(integernumber) == int:
    print("isinstance function better than type(integernumber) == int") #print isinstance function better than type(integernumber) == int

#For loop
stringisalist = "Zophie"
for eachstringisalist in stringisalist:
    print(eachstringisalist, end="_") #print Z_o_p_h_i_e_
numberslist = [11, 37, 10, 20, 2023, 1]
for loopeachnumber in numberslist: #Loop or print each number in numberslist list
    print(loopeachnumber) #print 11\n 37\n 10\n 20\n 2023\n 1
for loopeachnumber in numberslist[1:4]:
    print(loopeachnumber) #print 37\n 10\n 20\n
for forlooprangefunction in range(100, -51, -25):
    print(forlooprangefunction, end=", ") #print 100, 75, 50, 25, 0, -25, -50,
#Enumerate function assigns a number with an item in a list.  It returns a tuple of (index position of item,item) in a list.
enumeratelist = [1, 3, -7, 4, 9, -5, 4]
print(enumeratelist) #print [1, 3, -7, 4, 9, -5, 4]
print(enumerate(enumeratelist)) # print <enumerate object at 0x7fed1832a040>
print(list(enumerate(enumeratelist))) #print [(0, 1), (1, 3), (2, -7), (3, 4), (4, 9), (5, -5), (6, 4)]
for index, item in enumerate(enumeratelist):
    print("index position", index, ".  Item is", item, ".")
    '''
    index position 0 .  Item is 1 .
    index position 1 .  Item is 3 .
    index position 2 .  Item is -7 .
    index position 3 .  Item is 4 .
    index position 4 .  Item is 9 .
    index position 5 .  Item is -5 .
    index position 6 .  Item is 4 .
    '''
#Enumerate list
primitivebarchart = [19, 3, 15, 7, 11]
for index, value in enumerate(primitivebarchart):
    print(index, value, ("*" * value))
    '''
    0 19 *******************
    1 3 ***
    2 15 ***************
    3 7 *******
    4 11 ***********
    '''
#List comprehension
listcomprehensiontriples = [numbertriple * 3 for numbertriple in range(1, 7)]
print(listcomprehensiontriples) #print [3, 6, 9, 12, 15, 18]
listcomprehensiontriplesdoubledigits = [numbertriple * 3 for numbertriple in range(1, 7) if numbertriple > 3]
print(listcomprehensiontriplesdoubledigits) #print [12, 15, 18]
numbersasstringswithcommas = ", ".join([str(integervariable) for integervariable in range(1, 11)])
print(numbersasstringswithcommas) #print 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#Combine lists append lists
singlea = [1, 2, 3, 4, 5]
doubleb = [10, 11, 12, 13, 14]
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachsinglea) #print 1\n 2\n 3\n 4\n 5
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachdoubleb) #print 10\n 11\n 12\n 13\n 14
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachdoubleb, eachsinglea) #print 10 1\n 11 2\n 12 3\n 13 4\n 14 5
firstname = ["Bucky", "Tom", "Taylor"]
lastname = ["Roberts", "Hanks", "Swift"]
combinefirstnamelastname = zip(firstname, lastname)
print(combinefirstnamelastname) #print <zip object at 0x7f4ef275cac0>
for firstnameforloop, lastnameeachname in combinefirstnamelastname:
    print(firstnameforloop, end=",")
    print(lastnameeachname, end=";")
    print(firstnameforloop, lastnameeachname)
    '''
    Bucky,Roberts;Bucky Roberts
    Tom,Hanks;Tom Hanks
    Taylor,Swift;Taylor Swift
    '''
numbersa = [1, 5, 10, 79]
numbersb = [2, 3, 42, 79]
combinenumbersab = zip(numbersa, numbersb)
for eachnumbersa, eachnumbersb in combinenumbersab:
    if eachnumbersa > eachnumbersb:
        print(eachsinglea, "in numbersa is greater than", eachnumbersb)
    elif eachnumbersb > eachnumbersa:
        print(eachnumbersb, "in numbersb is greater than", eachsinglea)
    elif eachnumbersa == eachnumbersb:
        print("Numbers are equal")
    else:
        print("Error")
    '''
    2 in numbersb is greater than 5
    5 in numbersa is greater than 3
    42 in numbersb is greater than 5
    Numbers are equal
    '''
forloopdictionary = {"Tony": "cool but smells", "Emma": "sits behind me", "Lucy": "asks too many questions"}
for keyonly in sorted(forloopdictionary.keys()):
    print(keyonly, end=",") #print Emma,Lucy,Tony,
for valueonly in forloopdictionary.values():
    print(valueonly, end=";") #print cool but smells;sits behind me;asks too many questions;
for key, value in forloopdictionary.items():
    print(key + " " + value, end="/") #print Tony cool but smells/Emma sits behind me/Lucy asks too many questions/
#Loop tuples
tupleunpacking = [(1, 2), (3, 7), (9, 5)]
for eachtuple in tupleunpacking:
    print(eachtuple[0], eachtuple[1])
    '''
    1 2
    3 7
    9 5
    '''
for lefttuple, righttuple in tupleunpacking:
    print(lefttuple * righttuple) #print 2\n 21\n 45
#Dictionary comprehension and nested dictionaries
gradesstudents = {"Susan": {"Ma": 45, "En": 37, "Fr": 54}, "Peter": {"Ma": 62, "En": 58, "Fr": 59}, "George": {"Ma": 49, "En": 47, "Fr": 60}, "Mary": {"Ma": 78, "En": 83, "Fr": 62}, "New student Becky": {"Ma": 66, "En": 77, "Fr": 88}}
print(gradesstudents) #print {'Susan': {'Ma': 45, 'En': 37, 'Fr': 54}, 'Peter': {'Ma': 62, 'En': 58, 'Fr': 59}, 'George': {'Ma': 49, 'En': 47, 'Fr': 60}, 'Mary': {'Ma': 78, 'En': 83, 'Fr': 62}, 'New student Becky': {'Ma': 66, 'En': 77, 'Fr': 88}}
for key, value, in gradesstudents.items():
    print(key, value)
    '''
    Susan {'Ma': 45, 'En': 37, 'Fr': 54}
    Peter {'Ma': 62, 'En': 58, 'Fr': 59}
    George {'Ma': 49, 'En': 47, 'Fr': 60}
    Mary {'Ma': 78, 'En': 83, 'Fr': 62}
    New student Becky {'Ma': 66, 'En': 77, 'Fr': 88}
    '''
gradesstudentsnames = [names for names in gradesstudents.keys()]
print(gradesstudentsnames) #print ['Susan', 'Peter', 'George', 'Mary', 'New student Becky']
for eachgradesstudentsnames in gradesstudentsnames:
    print(eachgradesstudentsnames, gradesstudents[eachgradesstudentsnames], gradesstudents[eachgradesstudentsnames]["En"])
    '''
    Susan {'Ma': 45, 'En': 37, 'Fr': 54} 37
    Peter {'Ma': 62, 'En': 58, 'Fr': 59} 58
    George {'Ma': 49, 'En': 47, 'Fr': 60} 47
    Mary {'Ma': 78, 'En': 83, 'Fr': 62} 83
    New student Becky {'Ma': 66, 'En': 77, 'Fr': 88} 77
    '''
months = {"January": 1, "February": 2, "March": 3, "Add December": 12}
print(months) #print {'January': 1, 'February': 2, 'March': 3, 'Add December': 12}
dictionarycomprehension = {monthnumber: monthname for monthname, monthnumber in months.items()}
print(dictionarycomprehension) #print {1: 'January', 2: 'February', 3: 'March', 12: 'Add December'}
keylist = ["football", "baseball", "basketball", "hockey"]
valuelist = ["49ers", "Giants", "Warriors", "Sharks"]
print(list(zip(keylist, valuelist))) #print [('football', '49ers'), ('baseball', 'Giants'), ('basketball', 'Warriors'), ('hockey', 'Sharks')]
combinelistsdictionary = {key: value for key, value in list(zip(keylist, valuelist))}
print(combinelistsdictionary) #print {'football': '49ers', 'baseball': 'Giants', 'basketball': 'Warriors', 'hockey': 'Sharks'}


#While loop
initializewhileloop = "This sentence is true"
while initializewhileloop:
    print("While loop continues because condition is true")
    initializewhileloop = input("Stop the while loop by pressing enter.  Pressing enter the initializewhileloop is null and False which stop the while loop or exits the while loop. ")
initializeuserslist = ["Alice", "Brian", "Candace", "David", "Elaine", "Fox"]
movenamesherelist = []
while initializeuserslist:
    deletelastentry = initializeuserslist.pop()
    movenamesherelist.append(deletelastentry)
print("initializeuserslist names are now at movenamesherelist.  Use a comma to concatenate a list to a string print function", movenamesherelist) #print initializeuserslist names are now at movenamesherelist.  Use a comma to concatenate a list to a string print function ['Fox', 'Elaine', 'David', 'Candace', 'Brian', 'Alice']
pets = ["dog", "there is a cat in pets list", "dog", "goldfish", "there is a cat in pets list", "rabbit", "there is a cat in pets list"]
while "there is a cat in pets list" in pets:
    pets.remove("there is a cat in pets list")
print("The cat is removed in pets", pets) #print The cat is removed in pets ['dog', 'dog', 'goldfish', 'rabbit']
nameandhobbydictionary = {}
while True:
    name = input("What is your name? ")
    hobby = input("What is your hobby? ")
    nameandhobbydictionary[name] = hobby
    exitwhileloop = input("Do you want to exit while True loop.  While loop loops as long as loop is true.  Type Y to exit? ")
    if exitwhileloop == "Y":
        break
    else:
        continue
print(nameandhobbydictionary) #print {'Raymond': 'Exercise', 'Raymond2': 'Read books', 'Raymond3': 'Board games'}
import random
counter = 0
abunchofnumbers = []
while counter < 20:
    append20numbers = random.randint(1, 21)
    abunchofnumbers.append(append20numbers)
    counter += 1
print(abunchofnumbers) #print [6, 17, 12, 7, 18, 12, 3, 17, 13, 6, 11, 6, 19, 19, 5, 20, 21, 16, 19, 6]
whileloopkeepgoingvariable = "yes"
while whileloopkeepgoingvariable == "yes":
    print(whileloopkeepgoingvariable)
    print("The while loop continues to loop because the while loop variable whileloopkeepgoingvariable is true.")
    randomnumber = random.randint(1, 20)
    print(randomnumber)
    if randomnumber == 20:
        print("Exit the while loop because the variable whileloopkeepgoingvariable is not equal to yes.")
        whileloopkeepgoingvariable = "No.  Exit the while loop"
    else:
        whileloopkeepgoingvariable = "yes"
    '''
    yes
    The while loop continues to loop because the while loop variable whileloopkeepgoingvariable is true.
    15
    yes
    The while loop continues to loop because the while loop variable whileloopkeepgoingvariable is true.
    11
    yes
    The while loop continues to loop because the while loop variable whileloopkeepgoingvariable is true.
    20
    Exit the while loop because the variable whileloopkeepgoingvariable is not equal to yes.
    '''
stopnumber = ""
while stopnumber != 43:
    print("Inside the while loop.")
    stopnumber = int(input("Type the stop number 43 to exit or to stop the loop.  "))
    '''
    Inside the while loop.
    Type the stop number 43 to exit or to stop the loop.  987
    Inside the while loop.
    Type the stop number 43 to exit or to stop the loop.  24813
    Inside the while loop.
    Type the stop number 43 to exit or to stop the loop.  -4
    Inside the while loop.
    Type the stop number 43 to exit or to stop the loop.  43
    '''
guessnumber = 24
userguess = int(input("I am thinking of a number between 1 and 50.  Guess the number? "))
while True:
    if userguess == guessnumber:
        print("Correct, you win.  Exit while loop.")
        break
    elif userguess > guessnumber:
        userguess = int(input("Too high.  I'm thinking of a number between 1 and 50.  Guess again. "))
    elif userguess < guessnumber:
        userguess = int(input("Too low.  I'm thinking of a number between 1 and 50.  Guess again. "))
    '''
    I am thinking of a number between 1 and 50.  Guess the number? 5
    Too low.  I'm thinking of a number between 1 and 50.  Guess again. 25
    Too high.  I'm thinking of a number between 1 and 50.  Guess again. 16
    Too low.  I'm thinking of a number between 1 and 50.  Guess again. 33
    Too high.  I'm thinking of a number between 1 and 50.  Guess again. 24
    Correct, you win.  Exit while loop.
    '''
while True:
    name = input("Who are you?  Enter Joe to proceed; otherwise, while loop goes back to the top of while loop.  There is no initialization. ")
    if name != "Joe":
        continue
    password = input("What is the password?  It's a fish ")
    if password == "swordfish":
        print("Exiting while loop.  Break")
        break
    '''
    Who are you?  Enter Joe to proceed; otherwise, while loop goes back to the top of while loop.  There is no initialization. Buck
    Who are you?  Enter Joe to proceed; otherwise, while loop goes back to the top of while loop.  There is no initialization. Joe
    What is the password?  It's a fish Goldfish
    Who are you?  Enter Joe to proceed; otherwise, while loop goes back to the top of while loop.  There is no initialization. Joe
    What is the password?  It's a fish karp
    Who are you?  Enter Joe to proceed; otherwise, while loop goes back to the top of while loop.  There is no initialization. Joe
    What is the password?  It's a fish swordfish
    Exiting while loop.  Break
    '''

secretword = "giraffe"
guess = ""
guesscount = 0
guesslimit = 3
outofguesses = False
print(guess != secretword) #print True
print(outofguesses is False) #print True.  RM:  It's counterintuitive  outofguesses is really False which is True.
print(guess != secretword and outofguesses is False) #print True
print(guesscount, guess != secretword, outofguesses is False) #print 0 True True
print(True and False) #print False
print(False and False) #print False
while guess != secretword and outofguesses is False:
    if guesscount < guesslimit:
        print(f"Cheat.  The secret word is {secretword}")
        guess = input("Guess the secret word: ")
        guesscount += 1
        print(guesscount, guess != secretword, outofguesses)
    else:
        print("You're out of guesses.  outofguesses variable is True.  Exit while loop.")
        outofguesses = True
    '''
    Cheat.  The secret word is giraffe
    Guess the secret word: 34
    1 True False
    Cheat.  The secret word is giraffe
    Guess the secret word: opop
    2 True False
    Cheat.  The secret word is giraffe
    Guess the secret word: giraffe
    3 False False
    '''
whileloopelse = "The while loop else statement is optional"
whileloopcondition = 0
while whileloopcondition < 5:
    print("While loop body.  The whileloopcondition is a Boolean expression True or False", whileloopcondition)
    whileloopcondition += 1
else:
    print("Break while loop or exit while loop.  Some programmers omit the else because the else statement is optional.", whileloopcondition)
'''
While loop body.  The whileloopcondition is a Boolean expression True or False 0
While loop body.  The whileloopcondition is a Boolean expression True or False 1
While loop body.  The whileloopcondition is a Boolean expression True or False 2
While loop body.  The whileloopcondition is a Boolean expression True or False 3
While loop body.  The whileloopcondition is a Boolean expression True or False 4
Break while loop or exit while loop.  Some programmers omit the else because the else statement is optional. 5
'''
