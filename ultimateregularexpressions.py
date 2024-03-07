#Regular expressions specify a pattern of text to search.  Regular expressions, or regexes for short, are descriptions for a pattern of text.  For example, a \d in regex stands for a digit character from 0 to 9.  Regex \d\d\d-\d\d\d-\d\d\d\d is a phone number string of three numbers, a hyphen, three numbers, a hyphen, and four numbers.  Any other string doesn't match regex \d\d\d-\d\d\d-\d\d\d\d.
import re

matchfivestringnumbers = "02215"
print(re.fullmatch(matchfivestringnumbers, "02215")) #print <re.Match object; span=(0, 5), match='02215'>
print(re.fullmatch(matchfivestringnumbers, "02215") is True) #print False
print(re.fullmatch(matchfivestringnumbers, "02215") == True) #print False
if re.fullmatch(matchfivestringnumbers, "02215"):
    print("True") #print True
print(re.fullmatch(matchfivestringnumbers, "13329")) #print None

#Four steps using Python regular expression summarized:  1 import regex module import re.  2 Create a regex object with the re.compile() function.  Use a raw string.  3 Pass the string to search using the search() method.  It returns a Match object first matched text.  4 Call the Match object's group() method to return a string of the actual matched text.  groups() method can work.
#search() method returns a Match object first matched text.  findall() method returns a string of every match in a list.
vowelleters = re.compile(r"[aeiouAEIOU]")
stringsentence = "RoboCop eats baby food.  BABY FOOD."
extractvowels = vowelleters.findall(stringsentence)
print(extractvowels) #print ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
#Use the caret character before defining the character class as the negative or not
consonantletters = re.compile(r"[^aeiouAEIOU]")
extractconsonants = consonantletters.findall(stringsentence)
print(extractconsonants) #print ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
lettersnumbersranges = re.compile(r"[M-Za-f4-7]")
stringsentence = "RoboCop eats baby food.  4 9 1 BABY FOOD."
extractselectedrangelettersnumbers = lettersnumbersranges.findall(stringsentence)
print(extractselectedrangelettersnumbers) #print ['R', 'b', 'e', 'a', 'b', 'a', 'b', 'f', 'd', '4', 'Y', 'O', 'O']
lettersnumbersranges = re.compile(r"[M-Za-f4-7 ]")
stringsentence = "RoboCop eats baby food.  4 9 1 BABY FOOD."
extractselectedrangelettersnumbersplusspaces = lettersnumbersranges.findall(stringsentence)
print(extractselectedrangelettersnumbersplusspaces) #print ['R', 'b', ' ', 'e', 'a', ' ', 'b', 'a', 'b', ' ', 'f', 'd', ' ', ' ', '4', ' ', ' ', ' ', 'Y', ' ', 'O', 'O']
mustbeginwithcaret = re.compile(r"^Begins with hello")
stringsentence = "Begins with hello world ends with goodbye."
extractstartswith = mustbeginwithcaret.search(stringsentence)
print(extractstartswith) #print <re.Match object; span=(0, 17), match='Begins with hello'>
print(extractstartswith.group()) #print Begins with hello
extractstartswith = mustbeginwithcaret.findall(stringsentence)
print(extractstartswith) #print ['Begins with hello']
mustendswithdollarsign = re.compile(r"ends with goodbye\.$")
extractendswith = mustendswithdollarsign.search(stringsentence).group()
print(extractendswith) #print ends with goodbye.
#The period match any character except for a new line.  Match a single character.
singlecharacterwildcard = re.compile(r".at")
findmultipleswithat = "The cat in the hat sat on the flat mat."
#print(singlecharacterwildcard.find(findmultipleswithat)) #print AttributeError: 're.Pattern' object has no attribute 'find'
print(singlecharacterwildcard.findall(findmultipleswithat)) #print ['cat', 'hat', 'sat', 'lat', 'mat']
print(singlecharacterwildcard.search(findmultipleswithat)) #print <re.Match object; span=(4, 7), match='cat'>
print(singlecharacterwildcard.search(findmultipleswithat).group()) #print cat
#The period match any single character except the new line and the asterisk matches zero or more of the character.  Need the period in front of the asterisk or error message appears.  The period asterisk default matches as much text as possible.
findmultiplesat = re.compile(r".*at")
print(findmultiplesat.findall(findmultipleswithat)) #print ['The cat in the hat sat on the flat mat']
#findmultiplesatnoperiod = re.compile(r"*at") #return re.error: nothing to repeat at position 0
#print(findmultiplesatnoperiod.findall(findmultipleswithat)) #print re.error: nothing to repeat at position 0
multiplecharacterswildcardbefore = re.compile(r".*jake")
findjake = "The snake begins with jake from Florida."
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
firstnamelastnameingroups = re.compile(r"First Name: (.*) Last Name: (.*)")
firstnamelastname1 = "First Name: Al Last Name: Sweigart"
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
firstnamelastnamegreedy = re.compile(r"First Name: .*? Last Name: .*?")
firstnamelastname1 = "First Name: Al Last Name: Sweigart"
extractnamessearchobject = firstnamelastnamegreedy.search(firstnamelastname1)
print(extractnamessearchobject) #print <re.Match object; span=(0, 26), match='First Name: Al Last Name: '>
print(extractnamessearchobject.group()) #print First Name: Al Last Name:
print(extractnamessearchobject.groups()) #print ()
firstnamelastnamegreedy = re.compile(r"First Name: .*?.* Last Name: .*?.*")
firstnamelastname1 = "First Name: Al Last Name: Sweigart"
extractnamessearchobject = firstnamelastnamegreedy.search(firstnamelastname1)
print(extractnamessearchobject) #print <re.Match object; span=(0, 34), match='First Name: Al Last Name: Sweigart'>
print(extractnamessearchobject.group()) #print First Name: Al Last Name: Sweigart
print(firstnamelastnamegreedy.findall(firstnamelastname1)) #print ['First Name: Al Last Name: Sweigart']
firstnamelastnamegreedy = re.compile(r"First Name: .*?.* Last Name: .*?.*")
firstnameslastnames1 = "First Name: Al Moose Last Name: Sweigart Booth"
extractnamessearchobject = firstnamelastnamegreedy.search(firstnameslastnames1)
print(extractnamessearchobject) #print <re.Match object; span=(0, 46), match='First Name: Al Moose Last Name: Sweigart Booth'>
print(extractnamessearchobject.group()) #print First Name: Al Moose Last Name: Sweigart Booth
print(firstnamelastnamegreedy.findall(firstnameslastnames1)) #print ['First Name: Al Moose Last Name: Sweigart Booth']
firstnamelastnamegreedycarrots = re.compile(r"First Name: <.*?> Last Name: <.*?>")
firstnameslastnamescarrots = "First Name: <Al Moose> Last Name: <Sweigart Booth>"
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
nonewline = re.compile(".*")
multiplelinestring = "One run.\n  Two shoes.\n  Three trees.\n"
print(nonewline.search(multiplelinestring)) #print <re.Match object; span=(0, 8), match='One run.'>
extractmultiplelinestringobject = nonewline.search(multiplelinestring)
print(extractmultiplelinestringobject.group()) #print One run.
print(extractmultiplelinestringobject.groups()) #print ()
yesnewline = re.compile(".*", re.DOTALL)
multiplelinestring = "One run.\n  Two shoes.\n  Three trees.\n"
print(yesnewline.search(multiplelinestring)) #print <re.Match object; span=(0, 37), match='One run.\n  Two shoes.\n  Three trees.\n'>
extractmultiplelinestringobject = yesnewline.search(multiplelinestring)
print(extractmultiplelinestringobject.group()) #print One run.  Two shoes.  Three trees.
print(extractmultiplelinestringobject.groups()) #print ()
#Include re.IGNORECASE or re.I as a second argument to re.compile() to search no exact casing
caseinsensitive = re.compile(r"seuss", re.I)
drseussstring = "Author Dr. Seuss wrote children's books for the World whole."
print(caseinsensitive.search(drseussstring)) #print <re.Match object; span=(11, 16), match='Seuss'>
extractseussobject = caseinsensitive.search(drseussstring)
print(extractseussobject.group()) #print Seuss
#Character classes.  RM:  ignore the backslash escape character
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
matchfivestringnumberscompile = re.compile(r"\d{5}")
print(matchfivestringnumberscompile.findall(matchfivestringnumbers)) #print ['02215']

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
replaceagentname = re.compile(r"Agent \w+")
originalagentstring = "Agent Alice gave the secret documents to Agent Bob."
print(originalagentstring) #print Agent Alice gave the secret documents to Agent Bob.
print(replaceagentname.sub("replaceAgentwithCENSORED", originalagentstring)) #print replaceAgentwithCENSORED gave the secret documents to replaceAgentwithCENSORED.
partialreplacenamefirstgroup = re.compile(r"Agent (\w)\w*") #first group is in parenthesis
originalagentstring = "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.  Agent longassnamereplacewithasterisk."
print(originalagentstring) #print Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.  Agent longassnamereplacewithasterisk.
print(partialreplacenamefirstgroup.sub(r"\1*****", originalagentstring)) #print A***** told C***** that E***** knew B***** was a double agent.  l*****. #RM:  I'm guessing the \1 is for the group(\w) to replace name with *****.

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

#re.VERBOSE is used to write comments in regular expressions.  re.compile() takes only a single value as its second argument.  Use the pipe character | which is called a bitwise or operator.
multiplesecondarguments = re.compile(r"something", re.IGNORECASE | re.DOTALL)
multiplesecondarguments = re.compile(r"something", re.IGNORECASE | re.DOTALL | re.VERBOSE)
