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
