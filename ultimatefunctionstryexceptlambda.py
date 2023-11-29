#Functions
def functionobjectname(inputvariable):
    return "The function object named functionobjectname returns {} from the inputvariable variable".format(inputvariable)


print(functionobjectname("Python calls or invokes the functionobjectname function giving it input")) #print The function object named functionobjectname returns Python calls or invokes the functionobjectname function giving it input from the inputvariable variable

def firstlineinfunction(functioninput):
    "This is the docstring.  If the first line of the function is a string, then the string is seen as the documentation for the function.  Technically, the docstring is stored in the function's __doc__attribute."
    return "The string value inputted when calling firstlineinfunction function is {}".format(functioninput)


print(firstlineinfunction("Give To Function firstlineinfunction")) #print The string value inputted when calling firstlineinfunction function is Give To Function firstlineinfunction
help(firstlineinfunction)
'''
Help on function firstlineinfunction in module __main__:

firstlineinfunction(functioninput)
    This is the docstring.  If the first line of the function is a string, then the string is seen as the documentation for the function.  Technically, the docstring is stored in the function's __doc__attribute.
(END)
'''

def printreturn():
    print("The print statement in a function")
    return "The return statement in a function"


printreturn() #return The print statement in a function
print(printreturn())
'''
The print statement in a function
The return statement in a function
'''

def multiplelinesinfunction(insertvalue):
    """
    Triple double quotes better docstring.
    Write multiple lines.
    Docstring tells user what the function does, how to run the function, and what it returns.
    """
    return "The string value inputted when calling multiplelinesinfunction function is {}".format(insertvalue)


print(multiplelinesinfunction("Print the docstring type the syntax help(multiplelinesinfunction)")) #print The string value inputted when calling multiplelinesinfunction function is Print the docstring type the syntax help(multiplelinesinfunction)
help(multiplelinesinfunction)
'''
Help on function multiplelinesinfunction in module __main__:

multiplelinesinfunction(insertvalue)
    Triple double quotes better docstring.
    Write multiple lines.
    Docstring tells user what the function does, how to run the function, and what it returns.
'''

def multiplefunctioninputs(variable1, variable2):
    return "I make a rhyme " + variable1 + " and " + variable2 + "."


print(multiplefunctioninputs("blue", "clue")) #print I make a rhyme blue and clue.

def defaultfunctionvariable(dynamicvariable, defaultvariable=17):
    return (dynamicvariable + defaultvariable)


print(defaultfunctionvariable(5)) #print 22
print(defaultfunctionvariable(5, 20)) #print 25
print(defaultfunctionvariable(defaultvariable=4, dynamicvariable=50)) #print 54

def multipledefaultfunctionvariables(name="Raymond", action="jump", braincells=500000000, item="glue"):
    print(name + " " + action + " " + item, braincells, "using print() function to return the result.")


multipledefaultfunctionvariables(action="run") #return Raymond run glue 500000000 using print() function to return the result.
multipledefaultfunctionvariables(action="sleep", braincells=100000000) #return Raymond sleep glue 100000000 using print() function to return the result.

def optionalfunctionarguments(hobby, show, optionalargument=""):
    return "%s hobby, %s show, optionalargument is blank using doublequotes %s" % (hobby, show, optionalargument)


print(optionalfunctionarguments("hobbycook", "show Breaking Bad", "New Mexico")) #print hobbycook hobby, show Breaking Bad show, optionalargument is blank using doublequotes New Mexico
print(optionalfunctionarguments(show="showargument", hobby="hobbyargument")) #print hobbyargument hobby, showargument show, optionalargument is blank using doublequotes

def multiplevaluesonelistargument(manynumberslist):
    firstnumberonly, *middlenumbers, lastnumberonly = manynumberslist
    print(firstnumberonly)
    print(lastnumberonly)
    print(middlenumbers)


multiplevaluesonelistargument([65, 76, 98, 54, 21]) #return 65\n 21\n [76, 98, 54]

def multiplevaluesstringoneargument(*manystrings):
    return "".join(manystrings)


print(multiplevaluesstringoneargument("Ed", "Al", "Winry", "Riza", "Roy", "Mei Chang")) #print EdAlWinryRizaRoyMei Chang
print(multiplevaluesstringoneargument(str(5), str(99), str(-42))) #print 599-42

def multiplevalues(anynumber, *words):
    print(anynumber)
    print(words)


multiplevalues(5, "yum", "boo", "black") #print 5\n ('yum', 'boo', 'black')

def useanotherfunction(theotherfunctionname, *arguments):
    return theotherfunctionname(*arguments)


print(useanotherfunction(multiplevaluesstringoneargument, "red", "green", "blue", "yellow")) #print redgreenblueyellow
print(useanotherfunction(optionalfunctionarguments, "flowers", "Three's Company", "1980s")) #print flowers hobby, Three's Company show, optionalargument is blank using doublequotes 1980s

def nestedfunction(inputnumbers):
    sumnumbers = sum(inputnumbers)
    averagenumbers = (sumnumbers / len(inputnumbers))
    return averagenumbers
def functionnumbersinput():
    return [1, 35, 61, 92]


print(nestedfunction(functionnumbersinput())) #print 47.25

def printresultandreturnresult(*numbers, weather="sunny"):
    total = 0
    print(weather) #RM:  No need for the asterik
    print(numbers) #RM:  No need for the asterik
    for eachnumbers in numbers: #RM:  No need for the asterik in numbers
        total += eachnumbers
    return total, weather


print(printresultandreturnresult(3, 32, 55, weather="rainy")) #print rainy\n (3, 32, 55)\n (90, 'rainy')

def printresultandreturnresult2(weather2="foggy", *numbers2):
    total2 = 0
    print(weather2)
    print(numbers2)
    print(type(numbers2))
    for eachnumbers2 in numbers2:
        total2 += eachnumbers2
    return weather2 and total2


print(printresultandreturnresult2) #print <function printresultandreturnresult2 at 0x7f77f3c76c10>
print(printresultandreturnresult2())
'''
foggy
()
<class 'tuple'>
0
'''
print(printresultandreturnresult2("Snow", 90, 210))
'''
(90, 210)
<class 'tuple'>
300
'''

def callmyownfunction(guessnumber):
    print(guessnumber)
    if guessnumber == 5:
        print("You Won.  Don't call the callmyownfunction()")
    else:
        anotherguessnumber = int(input("Enter a number between one and ten "))
        callmyownfunction(anotherguessnumber)


firstinput = 7
callmyownfunction(firstinput)
'''
7
Enter a number between one and ten 3
3
Enter a number between one and ten 2
2
Enter a number between one and ten 8
8
Enter a number between one and ten 5
5
You Won.  Don't call the callmyownfunction()
'''

#double asterisks before the parameter **userinfo cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.  Function works no matter how many additional key-value pairs are provided in the function call.
def buildprofile(first, last, **userinfo):
    profile = {}
    profile["firstname"] = first
    profile["lastname"] = last
    for key, value in userinfo.items():
        profile[key] = value
    return profile


print(buildprofile("albert", "einstein", location="princeton", field="physics")) #print {'location': 'princeton', 'field': 'physics', 'lastname': 'einstein', 'firstname': 'albert'}
print(buildprofile("Jackie", "Chan", hobbies="books, karate, chow mein", favorite_color="red", car="audi")) #print {'lastname': 'Chan', 'firstname': 'Jackie', 'hobbies': 'books, karate, chow mein', 'car': 'audi', 'favorite_color': 'red'}
#parent and child functions

numberlist1match = [1, 4, 6, 3]
numberlist2match = [1, 57, 3]
numberlist2unmatch = [1, 57, 9]
def differencereturnand(list1, list2):
    firstnumbermatch = list1[0] == list2[0]
    lastnumbermatch = list1[-1] == list2[-1]
    return firstnumbermatch and lastnumbermatch
def differencereturncomma(list1, list2):
    firstnumbermatch = list1[0] == list2[0]
    lastnumbermatch = list1[-1] == list2[-1]
    return firstnumbermatch, lastnumbermatch


print(differencereturnand(numberlist1match, numberlist2match)) #print True
print(differencereturnand(numberlist1match, numberlist2unmatch)) #print False
print(differencereturncomma(numberlist1match, numberlist2match), "is a tuple.") #print (True, True)  is a tuple.
print(differencereturncomma(numberlist1match, numberlist2unmatch), "is a tuple.") #print (True, False)  is a tuple.

def definedatatypes(anynumber, integervariable: int, defaultintegervariable: int=40): #RM:  SyntaxError: non-default argument follows default argument
    print(integervariable)
    print(type(integervariable))
    print(defaultintegervariable)
    print(type(defaultintegervariable))
    print(anynumber)
    print(type(anynumber))


definedatatypes(integervariable=178, anynumber=500)
'''
178
<class 'int'>
40
<class 'int'>
500
<class 'int'>
'''

def savefunctionresults(number1: int, number2: int, number3: int, astring: str):
    number1answer = number1 + 100
    number2answer = number2 * 200
    number3answer = number3 / 300
    astring = "Change astring input to bread"
    return (number1answer, number2answer, number3answer, astring) #RM:  return number1answer, number2answer, number3answer, astring with the parenthesis is the same results


input1, input2, input3, input4 = 400, 1200, 3000, "Tie Die"
print(savefunctionresults(input1, input2, input3, input4)) #print (500, 240000, 10.0, 'Change astring input to bread')
savefunctionresultsvariable = savefunctionresults(input1, input2, input3, input4)
print(savefunctionresultsvariable) #print (500, 240000, 10.0, 'Change astring input to bread')

#Global variables, local variables
globalvariable = "The variable is global.  Use the global variable anywhere."
def localvariable():
    global globalvariable
    print("localvariable() function.  Print the global variable: " + globalvariable)


print(globalvariable) #print The variable is global.  Use the global variable anywhere.
localvariable() #return localvariable() function.  Print the global variable: The variable is global.  Use the global variable anywhere.
if "globalvariable" in globals():
    print("The if checks globalvariable is a global variable.") #print The if checks globalvariable is a global variable.

def returnlocalvariable():
    localvariable = 200
    return "returnlocalvariable() function is " + str(localvariable) #RM:  "returnlocalvariable() function is", localvariable returns tuple ('returnlocalvariable() function is', 200)


print(returnlocalvariable()) #print returnlocalvariable() function is 200

globalvariablelargestnumber = 0
def inefficientreturnglobalvariable(numberlist):
    largestnumber = 0
    for eachnumberlist in numberlist:
        if eachnumberlist > largestnumber:
            largestnumber = eachnumberlist
    return largestnumber


globalvariablelargestnumber = inefficientreturnglobalvariable([45, 3, 67, 357, 33])
print(globalvariablelargestnumber) #print 357

globalvariablelargestnumber = 0
def efficientreturnglobarvariable(numberlist):
    global globalvariablelargestnumber
    largestnumber = 0
    for eachnumberlist in numberlist:
        if eachnumberlist > largestnumber:
            largestnumber = eachnumberlist
    globalvariablelargestnumber = largestnumber
    print(globalvariablelargestnumber)


efficientreturnglobarvariable([45, 3, 67, 357, 33]) #return 357

#List map filter function.  Function iterators.
def listmapfunction(dollars):
    return dollars * 2


doubleincome = [10, 30, 75]
print(listmapfunction(doubleincome)) #print [10, 30, 75, 10, 30, 75]
print(map(listmapfunction, doubleincome)) #print <map object at 0x7fd85db69b20>
print(list(map(listmapfunction, doubleincome))) #print [20, 60, 150

def greaterthantenfilterlist(numberlist):
    return numberlist > 10


thenumberlist = [5, 7, 345, 78, 34, 5]
print(filter(greaterthantenfilterlist, thenumberlist)) #print <filter object at 0x7f781b675ca0>
print(list(filter(greaterthantenfilterlist, thenumberlist))) #print [345, 78, 34]
print(list(map(greaterthantenfilterlist, thenumberlist))) #print [False, False, True, True, True, False]

def beginswithletterfilterlist(wordlist, prefix="e"):
    return wordlist.startswith(prefix)


thewordlist = ["earth", "unicycle", "moose", "beed", "eradicate"]
#print(filter(beginswithletterfilterlist, thewordlist,"e")) #error message filter expected 2 arguments
print(filter(beginswithletterfilterlist, thewordlist)) #print <filter object at 0x7f7ca0627828>
print(list(filter(beginswithletterfilterlist, thewordlist))) #print ['earth', 'eradicate']

def squarednumbers(numbers):
    return numbers**2


numbers = [1, 2, 3, 4, 5]
#print(squarednumbers(numbers)) #TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
print(map(squarednumbers, numbers)) #print <map object at 0x7f9c2fa9c9d0>
print(list(map(squarednumbers, numbers))) #print [1, 4, 9, 16, 25]
def uppercaseletters(string):
    return string.upper()


letters = ["abc", "def", "ghi"]
print(list(map(uppercaseletters, letters))) #print ['ABC', 'DEF', 'GHI']

def greaterthanthreenumbers(numberslist):
    return numberslist > 3


numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(greaterthanthreenumbers, numbers))) #print [4, 5, 6]
print(list(map(greaterthanthreenumbers, numbers))) #print [False, False, False, True, True, True]

from random import shuffle
def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return "".join(anagram)


words = ["beetroot", "carrots", "potatoes"]
print(map(jumble, words)) #print <map object at 0x7fbc09ee02e8>
print(list(map(jumble, words))) #print ['etetboro', 'scrrtoa', 'oaptsoet']

#List comprehension functions
#RM:  using jumble function above
words = ["beetroot", "carrots", "potatoes"]
functioninsidelistcomprehension = [jumble(eachwords) for eachwords in words]
print(functioninsidelistcomprehension) #print ['robteeto', 'aotrscr', 'pstoeota']

#Parent child functions
def functionone(n):
    return n + 1
def functiontwo(n):
    return functionone(n) + 2


print(functionone(10)) #print 11
print(functiontwo(10)) #print 13.  functiontwo receives 10.  functiontwo returns functionone 10+1 which is 11.  functiontwo 11+2 which is 13.

def giverfunction(initialist):
    print(initialist)
    finalist = sorted(initialist)
    return finalist
def receiverfunction(updatelist):
    print("I have the giverfunction initiallist updated", updatelist)


childlist = ["zebra", "apple", "honey", "comb", "stick", "ball"]
print(giverfunction(childlist))
'''
['zebra', 'apple', 'honey', 'comb', 'stick', 'ball']
['apple', 'ball', 'comb', 'honey', 'stick', 'zebra']
'''
receiverfunction(childlist) #print I have the giverfunction initiallist updated ['zebra', 'apple', 'honey', 'comb', 'stick', 'ball']
receiverfunction(giverfunction(childlist))
'''
['zebra', 'apple', 'honey', 'comb', 'stick', 'ball']
I have the giverfunction initiallist updated ['apple', 'ball', 'comb', 'honey', 'stick', 'zebra']
'''

def firstfunctionparent():
    def secondfunctionchild():
        return "secondfunctionchild() as a string"


firstfunctionparent() #print *blank*
print(firstfunctionparent()) #print None

def firstfunctionparent():
    def secondfunctionchild():
        return "secondfunctionchild() as a string"
    return "firstfunctionparent() as a string"


firstfunctionparent() #print *blank*
print(firstfunctionparent()) #print firstfunctionparent() as a string
print(type(firstfunctionparent())) #print <class 'str'>
# secondfunctionchild() #NameError: name 'secondfunctionchild' is not defined

def firstfunctionparent():
    print("Create a new function object assigned to variable secondfunction.  secondfunction is a local variable local to firstfunction.  firstfunction returns the secondfunctionchild function and not a string 'firstfunctionparent() as a string'.")

    def secondfunctionchild():
        print("Inside the secondfunctionchild() did I print?")
        return "secondfunctionchild() as a string"
    return secondfunctionchild


firstfunctionparent() #print Create a new function object assigned to variable secondfunction.  secondfunction is a local variable local to firstfunction.  firstfunction returns the secondfunctionchild function and not a string 'firstfunctionparent() as a string'.
print(firstfunctionparent())
'''
Create a new function object assigned to variable secondfunction.  secondfunction is a local variable local to firstfunction.  firstfunction returns the secondfunctionchild function and not a string 'firstfunctionparent() as a string'.
<function firstfunctionparent.<locals>.secondfunctionchild at 0x7f3bc99a3160>
'''
print(type(firstfunctionparent()))
'''
Create a new function object assigned to variable secondfunction.  secondfunction is a local variable local to firstfunction.  firstfunction returns the secondfunctionchild function and not a string 'firstfunctionparent() as a string'.
<class 'function'>
'''
#secondfunctionchild() #NameError: name 'secondfunctionchild' is not defined
accesssecondfunctionchildvariable = firstfunctionparent()
print(accesssecondfunctionchildvariable())
'''
Create a new function object assigned to variable secondfunction.  secondfunction is a local variable local to firstfunction.  firstfunction returns the secondfunctionchild function and not a string 'firstfunctionparent() as a string'.
Inside the secondfunctionchild() did I print?
secondfunctionchild() as a string
'''

def firstfunctionparent():
    def secondfunctionchild(a, b):
        return a + b
    return secondfunctionchild


accesssecondfunctionchildvariable = firstfunctionparent()
print(accesssecondfunctionchildvariable(4, 5)) #print 9

def firstfunctionparent():
    def secondfunctionchild(a, b):
        def thirdfunctionchild(n):
            return n * 2
        return thirdfunctionchild(a) + thirdfunctionchild(b)
    return secondfunctionchild


accesssecondfunctionchildvariable = firstfunctionparent()
print(accesssecondfunctionchildvariable(4, 5)) #print 18

def firstfunctionparent(number):
    print("firstfunctionparent", number)

    def secondfunctionchild():
        print("secondfunctionparent", number)
        return f"secondfunctionchild() function number {number}"
    return secondfunctionchild


firstfunctionparent(111) #return firstfunctionparent 111
print(firstfunctionparent(222))
'''
firstfunctionparent 222
<function firstfunctionparent.<locals>.secondfunctionchild at 0x7f25424c70d0>
'''
accesssecondfunctionchildvariable = firstfunctionparent(333) #returns firstfunctionparent 333.  RM:  I can't explain a variable assignment returns a result.  Is it the print(number) in firstfunctionparent?  Yes.
print(accesssecondfunctionchildvariable) #print <function firstfunctionparent.<locals>.secondfunctionchild at 0x7f2b93f780d0>
print(accesssecondfunctionchildvariable())
'''
secondfunctionparent 333
secondfunctionchild() function number 333
'''

def firstfunctionparent(name):
    remainingpoints = 5

    def secondfunctionchild():
        nonlocal remainingpoints #local variable from firstfunctionparent function declared in secondfunctionchild function
        while True:
            print(remainingpoints)
            if remainingpoints <= 0:
                return "Game over"
            else:
                remainingpoints -= 1
                print(f"Hello {name}")
    return secondfunctionchild


accesssecondfunctionchildvariable = firstfunctionparent("Raymond")
print(accesssecondfunctionchildvariable())
'''
5
Hello Raymond
4
Hello Raymond
3
Hello Raymond
2
Hello Raymond
1
Hello Raymond
0
Game over
'''

#Embed functions calls or multiple calls function multiple functions
def functiononeaddten(number):
    return number + 10
def functiontwodouble(number):
    return number * 2
def functionthreetriple(number):
    return number * 3


variablenumber = 3
print(functiononeaddten(variablenumber)) #print 13
print(functiontwodouble(variablenumber)) #print 6
print(functionthreetriple(variablenumber)) #print 9
print(functiononeaddten(functiontwodouble(functionthreetriple(variablenumber)))) #print 28.  ((3*3)*2)+10

#Call functions from another file.  Also call classes from another file.
from functionsfile import formattedname  #RM:  functionsfile is functionsfile.py file in the same directory
firstname = lowercaseraymond
lastname = uppercasemar
outputformattedname = formattedname(firstname, lastname)
print("{} is your name formatted.".format(outputformattedname)) #print Raymond Mar is your name formatted.

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
# survey.showresponse() #return The list ['HTML', 'Python', 'SQL', 'CSS', 'JavaScript', 'DAX']\n Your languages are HTML, Python, SQL, CSS, JavaScript, DAX\n HTML, Python, SQL, CSS, JavaScript, DAX

#Stack frames, keep local variables
def doineedtokeeplocalvariables(x, y):
    z = x + y
    return z


print(doineedtokeeplocalvariables(10, 11)) #print 21

import inspect
def keeplocalvariables(x, y):
    z = x + y
    print(f"x+y={z}")


print(keeplocalvariables(10, 11))
'''
x+y=21
None
'''
variabletokeeplocalvariable = keeplocalvariables(110, 111)
print(variabletokeeplocalvariable)
'''
x+y=221
None
'''

def keeplocalvariableswithinspect(x, y):
    z = x + y
    print(f"x+y={z}")
    return z, inspect.currentframe()


print(keeplocalvariableswithinspect(10, 11))
'''
x+y=21
(21, <frame at 0x7f4c609a6440, file 'yytest.py', line 255, code keeplocalvariableswithinspect>)
'''
variabletokeeplocalvariable = keeplocalvariableswithinspect(110, 111)
print(variabletokeeplocalvariable)
'''
x+y=221
(221, <frame at 0x7f4c609a6440, file 'yytest.py', line 255, code keeplocalvariableswithinspect>)
'''
print(variabletokeeplocalvariable[0]) #print 221
