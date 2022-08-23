#Automate The Boring Stuff With Python By Al Sweigart Chapter 07 Pattern Matching With Regular Expressions
#Regular expressions specify a pattern of text to search.  Regular expressions, or regexes for short, are descriptions for a pattern of text.  For example, a \d in regex stands for a digit character from 0 to 9.  Regex \d\d\d-\d\d\d-\d\d\d\d is a phone number string of three numbers, a hyphen, three numbers, a hyphen, and four numbers.  Any other string doesn't match regex \d\d\d-\d\d\d-\d\d\d\d.
def checkisphonenumber(text):
    if len(text) != 12: #check text is 12 characters
        return False
    for i in range(0, 3): #check numeric characters
        if not text[i].isdecimal():
            return False
    if text[3] != "-": #check hyphen at the index 3
        return False
    for i in range(4, 7): #check numeric characters
        if not text[i].isdecimal():
            return False
    if text[7] != "-": #check hyphen at the index 7
        return False
    for i in range(8, 12): #check numeric characters
        if not text[i].isdecimal():
            return False
    return True


print(checkisphonenumber('415-555-4242')) #print True
print(checkisphonenumber('Moshi moshi')) #print False

# messagewithtwophonenumbers = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
# for i in range(0, len(messagewithtwophonenumbers)):
#     chunkof12characters = messagewithtwophonenumbers[i:i + 12]
#     if checkisphonenumber(chunkof12characters):
#         print("Phone number found: " + chunkof12characters)
#     else:
#         print("No phone number: " + chunkof12characters)
#     '''
#     No phone number: Call me at 4
#     No phone number: all me at 41
#     No phone number: ll me at 415
#     No phone number: l me at 415-
#     No phone number:  me at 415-5
#     No phone number: me at 415-55
#     No phone number: e at 415-555
#     No phone number:  at 415-555-
#     No phone number: at 415-555-1
#     No phone number: t 415-555-10
#     No phone number:  415-555-101
#     Phone number found: 415-555-1011
#     ...
#     No phone number: 1011 tomorro
#     No phone number: 011 tomorrow
#     No phone number: 11 tomorrow.
#     No phone number: 1 tomorrow.
#     ...
#     Phone number found: 415-555-9999
#     ...
#     No phone number: fice.
#     No phone number: ice.
#     No phone number: ce.
#     No phone number: e.
#     No phone number: .
#     '''
import re
#A regex object's search() method searches the string it is passed for matches.  The search() method returns None if the regex pattern is not found in the string.  If the pattern is found, the search() method returns a Match object.  Match objects have a group() method which returns the actual matched text from the searched string.
phonenumberregex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
message = "My number is 415-555-4242."
findphonenumber = phonenumberregex.search(message)
print("Phone number found? " + findphonenumber.group()) #print Phone number found? 415-555-4242
try:
    print("Phone number found under try except. " + findphonenumber.group()) #print Phone number found under try except. 415-555-4242
except AttributeError:
    print("Phone number not found")

messagenophonenumber = "My number is 41-555-4242."
findphonenumber2 = phonenumberregex.search(messagenophonenumber)
#print("Phone number found? " + findphonenumber2.group()) #print AttributeError: 'NoneType' object has no attribute 'group'
try:
    print("Phone number found? " + findphonenumber2.group()) #AttributeError
except AttributeError:
    print("Phone number not found")
#Four steps using Python regular expression summarized:  1 import regex module import re.  2 Create a regex object with the re.compile() function.  Use a raw string.  3 Pass the string to search using the search() method.  It returns a Match object.  4 Call the Match object's group() method to return a string of the actual matched text.
#Enter the escape character \\ to print a single backslash.  \\n in regexp is a backslash and lowercase letter n.  However, type a letter r before the first quote in the string value makes the string value as a raw string which doesn't use escape characters.
phonenumberregexgrouping = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
message = "My number is 415-555-4242."
findphonenumber = phonenumberregexgrouping.search(message)
print(findphonenumber.group(1)) #print 415
print(findphonenumber.group(2)) #print 555-4242
print(findphonenumber.group(0)) #print 415-555-4242
print(findphonenumber.group()) #print 415-555-4242
print(findphonenumber.groups()) #print ('415', '555-4242')
areacode, mainnumber = findphonenumber.groups()
print(areacode) #print 415
print(mainnumber) #print 555-4242
phonenumberregexgroupingescapecharacter = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
message = "My number is (415) 555-4242."
findphonenumber = phonenumberregexgroupingescapecharacter.search(message)
areacode, mainnumber = findphonenumber.groups()
print(areacode) #print (415)
print(mainnumber) #print 555-4242
pipecharacteror = re.compile(r"Batman|Tina Fey")
searchbatman = pipecharacteror.search("Batman and Tina Fey.")
print(searchbatman.group()) #print Batman
searchtinafey = pipecharacteror.search("Tina Fey and Batman.")
print(searchtinafey.group()) #print Tina Fey
pipecharacteror = re.compile(r"Bat(man|mobile|copter|bat)")
findbatmobile = pipecharacteror.search("Batmobile lost a wheel")
print(findbatmobile.group()) #print Batmobile
print(findbatmobile.group(1)) #print mobile
print(findbatmobile.group(0)) #print Batmobile
findbatcopter = pipecharacteror.search("The bat man flew the Batcopter with wheels")
print(findbatcopter.group()) #print Batcopter
#The question mark ? flags the group to the left of ? as an optional part of the pattern.
questionmarkoptional = re.compile(r"Bat(wo)?man")
findbatman = questionmarkoptional.search("The Adventures Of Batman")
print(findbatman.group()) #print Batman
findbatwoman = questionmarkoptional.search("The Adventures Of Batwoman")
print(findbatwoman.group()) #print Batwoman
phonenumberregexoptionalareacode = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
message = "My number is 555-4242."
findphonenumber = phonenumberregexoptionalareacode.search(message)
print(findphonenumber.group(0)) #print 555-4242
asteriskmatchzeroormore = re.compile(r"Bat(wo)*man")
findbatman = asteriskmatchzeroormore.search("The Adventures of Batman")
print(findbatman.group()) #print Batman.  RM:  (wo)* matched zero instances of wo in the string
findbatwoman = asteriskmatchzeroormore.search("The Adventures of Batwoman")
print(findbatwoman.group()) #print Batwoman
findbatwowos = asteriskmatchzeroormore.search("The Adventures of Batwowowowoman")
print(findbatwowos.group()) #print Batwowowowoman
plusmatchoneormore = re.compile(r"Bat(wo)+man")
findbatwoman = plusmatchoneormore.search("The Adventures of Batwoman")
print(findbatwoman.group()) #print Batwoman
findbatwowos = plusmatchoneormore.search("The Adventures of Batwowowowoman")
print(findbatwowos.group()) #print Batwowowowoman
findbatman = plusmatchoneormore.search("The Adventures of Batman")
try:
    print(findbatman.group())
except AttributeError:
    print("Batwoman not found") #print Batwoman not found
#Use curly brackets for specific repetitions.  If you have a group to repeat a specific number of times, then type the number in curly brackets to the right of the group.  (Ha){3} searchs for HaHaHa.  (Ha){3,5} searchs for HaHaHa, HaHaHaHa, and HaHaHaHaHa.  (Ha){3,} searchs for three or more Ha.  (Ha){,6} searches for zero to six instances of Ha.  (Ha)(Ha)(Ha) is the same as (Ha){3}.  (Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha)(Ha) is the same as (Ha){3,5}.
curlybracketsrepetitions = re.compile(r"(Ha){3}")
hahaha = curlybracketsrepetitions.search("Three HaHaHa in the string")
print(hahaha.group()) #print HaHaHa
greedydefaultlongestpossibility = re.compile(r"(Ha){3,5}")
hahahahaha5 = greedydefaultlongestpossibility.search("HaHaHaHaHa")
print(hahahahaha5.group()) #print HaHaHaHaHa
notgreedydefaultlongestpossibility = re.compile(r"(Ha){3,5}?")
hahahahaha3 = notgreedydefaultlongestpossibility.search("HaHaHaHaHa")
print(hahahahaha3.group()) #print HaHaHa
#search() method returns a Match object first matched text.  findall() method returns a string of every match in a list.
phonenumberregex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
firsttwophonenumbers = phonenumberregex.search("Cell:  415-555-9999 Work:  212-555-0000")
print(firsttwophonenumbers.group())
alltwophonenumbers = phonenumberregex.findall("Cell:  415-555-9999 Work:  212-555-0000")
print(alltwophonenumbers) #print ['415-555-9999', '212-555-0000'].  RM:  there's no alltwophonenumbers.group()
phonenumberregexgrouping = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
alltwophonenumbersgroups = phonenumberregexgrouping.findall("Cell:  415-555-9999 Work:  212-555-0000")
print(alltwophonenumbersgroups) #print [('415', '555-9999'), ('212', '555-0000')]
#Character classes.  RM:  ignore the backslash escape character
'''
\\d Any numeric digit from 0 to 9.
\\D Any character that is not a numeric digit from 0 to 9.
\\w Any letter, numeric digit, or the underscore character.  (Think of this as matching “word” characters.)
\\W Any character that is not a letter, numeric digit, or the underscore character.
\\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
\\S Any character that is not a space, tab, or newline.
'''
xmasregex = re.compile(r"\d+\s\w+") #xmasregex match text with one or more numeric digits \d+, a whitespace character \s, and oneor more letter or digit or underscore characters \w+.
print(xmasregex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge")) #print ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
definecharacterclassfindvowles = re.compile(r"[aeiouAEIOU]")
print(definecharacterclassfindvowles.findall("RoboCop eats baby food.  BABY FOOD.")) #print ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
#Use the caret character before defining the character class as the negative or not
definecharacterclassfindconsonants = re.compile(r"[^aeiouAEIOU ]")
print(definecharacterclassfindconsonants.findall("RoboCop eats baby food.  BABY FOOD.")) #print ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']  #RM:  periods are included.  Spaces are excluded.
definerangelettersnumbers = re.compile(r"[M-Zb-e4-7]")
print(definerangelettersnumbers.findall("RoboCop eats baby food. 4 9 1 BABY FOOD.")) #print ['R', 'b', 'e', 'b', 'b', 'd', '4', 'Y', 'O', 'O']
caretbeginswith = re.compile(r"^Hello")
print(caretbeginswith.search("Hello world!")) #print <re.Match object; span=(0, 5), match='Hello'>
objectvariable = caretbeginswith.search("Hello world!")
print(objectvariable) #print <re.Match object; span=(0, 5), match='Hello'>
print(caretbeginswith.findall("Hello world!")) #print ['Hello']
dollarsignendswith = re.compile(r"\d$")
print(dollarsignendswith.search("Your number is 42")) #print <re.Match object; span=(16, 17), match='2'>
print(dollarsignendswith.findall("Your number is 42")) #print ['2']
dollarsignendswithplus = re.compile(r"\d+$")
print(dollarsignendswithplus.findall("Your number is 42")) #print ['42']
caretbeginswithanddollarendswith = re.compile(r"^\d+$")
print(caretbeginswithanddollarendswith.search("1234567890")) #print <re.Match object; span=(0, 10), match='1234567890'>
print(caretbeginswithanddollarendswith.findall("1234567890")) #print ['1234567890']
print(caretbeginswithanddollarendswith.search("12345xyz67890")) #print None
#The period match any character except for a new line.  Match a single character.
periodwildcard = re.compile(r".at")
print(periodwildcard.findall("The cat in the hat sat on the flat mat.")) #print ['cat', 'hat', 'sat', 'lat', 'mat']
#The period match any single character except the new line and the star matches zero or more of the character
periodstarwildcard = re.compile(r".*at")
print(periodstarwildcard.findall("The cat in the hat sat on the flat mat.")) #print ['The cat in the hat sat on the flat mat']
firstnamelastnameingroups = re.compile(r"First Name: (.*) Last Name: (.*)")
person = firstnamelastnameingroups.search("First Name: Al Last Name: Sweigart")
print(person.group(1)) #print Al
print(person.group(2)) #print Sweigart
firstnamelastname = re.compile(r"First Name: *.* Last Name: *.* ")
person = firstnamelastname.findall("First Name: Al Last Name: Sweigart")
print(person) #print ['First Name: Al Last Name: ']
firstnamelastname = re.compile(r"First Name: *\w* Last Name: *\w* ")
person = firstnamelastname.findall("First Name: Al Last Name: Sweigart")
print(person) #print ['First Name: Al Last Name: ']
#periodstar default is greedy which matches as much text as possible.  Add a question mark for nongreedy which doesn't match as much text
periodstarnotgreedy = re.compile(r"<.*?>")
dinner = periodstarnotgreedy.search("<To serve man> for dinner.>")
print(dinner) #print <re.Match object; span=(0, 14), match='<To serve man>'>
print(dinner.group()) #print <To serve man>
periodstargreedy = re.compile(r"<.*>")
dinner = periodstargreedy.search("<To serve man> for dinner.>")
print(dinner.group()) #print <To serve man> for dinner.>
#periodstar doesn't match a newline.  Include re.DOTALL to match all characters including the newline \n
nonewline = re.compile(".*")
print(nonewline.search("Serve the public trust. \nProtect the innocent. \nUpload the law.").group()) #print Serve the public trust.
yesnewline = re.compile(".*", re.DOTALL)
print(yesnewline.search("Serve the public trust. \nProtect the innocent. \nUpload the law.").group()) #print Serve the public trust.\n Protect the innocent.\n Upload the law.
#Include re.IGNORECASE or re.I as a second argument to re.compile() to search no exact casing
caseinsensitive = re.compile(r"robocop", re.I)
print(caseinsensitive.search("RoboCop is part man, part machine, all copy.").group()) #print RoboCop
#The sub() method substitutes next text in place of the patterns.  Replace text in search results.
replacename = re.compile(r"Agent \w+")
print(replacename.sub("replacewithCENSORED", "Agent Alice gave the secret documents to Agent Bob.")) #print replacewithCENSORED gave the secret documents to replacewithCENSORED.
partialreplacenamefirstgroup = re.compile(r"Agent (\w)\w*") #first group is in parenthesis
print(partialreplacenamefirstgroup.sub(r"\1*****", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.  Agent longassnamereplacewithasterisk.")) #print A***** told C***** that E***** knew B***** was a double agent.  l*****.
#re.VERBOSE is used to write comments in regular expressions.  re.compile() takes only a single value as its second argument.  Use the pipe character | which is called a bitwise or operator.
multiplesecondarguments = re.compile(r"something", re.IGNORECASE | re.DOTALL)
multiplesecondarguments = re.compile(r"something", re.IGNORECASE | re.DOTALL | re.VERBOSE)
