class Boat():
    pass


print(Boat()) #print <__main__.Boat object at 0x7fc9fdd654c0>
boatinstance = Boat()
print(boatinstance) #print <__main__.Boat object at 0x7fc9fdd654c0>
print(id(boatinstance)) #print 140505523836096
anotherboatinstance = Boat()
print(anotherboatinstance) #print <__main__.Boat object at 0x7fc9fdd654c0>
print(id(anotherboatinstance)) #print 140505523836096

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
stankyobject = Thenewbostongirlyesfunctions("Stanky")
stankyobject.favoritehobby("sewing")
'''
female
Stanky's favorite hobby is sewing.  I define an instance self.hobby in the favoritehobby() function
'''
print(stankyobject.hobby) #print sewing
print(stankyobject.yesclassvariable) #print female
print(stankyobject.nameinstancevariable) #print Stanky

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
lesliediner = Restaurant("Leslie's", "American Diner")
lesliediner.firstcallclassrestaurant() #return The initial values for restaurantname, cusininetype, and number of customers are the following: Leslie's; American Diner, 0.  I changed variable name restaurantname to self.differentvariablename
lesliediner.describerestaurant() #return Leslie's servces the kind of food American Diner inside the class Restaurant().
lesliediner.printchangenumbercustomers() #return The number of customers changed is 0
lesliediner.initialnumbercustomers(2)
lesliediner.readnumbercustomers() #return 2 customers have been served at Leslie's
lesliediner.addmorecustomers(50)
lesliediner.printchangenumbercustomers() #return The number of customers changed is 50
lesliediner.readnumbercustomers() #return 52 customers have been served at Leslie's
print("Notice use the self variables when referencing the class Restaurant() outside the class. " + lesliediner.differentvariablename + " is the restaurant name. " + lesliediner.cuisinetype + " is the restaurant type.") #print Notice use the self variables when referencing the class Restaurant() outside the class. Leslie's is the restaurant name. American Diner is the restaurant type.

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
