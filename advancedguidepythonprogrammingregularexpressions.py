#Advanced Guide To Python 3 Programming by John Hunt Chapter 22 Regular Expressions In Python
#Regex or re is a sequence of characters such as letters, numbers, and special characters forming a pttern to search text, text files, CSV files, and Excel files.  Search for the text containing sequences of characters which match the pattern.  Use the built-in module re.  There are additional third party modules supporting regular expressions.
import re
truestring = "Hello \n World"
print(truestring)
'''
Hello 
 World
'''
rawstring = r"Hello \n World"
print(rawstring) #print Hello \n World
starwarsmusic = "john williams"
searchpatternbigjorlittlej = "[Jj]ohn"
print(re.search(searchpatternbigjorlittlej, starwarsmusic)) #print <re.Match object; span=(0, 4), match='john'>
searchfunction = re.search(searchpatternbigjorlittlej, starwarsmusic)
print(searchfunction) #print <re.Match object; span=(0, 4), match='john'>
if re.search(searchpatternbigjorlittlej, starwarsmusic):
    print("Found match") #print Found match
#The search() function searches the string for a match.  It returns a Match object if there is a match.  The signature of the function is re.search(pattern, string, flags=0).  pattern is the regular expression used in the matching process, string is the string to be searched, flags are optional flags to modify the search operation.
pricestring = "The price is 23.55"
containintegers = r"\d+"
if re.search(containintegers, pricestring):
    print("Contains integers") #print Contains integers
selectmusician = "Play some Adele"
musiciansor = r"Beatles|Adele|Gorillaz"
if re.search(musiciansor, selectmusician, flags=0):
    print("Musician found.  Playing now.") #print Musician found.  Playing now.
selectmusiciancaseinsensitive = "Play some adele"
musiciansorcaseinsensitive = r"Beatles|Adele|Gorillaz"
if re.search(musiciansorcaseinsensitive, selectmusiciancaseinsensitive, flags=2):
    print("Musician found.  Playing now.  Case insensitive worked?  flags=2") #print Musician found.  Playing now.  Case insensitive worked?  flags=2
#The match() function searches the beginning of a string for a match.  match() function works the same as search() function.  match() function checks at the beginning of the string.  search() function checks anywhere in the string.
#The findall() function returns a list of containing all matches.  re.findall(pattern, string, flags=0).  The string is scanned from left to right.  Matches are returned in the order found.
searchstring = "The rain in Spain stays mainly on the plain"
resultslist = re.findall("[a-zA-Z]{2}ai.", searchstring) #Look for a substring with two letters ending with ai and a single character.
print(resultslist) #print ['Spain', 'plain']
#The split() function returns a list where the string is split at each match.  RM:  split() is a basic Python.  re.split(pattern, string, maxsplit=0,flags=0).
searchstring = "It was a hot summer night"
splitatspace = r"\s" #\s returns a match where the string contains a white space character.  \S returns a match where the string doesn't contain a white space character
splitsearchstring = re.split(splitatspace, searchstring)
print(splitsearchstring) #print ['It', 'was', 'a', 'hot', 'summer', 'night']
#The sub() function replaces occurrences of the regular expression pattern in the string with the repl string.  re.sub(pattern, repl, string, max=0).
searchpattern = "(England|Wales|Scotland)"
inputstring = "England for football, Wales for Rugby, and Scotland for the Highland games."
replacefinal = re.sub(searchpattern, "Replacement here all England", inputstring)
print(replacefinal) #print Replacement here all England for football, Replacement here all England for Rugby, and Replacement here all England for the Highland games.
replacefirsttwofinal = re.sub(searchpattern, "Replacement here all England", inputstring, 2)
print(replacefirsttwofinal) #print Replacement here all England for football, Replacement here all England for Rugby, and Scotland for the Highland games.
replacecountfinal = re.subn(searchpattern, "Tuple Replacement here all England and count replacements", inputstring)
print(replacecountfinal) #print ('Tuple Replacement here all England and count replacements for football, Tuple Replacement here all England and count replacements for Rugby, and Tuple Replacement here all England and count replacements for the Highland games.', 3)
print("\n")
#The compile() function compiles a regular expression pattern into a regular expression object.  The regular expression object can be used for other methods such as match() and search().  re.compile(pattern, flags=0).  The compiled regular expression objects methods and attributes are different than their function counterparts.
searchpattern = "(England|Wales|Scotland)"
inputstring = "England for football, Wales for Rugby, and Scotland for the Highland games."
repattern = re.compile(searchpattern)
replacefinal = repattern.sub("Replacement here all England", inputstring)
print(replacefinal) #print Replacement here all England for football, Replacement here all England for Rugby, and Replacement here all England for the Highland games.
splitstring = repattern.split(inputstring)
print(splitstring) #print ['', 'England', ' for football, ', 'Wales', ' for Rugby, and ', 'Scotland', ' for the Highland games.'].  RM:  correct split.  Split by England, Wales, or Scotland.
searchstring = repattern.search(inputstring)
print(searchstring) #print <re.Match object; span=(0, 7), match='England'>
searchstring = repattern.search(inputstring)
print(searchstring[0]) #print England
searchstring = repattern.search(inputstring)
print(searchstring[1]) #print England
searchstring = repattern.search(inputstring, 1, 50)
print(searchstring) #print <re.Match object; span=(22, 27), match='Wales'>
searchstring = repattern.search(inputstring, 1, 50)
print(type(searchstring)) #print <class 're.Match'>
searchstring = repattern.search(inputstring, 1, 50)
print(searchstring[1]) #print Wales
searchstring = repattern.search(inputstring, 1, 50)
print(searchstring[0]) #print Wales
