#The Quick Python Book by Naomi Ceder Chapter 15 Classes And Object Oriented Programming
#A class is a data type.  All the data types are classes.  Python gives powerful tools to manipulate every class behavior.  Define class with the class statement class Classname: body.  The body is a list of Python statements which are variable assignments and function definitions.  No assignments or function definitions are required.  The body can be a single pass statement.  Class identifiers are in CapCase which means the first letter of each component word is capitalized.  Create a new object of the class type which is an instance by calling the class name as a function.  The new object or instance is defined after the class is created.  For example, instancename = MyClassName().
#The field of an instance or structure are accessed and assigned by dot notation.
class Circle:
    pass


circleinstance1 = Circle()
circleinstance1.radius = 5
print(2 * 3.14 * circleinstance1.radius) #print 31.400000000000002
circleinstance2 = Circle()
circleinstance2.radius = 17
print(2 * 3.14 * circleinstance2.radius) #print 106.76
#Initialize fields of an instance automatically using an __init__ initialization method.  The function is run every time an instance of the class is created.  The new instance first agument is self.  Python classes may only have one __init__ method.
#radius is an instance variable.  Each instance has its own copy of radius.  The value stored in the copy may be different from the values stored in the radius variable in other instances.  Create an instance variable by assigning to a field of a class instance instance.variable = value.  For example overrideselfradius.radius = 6.
#All instance variables require explicit mention of the containing instance which is instance.variable.
#Define another method which is user defined methods.  Call the user defined methods with a method invocation syntax consisting of the instance name and period and method name to be invoked; for example, areaofacircleinstance.area() for which area() is the method name.
class CircleRadius1:
    def __init__(self):
        self.radius = 1


circleinstanceradius1 = CircleRadius1()
print(2 * 3.14 * circleinstanceradius1.radius) #print 6.28
overrideselfradius = CircleRadius1()
overrideselfradius.radius = 6 #override the self.radius field
print(2 * 3.14 * overrideselfradius.radius) #print 37.68
#A method is a function associated with a particular class.  __init__ is a method.
class CircleArea:
    def __init__(self):
        self.radius = 1
    def area(self):
        return self.radius * self.radius * 3.14159


areaofacircleinstance = CircleArea()
areaofacircleinstance.radius = 10
print(areaofacircleinstance.area()) #print 314.159
#Methods can be invoked with arguments if the method definitions accept arguments.
class CircleUserDefineRadius:
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14159


userinputradiusinstance = CircleUserDefineRadius(8)
print(userinputradiusinstance.area()) #print 201.06176
defaultinputradiusinstance = CircleUserDefineRadius()
print(defaultinputradiusinstance.area()) #print 3.14159
#A class variable is a variable associated with a class.  A class variable is not an instance of a class.  A class variable is accessible by all instances of the class.
class CircleClassVariable:
    piclassvariable = 3.14159
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * CircleClassVariable.piclassvariable


print(CircleClassVariable.piclassvariable) #print 3.14159
CircleClassVariable.piclassvariable = 1011
print(CircleClassVariable.piclassvariable) #print 1011
classvariableinstance1 = CircleClassVariable(9)
print(classvariableinstance1.area()) #print 81891.  9*9*1011=81891
CircleClassVariable.piclassvariable = 3.14159
print(CircleClassVariable.piclassvariable) #print 3.14159
classvariableinstance1 = CircleClassVariable(9)
print(classvariableinstance1.area()) #print 254.46878999999998
print(CircleClassVariable) #print <class '__main__.CircleClassVariable'>
print(classvariableinstance1.__class__) #print <class '__main__.CircleClassVariable'>
print(classvariableinstance1.__class__.piclassvariable) #print 3.14159
print(classvariableinstance1.piclassvariable) #print 3.14159
class CircleTotalAreas:
    """Class description here"""
    allcircleslist = [] #Class variable containing list of all circles created
    piclassvariable = 3.14159
    def __init__(self, radius=1):
        """Create a circle with the given radius"""
        self.radius = radius
        self.__class__.allcircleslist.append(self) #Adds instance to the allcircleslist
    def area(self):
        """Calculate area of a circle"""
        return self.__class__.piclassvariable * self.radius * self.radius
    def printallcircleslist(self):
        # return self.__class__.allcircleslist
        return self.allcircleslist
    @staticmethod
    def addtotalareas():
        """Static method add all circle areas calculated"""
        total = 0
        for eachareacircle in CircleTotalAreas.allcircleslist:
            total = total + eachareacircle.area()
        return total


print(CircleTotalAreas.__doc__) #print Class description here
print(CircleTotalAreas.area.__doc__) #print Calculate area of a circle
print(CircleTotalAreas.addtotalareas.__doc__) #print Static method add all circle areas calculated
instanceradius1 = CircleTotalAreas()
print(instanceradius1.area()) #print 3.14159
print(instanceradius1.printallcircleslist()) #print [<__main__.CircleTotalAreas object at 0x7f08572eb880>]
print(instanceradius1.allcircleslist) #print [<__main__.CircleTotalAreas object at 0x7f08572eb880>]
print(instanceradius1.addtotalareas) #print <function CircleTotalAreas.addtotalareas at 0x7f6cf5c00430>
print(instanceradius1.addtotalareas()) #print 3.14159
instanceradius2 = CircleTotalAreas(2)
print(instanceradius2.area()) #print 12.56636
print(instanceradius2.addtotalareas()) #print 15.70795
instanceradius3 = CircleTotalAreas(3)
print(instanceradius3.area()) #print 28.274309999999996
print(instanceradius3.addtotalareas()) #print 43.98226
print(instanceradius3.printallcircleslist()) #print [<__main__.CircleTotalAreas object at 0x7f5639977880>, <__main__.CircleTotalAreas object at 0x7f56399779a0>, <__main__.CircleTotalAreas object at 0x7f5639977a00>]
print(instanceradius3.allcircleslist) #print [<__main__.CircleTotalAreas object at 0x7f5639977880>, <__main__.CircleTotalAreas object at 0x7f56399779a0>, <__main__.CircleTotalAreas object at 0x7f5639977a00>]
print(instanceradius3.addtotalareas) #print <function CircleTotalAreas.addtotalareas at 0x7f6cf5c00430>
class CircleTotalAreasClassMethod:
    """Class description here"""
    allcircleslist = [] #Class variable containing list of all circles created
    piclassvariable = 3.14159
    def __init__(self, radius=1):
        """Create a circle with the given radius"""
        self.radius = radius
        self.__class__.allcircleslist.append(self) #Adds instance to the allcircleslist
    def area(self):
        """Calculate area of a circle"""
        return self.__class__.piclassvariable * self.radius * self.radius
    def printallcircleslist(self):
        # return self.__class__.allcircleslist
        return self.allcircleslist
    @classmethod
    def addtotalareas(cls): #class parameter is traditionally cls
        """Static method add all circle areas calculated"""
        total = 0
        for eachareacircle in cls.allcircleslist:
            total = total + eachareacircle.area()
        return total


instanceradius4 = CircleTotalAreasClassMethod(4)
instanceradius5 = CircleTotalAreasClassMethod(5)
print(instanceradius5.addtotalareas()) #print 128.80518999999998.  ((4^2)*3.14159)+((5^2)*3.14159) =128.8052
print(CircleTotalAreasClassMethod.addtotalareas()) #print 128.80518999999998.  ((4^2)*3.14159)+((5^2)*3.14159) =128.8052
#Inheritance
class ShapeParent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Square(ShapeParent):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side
class Circle(ShapeParent):
    def __init__(self, r=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = r
class Parent:
    defaultgreeteing = "Hello"
    def setparent(self):
        self.x = "Class Parent"
    def printparent(self):
        print(self.x)
class Child(Parent):
    def setchild(self):
        self.x = "Class Child"
    def printchild(self):
        print(self.x)


childinstance = Child()
childinstance.setchild()
childinstance.printchild() #return Class Child
childinstance.printparent() #return Class Child.  RM:  setparent() method wasn't run for childinstance
childinstance.setparent()
childinstance.printparent() #return Class Parent.  RM:  setparent() method was run for childinstance
childinstance.setparent()
parentinstance = Parent()
parentinstance.setparent()
parentinstance.printparent()  #return Class Parent
#parentinstance.setchild() #return AttributeError: 'Parent' object has no attribute 'setchild'

#The Quick Python Book by Naomi Ceder Chapter 16 Regular Expressions
#Regular expressions recognize data and extract data from certain patterns of text.  A regex recognizes a piece of text or a string to match the text or string.  A regex is defined by a string in which certain characters or metacharacters to match many text or strings.  Text parsing text parse.
import re
regexp = re.compile("hello")
count = 0
searchfile = open("temp.txt") #temp.txt contains hello in a line
for eachline in searchfile.readlines():
    if regexp.search(eachline):
        count = count + 1
searchfile.close()
print(count) #print 1
regexpverticalbaror1 = re.compile("hello|Hello")
regexpverticalbaror2 = re.compile("(h|H)ello") #The parentheses group characters
regexpverticalbaror3 = re.compile("[hH]ello") #The brackets matches any single character.  [a-z] matches a single character between a and z.  [0-9A-Z] matches any digit or any uppercase character.  Include a real hyphen in the brackets put the hyphen as the first character; for example [-012] matches a hyphen, 0, 1, or 2.
count = 0
searchfile = open("temp.txt") #temp.txt contains hello in a line
for eachline in searchfile.readlines():
    if regexpverticalbaror3.search(eachline):
        count = count + 1
searchfile.close()
print(count) #print 1
regexpbackslash = re.compile("\\\\ten") #four backslashes to search for one backslash.  The first two backslashs is a special sequence representing a single backslash and the second two backslashes is a sepcial sequence representing another single backslash.  Two single backslashes \\ results in two actual backslashes in the Python string.  re.compile("\\\\ten") becomes re.compile("\\ten") which is the correct search for \ten Python string.
count = 0
searchfile = open("temp.txt") #temp.txt contains \ten
for eachline in searchfile.readlines():
    if regexpbackslash.search(eachline):
        count = count + 1
searchfile.close()
print(count) #print 1
oneletterandhyphen = re.compile("[-a-zA-Z]")
manyletterandhyphen = re.compile("[-a-zA-Z]+") #The plus sign repeats whatever comes before it one or more times as necessary to match the string being processed.  [-a-zA-Z]+ matches a single name such as Kenneth or McDonald or Perkin-Elmer or - or -a-b-c.
phohenumber = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") #\d matches any number.  The regex is three digits, a hyphen, three digits, a hyphen, and four digits.
phohenumberoptionalareacode = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d") #\d matches any number.  The ? special character says anything before the ? is optional.  The regex is three digits optional, a hyphen optional, three digits, a hyphen, and four digits.
phohenumberoptionalareacode = re.compile(r"(\d{3}-)?\d{3}-\d{4}") #\d matches any number.  The {} curly braces indicates the number of times a pattern repeats.  The regex is three digits optional, a hyphen optional, three digits, a hyphen, and four digits.
#Commas, colons, and spaces don't have special meanings.
namephonenumber = re.compile(r"[-a-zA-Z]+, [-a-zA-Z]+( [-a-zA-Z]+)?: (\d{3}-)?\d{3}-\d{4}") #Last name, comma, space, first name, space, middle name optional, colon, space, phone number for which area code optional.
namephonenumberlabel = re.compile(r"(?P<last>[-a-zA-Z]+,) (?P<first>[-a-zA-Z]+)( (?P<middle>[-a-zA-Z]+))?: (?P<phone>(\d{3}-)?\d{3}-\d{4})")
searchfile = open("temp.txt") #temp.txt contains lastname, firstname: 408-555-1234 and lastname, firstname middlenamenoareacode: 555-7890
for eachline in searchfile.readlines():
    result = namephonenumberlabel.search(eachline)
    print(result)
    if result == None:
        print("No found")
    else:
        lastname = result.group("last")
        firstname = result.group("first")
        middlename = result.group("middle")
        if middlename == None:
            middlename = ""
        phonenumber = result.group("phone")
        print("Return search result-->Name:", lastname, firstname, middlename, "Number:", phonenumber)
'''
...
<re.Match object; span=(0, 33), match='lastname, firstname: 408-555-1234'>
Return search result-->Name: lastname, firstname  Number: 408-555-1234
None
No found
None
No found
<re.Match object; span=(0, 50), match='lastname, firstname middlenamenoareacode: 555-789>
Return search result-->Name: lastname, firstname middlenamenoareacode Number: 555-7890
'''
searchfile.close()
doublethe = "If the the problem is textual, use the the re module"
pattern = r"the the"
finddoublethe = re.compile(pattern)
print(finddoublethe.sub("the", doublethe)) #print If the problem is textual, use the re module.  The sub method uses findddoublethe to scan pattern to produce a new string replacing all matching substrings with the value in the first argument.  Replace the double the doublethe variable with "the".
integerstring = "1 2 3 4 5"
def convertintegertofloatfunction(matchobject):
    return(matchobject.group("numberlabel") + ".0")


searchpattern = r"(?P<numberlabel>[0-9]+)" #Looks for a number consisting of one or more digits.  Give each a name numberlabel.
regexpsearchintegerinstring = re.compile(searchpattern)
print(regexpsearchintegerinstring.sub(convertintegertofloatfunction, integerstring)) #print 1.0 2.0 3.0 4.0 5.0.  Take integerstring matching numberlabel to the function convertintegertofloatfunction.  The function uses group to extract the matching substring from the match object matchobject to produce a new string concatenate with .0.  sub returns the new string.

#The Quick Python Book by Naomi Ceder Chapter 17 Data Types As Objects
print(type(5)) #print <class 'int'>
print(type(["hello", "goodbye"])) #print <class 'list'>
objectyperesult = type(5)
print(type(objectyperesult)) #print <class 'type'>
print(type("hello") == type("goodbye")) #print True
class ClassA:
    pass
class ClassB(ClassA):
    pass


instanceclassb = ClassB()
print(type(instanceclassb)) #print <class '__main__.ClassB'>
print(instanceclassb.__class__) #print <class '__main__.ClassB'>
instanceclassbtype = instanceclassb.__class__
print(instanceclassbtype == ClassB) #print True #A class is a Python object which can be stored or passed around like any Python object.
print(instanceclassbtype.__name__) #print ClassB
print(instanceclassbtype.__bases__) #print (<class '__main__.ClassA'>,).  Find what classes a class inherits.
class ClassC:
    pass
class ClassD:
    pass
class ClassE(ClassD):
    pass


x = 12
instanceclassc = ClassC()
instanceclassd = ClassD()
instanceclasse = ClassE()
#isinstance function determines a class is passed into a function or method
print(isinstance(x, ClassE)) #print False
print(isinstance(instanceclassc, ClassE)) #print False
print(isinstance(instanceclasse, ClassE)) #print True
print(isinstance(instanceclasse, ClassD)) #print True
print(isinstance(instanceclassd, ClassE)) #print False
y = 12
print(isinstance(y, type(5))) #print True
print(issubclass(ClassC, ClassD)) #print False
print(issubclass(ClassE, ClassD)) #print True
print(issubclass(ClassD, ClassD)) #print True
print(issubclass(ClassE.__class__, ClassD)) #print False
print(issubclass(instanceclasse.__class__, ClassD)) #print True
#Use __getitem__ method attribute to open files or read files
class LineReader:
    def __init__(self, filename):
        self.openfileobject = open(filename, "r")
    def __getitem__(self, index):
        readlineinfile = self.openfileobject.readline()
        if readlineinfile == "": #if no more lines to read in file, then close self.openfileobject file object
            self.openfileobject.close()
            raise IndexError
        else:
            return readlineinfile


for x in LineReader("temp.txt"):
    print(x)
    '''
    201903blog.html

    46 <p><b>*kcea 89.1 fm.</b>  the big band radio station in the nor cal peninsula area is back on the air.  the radio station is located in the sequoia union high school district at menlo-atherton high school.  the website is <a href="http://www.kcea.org">kcea.org.</a></p>



    hello

    world
    ...
    '''

#The Quick Python Book by Naomi Ceder Chapter 18 Packages
#A module is a file containing code.  A module defines a group of Python functions or other objects.
#A package is a directory containing code and further subdirectories.  A package contains a group of usually related code files or modules.  Packatges are a natural extension of the module concept and are designed to handle very large projects.  Packages group related modules.

#The Quick Python Book by Naomi Ceder Chapter 21 Processing Data Files
#ASCII encoding is 128 characters.  95 characters are printable.
#Unicode encoding is called UTF-8.  UTF-8 accepts basic ASCII characters and allows an almost unlimited set of other characters and symbols according to the Unicode standard.  UTF-8 was used in more than 85% of web pages as of the date the book is written.
#The open() function accepts optional errors parameters to deal with encoding errors when reading or writing.  The default option is strict which causes an error to be raised whenever an encoding error is encountered.  Other options are ignore which causes the character causing the error to be skipped.  Option replace which causes the character to be replaced by a marker character usually ?.  Option backslashreplace which replaces the character with a backslash escape sequence.  Option surrogateescape which translates the offending character to a private Unicode code point on reading and back to the original sequence of bytes on writing.
#Examples option function:  open("test.txt", errors="ignore").read(), open("test.txt", errors="replace").read() default replaces with ?, open("test.txt", errors="surrogateescape").read(), open("test.txt", errors="backslashreplace").read()
mobytext = open("moby01.txt").read()
mobyparagraphs = mobytext.split("\n\n")
print(mobyparagraphs)
'''
["Call me Ishmael. Some years ago--never mind how long precisely--\nhaving little or no money in my purse, and nothing particular\nto interest me on shore, I thought I would sail about a little\nand see the watery part of the world. It is a way I have\nof driving off the spleen and regulating the circulation.\nWhenever I find myself growing grim about the mouth;\nwhenever it is a damp, drizzly November in my soul; whenever I\nfind myself involuntarily pausing before coffin warehouses,\nand bringing up the rear of every funeral I meet;\nand especially whenever my hypos get such an upper hand of me,\nthat it requires a strong moral principle to prevent me from\ndeliberately stepping into the street, and methodically knocking\npeople's hats off--then, I account it high time to get to sea\nas soon as I can. This is my substitute for pistol and ball.\nWith a philosophical flourish Cato throws himself upon his sword;\nI quietly take to the ship. There is nothing surprising in this.\nIf they but knew it, almost all men in their degree, some time\nor other, cherish very nearly the same feelings towards\nthe ocean with me.", 'There now is your insular city of the Manhattoes, belted round by wharves\nas Indian isles by coral reefs--commerce surrounds it with her surf.\nRight and left, the streets take you waterward. Its extreme downtown\nis the battery, where that noble mole is washed by waves, and cooled\nby breezes, which a few hours previous were out of sight of land.\nLook at the crowds of water-gazers there.']
'''
print(mobyparagraphs[1])
'''
There now is your insular city of the Manhattoes, belted round by wharves
as Indian isles by coral reefs--commerce surrounds it with her surf.
Right and left, the streets take you waterward. Its extreme downtown
is the battery, where that noble mole is washed by waves, and cooled
by breezes, which a few hours previous were out of sight of land.
Look at the crowds of water-gazers there.
'''
mobyparagraphsindex1lowercase = mobyparagraphs[1].lower()
mobyparagraphsindex1lowercase = mobyparagraphsindex1lowercase.replace(".", "")
mobyparagraphsindex1lowercase = mobyparagraphsindex1lowercase.replace(",", "")
mobyparagraphsindex1lowercasesplitwords = mobyparagraphsindex1lowercase.split()
print(mobyparagraphsindex1lowercasesplitwords)
'''
['there', 'now', 'is', 'your', 'insular', 'city', 'of', 'the', 'manhattoes', 'belted', 'round', 'by', 'wharves', 'as', 'indian', 'isles', 'by', 'coral', 'reefs--commerce', 'surrounds', 'it', 'with', 'her', 'surf', 'right', 'and', 'left', 'the', 'streets', 'take', 'you', 'waterward', 'its', 'extreme', 'downtown', 'is', 'the', 'battery', 'where', 'that', 'noble', 'mole', 'is', 'washed', 'by', 'waves', 'and', 'cooled', 'by', 'breezes', 'which', 'a', 'few', 'hours', 'previous', 'were', 'out', 'of', 'sight', 'of', 'land', 'look', 'at', 'the', 'crowds', 'of', 'water-gazers', 'there']
'''
pipestext = open("datapipes.txt").read()
pipestextparagraphs = pipestext.split("|")
print(pipestextparagraphs)
'''
['State', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)\nIllinois', '1979/01/01', '17.48', '994\nIllinois', '1979/01/02', '4.64', '994\nIllinois', '1979/01/03', '11.05', '994\nIllinois', '1979/01/04', '9.51', '994\nIllinois', '1979/05/15', '68.42', '994\nIllinois', '1979/05/16', '70.29', '994\nIllinois', '1979/05/17', '75.34', '994\nIllinois', '1979/05/18', '79.13', '994\nIllinois', '1979/05/19', '74.94', '994']
'''
eachlinealist = []
for eachline in open("datapipes.txt"):
    eachlinealist.append(eachline.strip().split("|"))
print(eachlinealist)
'''
[['State', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)'], ['Illinois', '1979/01/01', '17.48', '994'], ['Illinois', '1979/01/02', '4.64', '994'], ['Illinois', '1979/01/03', '11.05', '994'], ['Illinois', '1979/01/04', '9.51', '994'], ['Illinois', '1979/05/15', '68.42', '994'], ['Illinois', '1979/05/16', '70.29', '994'], ['Illinois', '1979/05/17', '75.34', '994'], ['Illinois', '1979/05/18', '79.13', '994'], ['Illinois', '1979/05/19', '74.94', '994']]
'''
import csv
eachlinealistcsvmodule = [eachline for eachline in csv.reader(open("datapipes.txt", newline=""), delimiter="|")]
print(eachlinealistcsvmodule)
'''
[['State', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)'], ['Illinois', '1979/01/01', '17.48', '994'], ['Illinois', '1979/01/02', '4.64', '994'], ['Illinois', '1979/01/03', '11.05', '994'], ['Illinois', '1979/01/04', '9.51', '994'], ['Illinois', '1979/05/15', '68.42', '994'], ['Illinois', '1979/05/16', '70.29', '994'], ['Illinois', '1979/05/17', '75.34', '994'], ['Illinois', '1979/05/18', '79.13', '994'], ['Illinois', '1979/05/19', '74.94', '994']]
'''
eachlinealistcsvmodulecsvfile = [eachline for eachline in csv.reader(open("datapipes.csv", newline=""))]
print(eachlinealistcsvmodulecsvfile)
'''
[['Notes', 'State', 'State Code', 'Month Day, Year', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)', 'Min Temp for Daily Max Air Temp (F)', 'Max Temp for Daily Max Air Temp (F)', 'Avg Daily Max Heat Index (F)', 'Record Count for Daily Max Heat Index (F)', 'Min for Daily Max Heat Index (F)', 'Max for Daily Max Heat Index (F)', 'Daily Max Heat Index (F) % Coverage ', 'Illinois', '17', 'Jan 01, 1979', '1979/01/ 01', '17.48', '994', '6.00', '30.50', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'Jan 02, 1979', '1979/01/02', '4.64', '994', '- 6.40', '15.80', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'Jan 03, 1979', '1979/01/03', '11.05', '994', '- 0.70', '24.70', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'Jan 04, 1979', '1979/01/ 04', '9.51', '994', '0.20', '27.60', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'May 15, 1979', '1979/05/ 15', '68.42', '994', '61.00', '75.10', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'May 16, 1979', '1979/05/ 16', '70.29', '994', '63.40', '73.50', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'May 17, 1979', '1979/05/ 17', '75.34', '994', '64.00', '80.50', '82.60', '2', '82.40', '82.80', '0.20% ', 'Illinois', '17', 'May 18, 1979', '1979/05/ 18', '79.13', '994', '75.50', '82.10', '81.42', '349', '80.20', '83.40', '35.11% ', 'Illinois', '17', 'May 19, 1979', '1979/05/ 19', '74.94', '994', '66.90', '83.10', '82.87', '78', '81.60', '85.20', '7.85%']]
'''
for eachline in csv.reader(open("datapipes.csv", newline="")):
    print(eachline)
    '''
    ['Notes', 'State', 'State Code', 'Month Day, Year', 'Month Day, Year Code', 'Avg Daily Max Air Temperature (F)', 'Record Count for Daily Max Air Temp (F)', 'Min Temp for Daily Max Air Temp (F)', 'Max Temp for Daily Max Air Temp (F)', 'Avg Daily Max Heat Index (F)', 'Record Count for Daily Max Heat Index (F)', 'Min for Daily Max Heat Index (F)', 'Max for Daily Max Heat Index (F)', 'Daily Max Heat Index (F) % Coverage ', 'Illinois', '17', 'Jan 01, 1979', '1979/01/ 01', '17.48', '994', '6.00', '30.50', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'Jan 02, 1979', '1979/01/02', '4.64', '994', '- 6.40', '15.80', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'Jan 03, 1979', '1979/01/03', '11.05', '994', '- 0.70', '24.70', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'Jan 04, 1979', '1979/01/ 04', '9.51', '994', '0.20', '27.60', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'May 15, 1979', '1979/05/ 15', '68.42', '994', '61.00', '75.10', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'May 16, 1979', '1979/05/ 16', '70.29', '994', '63.40', '73.50', 'Missing', '0', 'Missing', 'Missing', '0.00% ', 'Illinois', '17', 'May 17, 1979', '1979/05/ 17', '75.34', '994', '64.00', '80.50', '82.60', '2', '82.40', '82.80', '0.20% ', 'Illinois', '17', 'May 18, 1979', '1979/05/ 18', '79.13', '994', '75.50', '82.10', '81.42', '349', '80.20', '83.40', '35.11% ', 'Illinois', '17', 'May 19, 1979', '1979/05/ 19', '74.94', '994', '66.90', '83.10', '82.87', '78', '81.60', '85.20', '7.85%']
    '''
eachlinealistcsvmoduledictionary = [eachline for eachline in csv.DictReader(open("datapipes.csv", newline=""))]
print(eachlinealistcsvmoduledictionary) #print []
from openpyxl import Workbook
workbookobject = Workbook()
worksheetobject = workbookobject.active
worksheetobject.title = "worksheet name Temperature Data"
for eachrow in eachlinealist:
    worksheetobject.append(eachrow)
workbookobject.save("datapipesexcel.xlsx") #Excel file datapipesexcel.xlsx created good Excel file with header and each row a record
workbookobject2 = Workbook()
worksheetobject2 = workbookobject2.active
worksheetobject2.title = "worksheet name Temperature Data 2"
for eachline in csv.reader(open("datapipes.csv", newline="")):
    worksheetobject2.append(eachline)
workbookobject.save("datapipesexcel2.xlsx") #Excel file datapipesexcel2.xlsx created good Excel file with header and each row a record