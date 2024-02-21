#Everything in Python is an object.  Houses are built from blueprints.  Objects are built from classes.  Object-based programming is create objects and use objects from existing classes.  For example, int, float, str, list, tuple, dict, set, Decimal from the standard library, arrays from NumPy, Figures from Matplotlib, and DataFrames from Pandas.
#Object Oriented Programming OOP.  Class example.  The instance initializer method or constructor is always __init__.  Instance variables are created and initialized at __init__.  Methods are like functions in classes defined using the def keyword.  The first argument in any method is self.  Self is set to the instance which invoked the method.
#Inheritance or inheriting:  take an attribute or variable from another class
#Methods:  a function in a class
#Base class:  The initial class or the first class.  Also called superclass.
#Derived class:  The new class or the class created after the base class.  Also called subclass.
#Polymorphism:  Program "in the general" rather than "in the specific."  Send the same method call to objects possibly of many different types.  Each object responds by "doing the right thing."  The same method call takes on "many forms."
#The class name which begins with an uppercase letter is used in a constructor expression to create an object for class name.  The class name also invokes the class's __init__ method.  __init__ is the initializing class object.
#Save the class name to a variable classnamevariable creates a new object.  The __init__ method initializes the data.  Each new class you create provides an __init__ method which specifies how to initialize an object's data attributes.
#When you call a method for a specific object, Python implicitly passes a reference to that object as the method's first argument.  Python programmers call a method's first parameter self.  A class's methods must use the self reference to access the object's attributes and other methods.  The __init__ method also specifies parameters for the other variables.
#When an object of a class is created, the object doesn't have any attributes.  The attributes are added dynamically using the self.attributename = value.
#Any attribute name beginning with an underscore is for a class's internal use only.  Attributes don't begin with an underscore are considered ppublicly accessible.

class Boat():
    pass


print(Boat()) #print <__main__.Boat object at 0x7fc9fdd654c0>
boatinstance = Boat()
print(boatinstance) #print <__main__.Boat object at 0x7fc9fdd654c0>
print(id(boatinstance)) #print 140505523836096
anotherboatinstance = Boat()
print(anotherboatinstance) #print <__main__.Boat object at 0x7fc9fdd654c0>
print(id(anotherboatinstance)) #print 140505523836096

#The field of an instance or structure are accessed and assigned by dot notation.
class Circle:
    pass


circleinstance1 = Circle()
circleinstance1.radius = 5
print(2 * 3.14 * circleinstance1.radius) #print 31.400000000000002
circleinstance2 = Circle()
circleinstance2.radius = 17
print(2 * 3.14 * circleinstance2.radius) #print 106.76

class Thenewbostonenemynoinit:
    startinglives = 3
    def attack(self):
        print("Ouch.  def attack(self) attacked me.  Subtract one starting life.")
        self.startinglives -= 1
    def printstartinglives(self):
        if self.startinglives <= 0:
            print("I'm dead.  def printstartinglives(self) prints the startinglives variable which is now", self.startinglives)
        else:
            print("{} is the number of startinglives variable remaining.  def printstartinglives(self) prints the startinglives variable".format(self.startinglives))


objectforThenewbostonenemynoinit1 = Thenewbostonenemynoinit()
print(objectforThenewbostonenemynoinit1.startinglives) #print 3
objectforThenewbostonenemynoinit1.printstartinglives() #return 3 is the number of startinglives variable remaining.  def printstartinglives(self) prints the startinglives variable
objectforThenewbostonenemynoinit1.attack()
print(objectforThenewbostonenemynoinit1.startinglives) #print 2
objectforThenewbostonenemynoinit1.printstartinglives() #return 2 is the number of startinglives variable remaining.  def printstartinglives(self) prints the startinglives variable
objectforThenewbostonenemynoinit1.attack()
objectforThenewbostonenemynoinit1.attack()
objectforThenewbostonenemynoinit1.printstartinglives() #return I'm dead.  def printstartinglives(self) prints the startinglives variable which is now 0
objectforThenewbostonenemynoinit2 = Thenewbostonenemynoinit()
objectforThenewbostonenemynoinit2.attack()
objectforThenewbostonenemynoinit2.attack()
objectforThenewbostonenemynoinit2.attack()
objectforThenewbostonenemynoinit2.attack()
objectforThenewbostonenemynoinit2.attack()
objectforThenewbostonenemynoinit2.printstartinglives() #return I'm dead.  def printstartinglives(self) prints the startinglives variable which is now -2

class Thenewbostongirlnofunctions():
    withclassvariable = "female"
    def __init__(self, name):
        self.nameinstancevariable = name


rachelobject = Thenewbostongirlnofunctions("Rachel")
stankyobject = Thenewbostongirlnofunctions("Stanky")
print(rachelobject) #print <__main__.Thenewbostongirlnofunctions object at 0x7ff27908e4c0>
print(rachelobject.withclassvariable) #print female
print(rachelobject.nameinstancevariable) #print Rachel
print(stankyobject) #print <__main__.Thenewbostongirlnofunctions object at 0x7ff27908e4c0>
print(stankyobject.withclassvariable) #print female
print(stankyobject.nameinstancevariable) #print Stanky

#Initialize fields of an instance automatically using an __init__ initialization method.  The function is run every time an instance of the class is created.  The new instance first agument is self.  Python classes may only have one __init__ method.
#nameinstancevariable is an instance variable.  Each instance has its own copy of name.  The value stored in the copy may be different from the values stored in the name variable in other instances.  Create an instance variable by assigning to a field of a class instance instance.variable = value.  For example rachelobject.hobby = "Override chess as favoritehobby".
#All instance variables require explicit mention of the containing instance which is instance.variable.
class Thenewbostongirlyesfunctions():
    yesclassvariable = "female"
    def __init__(self, name):
        self.nameinstancevariable = name
    def favoritehobby(self, hobby):
        #print(yesclassvariable) #print NameError: name 'yesclassvariable' is not defined
        print(self.yesclassvariable)
        self.hobby = hobby
        print("{}'s favorite hobby is {}.  I define an instance self.hobby in the favoritehobby() function".format(self.nameinstancevariable, self.hobby))


rachelobject = Thenewbostongirlyesfunctions("Rachel")
rachelobject.favoritehobby("chess")
'''
female
Rachel's favorite hobby is chess.  I define an instance self.hobby in the favoritehobby() function
'''
print(rachelobject.yesclassvariable) #print female
print(rachelobject.nameinstancevariable) #print Rachel
rachelobject.hobby = "Override chess as favoritehobby"
print(rachelobject.hobby) #print Override chess as favoritehobby
rachelobject.favoritehobby("Hobby is back to chess")
'''
female
Rachel's favorite hobby is Hobby is back to chess.  I define an instance self.hobby in the favoritehobby() function
'''
stankyobject = Thenewbostongirlyesfunctions("Stanky")
stankyobject.favoritehobby("sewing")
'''
female
Stanky's favorite hobby is sewing.  I define an instance self.hobby in the favoritehobby() function
'''
print(stankyobject.hobby) #print sewing
print(stankyobject.yesclassvariable) #print female
print(stankyobject.nameinstancevariable) #print Stanky

class Foollistvariables():
    def __init__(self, onenumber, listofnumbers):
        self.onenumber = onenumber
        self.listofnumbers = listofnumbers


call01foollist = Foollistvariables(10, [100, 200, 300])
print(call01foollist.onenumber) #print 10
print(call01foollist.listofnumbers) #print [100, 200, 300]
print(vars(call01foollist)) #print {'onenumber': 10, 'listofnumbers': [100, 200, 300]}

class Thenewbostontuna:
    def __init__(self):
        print("Blrrblrlbrlbrbr.  The __init__ is always returned when the class is called the first time.")
    def swim(self):
        print("I am swimming")
    def sleep(self):
        print("I am sleeping")
    def eat(self):
        print("I am eating")


defineobjectThenewbostontuna1 = Thenewbostontuna()
defineobjectThenewbostontuna1.swim() #return Blrrblrlbrlbrbr.  The __init__ is always returned when the class is called the first time.\n I am swimming
defineobjectThenewbostontuna1.sleep() #return I am sleeping
defineobjectThenewbostontuna1.eat() #return I am eating
defineobjectThenewbostontuna2 = Thenewbostontuna()
defineobjectThenewbostontuna2.eat() #return Blrrblrlbrlbrbr.  The __init__ is always returned when the class is called the first time.\n I am eating
defineobjectThenewbostontuna2.sleep() #return I am sleeping
defineobjectThenewbostontuna2 = Thenewbostontuna()
defineobjectThenewbostontuna2.sleep() #return Blrrblrlbrlbrbr.  The __init__ is always returned when the class is called the first time.\n I am sleeping
defineobjectThenewbostontuna2.sleep() #return I am sleeping
defineobjectThenewbostontuna3 = Thenewbostontuna()
defineobjectThenewbostontuna3.eat() #return Blrrblrlbrlbrbr.  The __init__ is always returned when the class is called the first time.\n I am eating
defineobjectThenewbostontuna3.sleep() #return I am sleeping
defineobjectThenewbostontuna3.swim() #return  I am swimming

#Three questions for the class Question
threequestions = ["What color are applies?\n(a) Red or Green\n(b) Purple\n(c) Orange\n\n", "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n", "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"]
for eachthreequestions in threequestions:
    print(eachthreequestions)
    '''
    What color are applies?
    (a) Red or Green
    (b) Purple
    (c) Orange


    What color are Bananas?
    (a) Teal
    (b) Magenta
    (c) Yellow


    What color are strawberries?
    (a) Yellow
    (b) Red
    (c) Blue
    '''
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


answers = [Question(threequestions[0], "a"), Question(threequestions[1], "c"), Question(threequestions[2], "b")]
print(answers) #print [<__main__.Question object at 0x7f058a24e4c0>, <__main__.Question object at 0x7f058a0b3ca0>, <__main__.Question object at 0x7f058a0b3b50>]
print(answers[0].question)
'''
What color are applies?
(a) Red or Green
(b) Purple
(c) Orange
'''
print(answers[1].answer) #print c
#Function contestant answers three questions
def quiz(inputquestionsanswers):
    score = 0
    for eachinputquestionsanswers in inputquestionsanswers:
        print("eachinputquestionsanswers.answer variable: " + eachinputquestionsanswers.answer)
        print("eachinputquestionsanswers.question variable: " + eachinputquestionsanswers.question)
        contestantanswers = input("Contestant answer the eachinputquestionsanswers.question variable: " + eachinputquestionsanswers.question)
        if contestantanswers == eachinputquestionsanswers.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(answers)) + " correct")


quiz(answers)
'''
eachinputquestionsanswers.answer variable: a
eachinputquestionsanswers.question variable: What color are applies?
(a) Red or Green
(b) Purple
(c) Orange


Contestant answer the eachinputquestionsanswers.question variable: What color are applies?
(a) Red or Green
(b) Purple
(c) Orange

a
eachinputquestionsanswers.answer variable: c
eachinputquestionsanswers.question variable: What color are Bananas?
(a) Teal
(b) Magenta
(c) Yellow


Contestant answer the eachinputquestionsanswers.question variable: What color are Bananas?
(a) Teal
(b) Magenta
(c) Yellow

b
eachinputquestionsanswers.answer variable: b
eachinputquestionsanswers.question variable: What color are strawberries?
(a) Yellow
(b) Red
(c) Blue


Contestant answer the eachinputquestionsanswers.question variable: What color are strawberries?
(a) Yellow
(b) Red
(c) Blue

c
You got 1/3 correct
'''

#Methods can be invoked with arguments if the method definitions accept arguments.
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def theinit(self):
        print("__init__ initialize class Dog().  First word is self inside parenthesis.  Add self. to the variables name and age receiving the dog's name and the dog's age.")
        print("%s and %d are the self.name and self.age." % (self.name, self.age))
    def dogsit(self):
        print("Call dogsit() inside class Dog().  Sit down " + self.name)
    def dogrollover(self):
        print("Call dogrollover() inside class Dog().  Rollover %s." % self.name)
    def dogage(self):
        print("Call dogage() inside class Dog().  {} age is {}." .format(self.name, self.age))


firstcallclassdog = Dog("Willie", 6)
firstcallclassdog.theinit() #return __init__ initialize class Dog().  First word is self inside parenthesis.  Add self. to the variables name and age receiving the dog's name and the dog's age.\n Willie and 6 are the self.name and self.age.
firstcallclassdog.dogsit() #return Call dogsit() inside class Dog().  Sit down Willie
firstcallclassdog.dogrollover() #return Call dogrollover() inside class Dog().  Rollover Willie
firstcallclassdog.dogage() #return Call dogage() inside class Dog().  Willie age is 6.
print("Identify the first variable name passing to class Dog() firstcallclassdog: {}".format(firstcallclassdog.name)) #print Identify the first variable name passing to class Dog() firstcallclassdog: Willie
print("Identify the second variable age passing to class Dog() firstcallclassdog: {}".format(firstcallclassdog.age)) #print Identify the second variable age passing to class Dog() firstcallclassdog: 6
secondcallclassdog = Dog("Lucy", 3)
secondcallclassdog.theinit() #return __init__ initialize class Dog().  First word is self inside parenthesis.  Add self. to the variables name and age receiving the dog's name and the dog's age.\n Lucy and 3 are the self.name and self.age.
secondcallclassdog.dogsit() #return Call dogsit() inside class Dog().  Sit down Lucy
secondcallclassdog.dogrollover() #return Call dogrollover() inside class Dog().  Rollover Lucy.
secondcallclassdog.dogage() #return Call dogage() inside class Dog().  Lucy age is 3.
print("Identify the first variable name passing to class Dog() secondcallclassdog: {}".format(secondcallclassdog.name)) #print Identify the first variable name passing to class Dog() secondcallclassdog: Lucy
print("Identify the second variable age passing to class Dog() secondcallclassdog: {}".format(secondcallclassdog.age)) #print Identify the second variable age passing to class Dog() secondcallclassdog: 3
secondcallclassdogagain = Dog("Lucy", 3)
secondcallclassdogagain.theinit() #return __init__ initialize class Dog().  First word is self inside parenthesis.  Add self. to the variables name and age receiving the dog's name and the dog's age.\n Lucy and 3 are the self.name and self.age.
secondcallclassdogagain.dogsit() #return Call dogsit() inside class Dog().  Sit down Lucy
secondcallclassdogagain.dogrollover() #return Call dogrollover() inside class Dog().  Rollover Lucy.
secondcallclassdogagain.dogage() #return Call dogage() inside class Dog().  Lucy age is 3.
print("Identify the first variable name passing to class Dog() secondcallclassdogagain: {}".format(secondcallclassdogagain.name)) #print Identify the first variable name passing to class Dog() secondcallclassdogagain: Lucy
print("Identify the second variable age passing to class Dog() secondcallclassdogagain: {}".format(secondcallclassdogagain.age)) #print Identify the second variable age passing to class Dog() secondcallclassdogagain: 3

class Capitalizeclassesnumbers():
    def __init__(self):
        self.number = 0
    def printnumber(self):
        print(self.number)
    def addnumber(self, increase):
        self.number += increase
    def subtractnumber(self, decrease):
        self.number -= decrease


instance1 = Capitalizeclassesnumbers()
instance1.printnumber() #return 0
instance1.addnumber(5)
instance1.printnumber() #return 5
instance1.subtractnumber(50)
instance1.printnumber() #return -45
instance2 = Capitalizeclassesnumbers()
instance2.subtractnumber(100)
instance2.subtractnumber(250)
instance2.addnumber(1000)
instance2.printnumber() #print 650
instance2 = Capitalizeclassesnumbers()
instance2.subtractnumber(111)
instance2.addnumber(999)
instance2.addnumber(1000)
instance2.printnumber() #print 1888

#Class description class definition class describe class help
class Fruit():
    """
    A class which makes various tasty fruits.
    Docstring.  A second line.
    """
    def __init__(self, fruitname, color, flavor, poisonous=False):
        self.name = fruitname
        self.color = color
        self.flavor = flavor
        self.ispoison = poisonous
    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
        print("I'm a {} {} and I taste {}.".format(self.color, self.name, self.flavor))
        print("I'm a " + self.color + " " + self.name + " and I taste " + self.flavor)
    def isedible(self):
        if self.ispoison:
            print("Don't eat me!  I'm super poisonous.")
        else:
            print("Yep! I'm edible.")


lemon = Fruit("lemon", "yellow", "sour", False)
help(lemon)
'''
Help on Fruit in module __main__ object:

class Fruit(builtins.object)
 |  Fruit(fruitname, color, flavor, poisonous=False)
 |  
 |  A class which makes various tasty fruits.
 |  Docstring.  A second line.
 |  
 |  Methods defined here:
 |  
 |  __init__(self, fruitname, color, flavor, poisonous=False)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  description(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
'''
print(lemon.__doc__)
'''
    A class which makes various tasty fruits.
    Docstring.  A second line.
'''
lemon.description()
'''
I'm a yellow lemon and I taste sour.
I'm a yellow lemon and I taste sour.
I'm a yellow lemon and I taste sour
'''
lemon.isedible() #return Yep! I'm edible.

class Restaurant():
    def __init__(self, restaurantname, cuisinetype):
        self.differentvariablename = restaurantname
        self.cuisinetype = cuisinetype
        self.needselfchangenumbercustomers = 0
    def firstcallclassrestaurant(self):
        print("The initial values for restaurantname, cusininetype, and number of customers are the following: {}; {}, {}.  I changed variable name restaurantname to self.differentvariablename".format(self.differentvariablename, self.cuisinetype, self.needselfchangenumbercustomers))
    def describerestaurant(self):
        print(self.differentvariablename + " servces the kind of food " + self.cuisinetype + " inside the class Restaurant().")
    #print the number of customers method below from __init__
    def printchangenumbercustomers(self):
        print("The number of customers changed is", self.needselfchangenumbercustomers)
    def initialnumbercustomers(self, initialcustomersserved):
        self.customersserved = initialcustomersserved
    def readnumbercustomers(self):
        print(self.customersserved, "customers have been served at " + self.differentvariablename)
    def addmorecustomers(self, morecustomersserved):
        self.customersserved += morecustomersserved
        self.needselfchangenumbercustomers = morecustomersserved


mingchinese = Restaurant("Ming River Restaurant", "Chinese")
mingchinese.firstcallclassrestaurant() #return The initial values for restaurantname, cusininetype, and number of customers are the following: Ming River Restaurant; Chinese, 0.  I changed variable name restaurantname to self.differentvariablename
mingchinese.describerestaurant() #return Ming River Restaurant servces the kind of food Chinese inside the class Restaurant().
mingchinese.printchangenumbercustomers() #return The number of customers changed is 0
mingchinese.initialnumbercustomers(500)
mingchinese.readnumbercustomers() #return 500 customers have been served at Ming River Restaurant
mingchinese.addmorecustomers(100)
mingchinese.printchangenumbercustomers() #return The number of customers changed is 100
mingchinese.readnumbercustomers() #return 600 customers have been served at Ming River Restaurant
print("Notice use the self variables when referencing the class Restaurant() outside the class. " + mingchinese.differentvariablename + " is the restaurant name. " + mingchinese.cuisinetype + " is the restaurant type.") #print Notice use the self variables when referencing the class Restaurant() outside the class. Ming River Restaurant is the restaurant name. Chinese is the restaurant type.
lesliediner = Restaurant(cuisinetype="American Diner", restaurantname="Leslie's", )
lesliediner.firstcallclassrestaurant() #return The initial values for restaurantname, cusininetype, and number of customers are the following: Leslie's; American Diner, 0.  I changed variable name restaurantname to self.differentvariablename
lesliediner.describerestaurant() #return Leslie's servces the kind of food American Diner inside the class Restaurant().
lesliediner.printchangenumbercustomers() #return The number of customers changed is 0
lesliediner.initialnumbercustomers(2)
lesliediner.readnumbercustomers() #return 2 customers have been served at Leslie's
lesliediner.addmorecustomers(50)
lesliediner.printchangenumbercustomers() #return The number of customers changed is 50
lesliediner.readnumbercustomers() #return 52 customers have been served at Leslie's
print("Notice use the self variables when referencing the class Restaurant() outside the class. " + lesliediner.differentvariablename + " is the restaurant name. " + lesliediner.cuisinetype + " is the restaurant type.") #print Notice use the self variables when referencing the class Restaurant() outside the class. Leslie's is the restaurant name. American Diner is the restaurant type.

#A class variable is a variable associated with a class.  A class variable is not an instance of a class.  A class variable is accessible by all instances of the class.
class CharacterClassVariable():
    #class variables or static variables
    totalnumberofcharacters = 0
    maximumhealth = 150
    lastname = "Potter"
    def __init__(self, firstname, lastname):
        #instance variables
        self.firstname = firstname
        self.lastname = lastname
        self.health = CharacterClassVariable.maximumhealth
        # CharacterClassVariable.totalnumberofcharacters += 1
        CharacterClassVariable.totalnumberofcharacters = CharacterClassVariable.totalnumberofcharacters + 1
    def __repr__(self):
        """Return CharacterClassVariable something for repr()"""
        return self.firstname + " " + self.lastname

    def __str__(self):
        """Return CharacterClassVariable string in another format"""
        print("{} {}".format(self.firstname, self.lastname))

    def __somethingbetween__(self):
        return "All you need is love"


bob = CharacterClassVariable(firstname="Bob", lastname="")
print(CharacterClassVariable.totalnumberofcharacters) #print 1
print(bob.totalnumberofcharacters) #print 1
ryan = CharacterClassVariable("Ryan", "Willow")
print(ryan) #print <__main__.CharacterClassVariable object at 0x7f5693dadfd0>
print(ryan.totalnumberofcharacters) #print 2
print(CharacterClassVariable.totalnumberofcharacters) #print 2
charlie = CharacterClassVariable("Charlie", "Hanks")
print(charlie.totalnumberofcharacters) #print 3
print(CharacterClassVariable.totalnumberofcharacters) #print 3
print(charlie.totalnumberofcharacters) #print 3
print(charlie.__repr__()) #print Charlie Hanks.  Display an object.
charlie.__str__() #return Charlie Hanks.  Display an object.
print(charlie.__somethingbetween__()) #print All you need is love.  Display an object.

class CharacterClassVariablecorrect():
    #class variables or static variables
    totalnumberofcharacters = 0
    maximumhealth = 150
    lastname = "Potter"
    def __init__(self, firstname, lastname):
        #instance variables
        self.firstname = firstname
        self.lastname = lastname
        self.health = CharacterClassVariablecorrect.maximumhealth
        self.totalnumberofcharacters = self.totalnumberofcharacters + 1


bob = CharacterClassVariablecorrect(firstname="Bob", lastname="")
print(CharacterClassVariablecorrect.totalnumberofcharacters) #print 0
print(bob.totalnumberofcharacters) #print 1
ryan = CharacterClassVariablecorrect("Ryan", "Willow")
print(ryan) #print <__main__.CharacterClassVariablecorrect object at 0x7f5693f254c0>
print(CharacterClassVariablecorrect.totalnumberofcharacters) #print 0
print(ryan.totalnumberofcharacters) #print 1
charlie = CharacterClassVariablecorrect("Charlie", "Hanks")
print(CharacterClassVariablecorrect.totalnumberofcharacters) #print 0
print(charlie.totalnumberofcharacters) #print 1
print(charlie.totalnumberofcharacters) #print 1
print(charlie.totalnumberofcharacters) #print 1
print(CharacterClassVariablecorrect.totalnumberofcharacters) #print 0
print(CharacterClassVariablecorrect.maximumhealth) #print 150
CharacterClassVariablecorrect.maximumhealth = 150000150
print(CharacterClassVariablecorrect.maximumhealth) #print 150000150
petenewmaximumhealth = CharacterClassVariablecorrect("Pete", "Malark")
print(petenewmaximumhealth.health) #return 150000150
print(petenewmaximumhealth.__class__.maximumhealth) #print 150000150
print(petenewmaximumhealth.__class__) #print <class '__main__.CharacterClassVariablecorrect'>
print(petenewmaximumhealth.__class__.totalnumberofcharacters) #print 0
print(petenewmaximumhealth.totalnumberofcharacters) #print 1
print(petenewmaximumhealth.totalnumberofcharacters) #print 1

class Human():
    def __init__(self, initializevariablename, initializevariablegender):
        self.initializevariablename = initializevariablename
        self.initializevariablegender = initializevariablegender
    def returnname(self):
        return self.initializevariablename
    def returngender(self):
        return self.initializevariablegender
    def printsomething(self, variabletext):
        print("{} said {}".format(self.initializevariablename, variabletext))
    def printtwosomethings(self, variabletext1, variabletext2):
        print("%s said the following: " % (self.initializevariablename))
        print(variabletext1 + " and " + variabletext2)
    def givemethreenouns(self, *multiplenouns):
        print(multiplenouns)
        print(list(multiplenouns))
        print("\n".join(multiplenouns))


raymondclassobject = Human("nameRaymond", "genderMale")
print(raymondclassobject) #print <__main__.Human object at 0x7f7061ab24c0>
print("Print the raymondclassobject initializevariablename value " + raymondclassobject.initializevariablename) #print Print the raymondclassobject initializevariablename value nameRaymond
print("Return the raymondclassobject initializevariablename " + raymondclassobject.returnname()) #print Return the raymondclassobject initializevariablename nameRaymond
print("Print the raymondclassobject initializevariablegender value " + raymondclassobject.initializevariablegender) #print Print the raymondclassobject initializevariablegender value genderMale
print("Return the raymondclassobject initializevariablegender " + raymondclassobject.returngender()) #print Return the raymondclassobject initializevariablegender genderMale
raymondclassobject.printsomething("send the string to printsomething function") #return nameRaymond said send the string to printsomething function
raymondclassobject.printtwosomethings("something1", "something2")
'''
nameRaymond said the following: 
something1 and something2
'''
raymondclassobject.givemethreenouns("cat", "dog", "bird")
'''
('cat', 'dog', 'bird')
['cat', 'dog', 'bird']
cat
dog
bird
'''
spartanclassobject = Human("nameSpartan", "genderFemale")
print(spartanclassobject) #print <__main__.Human object at 0x7f762d430a00>
print("Print the spartanclassobject initializevariablename value" + spartanclassobject.initializevariablename) #print Print the spartanclassobject initializevariablename valuenameSpartan
print("Return the raymondclassobject initializevariablename value again " + raymondclassobject.initializevariablename) #print Return the raymondclassobject initializevariablename value again nameRaymond
print("Return the spartanclassobject initializevariablegender " + spartanclassobject.returngender()) #print Return the spartanclassobject initializevariablegender genderFemale
spartanclassobject.printsomething("spartanclassobject sends the string to printsomething function") #return nameSpartan said spartanclassobject sends the string to printsomething function
spartanclassobject.printtwosomethings("sparta1", "sparta2")
'''
nameSpartan said the following: 
sparta1 and sparta2
'''

#The class below doesn't use self when calling a function inside the class
class Boatnoselfinfunction():
    def __init__(self):
        self.cargoweight = 23
    def changecargoweight(newcargoweight):
        newcargoweight.cargoweight = 45
    def finalcargoweight(addedfunction):
        addedfunction.cargoweight = 678


boatinstance = Boatnoselfinfunction()
print(boatinstance.cargoweight) #print 23
boatinstance.changecargoweight()
print(boatinstance.cargoweight) #print 45
print(id(boatinstance)) #print 139715301301024
boatinstance = Boatnoselfinfunction()
print(boatinstance.cargoweight) #print 23
boatinstance.changecargoweight()
print(boatinstance.cargoweight) #print 45
print(id(boatinstance)) #print 139715302982848
boatinstance2 = Boatnoselfinfunction()
print(boatinstance2.cargoweight) #print 23
print(boatinstance2.cargoweight) #print 23
print(boatinstance2.cargoweight) #print 23
boatinstance2.changecargoweight()
print(boatinstance2.cargoweight) #print 45
print(boatinstance2.cargoweight) #print 45
print(id(boatinstance2)) #print 140586116297920
boatinstanceaddedfunction = Boatnoselfinfunction()
print(boatinstanceaddedfunction) #print <__main__.Boatnoselfinfunction object at 0x7f5fcdb9deb0>
print(boatinstanceaddedfunction.cargoweight) #print 23
print(id(boatinstanceaddedfunction)) #print 139752490430128
boatinstanceaddedfunction.changecargoweight()
print(boatinstanceaddedfunction.cargoweight) #print 45
print(id(boatinstanceaddedfunction)) #print 139752490430128
boatinstanceaddedfunction.changecargoweight()
print(boatinstanceaddedfunction.cargoweight) #print 45
print(id(boatinstanceaddedfunction)) #print 139752490430128
boatinstanceaddedfunction.finalcargoweight()
print(boatinstanceaddedfunction.cargoweight) #print 678
print(id(boatinstanceaddedfunction)) #print 139752490430128
boatinstance2.finalcargoweight()
print(boatinstance2.cargoweight) #print 678

#assign self to a class local variable
class Character():
    insideclass = 100
    def __init__(self, name):
        self.name = name
        self.insideclassnumber = Character.insideclass
    def finalhealth(self):
        namelength = len(self.name)
        return self.insideclassnumber - namelength


defineclassobjectraymond = Character("Raymond")
print(defineclassobjectraymond.insideclassnumber) #print 100
print(defineclassobjectraymond.name) #print Raymond
print(defineclassobjectraymond.finalhealth()) #print 93

class Characterlocalfunctionvariable():
    insideclass = 100
    def __init__(self, name):
        self.name = name
        self.insideclassnumber = Characterlocalfunctionvariable.insideclass
    def finalhealth(self):
        namelength = len(self.name)
        self.needselffunctionvariable = namelength
        return self.insideclassnumber - self.needselffunctionvariable


defineclassobjectfma = Characterlocalfunctionvariable("RizaRoyShiska")
print(defineclassobjectfma.insideclassnumber) #print 100
print(defineclassobjectfma.name) #print RizaRoyShiska
#print(defineclassobjectfma.needselffunctionvariable) #print AttributeError: 'Characterlocalfunctionvariable' object has no attribute 'needselffunctionvariable'
print(defineclassobjectfma.finalhealth()) #print 87
print(defineclassobjectfma.needselffunctionvariable) #print 13
defineclassobjectsailormoon = Characterlocalfunctionvariable("Sailor Jupiter")
print(defineclassobjectsailormoon.name) #print Sailor Jupiter
defineclassobjectsailormoon.finalhealth()
print(defineclassobjectsailormoon.needselffunctionvariable) #print 14
print(defineclassobjectsailormoon.finalhealth()) #print 86

#no assign self to a class local variable
class Alsocharacter():
    insideclass = 100
    def __init__(self, name):
        self.name = name
    def finalhealth(self):
        namelength = len(self.name)
        return Alsocharacter.insideclass - namelength


defineclassobjectpotter = Alsocharacter("HarryPotter")
print(defineclassobjectpotter.name) #print HarryPotter
defineclassobjectpotter.finalhealth()
print(defineclassobjectpotter.finalhealth()) #print 89
#print(defineclassobjectpotter.namelength) #print AttributeError: 'Alsocharacter' object has no attribute 'namelength'

class Additemsinshoppingcartdictionary():
    itemsincart = {}
    def __init__(self, customername):
        self.customername = customername
    def additem(self, product, price):
        self.itemsincart[product] = price


rockycart = Additemsinshoppingcartdictionary("Rocky")
rockycart.additem("broccoli", 50)
rockycart.additem("coffee", 10.20)
print(rockycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2}
rockycart.additem("caramel", 33)
print(rockycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'caramel': 33}
mapopcart = Additemsinshoppingcartdictionary("Ma")
mapopcart.additem("chocolate", 10)
mapopcart.additem("peas and carrots", 15)
print(mapopcart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'caramel': 33, 'chocolate': 10, 'peas and carrots': 15}
mapopcart = Additemsinshoppingcartdictionary("Pa")
mapopcart.additem("comic book", 1)
print(mapopcart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'caramel': 33, 'chocolate': 10, 'peas and carrots': 15, 'comic book': 1}
print(rockycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'caramel': 33, 'chocolate': 10, 'peas and carrots': 15, 'comic book': 1}
poponlycart = Additemsinshoppingcartdictionary("Pa")
poponlycart.additem("two comic books", 2)
print(poponlycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'caramel': 33, 'chocolate': 10, 'peas and carrots': 15, 'comic book': 1, 'two comic books': 2}
popspelledcorrectlyonlycart = Additemsinshoppingcartdictionary("Pop")
popspelledcorrectlyonlycart.additem("three comic books", 3)
print(poponlycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'caramel': 33, 'chocolate': 10, 'peas and carrots': 15, 'comic book': 1, 'two comic books': 2, 'three comic books': 3}

class Additemsinshoppingcardictionarycorrect():
    def __init__(self, customername):
        self.customername = customername
        self.itemsincart = {}
    def additem(self, product, price):
        self.itemsincart[product] = price


rockycart = Additemsinshoppingcardictionarycorrect("Rocky")
rockycart.additem("broccoli", 50)
rockycart.additem(price=10.20, product="coffee")
print(rockycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2}
rockycart.additem(price=33, product="caramel")
print(rockycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'caramel': 33}
macart = Additemsinshoppingcardictionarycorrect("Ma")
macart.additem("chocolate", 10)
macart.additem("peas and carrots", 15)
print(macart.itemsincart) #print {'chocolate': 10, 'peas and carrots': 15}
popcart = Additemsinshoppingcardictionarycorrect("Pa")
popcart.additem("comic book", 1)
print(macart.itemsincart) #print {'chocolate': 10, 'peas and carrots': 15}
print(popcart.itemsincart) #print {'comic book': 1}
print(rockycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'caramel': 33}

#Variables inside class only
class PrivateClass:
    def __init__(self):
        self.publicdata = "public"
        self.__privatedata = "private begins with two underscores"
    def printepublicdata(self):
        print("printing self.publicdata " + self.publicdata)
    def printeprivatedata(self):
        print("Did printeprivatedata print? " + self.__privatedata)


createprivateclassobject = PrivateClass()
print(createprivateclassobject.publicdata) #print private
createprivateclassobject.printepublicdata() #return printing self.publicdata public
try:
    print(createprivateclassobject.__privatedata)
except AttributeError:
    print("AttributeError.  'PrivateClass' object has no attribute '__privatedata'") #print AttributeError.  'PrivateClass' object has no attribute '__privatedata'

#Call class and call function inside class which is a method
class Chooseafunction():
    def __init__(self, name, defaultnull=""):
        self.name = name
        self.default = defaultnull
    def runfunctioninsideclass(self, numberdefaultblank=""):
        self.number = numberdefaultblank
        if self.number:
            print("runfunctioninsideclass self.number", self.number)
        else:
            print("There is no self.number")
    def function01(self):
        print(self.name + " is printed from function01 which is a method in a class")
    def function02(self):
        print(self.name + " is printed from function02 which is a method in a class")
    def function03(self):
        print(self.name + " is printed from function03 which is a method in a class")
        variableinsidefunction03 = "green"
        print(variableinsidefunction03 + " is printed from function03")
    def function04(self):
        print(self.name + " is printed from function04 which is a method in a class")
        number = int(input("Type a number: "))
        print(number)
    def runtwofunctions(self):
        print("Run two functions.  First function is runtwofunctions().  Second is jello() function with starwberry.")
        self.jello("strawberry")
    def jello(self, flavor):
        print("I received the flavor " + flavor)
    def function05(self, anything):
        #self.anything = anything
        print(self.name + " " + anything + " are printed from function05 which is a method in a class")
        number = int(input("Type a number for the second function runfunctioninsideclass: "))
        self.runfunctioninsideclass(number)


numberfunctiontest = Chooseafunction("Roy")
numberfunctiontest.runfunctioninsideclass(40) #return runfunctioninsideclass self.number 40
numberfunctiontest.runfunctioninsideclass() #return There is no self.number
bigg = Chooseafunction("Bigg")
bigg.function01() #return Bigg is printed from function01 which is a method in a class
bigg.function02() #return Bigg is printed from function02 which is a method in a class
function03only = Chooseafunction("Biv")
function03only.function03()
'''
Biv is printed from function03 which is a method in a class
green is printed from function03
'''
needinputfunction = Chooseafunction("Declare object first to access a function")
needinputfunction.function04()
'''
Declare object first to access a function is printed from function04 which is a method in a class
Type a number: 64
64
'''
twofunctions = Chooseafunction("Need a name", "object for defaultnull not null")
twofunctions.runtwofunctions()
'''
Run two functions.  First function is runtwofunctions().  Second is jello() function with starwberry.
I received the flavor strawberry
'''
jack = Chooseafunction("Jack")
jack.function05("no self for anything variable sent string object")
'''
Jack no self for anything variable sent string object are printed from function05 which is a method in a class
Type a number for the second function runfunctioninsideclass: 99
runfunctioninsideclass self.number 99
'''

#Inheritance is base classes and subclasses.  Loan is a base class.  CarLoan, HomeImprovementLoan, and MortgageLoan are subclasses.  Base classes tend to be more general.  Subclasses tend to be more specific.  More examples are student base class and graduate student and undergraduate student subclasses; shape base class and circle, triangle, rectangle, sphere, and cube subclasses; bankaccount base class and checking account and savings account subclasses; vehicle base class and cars, trucks, boats, and bicycles subclasses.
#Inheritance hierarchy example.  An administrator in the subclass is a faculty in the subclass is an employee in the subclass is a community member in the base class for which all are objects.  Another example shape is a base class separated to two dimensions hape and three dimensional shape subclasses which has circle, square, and triangle subclasses in two dimension shape and sphere, cube, and tetrahedron subclasses in the three dimension shape.
#Use inheritance to create new classes from existing classes.  Python assumes the class inherits directly from class object when you don't explicitly specify the base class.  The class hierarchy begins with class object.  The parentheses after a class name indicate inheritance and may contains a single class for single inheritance or a comma-separated list of base classes for multiple inheritance.  Multiple inheritance is beyond the scope of the book.
#The subclass starts essentially the same as the base class in single inheritance.
#Parent child class.  Class inheritance.  Thenewbostonchild class uses Thenewbostonparent class functions.
class Thenewbostonparent():
    def __init__(self, parentname):
        self.parentname = parentname
    def printparentname(self):
        print("Thenewbostonparent class printparentname method " + self.parentname)
    def noselfvariableparent(self):
        print("noselfvariableparent in Thenewbostonparent")
class Thenewbostonchild(Thenewbostonparent): #class Thenewbostonchild(Thenewbostonparent) inherits def printparentname(self) from class Thenewbostonparent
    def __init__(self, childname):
        self.childname = childname
    def printchildname(self):
        print("Thenewbostonchild class printchildname method " + self.childname)
    def noselfvariablechild(self):
        print("noselfvariablechild in Thenewbostonchild")


defineobjectchildthenewbostonchild = Thenewbostonchild("Bucky")
print(defineobjectchildthenewbostonchild) #print <__main__.Thenewbostonchild object at 0x7f21ed4114c0>
defineobjectchildthenewbostonchild.printchildname() #return Thenewbostonchild class printchildname method Bucky
#defineobjectchildthenewbostonchild.printparentname() #return AttributeError: 'Thenewbostonchild' object has no attribute 'parentname'
defineobjectparentthenewbostonparent = Thenewbostonparent("Roberts")
print(defineobjectparentthenewbostonparent) #print <__main__.Thenewbostonparent object at 0x7f17532d3eb0>
defineobjectparentthenewbostonparent.printparentname() #return Thenewbostonparent class printparentname method Roberts
# defineobjectparentthenewbostonparent.printchildname() #return AttributeError: 'Thenewbostonparent' object has no attribute 'printchildname'
defineobjectconfirmparentchild = Thenewbostonparent("Any parent")
defineobjectconfirmparentchild.noselfvariableparent() #return noselfvariableparent in Thenewbostonparent
#defineobjectconfirmparentchild.noselfvariablechild() #return AttributeError: 'Thenewbostonparent' object has no attribute 'noselfvariablechild'
defineobjectchildgetparent = Thenewbostonchild("Any child")
defineobjectchildgetparent.noselfvariablechild() #return noselfvariablechild in Thenewbostonchild
defineobjectchildgetparent.noselfvariableparent() #return noselfvariableparent in Thenewbostonparent

#Parent child class.  Child class overrides parent class.  No init.
class Parent():
    def printlastname(self):
        print("Parent class lastnamehere")
class Child():
    def printfirstname(self):
        print("Child class firstnamehere")
    def printlastname(self):
        print("Child class lastnamehere")


parentclassobject = Parent()
parentclassobject.printlastname() #return Parent class lastnamehere
childclassobject = Child()
childclassobject.printfirstname() #return Child class firstnamehere
childclassobject.printlastname() #return Child class lastnamehere

class Parenttobeinherited():
    def printlastname(self):
        print("Parenttobeinherited class lastnamehere")
    def dontprintinparenttobeinherited(self):
        print("Parenttobeinherited class.  Print the sentence there.")
class Child(Parenttobeinherited):
    def printfirstname(self):
        print("Child class firstnamehere")
    def printlastname(self):
        print("Override Parenttobeinherited() class.  Child class lastnamehere")


parentclassobject = Parenttobeinherited()
parentclassobject.printlastname() #return Parenttobeinherited class lastnamehere
childclassobject = Child()
childclassobject.printfirstname() #return Child class firstnamehere
childclassobject.printlastname() #return Override Parenttobeinherited() class.  Child class lastnamehere.  RM:  It's not an override.  I'm calling printlastname in Child class.
childclassobject.dontprintinparenttobeinherited() #print Parenttobeinherited class.  Print the sentence there.

#Simple standard multiple inheritance
class Mario():
    def move(self):
        print("Mario is moving")
class Mushroom():
    def supersize(self):
        print("Mario is bigger")
class Flowerinheritmariomushroomclasses(Mario, Mushroom):
    def fireball(size):
        print("Mario fires fireballs")


player1 = Mario()
player1.move() #return Mario is moving
#player1.supersize() #return AttributeError: 'Mario' object has no attribute 'supersize'
player2 = Flowerinheritmariomushroomclasses()
player2.move() #return Mario is moving
player2.supersize() #return Mario is bigger
player2.fireball() #return Mario fires fireballs

class Mario():
    def __init__(self, playername):
        self.playername = playername
    def move(self):
        print(self.playername + " is moving Mario")
class Eatmushrooom(Mario):
    def mushroom(self):
        print(self.playername + " eats the mushroom")
#class Supermario(Mario, Eatmushrooom): #TypeError: Cannot create a consistent method resolution order (MRO) for bases Mario, Eatmushrooom
class Supermario(Eatmushrooom):
    def jumps(self):
        print(self.playername + " breaks brick blocks")


player1mario = Mario("player1")
player1mario.move() #return player1 is moving Mario
player1eatmushroom = Eatmushrooom("player1")
player1eatmushroom.move() #return player1 is moving Mario
player1eatmushroom.mushroom() #return player1 eats the mushroom
player1supermario = Supermario("player1")
player1supermario.move() #return player1 is moving Mario
player1supermario.mushroom() #return player1 eats the mushroom
player1supermario.jumps() #return player1 breaks brick blocks
player2supermarioobjectonly = Supermario("player2")
print(player2supermarioobjectonly.playername) #print player2
player2supermarioobjectonly.move() #return player2 is moving Mario
player2supermarioobjectonly.mushroom() #return player2 eats the mushroom
player2supermarioobjectonly.jumps() #return player2 breaks brick blocks
print(issubclass(Supermario, Eatmushrooom)) #print True.  Check subclass.  Check class.
print(issubclass(Supermario, Mario)) #print True

class Parentclasscar():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def displaycar(self):
        thecar = "The car is {} {} {}".format(str(self.year), self.make, self.model)
        return thecar
class Childclasscargas(Parentclasscar):
    def __init__(self, gasbrand):
        self.gasbrand = gasbrand
    def driveswithwhatgas(self):
        thegascar = "The car {} {} {} drives with {}".format(str(self.year), self.make, self.model, self.gasbrand)
        return thegascar
class Childclasscargasmakemodelyearinitnoinheritance():
    def __init__(self, make, model, year, gasbrand):
        self.make = make
        self.model = model
        self.year = year
        self.gasbrand = gasbrand
    def driveswithwhatgas(self):
        thegascar = "The car {} {} {} drives with {}".format(str(self.year), self.make, self.model, self.gasbrand)
        return thegascar
class Childclasscargasmakemodelyearinit(Parentclasscar):
    def __init__(self, make, model, year, gasbrand):
        self.make = make
        self.model = model
        self.year = year
        self.gasbrand = gasbrand
    def driveswithwhatgas(self):
        thegascar = "The car {} {} {} drives with {}".format(str(self.year), self.make, self.model, self.gasbrand)
        return thegascar
class Childclasscargasmakemodelyearinitsuper(Parentclasscar):
    def __init__(self, make, model, year, gasbrand):
        super().__init__(make, model, year)
        self.gasbrand = gasbrand
    def driveswithwhatgas(self):
        thegascar = "The car {} {} {} drives with {}".format(str(self.year), self.make, self.model, self.gasbrand)
        return thegascar


parentraymondcar = Parentclasscar("Toyota", "Camry", 2005)
print(parentraymondcar.displaycar()) #print The car is 2005 Toyota Camry
childraymondcar = Childclasscargas("Chevron")
print(childraymondcar.driveswithwhatgas) #print <bound method Childclasscargas.driveswithwhatgas of <__main__.Childclasscargas object at 0x7f23f7bd0fd0>>
#print(childraymondcar.driveswithwhatgas()) #print AttributeError: 'Childclasscargas' object has no attribute 'year'
#childraymondcarwithallvariables = Childclasscargas("Toyota", "Camry", 2005, "Chevron") #TypeError: __init__() takes 2 positional arguments but 5 were given
childraymondcarallvariablesnoinheritance = Childclasscargasmakemodelyearinitnoinheritance("Toyota", "Camry", 2500, "Chevron")
print(childraymondcarallvariablesnoinheritance.driveswithwhatgas()) #print The car 2500 Toyota Camry drives with Chevron
childraymondcarallvariables = Childclasscargasmakemodelyearinit("Toyota", "Camry", 5002, "Chevron")
print(childraymondcarallvariables.driveswithwhatgas()) #print The car 5002 Toyota Camry drives with Chevron
childraymondcarallvariablesinitsuper = Childclasscargasmakemodelyearinitsuper("Toyota", "Camry", 5200, "Chevron")
print(childraymondcarallvariablesinitsuper.driveswithwhatgas()) #print The car 5200 Toyota Camry drives with Chevron
print(childraymondcarallvariablesinitsuper.displaycar()) #print The car is 5200 Toyota Camry

class Childclasselectric(Parentclasscar):
    def __init__(self, make, model, year, batterysize):
        super().__init__(make, model, year)
        self.batterysize = batterysize
    def carbatterysize(self):
        thebatterycar = "The battery car is {} {} {} driving with {} battery size.".format(str(self.year), self.make, self.model, self.batterysize)
        print(thebatterycar)


childraymondsbatterycar = Childclasselectric("Toyota", "Prius", "2022", 1000)
print(childraymondsbatterycar.year) #print 2022
childraymondsbatterycar.carbatterysize() #return The battery car is 2022 Toyota Prius driving with 1000 battery size.

#Instances as attributes and a class is a child to two parent classes or parent and grandparent
class Batterysize():
    def __init__(self, batterysizenumber=702):
        self.batterysizenumber = batterysizenumber
    def displaybatterysizenumber(self):
        print("The car has a " + str(self.batterysizenumber) + " -kwh battery.")
    def updatebatterysizenumber(self, newbatterhsizenumber):
        self.batterysizenumber = newbatterhsizenumber
class Grandchildclasselectricbatterysize(Parentclasscar):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batterysizenumber = Batterysize()


defaultbatterysizenumber = Batterysize()
print(defaultbatterysizenumber.batterysizenumber) #print 702
defaultbatterysizenumber.displaybatterysizenumber() #return The car has a 702 -kwh battery.
changedefaultbatterysizenumber = Batterysize(5327)
print(changedefaultbatterysizenumber.batterysizenumber) #print 5327
changedefaultbatterysizenumber.displaybatterysizenumber() #return The car has a 5327 -kwh battery.
changedefaultbatterysizenumber.updatebatterysizenumber(9890980)
print(changedefaultbatterysizenumber.batterysizenumber) #print 9890980
changedefaultbatterysizenumber.displaybatterysizenumber() #return The car has a 9890980 -kwh battery.
grandchildmakemodelyear = Grandchildclasselectricbatterysize("Nissan", "Leaf", 2023)
print(grandchildmakemodelyear.displaycar()) #print The car is 2023 Nissan Leaf
print(grandchildmakemodelyear.batterysizenumber) #print <__main__.Batterysize object at 0x7f388c2d97c0>
# print(grandchildmakemodelyear.batterysizenumber.displaybatterysizenumber()) #print The car has a 702 -kwh battery.\n None
grandchildmakemodelyear.batterysizenumber.displaybatterysizenumber() #print The car has a 702 -kwh battery.
grandchildmakemodelyear.batterysizenumber.updatebatterysizenumber(8981891)
grandchildmakemodelyear.batterysizenumber.displaybatterysizenumber() #print The car has a 8981891 -kwh battery.

#Check if instance check
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Person:
    def __init__(self, name, sex):
        self.personname = name
        self.sex = sex


emmaemployee = Employee("Emma", 22111)
brentperson = Person("Brent", "Male")
if isinstance(emmaemployee, Employee):
    print("Yes " + emmaemployee.name + "is in Employee class") #print Yes Emmais in Employee class
if isinstance(brentperson, Employee):
    print("Yes " + brentperson.name + " is in Employee class")
else:
    print("No " + brentperson.personname + " is not in Employee class") #print No Brent is not in Employee class
if isinstance(brentperson, Person):
    print("Yes " + brentperson.personname + " is in Person class") #print Yes Brent is in Person class

class Functionoutsideclass():
    def choosemathoperationoutisdeclass(self, tellmemathoperationfunction, *numbers):
        print("The result is {}".format(tellmemathoperationfunction(*numbers)))
def mathoperationadd(a, b):
    return a + b
def mathoperaetionmultiply(a, b):
    return a * b


defineobjectadd1 = Functionoutsideclass()
defineobjectadd1.choosemathoperationoutisdeclass(mathoperationadd, 3, 5) #return The result is 8.  It's a method.
print(defineobjectadd1.choosemathoperationoutisdeclass(mathoperationadd, 3, 5))
'''
The result is 8
None
'''
print(mathoperationadd(30, 50)) #print 80
defineobjectmultiply1 = Functionoutsideclass()
defineobjectmultiply1.choosemathoperationoutisdeclass(mathoperaetionmultiply, 4, 8) #return The result is 32.  It's a method.
print(mathoperaetionmultiply(40, 80)) #print 3200
defineobjectmultiply2 = Functionoutsideclass()
print(defineobjectmultiply2) #print <__main__.Functionoutsideclass object at 0x7fac5578e880>
defineobjectmultiply2.choosemathoperationoutisdeclass(mathoperaetionmultiply, 100, 333) #return The result is 33300.  It's a method.

#Context manager.  The __exit__ method as the except in the try except which traps exceptions.  Simple exception is include return True in Mycontextmanagertrue class.
#Defining "__enter__" and "__exit__" on your classes, you can give them the ability to work inside of "with" blocks, doing things automatically at the start and finish.  And you can even have them trap exceptions in a semi-automated way, without needing "try" and "except" anywhere around.

class Mycontextmanager(object):
    def __enter__(self):
        print("I'm the enter method.  I work before the with.  I start before the with")
        print("A second print function in the enter method for which the class must include (object).")
    def __exit__(self, type, value, traceback):
        print("I'm the exit method.  I work after the with.  I end after the with.")
        print("I don't understand the (. . ., type, value, and traceback) as the moment.")


with Mycontextmanager() as variablename:
    print("Hello.  I'm the first sentence in the with statement.")
    print("I'm the second sentence in the with statement.")
    '''
    I'm the enter method.  I work before the with.  I start before the with
    A second print function in the enter method for which the class must include (object).
    Hello.  I'm the first sentence in the with statement.
    I'm the second sentence in the with statement.
    I'm the exit method.  I work after the with.  I end after the with.
    I don't understand the (. . ., type, value, and traceback) as the moment.
    '''
# with Mycontextmanager() as errormessage:
#     print(10 / 0)
    '''
    I'm the enter method.  I work before the with.  I start before the with
    A second print function in the enter method for which the class must include (object).
    I'm the exit method.  I work after the with.  I end after the with.
    I don't understand the (. . ., type, value, and traceback) as the moment.
    Traceback (most recent call last):
      File "yytest.py", line 27, in <module>
        print(10 / 0)
    ZeroDivisionError: division by zero
    '''
class Contextmanagertypevaluetraceback(object):
    def __enter__(self):
        print("__enter__")
    def __exit__(self, type, traceback, value):
        print("__exit__")
        print(self)
        print("type={}".format(type))
        print("value=%s" % (value))
        print("traceback={}".format(traceback))
        return True


with Contextmanagertypevaluetraceback() as noerrormessage:
    print("The type, traceback, and value variables")
    '''
    __enter__
    The type, traceback, and value variables
    __exit__
    <__main__.Contextmanagertypevaluetraceback object at 0x7f5c7a4384c0>
    type=None
    value=None
    traceback=None
    '''

with Contextmanagertypevaluetraceback() as yeserrormessage:
    print(10 / 0)
    '''
    __enter__
    __exit__
    <__main__.Contextmanagertypevaluetraceback object at 0x7f26f063a4c0>
    type=<class 'ZeroDivisionError'>
    value=<traceback object at 0x7f26f0481500>
    traceback=division by zero
    '''

#Duck Typing:  A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used ("If it looks like a duck and quacks like a duck, it must be a duck.").  RM:  I don't understand.
class Boat():
    pass
    def earnings(self):
        return 1
class WellPaidDuck():
    def __repr__(self):
        return "Must be __repr__ I'm a well-paid duck"
    def __somethingelse__(self):
        return "__somethingelse__"
    def earnings(self):
        return 1000000.00


print(Boat()) #print <__main__.Boat object at 0x7fc9fdd654c0>
boatinstance = Boat()
print(boatinstance) #print <__main__.Boat object at 0x7fc9fdd654c0>
print(id(boatinstance)) #print 140505523836096
anotherboatinstance = Boat()
print(anotherboatinstance) #print <__main__.Boat object at 0x7fc9fdd654c0>
print(id(anotherboatinstance)) #print 140505523836096
print("\n")

duckobject = WellPaidDuck()
classinstanceslist = [boatinstance, anotherboatinstance, duckobject]
for eachclassinstanceslist in classinstanceslist:
    print(eachclassinstanceslist)
    print(eachclassinstanceslist.earnings())
    '''
    <__main__.Boat object at 0x7f2fbcc794c0>
    1
    <__main__.Boat object at 0x7f2fbcb52430>
    1
    Must be __repr__ I'm a well-paid duck
    1000000.0
    '''
