#Python For Programmers by Paul Deitel Chapter 08 Strings:  A Deeper Look
#Introduction To Regular Expressions
#Regular expressions can extract data from unstructured text such as social media posts, phone numbers, email addresses, zip codes, web page addresses, and social security numbers.  In additional, can extract data, web scrape, clean data, and transform data to another format.
import re
#fullmatch checks a string matches the pattern
matchfivestringnumbers = "02215"
if (re.fullmatch(matchfivestringnumbers, "02215")):
    print("Match") #print Match
else:
    print("No Match")
if (re.fullmatch(matchfivestringnumbers, "51220")):
    print("Match")
else:
    print("No Match") #print No Match
#Regular expressions metacharacters are the following:  [] {} () \ * + ^ $ ? . |
#\d is a character class representing a digit from 0 to 9.  A character class is a regular expression escape sequence which matches one character.  {number} is a quantifier.  A quantifier matches more than one character.  \d{5} is \d\d\d\d\d which is match five consecutive digits.
if (re.fullmatch(r"\d{5}", matchfivestringnumbers)): #r is the raw string useful for many backslash escape characters
    print("matchfivestringnumbers variable contains five digits") #print matchfivestringnumbers variable contains five digits
if (re.fullmatch("\\d{5}", matchfivestringnumbers)): #without raw string r
    print("matchfivestringnumbers variable contains five digits") #print matchfivestringnumbers variable contains five digits
if (re.fullmatch(r"\d{5}", "9876")):
    print("matchfivestringnumbers variable contains five digits")
else:
    print("matchfivestringnumbers variable contains not five digits") #print matchfivestringnumbers variable contains not five digits
'''
Common predefined character classes and their matches
\d any digit 0-9
\D any character not a digit
\s any whitespace character such as spaces, tabs, and newlines
\S any character not a whitespace
\w any word character or alphanumeric character which is uppercase letters, lowercase letters, digits, or underscores
\W any not a word character or alphanumeric character
'''
matchtwowords = "ultra combos7"
print(re.fullmatch(r"\w{5}\s\w{7}", matchtwowords)) #print <re.Match object; span=(0, 13), match='ultra combos7'>
if (re.fullmatch(r"\w{5}\s\w{7}", matchtwowords)):
    print("True") #print True
else:
    print("False")
matchwithsemicolon = "red;blue"
if (re.fullmatch(r"\D{3};\w{4}", matchwithsemicolon)):
    print("True semicolon") #print True semicolon
else:
    print("False semicolon")
#Square brackets define a custom character class which matches a single character.  For example [aeiou] matches a lowercase vowel, [A-Z] matches an uppercase letter, [a-z] matches a lowercase letter, and [a-zA-Z] matches any lowercase or uppercase letter
findletter = "r"
if (re.fullmatch(r"[a-zA-Z]", findletter)):
    print("Found any letter") #print Found any letter
findletters = "rR"
if (re.fullmatch(r"[a-zA-Z][a-zA-Z]", findletters)):
    print("Found any letters") #print Found any letters
#Asterik * is the quantifier.  A quantifier matches zero or more occurrences of its subexpression.  For example, [A-Z][a-z]* matches an uppercase letter and zero or more lowercase letters such as Amanda, Bo, or E.
dilbertcharacter = "Wally"
if (re.fullmatch("[A-Z][a-z]*", dilbertcharacter)):
    print("Found multiple lowercase letters after one uppercase letter") #print Found multiple lowercase letters after one uppercase letter
notdilbertcharacter = "eva"
if (re.fullmatch("[A-Z][a-z]*", notdilbertcharacter)):
    print("Found multiple lowercase letters after one uppercase letter")
else:
    print("No found multiple lowercase letters after one uppercase letter") #print No found multiple lowercase letters after one uppercase letter
#Caret ^ is the not symbol.  For example, [^a-z] matches a character not lowercase.
if (re.fullmatch("[^A-Z][a-z]*", notdilbertcharacter)):
    print("The first letter is not uppercase") #print The first letter is not uppercase
#Metacharacters in a custom character class are metacharacters themselves.  For example [*+$] matches asterik * or plus + or dollar $.
if (re.fullmatch("[*+$]", "*")):
    print("Found metacharacter asterik") #print Found metacharacter asterik
if (re.fullmatch("[+$!]", "!")):
    print("Found metacharacter exclamation") #print Found metacharacter exclamation
#Plus sign + to find one or more custom character class
if (re.fullmatch("[A-Z][a-z]+", dilbertcharacter)):
    print("There is one or more lowercase letter")
if (re.fullmatch("[A-Z][a-z]+", notdilbertcharacter)):
    print("There is one or more lowercase letter")
else:
    print("There is zero lowercase letter") #print There is zero lowercase letter
if (re.fullmatch("[A-Z]+[a-z]", "alllowercaseletters")):
    print("There is one or more uppercase letter")
else:
    print("There is zero uppercase letter") #print There is zero uppercase letter
#Question mark ? to find zero or one custom character class
#The labell?ed examples below l? indicates there can be zero or one letter l before the remaining characters ed or zero or one letter l to the left of the question mark
if (re.fullmatch("labell?ed", "labelled")):
    print("Found labell zero or one l before ed") #print Found labell zero or one l before ed
else:
    print("Didn't find labell")
if (re.fullmatch("labell?ed", "labeled")):
    print("Found labell zero or one l before ed") #print Found labell zero or one l before ed
else:
    print("Didn't find labell")
if (re.fullmatch("labell?ed", "labellled")):
    print("Found labell")
else:
    print("Didn't find labell because two or more l before ed") #print Didn't find labell because two or more l before ed
labellexperiment = "labellzed"
if (re.fullmatch("labell?ed", labellexperiment)):
    print("Found labell")
else:
    print("Didn't find labell") #print Didn't find labell.
if (re.fullmatch("Wal?l?y", dilbertcharacter)):
    print("There are at least one l's the two l's spelled in Wally") #print There are at least one l's the two l's spelled in Wally
#Curly brackets {number, } quantifier matches at least number occurrences.  Curly brackets {lowernumberinclusive, uppernumberinclusive} quantifier matches between lowernumber and uppernumber inclusive occurrences.
elevenletters = "dixowixoebr"
if (re.fullmatch(r"\w{11,}", elevenletters)):
    print("There are at least eleven letters") #print There are at least eleven letters
else:
    print("There are ten or fewer letters")
if (re.fullmatch(r"[a-z]{20,}", elevenletters)):
    print("There are at least twenty letters")
else:
    print("There are ninteen or fewer letters") #print There are ninteen or fewer letters
if (re.fullmatch("\\w{9,11}", elevenletters)):
    print("There are between nine and eleven letters inclusive") #print There are between nine and eleven letters inclusive
#re.sub function replaces patterns in a string.  re.sub replaces all occurrrences by default.  Set count=number to specify the maximum number of replacements.
numberstabed = "1\t2\t3\t4"
print(numberstabed) #print 1    2   3   4
print(re.sub(r"\t", ", ", numberstabed)) #print 1, 2, 3, 4.  Replace tab with comma and a space.
print(numberstabed) #print 1    2   3   4
print(re.sub(r"\t", ", ", numberstabed, count=2)) #print 1, 2, 3    4.  Replace tab with comma and a space two times.
#re.split function separates a string to list with a delimiter.  The examples separates each string by a comma and its whitespaces to a list.  Set maxsplit=number to specify the maximum number of splits.
numberswhitespaces = "1, 2, 3,4, 5,6,       7,8"
print(re.split(r",\s?", numberswhitespaces)) #print ['1', '2', '3', '4', '5', '6', '      7', '8']
print(re.split(r",\s*", numberswhitespaces)) #print ['1', '2', '3', '4', '5', '6', '7', '8']
print(re.split(r",\s+", numberswhitespaces)) #print ['1', '2', '3,4', '5,6', '7,8']
print(re.split(r",\s*", numberswhitespaces, maxsplit=3)) #print ['1', '2', '3', '4, 5,6,       7,8']
#search function looks for the first occurrence which matches the regular expression.  It returns a match object of type SRE_Match containing the matching substring.  The match object's group method returns the substring.  Include flags=re.IGNORECASE for case insensitive
firstoccurrenceseach = "Python is fun.  Learn Python okay."
searchresult = re.search("Python", firstoccurrenceseach)
searchresult.group()
if searchresult:
    print("Found Python first occurrence") #print Found Python first occurrence
else:
    print("Didn't find Python first occurrence")
#re.search returns None if the string doesn't match the pattern
# searchresult = re.search("learn", firstoccurrenceseach)
# searchresult.group()
# if searchresult:
#     print("Found fun first occurrence")
# else:
#     print("Didn't find fun first occurrence")
# #print AttributeError: 'NoneType' object has no attribute 'group'
searchresult = re.search("python", firstoccurrenceseach, flags=re.IGNORECASE)
searchresult.group()
if searchresult:
    print("Found python first occurrence") #print Found python first occurrence
else:
    print("Didn't find python first occurrence")
searchresult = re.search("^Python", firstoccurrenceseach)
searchresult.group()
if searchresult:
    print("Found Python at the beginning of the string using caret ^") #print Found Python at the beginning of the string using caret ^
else:
    print("Didn't find Python at the beginning of the string using caret ^")
# searchresult = re.search("^fun", firstoccurrenceseach)
# searchresult.group()
# if searchresult:
#     print("Found fun at the beginning of the string using caret ^")
# else:
#     print("Didn't find fun at the beginning of the string using caret ^")
# #print AttributeError: 'NoneType' object has no attribute 'group'
searchresult = re.search("okay.$", firstoccurrenceseach)
searchresult.group()
if searchresult:
    print("Found okay. at the end of the string using dollar sign $") #print Found okay. at the end of the string using dollar sign $
else:
    print("Didn't find okay. at the end of the string using dollar sign $")
# searchresult = re.search("Python$", firstoccurrenceseach)
# searchresult.group()
# if searchresult:
#     print("Found Python at the end of the string using dollar sign $") #print Found Python at the end of the string using dollar sign $
# else:
#     print("Didn't find Python at the end of the string using dollar sign $")
#AttributeError: 'NoneType' object has no attribute 'group'
#findall function finds every matching substring in a string and returns a list of the match substrings
contact = "Wally White, Home:  555-555-1234, Work:  555-555-4321"
print(re.findall(r"\d{3}-\d{3}-\d{4}", contact)) #print ['555-555-1234', '555-555-4321']
#finditer function finds every matching substring in a string and returns one match substrings at a time
for phonenumbers in re.finditer(r"\d{3}-\d{3}-\d{4}", contact):
    print(phonenumbers.group())
    '''
    555-555-1234
    555-555-4321
    '''
#Use parentheses metacharacter left parentheses ( and right parentheses ) to capture substrings in a match
nameemailaddress = "Charlie Cyan, e-mail:  demo1@deitel.com"
patternname = r"([A-Z][a-z]+ [A-Z][a-z]+)"
print(re.search(patternname, nameemailaddress)) #print <re.Match object; span=(0, 12), match='Charlie Cyan'>
print(type(re.search(patternname, nameemailaddress))) #print <class 're.Match'>
print(re.search(patternname, nameemailaddress).groups()) #print ('Charlie Cyan',)
print(re.search(patternname, nameemailaddress).groups()[0]) #print Charlie Cyan
patternnameemail = r"([A-Z][a-z]+ [A-Z][a-z]+), e-mail:  (\w+@\w+[.]\w{3})"
print(re.search(patternnameemail, nameemailaddress).groups()) #print ('Charlie Cyan', 'demo1@deitel.com')
print(re.search(patternnameemail, nameemailaddress).group(2)) #print demo1@deitel.com
