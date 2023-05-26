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
