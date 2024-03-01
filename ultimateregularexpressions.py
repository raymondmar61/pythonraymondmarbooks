#Regular expressions specify a pattern of text to search.  Regular expressions, or regexes for short, are descriptions for a pattern of text.  For example, a \d in regex stands for a digit character from 0 to 9.  Regex \d\d\d-\d\d\d-\d\d\d\d is a phone number string of three numbers, a hyphen, three numbers, a hyphen, and four numbers.  Any other string doesn't match regex \d\d\d-\d\d\d-\d\d\d\d.
import re

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
#Character classes.  RM:  ignore the backslash escape character
'''
\\d Any numeric digit from 0 to 9.
\\D Any character that is not a numeric digit from 0 to 9.
\\w Any letter, numeric digit, or the underscore character.  (Think of this as matching “word” characters.)
\\W Any character that is not a letter, numeric digit, or the underscore character.
\\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
\\S Any character that is not a space, tab, or newline.
'''
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
