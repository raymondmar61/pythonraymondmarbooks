#Strings
xstringescapecharacter = "Escape character backward slash\\ tab\t double quotes escape\" sentence."
print(xstringescapecharacter) #print Escape character backward slash\ tab   double quotes escape" sentence.
print(r"Begin the raw string in the print function with the letter r to return as-is.") #print Begin the raw string in the print function with the letter r to return as-is.
rawstring = r"D:/innovateinfinitely/blog/202306blog.html"
print(rawstring) #print D:/innovateinfinitely/blog/202306blog.html
concatenateplussign = "Hello " + "World"
print(concatenateplussign) #print Hello World
print("Print five times " * 5) #print Print five times Print five times Print five times Print five times Print five times
multiplelinestring = """Use triple quotes for multiple lines or
multi-line strings or multi line strings.
The last line ends with triple quotes.  Otherwise, Python
inserts a line break below."""
print(multiplelinestring)
'''
Use triple quotes for multiple lines or
multi-line strings or multi line strings.
The last line ends with triple quotes.  Otherwise, Python
inserts a line break below.
'''
print("override print function no newline\n", end="") #print override print function no newline use end parameter of "" end="" for the print function to not append the newline
lengthofastring = "Find the number of characters in a string."
print(len(lengthofastring)) #print 42
stringsplitindexing = "Use brackets to split a string beginning with the number zero and end with minus one."
print(stringsplitindexing) #print Use brackets to split a string beginning with the number zero.
print(stringsplitindexing[0]) #print U
print(stringsplitindexing[1:4]) #print se*space*
print(stringsplitindexing[1:9:2]) #print s rc
print(stringsplitindexing[-1]) #print .
print(stringsplitindexing[-2]) #print e
print(stringsplitindexing[1:]) #print se brackets to split a string beginning with the number zero and end with minus one.
print(stringsplitindexing[:-1]) #print Use brackets to split a string beginning with the number zero and end with minus one
print(stringsplitindexing[-10:-2]) #print minus on
print(stringsplitindexing[-2:-10:-1]) #print eno suni.  RM:  print(stringsplitindexing[-2:-10]) returns null
print(stringsplitindexing[-1::-1]) #print .eno sunim htiw dne dna orez rebmun eht htiw gninnigeb gnirts a tilps ot stekcarb esU
print(stringsplitindexing[::-1]) #print .eno sunim htiw dne dna orez rebmun eht htiw gninnigeb gnirts a tilps ot stekcarb esU
print(stringsplitindexing.index("Use")) #print 0.  Find the index position of a string
print(stringsplitindexing.index("s")) #print 1.  Find the index position of a string
print(stringsplitindexing.index("zero")) #print 57.  Find the index position of a string
print(stringsplitindexing.rindex("with")) #print 70.  Return the index position for the first occurrence starting from the end of the string.  The count, however, starts from the beginning.  70 is the index position 70 starting with 0 at the start of the string.
stripastring = "Goodbye\n"
print(stripastring[:-1]) #print Goodbye
cleanstring = "     5beforeremovespaces3after   "
print(cleanstring) #print *****5beforeremovespaces3after***
print(cleanstring.rstrip()) #print *****5beforeremovespaces3after
print(cleanstring.lstrip()) #print 5beforeremovespaces3after***
print(cleanstring.strip()) #print 5beforeremovespaces3after
specifycharactersremove = "www.python.org"
print(specifycharactersremove.strip("w")) #print .python.org
print(specifycharactersremove.strip("org")) #print www.python.
print(specifycharactersremove.strip("worg")) #print .python.
print(specifycharactersremove.strip("gorw")) #print .python. #Strip removes any and all characters no matter the order.  RM:  it doesn't work all the time.
print(specifycharactersremove.strip("gorwt")) #print .python.
print(specifycharactersremove.strip("gorwt.")) #print python
print(specifycharactersremove.strip("gorth")) #print www.python.
print(specifycharactersremove.strip("gorth.")) #print www.python
changecase = "The SENTENCE convert Upper Case lower case Casing"
print(changecase) #print The SENTENCE convert Upper Case lower case Casing
print(changecase.lower()) #print the sentence convert upper case lower case casing
print(changecase.upper()) #print THE SENTENCE CONVERT UPPER CASE LOWER CASE CASING
print(changecase.title()) #print The Sentence Convert Upper Case Lower Case Casing
print(changecase.capitalize()) #print The sentence convert upper case lower case casing
print(changecase.swapcase()) #print tHE sentence CONVERT uPPER cASE LOWER CASE cASING
checkcase = "Methods Check A String'S Case."
print(checkcase.isupper()) #print False
print(checkcase.islower()) #print False
print(checkcase.istitle()) #print True.  'S is capitalized for title!?!
print(checkcase.isalpha()) #print False.  isalpha() method can't have spaces.  Alphabetic characters only.
print(checkcase[0:7].isalpha()) #print True.  isalpha() method can't have spaces.  Alphabetic characters only.
print(checkcase[0:7].isalnum()) #print True.  isalnum() method can't have spaces.  isalnum searches for alpha numeric or alphanumeric or alpha-numeric.
print(checkcase.isspace()) #print False
checkspaces = " 4 cke x  sioj "
print(checkspaces.isspace()) #print False.  White spaces or spaces only.
alldecimals0to9base10 = "123789"
print(alldecimals0to9base10.isdecimal()) #print True.  Python isdecimal() function returns a Boolean value TRUE if the input string contains all decimal characters
print(alldecimals0to9base10.isdigit()) #print True.  No positive signs or negative signs.
print(alldecimals0to9base10.isnumeric()) #print True.  isnumeric is a numeric value without a positive sign or negative sign and no decimals.
splitstring = "Separate string by letters or spaces"
print(splitstring) #print Separate string by letters or spaces
print(splitstring.split()) #print ['Separate', 'string', 'by', 'letters', 'or', 'spaces']
print(splitstring.split(" ")) #print ['Separate', 'string', 'by', 'letters', 'or', 'spaces']
print(splitstring.split("\n")) #print ['Separate string by letters or spaces']
print(splitstring.split("r")) #print ['Sepa', 'ate st', 'ing by lette', 's o', ' spaces']
print(splitstring.split("r", 3)) #print ['Sepa', 'ate st', 'ing by lette', 's o', ' spaces'].  Split by the letter r three times.
howmanysplits = "a b c d"
print(howmanysplits) #print a b c d
print(howmanysplits.split()) #print ['a', 'b', 'c', 'd']
print(howmanysplits.split(" ", 1)) #print ['a', 'b c d']
print(howmanysplits.split(" ", 2)) #print ['a', 'b', 'c d']
print(howmanysplits.split(" ", 9)) #print ['a', 'b', 'c', 'd']
#A first argument is required when specifying the number of splits in the second argument.  To split on whitespace runs using the second argument, type None as the first argument.
print(howmanysplits.split(None, 1)) #print ['a', 'b c d']
print(howmanysplits.split(None, 2)) #print ['a', 'b', 'c d']
print(howmanysplits.split(None, 9)) #print ['a', 'b', 'c', 'd']
#pretendinputcolors = str(input("Enter a list of colors separated by a space "))
pretendinputcolors = "black white red"
print(pretendinputcolors) #print black white red
splitpretendinputcolors = pretendinputcolors.split()
print(splitpretendinputcolors) #print ['black', 'white', 'red']
splitbyspecificcharacter = "Separate by string character:  89, 97, 92"
print(splitbyspecificcharacter) #print Separate by string character:  89, 97, 92
splitcharactercolondoublespace = splitbyspecificcharacter.partition(":  ")
print(splitcharactercolondoublespace) #print ('Separate by string character', ':  ', '89, 97, 92')
print(list(splitcharactercolondoublespace)) #print ['Separate by string character', ':  ', '89, 97, 92']
#rpartition split search for the one separator from the end of the string
multiplesplitbyspecificcharacter = "D:/innovateinfinitely/blog/202306blog.html"
mainurl, rightmostforwardslash, htmlfile = multiplesplitbyspecificcharacter.rpartition("/")
print(mainurl) #print D:/innovateinfinitely/blog
print(rightmostforwardslash) #print /
print(htmlfile) #print 202306blog.html
doublesplitbyspecificcharacter = "Separate by string character:  89, 97, 92 :  45, 56, 78"
print(doublesplitbyspecificcharacter) #print Separate by string character:  89, 97, 92 :  45, 56, 78
doublesplitcharactercolondoublespace = doublesplitbyspecificcharacter.partition(":  ")
print(doublesplitcharactercolondoublespace) #print ('Separate by string character', ':  ', '89, 97, 92 :  45, 56, 78').  RM:  Single split at the first colon from the left.
print(list(doublesplitcharactercolondoublespace)) #print ['Separate by string character', ':  ', '89, 97, 92 :  45, 56, 78']
print(len(list(doublesplitcharactercolondoublespace))) #print 3
#splitlines reteurns a list of new strings representing the lines of text split at each newline
threelines = """This is line 1
    This is line 2
        This is line 3"""
print(threelines)
'''
This is line 1
    This is line 2
        This is line 3
'''
splitlineswithformatting = threelines.splitlines()
print(splitlineswithformatting) #print ['This is line 1', '    This is line 2', '        This is line 3']
splitlineswithformattingnewline = threelines.splitlines(True)
print(splitlineswithformattingnewline) #print ['This is line 1\n', '    This is line 2\n', '        This is line 3']
joinsplitinputcolors = ", ".join(splitpretendinputcolors)
print(joinsplitinputcolors) #print black, white, red
print(" ".join(splitpretendinputcolors)) #print black white red
print("\t".join(splitpretendinputcolors)) #print black  white   red
print("::".join(splitpretendinputcolors)) #print black::white::red
findstring = "Search string replace string"
print(findstring) #print Search string replace string
print(findstring.find("string")) #print 7.  Seven is the starting index number
print(findstring.find("string", 13)) #print 22.  22 is the starting index number.  13 is the index number to begin the find.
print(findstring.replace("Search", "Find")) #print Find string replace string
print(findstring.startswith("Search")) #print True
print(findstring.startswith("search")) #print False
print(findstring.startswith("string")) #print False
print(findstring.endswith("ing")) #print True
print(findstring.endswith("string")) #print True
searchinstring = "Mississippi"
print(searchinstring.find("zz")) #print -1
print(searchinstring.find("ss", 3)) #print 5.  Begin search at the third index position
print(searchinstring.find("ss", 1, 4)) #print 2.  Begin search at the first index position and end at the fourth index position
print(searchinstring.rfind("ss")) #print 5.  Start the search at the end of the string which returns the position of the first character of the last occurrence with respect to the start of the string.  There is no lfind method.
print(searchinstring.startswith(("mis", "Mss", "Misss", "Mrs", "checks all strings contained in tuple"))) #print False
print(searchinstring.endswith(("i", "u", "check all strings in tuple"))) #print True.  If the parameter with startswith or endswith is a tuple of strings, both methods check for all the strings in the tuple which returns True if any of them is found.
sortstring = "Sorting a string convert to a list by splitting and sort the list it is a nice day today"
print(sortstring) #print Sorting a string convert to a list by splitting and sort the list it is a nice day today
sortstringassplitlist = sortstring.split()
print(sortstringassplitlist.sort()) #print None
sortstringassplitlist.sort()
print(sortstringassplitlist) #print ['Sorting', 'a', 'a', 'a', 'and', 'by', 'convert', 'day', 'is', 'it', 'list', 'list', 'nice', 'sort', 'splitting', 'string', 'the', 'to', 'today']
sortlistofstrings = "It is a nice day today, isn't it?".split()
print(sortlistofstrings) #print ['It', 'is', 'a', 'nice', 'day', 'today,', "isn't", 'it?']
splitmethod = "Mississippi split by ss"
print(splitmethod.split("ss")) #print ['Mi', 'i', 'ippi split by ', '']
howmanysplits = "a b c d"
print(howmanysplits) #print a b c d
print(howmanysplits.split()) #print ['a', 'b', 'c', 'd']
print(howmanysplits.split(" ", 1)) #print ['a', 'b c d']
print(howmanysplits.split(" ", 2)) #print ['a', 'b', 'c d']
print(howmanysplits.split(" ", 9)) #print ['a', 'b', 'c', 'd']
#A first argument is required when specifying the number of splits in the second argument.  To split on whitespace runs using the second argument, type None as the first argument.
print(howmanysplits.split(None, 1)) #print ['a', 'b c d']
print(howmanysplits.split(None, 2)) #print ['a', 'b', 'c d']
print(howmanysplits.split(None, 9)) #print ['a', 'b', 'c', 'd']
sortlistofstrings.sort()
print(sortlistofstrings) #print ['It', 'a', 'day', 'is', "isn't", 'it?', 'nice', 'today,']
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
splitmethod = "You\t\t can have tabs\t\n \t and newlines " "mixed in"
print(splitmethod.expandtabs(1)) #expandtabs replaces tab characters with the specified number of spaces
'''
You   can have tabs 
   and newlines mixed in
'''
from collections import Counter
countwords = "Count the words in the string.  We hope to one day become the world's leader in free, education resources.  We are constantly discovering and adding more free content to the website everyday.  There is already an enormous amount of resoruces online that can be accessed for free by anyone in the world, the main issue right now is that very little of it is organized or structured in any way.  We want to be the solution to that problem."
print(countwords) #print Count the words in the string.  We hope to one day become the world's leader in free, education resources.  We are constantly discovering and adding more free content to the website everyday.  There is already an enormous amount of resoruces online that can be accessed for free by anyone in the world, the main issue right now is that very little of it is organized or structured in any way.  We want to be the solution to that problem.
print(countwords.count("the")) #print 7
print(countwords.count("the", 10)) #print 6.  Start the count at index position 10.
print(countwords.count("that", 253, 429)) #print 2.  Start the count at index position 253 inclusive and stop the count at index position 429 exclusive.
splitcountwords = countwords.split(" ")
topwords = Counter(splitcountwords)
threemostcommonwords = topwords.most_common(5)
print(threemostcommonwords) #print [('the', 7), ('in', 4), ('', 4), ('to', 4), ('We', 3)].  RM:  I intentionally double spaced after the periods.
from string import ascii_lowercase #print lower case alphabet letters
print(ascii_lowercase) #print abcdefghijklmnopqrstuvwxyz
print(type(ascii_lowercase)) #print <class 'str'>
print(*ascii_lowercase) #print a b c d e f g h i j k l m n o p q r s t u v w x y z
print(*list(ascii_lowercase)) #print a b c d e f g h i j k l m n o p q r s t u v w x y z
print([*"abcdefghijklmnopqrstuvwxyz"]) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Boolean
print(bool("return true" > "or return false using bool()")) #print True
print(bool("v" > "a")) #print True
print(bool(1 == 1)) #print True
print(any([True, False, 0, 1 < 0])) #print True
print(any([True, False, 0, 1 > 0])) #print True
print(any([False, True])) #print True
print(any([False])) #print False
print(any([])) #print False
print(all([True, False, 0, 1 < 0])) #print False
print(all([True, False, 0, 1 > 0])) #print False
print(all([True, True])) #print True
print(all([True, 34 < 5])) #print False
print(True and True) #print True
print(True and False) #print False
print(False and False) #print False
print(True, True) #print True True
print(True, False) #print True False
print(False, False) #print False False
intnumber = 80
floatnumber = 55.70
checkinteger = isinstance(intnumber, (int, float))
print(checkinteger) #print True
checkfloat = isinstance(floatnumber, (int, float))
print(checkfloat) #print True
print(intnumber is floatnumber) #print False
truestring = "A string is considered ture if it's not empty."
print(any(truestring)) #print True
print("string" in truestring) #print True
print("STRING" in truestring) #print False
print(3 in [1, 3, 4, 5, "check item in list"]) #print True
print(98 in [1, 3, 4, 5, "check item in list"]) #print False

#Variables
floatnumbertype = 6.91 #float
complexnumbertype = 3 + 2j #complex
print(type(complexnumbertype)) #print <class 'complex'>
booleantype = True
print(type(booleantype)) #print <class 'bool'>
print(not booleantype) #print False
assignvariablenone = None
print(assignvariablenone) #print None
x = "string variable attributes"
print(x) #print string variable attributes
print(globals()["x"]) #print string variable attributes
y = "a second string variable attributes"
print(globals())
'''
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fa125ad5b80>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'yytest.py', '__cached__': None, 'x': 'string variable attributes', 'y': 'a second string variable attributes'}
'''
print(type(globals())) #print <class 'dict'>
print(globals()["__cached__"]) #print None
attributevariable = "upper() is the attribute for attributevariable"
print(attributevariable) #print upper() is the attribute for attributevariable
uppermethod = attributevariable.upper() #Python finds the upper() method and executes upper() thanks to the parentheses
print(uppermethod) #print UPPER() IS THE ATTRIBUTE FOR ATTRIBUTEVARIABLE
variable1, variable2, variable3, variable4 = "four variables", "separated by", "four commas", "in one line"
print(variable1) #print four variables
print(variable2) #print separated by
print(variable3) #print four commas
print(variable4) #print in one line
[variable1, variable2, variable3, variable4] = ["four variables contained in a list", "separated by four", "commas all", "in one list"]
print(variable1) #print four variables contained in a list
print(variable2) #print separated by four
print(variable3) #print commas all
print(variable4) #print in one list
print(type(variable4)) #print <class 'str'>
(variable1, variable2, variable3, variable4) = ("four variables contained in a tuple", "separated", "by four commas all", "in one tuple")
print(variable1) #print four variables contained in a tuple
print(variable2) #print separated
print(variable3) #print by four commas all
print(variable4) #print in one tuple
print(type(variable4)) #print <class 'str'>
print(list((variable1, variable2, variable3))) #print ['four variables contained in a tuple', 'separated', 'by four commas all']
print([(variable1, variable2, variable3)]) #print ['four variables contained in a tuple', 'separated', 'by four commas all']
variable1, variable2, variable3, variable4 = ["assign me to four different variables"] * 4
print(variable1) #print assign me to four different variables
print(variable2) #print assign me to four different variables
print(variable3) #print assign me to four different variables
print(variable4) #print assign me to four different variables
print(type(variable4)) #print <class 'str'>
variable1 = variable2 = variable3 = variable4 = "four variables all equal to each other"
print(variable1) #print four variables all equal to each other
print(variable2) #print four variables all equal to each other
print(variable3) #print four variables all equal to each other
print(variable4) #print four variables all equal to each other
print(variable4 is variable1) #print True
variable1 = variable2 = variable3 = variable4 = ["list", "contains", "three entries"]
print(variable1) #print ["list", "contains", "three entries"]
print(variable2) #print ["list", "contains", "three entries"]
print(variable3) #print ["list", "contains", "three entries"]
print(variable4) #print ["list", "contains", "three entries"]
print(variable4 is variable1) #print True
dictionaryvaluea, dictionaryvalueb, dictionaryvaluec = ({"a key": "a value"}, {"b key": "b value"}, {"c key": "c value"})
print(dictionaryvaluea) #print {'a key': 'a value'}
print(dictionaryvalueb) #print {'b key': 'b value'}
print(dictionaryvaluec) #print {'c key': 'c value'}
#A stackoverflow says don't do the following any other object
dontdothis = {}
dontdothistoo = {}
dontdothis = dontdothistoo = {} #same dictionary object assigned to dontdothis, dontdothistoo.  Should not do this.
lista = listb = []
lista.append("append me to the lista and listb")
print(lista) #print ['append me to the lista and listb']
print(listb) #print ['append me to the lista and listb']
lista = listb = ["first entry already inside"]
lista.append("append me to the lista and listb")
print(lista) #print ['first entry already inside', 'append me to the lista and listb']
print(listb) #print ['first entry already inside', 'append me to the lista and listb']
leftlist, middlelist, rightlist = [[], [], []] #leftlist, middlelist, rightlist = [[] for _ in range(0, 3)] using lists or tuples also works
print(leftlist) #print []
print(middlelist) #print []
print(rightlist) #print []
leftlist.append("add text to the blank left list")
print(leftlist) #print ['add text to the blank left list']
print(middlelist) #print []
print(rightlist) #print []
rightlist.append("add text to the blank right list")
print(middlelist) #print []
print(rightlist) #print ['add text to the blank right list']
stringvariable = "The String"
integervariable = 457
decimalvariable = 3.14159
print("Use plus sign to concatenate string variables.  Integer is " + str(integervariable) + ".  String is " + stringvariable + ".") #print Use plus sign to concatenate string variables.  Integer is 457.  String is The String.
print("use comma to concateante numerical variables.  Integer is", integervariable, ".  Decimal is", decimalvariable, ".") #print use comma to concateante numerical variables.  Integer is 457 .  Decimal is 3.14159 .
print("Use the percent f for an integer as a floating number %f.  Use the percent s for a string %s." % (integervariable, stringvariable)) #print Use the percent f for an integer as a floating number 457.000000.  Use the percent s for a string The String.
print("Use the percent f for a decimal as a floating number %f." % (decimalvariable)) #print Use the percent f for a decimal as a floating number 3.141590.
print("Use the percent period 2 f for a decimal as a floating number two decimals %.2f." % (decimalvariable)) #print Use the percent period 2 f for a decimal as a floating number two decimals 3.14.
print("Use the percent d for a decimal as an integer %d." % (decimalvariable)) #print Use the percent d for a decimal as an integer 3.
print("Pi is %f" % (3.14159)) #print Pi is 3.141590
print("Pi is %.2f" % (3.14159)) #print Pi is 3.14
print("Pi is %6.2f" % (3.14159)) #print Pi is **3.14
print("Pi is %-6f for geometry circles" % (3.14159)) #print Pi is 3.141590 for geometry circles
print("Pi is %-6.2f" % (3.14159)) #print Pi is 3.14**
print("Use curly braces {{}}.  Double curly braces as escape curly brace.  Integer is {}.  String is {}.".format(integervariable, stringvariable)) #print Use curly braces {}.  Double curly braces as escape curly brace.  Integer is 457.  String is The String.
print("Type the colon period and number f for a floating number or decimal number from an integer {:.1f} {:.2f}.".format(integervariable, integervariable)) #print Type the colon period and number f for a floating number or decimal number from an integer 457.0 457.00.
print("Decimal variable return two decimals {:.2f}.".format(decimalvariable)) #print Decimal variable return two decimals 3.14.
print("Decimal variable return five decimals {:.5f}.".format(decimalvariable)) #Decimal variable return five decimals 3.14159.
print("Reference like index numbers {1} and {0} by position number {1}.".format("Position 0", "Position 1")) #print Reference like index numbers Position 1 and Position 0 by position number Position 1.
print("Reference like index numbers.  String index 1 is {1}.  Integer is index 0 {0}.".format(integervariable, stringvariable)) #print Reference like index numbers.  String index 1 is The String.  Integer is index 0 457.
print("Reference arguments in the .format.  {lastreference} and {firstreference} by position reference {middlereference}.".format(firstreference="Happy", middlereference="Belated", lastreference="Birthday")) #print Reference arguments in the .format.  Birthday and Happy by position reference Belated.
print("{0} is the food of {user[1]}".format("Ambrosia", user=["men", "the gods", "others"])) #print Ambrosia is the food of the gods
print("{0:10} is the food of gods".format("Ambrosia")) #print Ambrosia   is the food of gods.  Ambrosia90 is the food of gods.  10 spaces start at 0 pad with spaces.
print("{0:{2}} is the food of gods".format("Ambrosia", 55, 10)) #print Ambrosia   is the food of gods.  Ambrosia90 is the food of gods.  10 spaces start at 0 pad with spaces using the third parameter or the second index parameter.
print("{food:{width}} is the food of gods".format(food="Ambrosia", width=10)) #print Ambrosia   is the food of gods.  Ambrosia90 is the food of gods.  10 spaces start at 0.
print("{0:>10} is the food of gods".format("Ambrosia")) #print **Ambrosia is the food of gods.  >10 forces right justify of the field and pads with spaces
print("{0:&>10} is the food of gods".format("Ambrosia")) #print &&Ambrosia is the food of gods.  &>10 forces right justify of the field and pads with ampersands instead of spaces
print(f"F-string quick lesson.  Double curly braces as escape curly brace {{}}.  Print the stringvariable {stringvariable}.  Print the integer {integervariable}.") #print F-string quick lesson.  Double curly braces as escape curly brace {}.  Print the stringvariable The String.  Print the integer 457.
#f-strings for float values and integer values.  Letter f to format float values.  Letter d to format integer values.
print(f"Two decimal places for 17.489 is {17.489:.2f}.") #print Two decimal places for 17.489 is 17.49.
variable17489 = 17.489
print(f"Two decimal places for variable 17.489 is {variable17489:.2f}.") #print Two decimal places for variable 17.489 is 17.49.
print(f"Letter d to format integer number 8 is {8:d}.") #print Letter d to format integer number 8 is 8.
print(f"Field width 10 enclosed in brackets to see the integer 27 value align right decimal included in count:  [{27:10d}]") #print Field width 10 enclosed in brackets to see the integer 27 value align right:  [        27]
print(f"Field width 10 enclosed in backets to see the float 3.5 value align right decimal included in count:  [{3.5:10f}]") #print Field width 10 enclosed in backets to see the float 3.5 value align right[  3.500000]
print(f"Field width 10 enclosed in backets to see the float 12346578.9 value align right decimal included in count which didn't happend field width 15 with five zeros:  [{12345678.9:10f}]") #print Field width 10 enclosed in backets to see the float 12346578.9 value align right decimal included in count which didn't happend field width 15 with five zeros:  [12345678.900000]
print(f"Field width 10 enclosed in backets to see the float 1.23456789 value align right decimal included in count which didn't happen field width 8:  [{1.23456789:10f}]") #print Field width 10 enclosed in backets to see the float 1.23456789 value align right decimal included in count which didn't happend field display 8:  [  1.234568]
#< left align.  > right align.  ^ center align.
print(f"Field width left align 15 for integer 27 [{27:<15d}]") #print Field width less than 15 for integer 27 [27             ]
print(f"Field width left align 15 for integer 271234567890123 all fifteen digits printed [{271234567890123:<15d}]") #print Field width less than 15 for integer 271234567890123 all fifteen digits printed [271234567890123]
print(f"Field width left align 10 for integer 271234567890123 all fifteen digits printed [{271234567890123:<10d}]") #print Field width less than 10 for integer 271234567890123 all fifteen digits printed [271234567890123]
print(f"Field width left align 4 for floating number 3.5 all five zeros printed [{3.5:<4f}]") #print Field width left align 4 for floating number 3.5 all five zeros printed [3.500000]
print(f"Field width left align 1 for floating number 3.5 [{3.5:<.1f}]") #print Field width left align 1 for floating number 3.5 [3.5]
print(f'[{"single quote f-string Brackets assign count right align string 82 characters.":>82}]') #print [     single quote f-string Brackets assign count right align string 82 characters.]
print(f'[{"single quote f-string Brackets assign count right align string 82 characters.":>1}]') #print [single quote f-string Brackets assign count right align string 82 characters.]
print(f"Center align integer 27 width 8 [{27:^8d}]") #print Center align integer 27 width 8 [   27   ]
print(f'[{"Center the string or any number using the carrot sign 68 characters.":^74}]') #print [   Center the string or any number using the carrot sign 68 characters.   ].  Extra spaces of an unequal centering placed to the right.
print(f"Align positive negative with a space width one [{27:+1d}]") #print Align positive negative with a space width one [+27]
print(f"Align positive negative with a space width one [{-27:1d}]") #print Align positive negative with a space width one [-27]
print(f"Positive sign text numerical value width four [{27:+4d}]") #print Positive sign text numerical value width four [ +27]
print(f"Negative sign text numerical value width four [{-27:4d}]") #print Negative sign text numerical value width four [ -27]
print(f"Positive sign text numerical value width ten [{27:+10d}]") #print Positive sign text numerical value width ten[       +27]
print(f"Fill with zeros in front of numerical value width five [{27:+05d}]") #print Fill with zeros in front of numerical value width five [+0027]
print(f"Fill with zeros in front of numerical value width ten [{27:+010d}]") #print Fill with zeros in front of numerical value width ten [+000000027]
print(f"String integer value with commas {123456789:,d}.") #print String numerical value with commas 123,456,789.
print(f"String decimal value with commas {123456.78:,.3f}.") #print String numerical value with commas 123,456.780.
print(f"String decimal value with commas {123456.78:,.6f}.") #print String decimal value with commas 123,456.780000.
value = 42
stringinterpolation = f"The answer is {value}"
print(stringinterpolation) #print The answer is 42
pi = 3.1415
print(f"pi is {pi:{10}.{2}}") #print pi is *******3.1
value = "grapes"
print(f"String interpolation value variable {value}.") #print String interpolation value variable grapes.
