#Regular expressions specify a pattern of text to search.  Regular expressions, or regexes for short, are descriptions for a pattern of text.  For example, a \d in regex stands for a digit character from 0 to 9.  Regex \d\d\d-\d\d\d-\d\d\d\d is a phone number string of three numbers, a hyphen, three numbers, a hyphen, and four numbers.  Any other string doesn't match regex \d\d\d-\d\d\d-\d\d\d\d.
#Regex or re is a sequence of characters such as letters, numbers, and special characters forming a pattern to search text, text files, CSV files, and Excel files.  Search for the text containing sequences of characters which match the pattern.  Use the built-in module re.  There are additional third party modules supporting regular expressions.
import re

matchfivestringnumbers = "02215"
print(re.search(matchfivestringnumbers, "02215")) #print <re.Match object; span=(0, 5), match='02215'>
print(re.search(matchfivestringnumbers, "02215") is True) #print False
print(re.search(matchfivestringnumbers, "02215") == True) #print False
if re.search(matchfivestringnumbers, "02215"):
    print("True") #print True
if re.search(matchfivestringnumbers, "13329"):
    print("True")
else:
    print("False no search") #print False no search
print(re.search(matchfivestringnumbers, "35530")) #print None
matchfivestringnumbers = "02215"
print(re.fullmatch(matchfivestringnumbers, "02215")) #print <re.Match object; span=(0, 5), match='02215'>
print(re.fullmatch(matchfivestringnumbers, "02215") is True) #print False
print(re.fullmatch(matchfivestringnumbers, "02215") == True) #print False
if re.fullmatch(matchfivestringnumbers, "02215"):
    print("True") #print True
if re.fullmatch(matchfivestringnumbers, "13329"):
    print("True")
else:
    print("False no fullmatch") #print False no fullmatch
print(re.fullmatch(matchfivestringnumbers, "35530")) #print None
#The search() function searches the string for a match.  It returns a Match object if there is a match.  The signature of the function is re.search(pattern, string, flags=0).  pattern is the regular expression used in the matching process, string is the string to be searched, flags are optional flags to modify the search operation.
#The match() function searches the beginning of a string for a match.  match() function works the same as search() function.  match() function checks at the beginning of the string.  search() function checks anywhere in the string.
stringvariable = "find me at the beginning of the sentence"
print(re.match("find me at the beginning", stringvariable)) #print <re.Match object; span=(0, 24), match='find me at the beginning'>
print(re.search("find me at the beginning", stringvariable)) #print <re.Match object; span=(0, 24), match='find me at the beginning'>
print(re.match("at the begin", stringvariable)) #print None
print(re.search("at the begin", stringvariable)) #print <re.Match object; span=(8, 20), match='at the begin'>
compilerobjectfindme = re.compile(r"find me at the beginning")
compilerobjectatthe = re.compile(r"at the begin")
print(re.match(compilerobjectfindme, stringvariable)) #print <re.Match object; span=(0, 24), match='find me at the beginning'>
print(re.search(compilerobjectfindme, stringvariable)) #print <re.Match object; span=(0, 24), match='find me at the beginning'>
print(re.match(compilerobjectatthe, stringvariable)) #print None
print(re.search(compilerobjectatthe, stringvariable)) #print <re.Match object; span=(8, 20), match='at the begin'>
ifelsematch = re.match(compilerobjectfindme, stringvariable)
if ifelsematch:
    print("True") #print True
else:
    print("False")
ifelsesearch = re.search(compilerobjectfindme, stringvariable)
if ifelsesearch:
    print("True") #print True
else:
    print("False")
ifelsematch = re.match(compilerobjectatthe, stringvariable)
if ifelsematch:
    print("True")
else:
    print("False") #print False
ifelsesearch = re.search(compilerobjectatthe, stringvariable)
if ifelsesearch:
    print("True") #print True
else:
    print("False")
compilerobjectfindme = re.compile(r"find me at the beginning")
print(compilerobjectfindme.findall(stringvariable)) #print ['find me at the beginning']
searchgroupobject = compilerobjectfindme.search(stringvariable)
print(searchgroupobject.group()) #print find me at the beginning
matchgroupobject = compilerobjectfindme.match(stringvariable)
print(matchgroupobject.group()) #print find me at the beginning
compilerobjectatthe = re.compile(r"at the begin")
print(compilerobjectatthe.findall(stringvariable)) #print ['at the begin']
searchgroupobject = compilerobjectatthe.search(stringvariable)
print(searchgroupobject.group()) #print at the begin
matchgroupobject = compilerobjectatthe.match(stringvariable)
#print(matchgroupobject.group()) #print AttributeError: 'NoneType' object has no attribute 'group'

#Four steps using Python regular expression summarized:  1 import regex module import re.  2 Create a regex object with the re.compile() function.  Use a raw string.  3 Pass the string to search using the search() method.  It returns a Match object first matched text.  4 Call the Match object's group() method to return a string of the actual matched text.  groups() method can work.
#search() method returns a Match object first matched text.  The search function looks for the first occurrence which matches the regular expression.  It returns a match object of type SRE_Match containing the matching substring.  The match object's group method returns the substring.  Include flags=re.IGNORECASE for case insensitive
#The search() function searches the string for a match.  It returns a Match object if there is a match.  The signature of the function is re.search(pattern, string, flags=0).  pattern is the regular expression used in the matching process, string is the string to be searched, flags are optional flags to modify the search operation.
#findall() method returns a string of every match in a list.
#The compile() function compiles a regular expression pattern into a regular expression object.  The regular expression object can be used for other methods such as match() and search().  re.compile(pattern, flags=0).  The compiled regular expression objects methods and attributes are different than their function counterparts.
stringsentence = "RoboCop eats baby food.  BABY FOOD."
vowelleters = re.compile(r"[aeiouAEIOU]")
extractvowels = vowelleters.findall(stringsentence)
print(extractvowels) #print ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
#Use the caret character before defining the character class as the negative or not
consonantletters = re.compile(r"[^aeiouAEIOU]")
extractconsonants = consonantletters.findall(stringsentence)
print(extractconsonants) #print ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
stringsentence = "RoboCop eats baby food.  4 9 1 BABY FOOD."
lettersnumbersranges = re.compile(r"[M-Za-f4-7]")
extractselectedrangelettersnumbers = lettersnumbersranges.findall(stringsentence)
print(extractselectedrangelettersnumbers) #print ['R', 'b', 'e', 'a', 'b', 'a', 'b', 'f', 'd', '4', 'Y', 'O', 'O']
stringsentence = "RoboCop eats baby food.  4 9 1 BABY FOOD."
lettersnumbersranges = re.compile(r"[M-Za-f4-7 ]")
extractselectedrangelettersnumbersplusspaces = lettersnumbersranges.findall(stringsentence)
print(extractselectedrangelettersnumbersplusspaces) #print ['R', 'b', ' ', 'e', 'a', ' ', 'b', 'a', 'b', ' ', 'f', 'd', ' ', ' ', '4', ' ', ' ', ' ', 'Y', ' ', 'O', 'O']
stringsentence = "Begins with hello world ends with goodbye."
mustbeginwithcaret = re.compile(r"^Begins with hello")
extractstartswith = mustbeginwithcaret.search(stringsentence)
print(extractstartswith) #print <re.Match object; span=(0, 17), match='Begins with hello'>
print(extractstartswith.group()) #print Begins with hello
extractstartswith = mustbeginwithcaret.findall(stringsentence)
print(extractstartswith) #print ['Begins with hello']
mustendswithdollarsign = re.compile(r"ends with goodbye\.$")
extractendswith = mustendswithdollarsign.search(stringsentence).group()
print(extractendswith) #print ends with goodbye.
#The period match any character except for a new line.  Match a single character.
findmultipleswithat = "The cat in the hat sat on the flat mat."
singlecharacterwildcard = re.compile(r".at")
#print(singlecharacterwildcard.find(findmultipleswithat)) #print AttributeError: 're.Pattern' object has no attribute 'find'
print(singlecharacterwildcard.findall(findmultipleswithat)) #print ['cat', 'hat', 'sat', 'lat', 'mat']
print(singlecharacterwildcard.search(findmultipleswithat)) #print <re.Match object; span=(4, 7), match='cat'>
print(singlecharacterwildcard.search(findmultipleswithat).group()) #print cat
#The period match any single character except the new line and the asterisk matches zero or more of the character.  Need the period in front of the asterisk or error message appears.  The period asterisk default matches as much text as possible.
findmultiplesat = re.compile(r".*at")
print(findmultiplesat.findall(findmultipleswithat)) #print ['The cat in the hat sat on the flat mat']
#findmultiplesatnoperiod = re.compile(r"*at") #return re.error: nothing to repeat at position 0
#print(findmultiplesatnoperiod.findall(findmultipleswithat)) #print re.error: nothing to repeat at position 0
findjake = "The snake begins with jake from Florida."
multiplecharacterswildcardbefore = re.compile(r".*jake")
print(multiplecharacterswildcardbefore.findall(findjake)) #print ['The snake begins with jake']
multiplecharacterswildcardafter = re.compile(r"jake*.")
print(multiplecharacterswildcardafter.findall(findjake)) #print ['jake ']
multiplecharacterswildcardafterall = re.compile(r"jake.*")
print(multiplecharacterswildcardafterall.findall(findjake)) #print ['jake from Florida.']
multiplecharacterswildcardbeforeafter = re.compile(r".*jake*.")
print(multiplecharacterswildcardbeforeafter.findall(findjake)) #print ['The snake begins with jake ']
multiplecharacterswildcardbeforeafterall = re.compile(r".*jake.*")
print(multiplecharacterswildcardbeforeafterall.findall(findjake)) #print ['The snake begins with jake from Florida.']
#Search between strings
firstnamelastname1 = "First Name: Al Last Name: Sweigart"
firstnamelastnameingroups = re.compile(r"First Name: (.*) Last Name: (.*)")
extractnamessearchobject = firstnamelastnameingroups.search(firstnamelastname1)
print(extractnamessearchobject.groups()) #print ('Al', 'Sweigart')
print(extractnamessearchobject.group(1)) #print Al
print(extractnamessearchobject.group(2)) #print Sweigart
firstnameslastnames1 = "First Name: Al Moose Last Name: Sweigart Booth"
extractnamessearchobject = firstnamelastnameingroups.search(firstnameslastnames1)
print(extractnamessearchobject.groups()) #print ('Al Moose', 'Sweigart Booth')
firstnamelastnamefindall = re.compile(r"First Name: *.* Last Name: *.* ")
print(firstnamelastnamefindall.findall(firstnamelastname1)) #print ['First Name: Al Last Name: ']
#firstnamelastnamefindall = re.compile(r"First Name: .* Last Name: .* ")
#print(firstnamelastnamefindall.findall(firstnamelastname1)) #print []
firstnamelastnamefindall = re.compile(r"First Name: *\w* Last Name: *\w* ")
print(firstnamelastnamefindall.findall(firstnamelastname1)) #print ['First Name: Al Last Name: ']
#periodstar default is greedy which matches as much text as possible.  Add a question mark for nongreedy which doesn't match as much text
firstnamelastname1 = "First Name: Al Last Name: Sweigart"
firstnamelastnamegreedy = re.compile(r"First Name: .*? Last Name: .*?")
extractnamessearchobject = firstnamelastnamegreedy.search(firstnamelastname1)
print(extractnamessearchobject) #print <re.Match object; span=(0, 26), match='First Name: Al Last Name: '>
print(extractnamessearchobject.group()) #print First Name: Al Last Name:
print(extractnamessearchobject.groups()) #print ()
firstnamelastname1 = "First Name: Al Last Name: Sweigart"
firstnamelastnamegreedy = re.compile(r"First Name: .*?.* Last Name: .*?.*")
extractnamessearchobject = firstnamelastnamegreedy.search(firstnamelastname1)
print(extractnamessearchobject) #print <re.Match object; span=(0, 34), match='First Name: Al Last Name: Sweigart'>
print(extractnamessearchobject.group()) #print First Name: Al Last Name: Sweigart
print(firstnamelastnamegreedy.findall(firstnamelastname1)) #print ['First Name: Al Last Name: Sweigart']
firstnameslastnames1 = "First Name: Al Moose Last Name: Sweigart Booth"
firstnamelastnamegreedy = re.compile(r"First Name: .*?.* Last Name: .*?.*")
extractnamessearchobject = firstnamelastnamegreedy.search(firstnameslastnames1)
print(extractnamessearchobject) #print <re.Match object; span=(0, 46), match='First Name: Al Moose Last Name: Sweigart Booth'>
print(extractnamessearchobject.group()) #print First Name: Al Moose Last Name: Sweigart Booth
print(firstnamelastnamegreedy.findall(firstnameslastnames1)) #print ['First Name: Al Moose Last Name: Sweigart Booth']
firstnameslastnamescarrots = "First Name: <Al Moose> Last Name: <Sweigart Booth>"
firstnamelastnamegreedycarrots = re.compile(r"First Name: <.*?> Last Name: <.*?>")
extractnamessearchobjectcarrots = firstnamelastnamegreedycarrots.search(firstnameslastnamescarrots)
print(extractnamessearchobjectcarrots) #print <re.Match object; span=(0, 50), match='First Name: <Al Moose> Last Name: <Sweigart Booth>
print(extractnamessearchobjectcarrots.group()) #print First Name: <Al Moose> Last Name: <Sweigart Booth>
print(firstnamelastnamegreedycarrots.findall(firstnameslastnamescarrots)) #print ['First Name: <Al Moose> Last Name: <Sweigart Booth>']
firstnamelastnamegreedycarrots = re.compile(r"First Name: <.*?.*> Last Name: <.*?.*>")
extractnamessearchobjectcarrots = firstnamelastnamegreedycarrots.search(firstnameslastnamescarrots)
print(extractnamessearchobjectcarrots) #print <re.Match object; span=(0, 50), match='First Name: <Al Moose> Last Name: <Sweigart Booth>
print(extractnamessearchobjectcarrots.group()) #print First Name: <Al Moose> Last Name: <Sweigart Booth>
print(firstnamelastnamegreedycarrots.findall(firstnameslastnamescarrots)) #print ['First Name: <Al Moose> Last Name: <Sweigart Booth>']
#Include re.DOTALL to match all characters including the newline \n
multiplelinestring = "One run.\n  Two shoes.\n  Three trees.\n"
nonewline = re.compile(".*")
print(nonewline.search(multiplelinestring)) #print <re.Match object; span=(0, 8), match='One run.'>
extractmultiplelinestringobject = nonewline.search(multiplelinestring)
print(extractmultiplelinestringobject.group()) #print One run.
print(extractmultiplelinestringobject.groups()) #print ()
multiplelinestring = "One run.\n  Two shoes.\n  Three trees.\n"
yesnewline = re.compile(".*", re.DOTALL)
print(yesnewline.search(multiplelinestring)) #print <re.Match object; span=(0, 37), match='One run.\n  Two shoes.\n  Three trees.\n'>
extractmultiplelinestringobject = yesnewline.search(multiplelinestring)
print(extractmultiplelinestringobject.group()) #print One run.  Two shoes.  Three trees.
print(extractmultiplelinestringobject.groups()) #print ()
#Include re.IGNORECASE or re.I as a second argument to re.compile() to search no exact casing
drseussstring = "Author Dr. Seuss wrote children's books for the World whole."
caseinsensitive = re.compile(r"seuss", flags=re.IGNORECASE)
print(caseinsensitive.search(drseussstring)) #print <re.Match object; span=(11, 16), match='Seuss'>
extractseussobject = caseinsensitive.search(drseussstring)
print(extractseussobject.group()) #print Seuss#Character classes.  RM:  ignore the backslash escape character
'''
\\d Any numeric digit from 0 to 9.
\\D Any character that is not a numeric digit from 0 to 9.
\\w Any letter, numeric digit, or the underscore character.  (Think of this as matching “word” characters.)
\\W Any character that is not a letter, numeric digit, or the underscore character.
\\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
\\S Any character that is not a space, tab, or newline.
Regular expressions metacharacters are the following:  [] {} () \\ * + ^ $ ? . |
'''
#A character class is a regular expression escape sequence which matches one character.  {number} is a quantifier.  A quantifier matches more than one character.  \d{5} is \d\d\d\d\d which is match five consecutive digits.
matchfivestringnumbers = "02215"
matchfivestringnumberscompile = re.compile(r"\d\d\d\d\d")
print(matchfivestringnumberscompile.findall(matchfivestringnumbers)) #print ['02215']
#Use curly brackets for specific repetitions.  If you have a group to repeat a specific number of times, then type the number in curly brackets to the right of the group.  (Ha){3} searchs for HaHaHa.  (Ha){3,5} searchs for HaHaHa, HaHaHaHa, and HaHaHaHaHa.  (Ha){3,} searchs for three or more Ha.  (Ha){0,6} searches for zero to six instances of Ha.  (Ha)(Ha)(Ha) is the same as (Ha){3}.  (Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)(Ha) is the same as (Ha){3,5}.
matchfivestringnumberscompile = re.compile(r"\d{5}")
print(matchfivestringnumberscompile.findall(matchfivestringnumbers)) #print ['02215']
#Square brackets define a custom character class which matches a single character.  For example [aeiou] matches a lowercase vowel, [A-Z] matches an uppercase letter, [a-z] matches a lowercase letter, and [a-zA-Z] matches any lowercase or uppercase letter.  RM:  using findall returns all letters as a list; however, it seems using search() and group() follows the square brackets.
rwally = "rRWally"
findoneletterlowercase = re.compile(r"[a-z]")
print(findoneletterlowercase.findall(rwally)) #print ['r', 'a', 'l', 'l', 'y']
findoneletterallcases = re.compile(r"[a-zA-Z]")
print(findoneletterallcases.findall(rwally)) #print ['r', 'R', 'W', 'a', 'l', 'l', 'y']
rwallyobject = findoneletterallcases.search(rwally)
print(rwallyobject.group()) #print r
print(rwallyobject.group()) #print r
print(rwallyobject.group()) #print r
findtwoletterallcasescorrect = re.compile(r"[a-zA-Z][a-zA-Z]")
rwallyobject = findtwoletterallcasescorrect.search(rwally)
print(rwallyobject.group()) #print rR
#Asterik * is the quantifier.  A quantifier matches zero or more occurrences of its subexpression.  For example, [A-Z][a-z]* matches an uppercase letter and zero or more lowercase letters such as Amanda, Bo, or E.
findtwolettersandthereafter = re.compile(r"[a-zA-Z][a-zA-Z]*")
rwallyobject = findtwolettersandthereafter.search(rwally)
print(rwallyobject.group()) #print rRWally
print(rwallyobject.groups()) #print ()
firstlowercasethereafter = re.compile(r"[a-z]*")
rwallyobject = firstlowercasethereafter.search(rwally)
print(rwallyobject.group()) #print r
firstuppercaselowercasethereafter = re.compile(r"[A-Z][a-z]*")
#rwallyobject = notlowercaseyesuppercase.search(rwally)
#print(rwallyobject.group()) #print NameError: name 'notlowercaseyesuppercase' is not defined
first2uppercaselowercasethereafter = re.compile(r"[A-Z][A-Z][a-z]*")
rwallyobject = first2uppercaselowercasethereafter.search(rwally)
print(rwallyobject.group()) #print RWally
print(first2uppercaselowercasethereafter.findall(rwally)) #print ['RWally']
#Caret ^ is the not symbol.  For example, [^a-z] matches a character not lowercase.
notlowercasenotuppercase = re.compile(r"[^a-z][^A-Z]")
rwallyobject = notlowercasenotuppercase.search(rwally)
print(rwallyobject.group()) #print Wa
lowercasenotuppercase = re.compile(r"[a-z][^A-Z]")
rwallyobject = lowercasenotuppercase.search(rwally)
print(rwallyobject.group()) #print al
notlowercaseyesuppercase = re.compile(r"[^a-z][A-Z]")
rwallyobject = notlowercaseyesuppercase.search(rwally)
print(rwallyobject.group()) #print RW
print(notlowercaseyesuppercase.findall(rwally)) #print ['RW']
#Metacharacters in a custom character class are metacharacters themselves.  For example [*+$] matches asterik * or plus + or dollar $.
character = "!"
findmetacharacter = re.compile(r"[*+!]")
print(findmetacharacter.findall(character)) #print ['!']
character = "*"
findmetacharacter = re.compile(r"[*+!]")
print(findmetacharacter.findall(character)) #print ['!']
character = "*!"
findmetacharacter = re.compile(r"[*+!]")
print(findmetacharacter.findall(character)) #print ['*', '!']
charactersentence = "character* in a $entence!."
findmetacharacter = re.compile(r"[*+!]")
print(findmetacharacter.findall(charactersentence)) #print ['*', '!']
findmetacharacter = re.compile(r"[*]*[$]*[!]*[.]")
print(findmetacharacter.findall(charactersentence)) #print ['!.']
findmetacharacter = re.compile(r"[*]")
print(findmetacharacter.findall(charactersentence)) #print ['*']
findmetacharacter = re.compile(r"[*]*[$]")
print(findmetacharacter.findall(charactersentence)) #print ['$']
findmetacharacterandwords = re.compile(r"[a-z]*[*]")
print(findmetacharacterandwords.findall(charactersentence)) #print ['character*']
findmetacharacterandwords = re.compile(r"[a-z]*[*]\s[a-z]*\s[a-z]\s[$]")
print(findmetacharacterandwords.findall(charactersentence)) #print ['character* in a $']
#Plus sign + to find one or more custom character class
rwally = "rRWally"
customcharacterclass = re.compile(r"[a-z]+")
print(customcharacterclass.findall(rwally)) #print ['r', 'ally']
customcharacterclass = re.compile(r"[A-Z]+")
print(customcharacterclass.findall(rwally)) #print ['RW']
customcharacterclass = re.compile(r"[A-Z][a-z]+")
print(customcharacterclass.findall(rwally)) #print ['Wally']
customcharacterclass = re.compile(r"[a-z][A-Z]+")
print(customcharacterclass.findall(rwally)) #print ['rRW']
customcharacterclass = re.compile(r"[a-zA-Z]+")
print(customcharacterclass.findall(rwally)) #print ['rRWally']
customcharacterclass = re.compile(r"[A-Za-z]+")
print(customcharacterclass.findall(rwally)) #print ['rRWally']
customcharacterclass = re.compile(r"[A-Z]+[a-z]")
print(customcharacterclass.findall(rwally)) #print ['RWa']
hyphenstring = "okay -submarine plane"
lettersandhyphen = re.compile(r"[-a-z]")
print(lettersandhyphen.findall(hyphenstring)) #print ['o', 'k', 'a', 'y', '-', 's', 'u', 'b', 'm', 'a', 'r', 'i', 'n', 'e', 'p', 'l', 'a', 'n', 'e']
onehyphenandletter = re.compile(r"[-]\w")
print(onehyphenandletter.findall(hyphenstring)) #print ['-s']
#Question mark ? to find zero or one custom character class
labelvariable = "labelled"
questionmarkcustom = re.compile(r"labell?ed") #The labell?ed examples before l? indicates there can be zero or one letter l before the remaining characters ed or zero or one letter l to the left of the question mark
print(questionmarkcustom.findall(labelvariable)) #print ['labelled'].  Zero or one letter l between label and the ed.
labelvariable = "labeled"
questionmarkcustom = re.compile(r"labell?ed")
print(questionmarkcustom.findall(labelvariable)) #print ['labeled'].  Zero or one letter l between label and the ed.
labelvariable = "labellled"
questionmarkcustom = re.compile(r"labell?ed")
print(questionmarkcustom.findall(labelvariable)) #print [].  Two letter l's between label and the ed.  Return nothing.
labelvariable = "labelllzzed"
questionmarkcustom = re.compile(r"labell?ed")
print(questionmarkcustom.findall(labelvariable)) #print [].  One additional letter l and two letters z's between label and the ed.  Return nothing.
labelvariable = "labeled"
questionmarkcustom = re.compile(r"labe?led")
print(questionmarkcustom.findall(labelvariable)) #print ['labeled'].  Zero or one letter e between lab and the led.
labelvariable = "labled"
questionmarkcustom = re.compile(r"labe?led")
print(questionmarkcustom.findall(labelvariable)) #print ['labled'].  Zero or one letter e between lab and the led.
labelvariable = "labzled"
questionmarkcustom = re.compile(r"labe?led")
print(questionmarkcustom.findall(labelvariable)) #print [].  No zero or one letter e between lab and the led.  z is not in the compile.
labelvariable = "labzled"
questionmarkcustom = re.compile(r"labz?led")
print(questionmarkcustom.findall(labelvariable)) #print ['labzled'].  Zero or one letter z between lab and the led.
labelvariable = "labzled"
questionmarkcustom = re.compile(r"labz?led")
print(questionmarkcustom.findall(labelvariable)) #print ['labzled'].  Zero or one letter z between lab and the led.
rwally = "rRWally"
questionmarkcustom = re.compile(r"r?RWa?llz?y")
print(questionmarkcustom.findall(rwally)) #print ['rRWally'].  z? means a z or no z after the ll and before the y.
#Curly brackets {number, } quantifier matches at least number occurrences.  Curly brackets {lowernumberinclusive, uppernumberinclusive} quantifier matches between lowernumber and uppernumber inclusive occurrences.
fivewordssevenwords = "ultra combos7"
fivewordssevenwordscompile = re.compile(r"\w{5}\s\w{7}")
print(fivewordssevenwordscompile.findall(fivewordssevenwords)) #print ['ultra combos7']
threewordssemicolonfivewords = "red;blues"
threewordssemicolonfivewordscompile = re.compile(r"\w{3};\w{4}")
print(threewordssemicolonfivewordscompile.findall(threewordssemicolonfivewords)) #print ['red;blue']
threewordssemicolonfivewordsobject = threewordssemicolonfivewordscompile.search(threewordssemicolonfivewords)
print(threewordssemicolonfivewordsobject.group()) #print red;blue
print(threewordssemicolonfivewordsobject.groups()) #print ()
#print(threewordssemicolonfivewordsobject.group(1)) #print IndexError: no such group
elevenletters = "dixowixoebr"
findelevenletters = re.compile(r"\w{11,}")
print(findelevenletters.findall(elevenletters)) #print ['dixowixoebr']
findnineelevenletters = re.compile(r"\w{9,11}")
print(findnineelevenletters.findall(elevenletters)) #print ['dixowixoebr']
findelevenletters = re.compile(r"[b-x]{11,}")
print(findelevenletters.findall(elevenletters)) #print ['dixowixoebr']
findelevenletters = re.compile(r"[d][^I][b-x]{8,10}[r]")
print(findelevenletters.findall(elevenletters)) #print ['dixowixoebr']
xmasregex = re.compile(r"\d+\s\w+") #xmasregex \d+ match text with one or more numeric digits, \s a whitespace character, and \w+ one or more letter or digit or underscore characters
twelvedaysofxmas = "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
twelvedaysofxmaslist = xmasregex.findall(twelvedaysofxmas)
print(twelvedaysofxmaslist) #print ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
laststringwithdollarsign = re.compile(r"\w+$")
lastxmasgift = laststringwithdollarsign.findall(twelvedaysofxmas)
print(lastxmasgift) #print ['partridge']
firstnumberlaststring = re.compile(r"^\d+|\w+$") #RM:  needed the pipe character | or
firstnumberlastxmasgift = firstnumberlaststring.findall(twelvedaysofxmas)
print(firstnumberlastxmasgift) #print ['12', 'partridge']
phonenumberregexgrouping = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
phonenumbermessage = "My number grouped is 415-555-4242"
findphonenumber = phonenumberregexgrouping.search(phonenumbermessage)
print(findphonenumber.group()) #print 415-555-4242
print(findphonenumber.group(0)) #print 415-555-4242
print(findphonenumber.group(1)) #print 415
print(findphonenumber.group(2)) #print 555-4242
print(findphonenumber.groups()) #print ('415', '555-4242')
areacode, mainnumber = findphonenumber.groups()
print(areacode) #print 415
print(mainnumber) #print 555-4242
#Enter the escape character \\ to print a single backslash.  \\n in regexp is a backslash and lowercase letter n.  However, type a letter r before the first quote in the string value makes the string value as a raw string which doesn't use escape characters.
phonenumberregexgroupingescapecharacters = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
phonenumbermessageescapecharacters = "My number grouped is (415) 555-4242"
findphonenumber = phonenumberregexgroupingescapecharacters.search(phonenumbermessageescapecharacters)
print(findphonenumber.group(1)) #print (415)
areacode, mainnumber = findphonenumber.groups()
print(areacode) #print (415)
print(mainnumber) #print 555-4242
pipecharacteror = re.compile(r"Batman|Tina Fey")
batmanstring = "Batman and Tina Fey"
searchbatman = pipecharacteror.search(batmanstring)
print(searchbatman.group()) #print Batman
pipecharacteror = re.compile(r"Tina Fey|Batman")
tinafeystring = "Tina Fey and Batman"
searchtinafey = pipecharacteror.search(tinafeystring)
print(searchtinafey.group()) #print Tina Fey
pipecharacteror = re.compile(r"Bat(man|mobile|copter|bat)")
stringsearch = "Batmobile lost a wheel"
findbatmobile = pipecharacteror.search(stringsearch)
print(findbatmobile.group()) #print Batmobile
print(findbatmobile.group(0)) #print Batmobile
print(findbatmobile.group(1)) #print mobile
stringsearch = "The bat man flew the case sensitive Batcopter with wheels"
findbatcopter = pipecharacteror.search(stringsearch)
print(findbatcopter.group()) #print Batcopter
print(findbatcopter.groups()) #print ('copter',)
#The question mark ? flags the group to the left of ? as an optional part of the pattern.
questionmarkoptional = re.compile(r"Bat(wo)?man")
findbatman = questionmarkoptional.search("The Adventures Of Batman")
print(findbatman.group()) #print Batman
findbatwoman = questionmarkoptional.search("The Adventures Of Batwoman not print Batman")
print(findbatwoman.group(0)) #print Batwoman
print(findbatwoman.group(1)) #print wo
print(findbatwoman.groups()) #print ('wo',)
phonenumberreggexoptionalareacode = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
phonenumbermessage = "My optional area code yes area code is 415-555-4242"
findphonenumber = phonenumberreggexoptionalareacode.search(phonenumbermessage)
print(findphonenumber.group()) #print 415-555-4242
print(findphonenumber.group(0)) #print 415-555-4242
print(findphonenumber.group(1)) #print 415-
print(findphonenumber.groups()) #print ('415-',)
phonenumbermessage = "My optional area code no area code is 555-4242"
findphonenumber = phonenumberreggexoptionalareacode.search(phonenumbermessage)
print(findphonenumber.group()) #print 555-4242
print(findphonenumber.group(0)) #print 555-4242
print(findphonenumber.group(1)) #print None
print(findphonenumber.groups()) #print (None,)
asteriskmatchzeroormore = re.compile(r"Bat(wo)*man")
findbatman = asteriskmatchzeroormore.search("The Adventures of Batman")
print(findbatman.group()) #print Batman.  RM:  (wo)* matched zero instances of wo in the string
findbatwoman = asteriskmatchzeroormore.search("The Adventures of Batwoman")
print(findbatwoman.group()) #print Batwoman
findbatwowos = asteriskmatchzeroormore.search("The Adventures of Batwowowowoman")
print(findbatwowos.group()) #print Batwowowowoman
findbatmanbatwoman = asteriskmatchzeroormore.search("The Adventures of Batman and Batwoman")
print(findbatmanbatwoman.group()) #print Batman
print(findbatmanbatwoman.group(1)) #print None
print(findbatmanbatwoman.groups()) #print (None,)
plusmatchoneormore = re.compile(r"Bat(wo)+man")
try:
    findbatman = plusmatchoneormore.search("The Adventures of Batman")
    print(findbatman.group())
except AttributeError:
    print("Must match at least one Batwoman") #print Must match at least one Batwoman
findbatwoman = plusmatchoneormore.search("The Adventures of Batwoman")
print(findbatwoman.group()) #print Batwoman
findbatwowos = plusmatchoneormore.search("The Adventures of Batwowowowoman")
print(findbatwowos.group()) #print Batwowowowoman
findbatmanbatwoman = plusmatchoneormore.search("The Adventures of Batman and Batwowoman")
print(findbatmanbatwoman.group()) #print Batwowoman
print(findbatmanbatwoman.group(1)) #print wo
print(findbatmanbatwoman.groups()) #print ('wo',)
#Use curly brackets for specific repetitions.  If you have a group to repeat a specific number of times, then type the number in curly brackets to the right of the group.  (Ha){3} searchs for HaHaHa.  (Ha){3,5} searchs for HaHaHa, HaHaHaHa, and HaHaHaHaHa.  (Ha){3,} searchs for three or more Ha.  (Ha){0,6} searches for zero to six instances of Ha.  (Ha)(Ha)(Ha) is the same as (Ha){3}.  (Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)(Ha) is the same as (Ha){3,5}.
curlybarcketsrepetitions = re.compile(r"(Bat(wo)){1,3}")
findbatwoman = curlybarcketsrepetitions.search("The Adventures of Batwoman")
print(findbatwoman.group()) #print Batwo
findbatwowos = curlybarcketsrepetitions.search("The Adventures of Batwowowowoman")
print(findbatwowos.group()) #print Batwo
findbatmanbatwoman = curlybarcketsrepetitions.search("The Adventures of Batman and Batwowoman")
print(findbatmanbatwoman.group()) #print Batwo
curlybarcketsrepetitions = re.compile(r"Bat(wo){1,3}man")
findbatwoman = curlybarcketsrepetitions.search("The Adventures of Batwoman")
print(findbatwoman.group()) #print Batwoman
findbatwowos = curlybarcketsrepetitions.search("The Adventures of Batwowowoman")
print(findbatwowos.group()) #print Batwowowoman
findbatmanbatwoman = curlybarcketsrepetitions.search("The Adventures of Batman and Batwoman")
print(findbatmanbatwoman.groups()) #print ('wo',)
#findall() method returns a string of every match in a list.  group() and groups() methods return AttributeError.
phonenumberregex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phonenumbermessage = "My phone numbers grouped are Cell:  415-555-9999 and Work:  212-555-0000 and Home:  408-222-7777"
findmultiplephonenumbers = phonenumberregex.findall(phonenumbermessage)
print(findmultiplephonenumbers) #print ['415-555-9999', '212-555-0000', '408-222-7777']
phonenumberregexgrouping = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
phonenumbermessage = "My phone numbers grouped are Cell:  415-555-9999 and Work:  212-555-0000 and Home:  408-222-7777"
findmultiplephonenumbers = phonenumberregexgrouping.findall(phonenumbermessage)
print(findmultiplephonenumbers) #print [('415', '555-9999'), ('212', '555-0000'), ('408', '222-7777')]
pipecharacteror = re.compile(r"Batman|Batwoman")
findbatmanbatwoman = pipecharacteror.findall("The Adventures of Batman and Batwoman with more Batwoman and Batman")
print(findbatmanbatwoman) #print ['Batman', 'Batwoman', 'Batwoman', 'Batman']
#The sub() method substitutes next text in place of the patterns.  Replace text in search results.
#The sub() function replaces occurrences of the regular expression pattern in the string with the repl string.  re.sub(pattern, repl, string, max=0).
replaceagentname = re.compile(r"Agent \w+")
originalagentstring = "Agent Alice gave the secret documents to Agent Bob."
print(originalagentstring) #print Agent Alice gave the secret documents to Agent Bob.
print(replaceagentname.sub("replaceAgentwithCENSORED", originalagentstring)) #print replaceAgentwithCENSORED gave the secret documents to replaceAgentwithCENSORED.
partialreplacenamefirstgroup = re.compile(r"Agent (\w)\w*") #first group is in parenthesis
originalagentstring = "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.  Agent longassnamereplacewithasterisk."
print(originalagentstring) #print Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.  Agent longassnamereplacewithasterisk.
print(partialreplacenamefirstgroup.sub(r"\1*****", originalagentstring)) #print A***** told C***** that E***** knew B***** was a double agent.  l*****. #RM:  I'm guessing the \1 is for the group(\w) to replace name with *****.
europeansports = "England for football, Wales for Rugby, and Scotland for the Highland games."
replacecountriescompile = re.compile(r"England|Wales|Scotland")
replacecountriesstring = "Replace the countries"
print(re.sub(replacecountriescompile, replacecountriesstring, europeansports)) #print Replace the countries for football, Replace the countries for Rugby, and Replace the countries for the Highland games.
replacefirstansecond = re.sub(replacecountriescompile, replacecountriesstring, europeansports, 2)
print(replacefirstansecond) #print Replace the countries for football, Replace the countries for Rugby, and Scotland for the Highland games.
replaceresulttuplesnumberreplaced = re.subn(replacecountriescompile, replacecountriesstring, europeansports)
print(replaceresulttuplesnumberreplaced) #print ('Replace the countries for football, Replace the countries for Rugby, and Replace the countries for the Highland games.', 3)

#Grouping and re.search no re.compile no compiling
nameemailaddress = "Charlie Cyan, e-mail:  demo1@deitel.com"
patternFirstnameLastnameonly = r"([A-Z][a-z]+ [A-Z][a-z]+)"
print(re.search(patternFirstnameLastnameonly, nameemailaddress)) #print <re.Match object; span=(0, 12), match='Charlie Cyan'>
print(type(re.search(patternFirstnameLastnameonly, nameemailaddress))) #print <class 're.Match'>
print(re.search(patternFirstnameLastnameonly, nameemailaddress).groups()) #print ('Charlie Cyan',)
print(re.search(patternFirstnameLastnameonly, nameemailaddress).groups()[0]) #print Charlie Cyan
print(re.search(patternFirstnameLastnameonly, nameemailaddress).group(1)) #print Charlie Cyan
matchasobject = re.search(patternFirstnameLastnameonly, nameemailaddress)
print(matchasobject) #print <re.Match object; span=(0, 12), match='Charlie Cyan'>
print(matchasobject.groups()) #print ('Charlie Cyan',)
print(matchasobject.groups()[0]) #print Charlie Cyan
patternFirstnameLastnameemail = r"([A-Z][a-z]+ [A-Z][a-z]+), e-mail:  (\w+[@]\w+[.]\w{3})"
print(re.search(patternFirstnameLastnameemail, nameemailaddress))
print(re.search(patternFirstnameLastnameemail, nameemailaddress).groups())
print(re.search(patternFirstnameLastnameemail, nameemailaddress).groups()[1]) #print demo1@deitel.com
print(re.search(patternFirstnameLastnameemail, nameemailaddress).group(2)) #print demo1@deitel.com
fullnamephonenumber = "Mylastname-hyphenated, Mymiddlename, Myfirstname: (650)-555-1298"
assigngroupnamescompileobject = re.compile(r"(?P<last>[-a-zA-Z]+), (?P<middle>[-a-zA-Z]+), (?P<first>[-a-zA-Z]+): (?P<phone>([(]\d{3}[)]-\d{3}-\d{4}))") #Last name, comma, space, middle name, comma, space, first name, colon, space, phone number with area code.  The plus sign + finds one or more custom character class
# assigngroupnamescompileobject = re.compile(r"(?P<last>[-a-zA-Z]+), ((?P<middle>[-a-zA-Z]+),)? (?P<first>[-a-zA-Z]+): (?P<phone>([(]\d{3}[)]-)?\d{3}-\d{4}") #Last name, comma, space, first name, space, middle name optional, colon, space, phone number for which area code optional.  Optional explanation is question mark ? finds zero or one custom character class.  The plus sign + finds one or more custom character class
compilesearchobject = assigngroupnamescompileobject.search(fullnamephonenumber)
print(compilesearchobject.group("last")) #print Mylastname-hyphenated
print(compilesearchobject.group("middle")) #print Mymiddlename
print(compilesearchobject.group("first")) #print Myfirstname
print(compilesearchobject.group("phone")) #print (650)-555-1298
partialfullnamephonenumber = "Mylastname-hyphenated, Myfirstnamenomiddlename: (650)-555-1298"
assigngroupnamescompileobjectoptionals = re.compile(r"(?P<last>[-a-zA-Z]+),((?P<middle>[-a-zA-Z]+,))? (?P<first>[-a-zA-Z]+): (?P<phone>(([(]\d{3}[)])?-\d{3}-\d{4}))") #Last name, comma, space, middle name optional, comma, space, first name, colon, space, phone number with area code optional.  Optional explanation is question mark ? finds zero or one custom character class.  The plus sign + finds one or more custom character class
compilesearchobject = assigngroupnamescompileobjectoptionals.search(partialfullnamephonenumber)
print(compilesearchobject.group("last")) #print Mylastname-hyphenated
if compilesearchobject.group("middle") == None:
    print("No middle name") #print No middle name
else:
    print(compilesearchobject.group("middle"))
print(compilesearchobject.group("first")) #print Myfirstnamenomiddlename
print(compilesearchobject.group("phone")) #print (650)-555-1298
partialfullnamepartialphonenumber = "Mylastname-hyphenated, Myfirstnamenomiddlename: 555-1298"
assigngroupnamescompileobjectoptionals = re.compile(r"(?P<last>[-a-zA-Z]+),((?P<middle>[-a-zA-Z]+,))? (?P<first>[-a-zA-Z]+): (?P<phone>(([(]\d{3}[)]-)?\d{3}-\d{4}))") #Last name, comma, space, middle name optional, comma, space, first name, colon, space, phone number with area code optional.  Optional explanation is question mark ? finds zero or one custom character class.  The plus sign + finds one or more custom character class
compilesearchobject = assigngroupnamescompileobjectoptionals.search(partialfullnamepartialphonenumber)
print(compilesearchobject.group("last")) #print Mylastname-hyphenated
if compilesearchobject.group("middle") == None:
    print("No middle name") #print No middle name
else:
    print(compilesearchobject.group("middle"))
print(compilesearchobject.group("first")) #print Myfirstnamenomiddlename
print(compilesearchobject.group("phone")) #print 555-1298
integerstring = "1 2 3 4 5"
def convertintegertofloatfunction(matchobject):
    return (matchobject.group("numberlabel") + ".0")


searchpattern = r"(?P<numberlabel>[0-9]+)" #Looks for a number consisting of one or more digits.  Give each name the group name numberlabel.
regexpsearchintegerinstring = re.compile(searchpattern)
print(regexpsearchintegerinstring.sub(convertintegertofloatfunction, integerstring)) #print 1.0 2.0 3.0 4.0 5.0.  Take integerstring matching the searchpattern to the function convertintegertofloatfunction.  The function uses group to extract the matching substring from the match object matchobject to produce a new string concatenate with .0.  sub returns the new string.

#A regex object's search() method searches the string it is passed for matches.  The search() method returns None if the regex pattern is not found in the string.  If the pattern is found, the search() method returns a Match object.  Match objects have a group() method which returns the actual matched text from the searched string.
phonenumberregex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phonenumbermessage = "Use \\d's to find digits or numbers and hyphens 415-555-4242"
findphonenumber = phonenumberregex.search(phonenumbermessage)
print(findphonenumber) #print <re.Match object; span=(47, 59), match='415-555-4242'>
print("Phone number found? " + findphonenumber.group()) #print Phone number found? 415-555-4242
try:
    print("Use try except to print phone number found " + findphonenumber.group()) #print Use try except to print phone number found 415-555-4242
except AttributeError:
    print("Phone number not found")
nophonenumbermessage = "Use \\d's to find digits or numbers and hyphens 41-555-4242."
findphonenumber = phonenumberregex.search(nophonenumbermessage)
print(findphonenumber) #print None
#print("Phone number found? " + findphonenumber.group()) #print AttributeError: 'NoneType' object has no attribute 'group'
try:
    print("Use try except to print phone number found " + nophonenumbermessage.group()) #print Use try except to print phone number found 415-555-4242
except AttributeError:
    print("Phone number not found") #print Phone number not found

#re.sub function replaces patterns in a string.  re.sub replaces all occurrrences by default.  Set count=number to specify the maximum number of replacements.
numberstabed = "1\t2\t3\t4"
print(numberstabed) #print 1    2   3   4
print(re.sub(r"\t", ", ", numberstabed)) #print 1, 2, 3, 4.  Replace tab with comma and a space.
print(numberstabed) #print 1    2   3   4
print(re.sub(r"\t", ", ", numberstabed, count=2)) #print 1, 2, 3    4.  Replace tab with comma and a space two times.
#re.split function separates a string to list with a delimiter.  The examples separates each string by a comma and its whitespaces to a list.  Set maxsplit=number to specify the maximum number of splits.
#The split() function returns a list where the string is split at each match.  re.split(pattern, string, maxsplit=0,flags=0).
#\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
#Question mark ? matches zero or one occurrence.  Asterik * matches zero or more occurrences.  Plus sign + matches one or more occurrences
numberswhitespaces = "1, 2, 3,4, 5,6,       7,8"
print(re.split(r",\s?", numberswhitespaces)) #print ['1', '2', '3', '4', '5', '6', '      7', '8'].  RM:  notice the comma before the \s.  Split by comma.
print(re.split(r",\s*", numberswhitespaces)) #print ['1', '2', '3', '4', '5', '6', '7', '8']
print(re.split(r",\s+", numberswhitespaces)) #print ['1', '2', '3,4', '5,6', '7,8']
print(re.split(r",\s*", numberswhitespaces, maxsplit=3)) #print ['1', '2', '3', '4, 5,6,       7,8']
hotstring = "It was a hot summer hot night"
splitathot = re.compile(r"hot")
print(re.split(splitathot, hotstring)) #print ['It was a ', ' summer ', ' night']
splitathotnospaces = re.compile(r" hot ")
print(re.split(splitathotnospaces, hotstring)) #print ['It was a', 'summer', 'night']
#re.finditer function finds every matching substring in a string and returns one match substrings at a time
contact = "Wally White, Home:  555-555-1234, Work:  555-555-4321"
print(re.findall(r"\d{3}-\d{3}-\d{4}", contact)) #print ['555-555-1234', '555-555-4321']
for phonenumbers in re.finditer(r"\d{3}-\d{3}-\d{4}", contact):
    print(phonenumbers.group())
    '''
    555-555-1234
    555-555-4321
    '''
#re.VERBOSE is used to write comments in regular expressions.  re.compile() takes only a single value as its second argument.  Use the pipe character | which is called a bitwise or operator.
multiplesecondarguments = re.compile(r"something", re.IGNORECASE | re.DOTALL)
multiplesecondarguments = re.compile(r"something", re.IGNORECASE | re.DOTALL | re.VERBOSE)
