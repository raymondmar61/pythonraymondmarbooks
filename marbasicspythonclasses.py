#Basics Python Classes Combine All Lessons Learned One Stop Book One Stop Documentation
#thenewbostonallvideos
#williamfisetallvideos
#pythoncrashcourse
#https://www.geeksforgeeks.org/python-isinstance-method/

class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def dogsit(self):
		print("Call dotsit() inside class Dog()-->Dog sit "+self.name)
	def dogrollover(self):
		print("%s is rolling over."%self.name)
	def dogage(self):
		print("The age of {} is {}.".format(self.age, self.name))
identifyself1 = Dog("Willie",6)
print("Identify the identifyself1 name outside class Dog() "+identifyself1.name) #print Identify the identifyself1 name outside class Dog() Willie
print("The age of identifyself1 is",identifyself1.age) #print The age of identifyself1 is 6
identifyself1.dogsit() #return Call dotsit() inside class Dog()-->Dog sit Willie
identifyself1.dogrollover() #return Willie is rolling over.
identifyself1.dogage() #return The age of 6 is Willie.
identifyself2 = Dog("Lucy",3)
print("Identify the identifyself2 name outside class Dog() "+identifyself2.name) #print Identify the identifyself2 name outside class Dog() Lucy
print("The age of identifyself2 is",identifyself2.age) #print The age of identifyself2 is 3
identifyself2.dogsit() #return Call dotsit() inside class Dog()-->Dog sit Lucy
identifyself2.dogrollover() #return Lucy is rolling over.
identifyself2.dogage() #return The age of 3 is Lucy.
anotherlucy3 = Dog("Lucy",3)
print("Identify the anotherlucy3 name outside class Dog() "+identifyself2.name) #print Identify the anotherlucy3 name outside class Dog() Lucy
print("The age of anotherlucy3 is",anotherlucy3.age) #print The age of anotherlucy3 is 3
anotherlucy3.dogsit() #return Call dotsit() inside class Dog()-->Dog sit Lucy
anotherlucy3.dogrollover() #return Lucy is rolling over.
anotherlucy3.dogage() #return The age of 3 is Lucy.
class Restaurant():
	def __init__(self, restaurantname, cuisinetype):
		self.restaurantname = restaurantname
		self.cuisinetype = cuisinetype
		self.needselfchangenumbercustomers = 0
	#print the number of customers method below __init__
	def printchangenumbercustomers(self):
		print("The number of customers changed is",self.needselfchangenumbercustomers)
	def describerestaurant(self):
		print(self.restaurantname+ " serves the kind of food "+self.cuisinetype+" inside the class Restaurant().")
	def setnumberserved(self, initialcustomersserved):
		self.customersserved = initialcustomersserved
	def readsetnumberserved(self):
		print(self.customersserved,"customers have been served at "+self.restaurantname)
	def changesetnumberserved(self, changenumbercustomers):
		self.customersserved+=changenumbercustomers
		self.needselfchangenumbercustomers = changenumbercustomers
mingchinese = Restaurant("Ming River Restaurant","Chinese")
print(mingchinese.restaurantname + " services the kind of food "+ mingchinese.cuisinetype+ "outside the class Restaurant().") #print Ming River Restaurant services the kind of food Chineseoutside the class Restaurant().
mingchinese.describerestaurant() #return Ming River Restaurant serves the kind of food Chinese inside the class Restaurant().
mingchinese.printchangenumbercustomers() #return The number of customers changed is 0
mingchinese.setnumberserved(500)
mingchinese.readsetnumberserved() #return 500 customers have been served at Ming River Restaurant
mingchinese.changesetnumberserved(100)
mingchinese.readsetnumberserved() #return 600 customers have been served at Ming River Restaurant
mingchinese.printchangenumbercustomers() #return The number of customers changed is 100
sanjayindian = Restaurant("Indian Curry","Indian")
print("What's the self.restaurantname outside Restaurant()? "+sanjayindian.restaurantname) #print What's the self.restaurantname outside Restaurant()? Indian Curry
print("What's the self.cuisinetype for "+sanjayindian.restaurantname+" outside Restaurant()? "+sanjayindian.cuisinetype) #print What's the self.cuisinetype for Indian Curry outside Restaurant()? Indian
sanjayindian.describerestaurant() #print Indian Curry serves the kind of food Indian inside the class Restaurant().
sanjayindian.printchangenumbercustomers() #print The number of customers changed is 0
sanjayindian.setnumberserved(500)
sanjayindian.readsetnumberserved() #print 500 customers have been served at Indian Curry
sanjayindian.changesetnumberserved(-100)
sanjayindian.readsetnumberserved() #print 400 customers have been served at Indian Curry
sanjayindian.printchangenumbercustomers() #print The number of customers changed is -100
class Playwithnumbers():
	def __init__(self):
		self.initialize = 0
	def printresult(self):
		print(self.initialize)
	def add(self, increment):
		self.initialize += increment
	def subtract(self, decrement):
		self.initialize -= decrement
firstattempt = Playwithnumbers()
firstattempt.printresult() #return 0
firstattempt.initialize = 1000
firstattempt.printresult() #return 1000
firstattempt.add(1000)
firstattempt.printresult() #return 2000
firstattempt.add(2000)
firstattempt.printresult() #return 4000
firstattempt.subtract(5555)
firstattempt.printresult() #return -1555

class Thenewbostontuna:
	def __init__(self):
		print("Blrrblrlbrlbrbr")
	def swim(self):
		print("I am swimming")
defineobjectThenewbostontuna1 = Thenewbostontuna()
defineobjectThenewbostontuna1.swim() #return Blrrblrlbrlbrbr\n I am swimming
defineobjectThenewbostontuna1.swim() #return I am swimming
defineobjectThenewbostontuna2 = Thenewbostontuna()
defineobjectThenewbostontuna2.swim() #return Blrrblrlbrlbrbr\n I am swimming
defineobjectThenewbostontuna2.swim() #return I am swimming
defineobjectThenewbostontuna2.swim() #return I am swimming
defineobjectThenewbostontuna3 = Thenewbostontuna()
defineobjectThenewbostontuna3.swim() #return Blrrblrlbrlbrbr\n I am swimming
defineobjectThenewbostontuna3.swim() #return I am swimming
defineobjectThenewbostontuna2.swim() #return I am swimming
class Thenewbostonenemy2:
	classvariable = "Reference class Thenewbostongirl variable"
	def __init__(self, lifecounter):
		self.lifecounter = lifecounter
	def getlifecounter(self):
		print(self.lifecounter)
	def subtractlife(self, hitnumber):
		self.lifecounter = self.lifecounter - hitnumber		
defineobjectThenewbostonenemy2one = Thenewbostonenemy2(5)
defineobjectThenewbostonenemy2one.getlifecounter() #return 5
defineobjectThenewbostonenemy2two = Thenewbostonenemy2(943)
defineobjectThenewbostonenemy2two.getlifecounter() #return 943
defineobjectThenewbostonenemy2two.subtractlife(100)
defineobjectThenewbostonenemy2two.getlifecounter() #return 843
defineobjectThenewbostonenemy2two.getlifecounter() #return 843
defineobjectThenewbostonenemy2two.subtractlife(744)
defineobjectThenewbostonenemy2two.getlifecounter() #return 99
defineobjectThenewbostonenemy2one.getlifecounter() #return 5
print(defineobjectThenewbostonenemy2one.lifecounter) #print 5 #RM:  reference class Thenewbostongirl below
#print(defineobjectThenewbostonenemy2one.hitnumber()) #error message AttributeError: 'Thenewbostonenemy2' object has no attribute 'hitnumber'
#print(defineobjectThenewbostonenemy2one.hitnumber) #error message AttributeError: 'Thenewbostonenemy2' object has no attribute 'hitnumber'
print(defineobjectThenewbostonenemy2one.classvariable) #print Reference class Thenewbostongirl variable
class Thenewbostongirl:
	gender = "female"
	def __init__(self, name):
		self.name = name #self.name is an instance variable
	def favoritehobby(self, hobby):
		#print(gender) #error message NameError: name 'gender' is not defined
		self.hobby = hobby
		print("{}'s favorite hobby is {}.".format(self.name, self.hobby))
rachel = Thenewbostongirl("Rachel")
stanky = Thenewbostongirl("Stanky")
print(rachel.gender) #print female
print(stanky.gender) #print female
print(rachel.name) #print Rachel
print(stanky.name) #print Stanky
rachel.favoritehobby("chess") #return Rachel's favorite hobby is chess.
class Thenewbostonenemy:
	life = 3
	def attack(self):
		print("Ouch.  def attack(self) attacked me.  Minus one life.")
		self.life -= 1
	def checklife(self):
		if self.life <=0:
			print("I'm dead.  def checklife(self) see the number of life.")
		else:
			print("{} is the number of life remaining.  def checklife(self) see the number of life.".format(self.life))
defineobjectforThenewbostonenemy1 = Thenewbostonenemy()
defineobjectforThenewbostonenemy1.attack() #return Ouch.  def attack(self) attacked me.  Minus one life.
defineobjectforThenewbostonenemy1.checklife() #return 2 is the number of life remaining.  def checklife(self) see the number of life.
defineobjectforThenewbostonenemy2 = Thenewbostonenemy()
defineobjectforThenewbostonenemy2.checklife() #return 3 is the number of life remaining.  def checklife(self) see the number of life.
defineobjectforThenewbostonenemy2.attack() #return Ouch.  def attack(self) attacked me.  Minus one life.
defineobjectforThenewbostonenemy2.attack() #return Ouch.  def attack(self) attacked me.  Minus one life.
defineobjectforThenewbostonenemy2.attack() #return Ouch.  def attack(self) attacked me.  Minus one life.
defineobjectforThenewbostonenemy2.checklife() #return I'm dead.  def checklife(self) see the number of life.

class Boat():
	def __init__(self):
		self.definecargoweight = 23
	def printdefinecargoweight(self):
		return self.definecargoweight
defineobjectBoat1 = Boat()
print("print definecargoweight value",defineobjectBoat1.definecargoweight) #print print definecargoweight value 23
print(defineobjectBoat1) #print <__main__.Boat object at 0x7f4b68c0a128>
print(defineobjectBoat1.printdefinecargoweight()) #print 23
defineobjectBoat2 = Boat()
print(defineobjectBoat2) #print <__main__.Boat object at 0x7fef924adac8>
print(defineobjectBoat2.printdefinecargoweight()) #print 23
class Character():
	classvariable = 100
	def __init__(self, name):
		self.name = name
		self.health = Character.classvariable
	def finalhealth(self):
		namelength = len(self.name)
		return self.health - namelength
defineobjectraymond = Character("raymond")
print(defineobjectraymond.finalhealth()) #print 93
class AlsoCharacter():
	classvariable = 100
	def __init__(self, name):
		self.name = name
	def finalhealth(self):
		namelength = len(self.name)
		return AlsoCharacter.classvariable - namelength
defineobjectraymond = AlsoCharacter("raymond")
print(defineobjectraymond.finalhealth()) #print 93
class Human():
	def __init__(self, initializevariable1name, initializevariable2gender):
		self.initializevariable1name = initializevariable1name
		self.initializevariable2gender = initializevariable2gender
	def printname(self):
		return self.initializevariable1name
	def printgender(self):
		return self.initializevariable2gender
	def speaksomething(self, textvariable):
		print("{} said {}".format(self.initializevariable1name, textvariable))
	def speaktwosometheings(self, textvariableone, textvariabletwo):
		print("%s said the following:" %(self.initializevariable1name))
		print(textvariableone+" and "+textvariabletwo)
	def givemethreenouns(self, *multiplenouns):
		print(multiplenouns)
		print(list(multiplenouns))
		print("\n".join(multiplenouns))
raymond = Human("nameraymond","gendermale")
print(raymond) #print <__main__.Human object at 0x7ff84eb23278>
print("print the class init variables "+raymond.initializevariable1name) #print print the class init variables nameraymond
print("print the class init variables "+raymond.initializevariable2gender) #print print the class init variables gendermale
print(raymond.printname()) #print nameraymond
print(raymond.printgender()) #print gendermale
raymond.speaksomething("sentence for the textvariable for speaksomething()") #print nameraymond said sentence for the textvariable for speaksomething()
raymond.speaktwosometheings("the first input","the second input") #print nameraymond said the following\n the first input and the second input
raymond.givemethreenouns("cat","dog","bird") #print ('cat', 'dog', 'bird')\n ['cat', 'dog', 'bird']\n cat\n dog\n bird
class FunctionOutsideClass():
	def choosemathoperation(self, tellmemathoperationfunction, *numbers):
		print("{}".format(tellmemathoperationfunction(*numbers)))
def mathoperationsadd(a, b):
	return a + b
def mathoperationsmultiply(a, b):
	return a * b
defineobjectadd1 = FunctionOutsideClass()
defineobjectadd1.choosemathoperation(mathoperationsadd, 3, 5) #print 8
defineobjectmultiply1 = FunctionOutsideClass()
defineobjectmultiply1.choosemathoperation(mathoperationsmultiply, 4, 8) #print 32
defineobjectadd2 = FunctionOutsideClass()
defineobjectadd2.choosemathoperation(mathoperationsadd, 100, 333) #print 433
class ClassName():
	def __init__(self):
		self._privatevariable = "private"
		self.publicvariable = "public"
	def _privateMethod(self):
		pass
	def _privateMethod2(self):
		pass
	def publicMethod(self):
		return 5
c = ClassName()
print(c._privateMethod()) #print None
print(c.publicMethod()) #print 5
print(c._privatevariable) #print private
print(c.publicvariable) #print public

#Parent child class
class Thenewbostonparent():
	def printlastname(self):
		print("Roberts")
class Thenewbostonchild(Thenewbostonparent):  #class Thenewbostonchild(Thenewbostonparent) inherits def printlastname(self) from class Thenewbostonparent
	def printfirstname(self):
		print("Bucky")
	# def printlastname(self):
	# 	print("Snitzleberg")
defineobjectThenewbostonchildbucky = Thenewbostonchild()
defineobjectThenewbostonchildbucky.printfirstname() #return Bucky
defineobjectThenewbostonchildbucky.printlastname() #return Roberts; however, if def printlastname(self): print("Snitzleberg") is uncommented, then return Snitzleberg because Thenewbostonchild(Thenewbostonparent)'s def printlastname(self) overrides Thenewbostonparent() def printlastname(self)
defineobjectThenewbostonchildraymond = Thenewbostonchild()
defineobjectThenewbostonchildraymond.printfirstname() #return Bucky
defineobjectThenewbostonchildraymond.printlastname() #return Roberts; however, if def printlastname(self): print("Snitzleberg") is uncommented, then return Snitzleberg because Thenewbostonchild(Thenewbostonparent)'s def printlastname(self) overrides Thenewbostonparent() def printlastname(self)
class Mario():
	def __init__(self, playername):
		self.playername = playername
	def move(self):
		print("{} is moving Mario".format(self.playername))
class Shroom(Mario):
	def eatshroom(self):
		print("{} made Mario eat the shroom".format(self.playername))
class BigMario(Shroom):  
#class BigMario(Mario, Shroom):  #error message TypeError: Cannot create a consistent method resolution order (MRO) for bases Mario, Shroom
	def fireflower(self):
		print("{} took the fireflower.  I can fire.".format(self.playername))
raymond = Mario("Raymond")
raymond.move() #return Raymond is moving Mario
edward = Shroom("Edward")
edward.move() #return Edward is moving Mario
edward.eatshroom() #return Edward made Mario eat the shroom
kathy = BigMario("Kathy")
kathy.move() #return Kathy is moving Mario
kathy.eatshroom() #return Kathy made Mario eat the shroom
kathy.fireflower() #return Kathy took the fireflower.  I can fire.
kathy.move() #return Kathy is moving Mario
#raymond.fireflower() #error message AttributeError: 'Mario' object has no attribute 'fireflower'
edward.eatshroom() #return Edward made Mario eat the shroom
edward.move() #return Edward is moving Mario
class Parentclasscar():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	def displaycar(self):
		thecar = "The car is {} {} {}.".format(str(self.year),self.make,self.model)
		return thecar
raymondscar = Parentclasscar("Toyota","Camry",2005)
print(raymondscar.displaycar()) #print The car is 2005 Toyota Camry.
class Childclasscargas(Parentclasscar):
	def __init__(self, make, model, year, gasbrand):
		super().__init__(make, model, year)
		self.gasbrand = gasbrand
	def driveswithwhatgas(self):
		thegascar = "The gas car is {} {} {} driving with {} gas.".format(str(self.year),self.make,self.model,self.gasbrand)
		print(thegascar)
raymonsgascar = Childclasscargas("Toyota","Camry",2005,"Chevron")
print(raymonsgascar.displaycar()) #print The car is 2005 Toyota Camry.
raymonsgascar.driveswithwhatgas() #return The gas car is 2005 Toyota Camry driving with Chevron gas.
class Childclasselectric(Parentclasscar):
	def __init__(self, make, model, year, batterysize):
		super().__init__(make, model, year)
		self.batterysize = batterysize
	def carbatterysize(self):
		thebatterycar = "The battery car is {} {} {} driving with {} battery size.".format(str(self.year),self.make,self.model,self.batterysize)
		print(thebatterycar)
raymondsbatterycar = Childclasselectric("Toyota","Prius","2018",1000)
print(raymondsbatterycar.displaycar()) #print The car is 2018 Toyota Prius.
raymondsbatterycar.carbatterysize() #return The battery car is 2018 Toyota Prius driving with 1000 battery size.
#Instances as attributes or a class is a child to two parent classes
class Batterysize2():
	def __init__(self, batterysize2=702):
		self.batterysize2 = batterysize2
	def displaycarbatterysize(self):
		print("The car has a "+str(self.batterysize2)+ "-kWh battery.")
	def updatedisplaycarbatterysize(self, newbattersize2):
		self.batterysize2 = newbattersize2
class Childclasselectricandbatterysize(Parentclasscar):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.batterysize2 = Batterysize2()
raymondsbatterycar2 = Childclasselectricandbatterysize("Nissan","Leaf",2019)
print(raymondsbatterycar2.displaycar()) #print The car is 2019 Nissan Leaf.
raymondsbatterycar2.batterysize2.displaycarbatterysize() #return The car has a 702-kWh battery.
raymondsbatterycaraudi = Childclasselectricandbatterysize("Audi","e-tron",2020)
raymondsbatterycaraudi.batterysize2 = Batterysize2(2000)
print(raymondsbatterycaraudi.displaycar()) #print The car is 2019 Nissan Leaf.
raymondsbatterycaraudi.batterysize2.displaycarbatterysize() #return The car has a 2000-kWh battery.
raymondsbatterycaraudi.batterysize2.updatedisplaycarbatterysize(12345)
raymondsbatterycaraudi.batterysize2.displaycarbatterysize() #return The car has a 12345-kWh battery.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
emmaemployee = Employee("Emma",11000)
brentperson = Person("Brent","Male")
if isinstance(emmaemployee,Employee):
    print("Yes "+emmaemployee.name+" is an Employee") #print Yes Emma is an Employee
if isinstance(brentperson,Employee):
    print("Yes "+brentperson.name+" is an Employee")
else:
    print("No "+brentperson.name+" is not an Employee") #print No Brent is not an Employee
class Developer(object):
    # Constructor 
    def __init__(self, name): 
        self.name = name
    def display(self): 
        print("Developer:", self.name, "-")
class PythonDeveloper(Developer):
    # Constructor 
    def __init__(self, name, language):
        self.name = name
        self.language = language   
    def display(self): 
        print("Python Developer:", self.name, "language:", self.language, "-")   
dev = Developer("Jhon")  # An Object of Developer 
dev.display()
result = isinstance(dev, Developer)
print("is an instance of a Developer Class? ", result, "\n")  #print Developer: Jhon - is an instance of a Developer Class?  True  
pythonDev = PythonDeveloper("Eric", "Python") # An Object of PythonDeveloper 
pythonDev.display(), 
result = isinstance(pythonDev, Developer)
print("is an instance of a Developer Class? ", result) #print Python Developer: Eric language: Python - is an instance of a Developer Class?  True

#Python With Statement Classes.pdf
#The the __exit__ method as the except in the try except which traps exceptions.  Simple exception is include return True in mycontextmanagertrue class.
#Defining "__enter__" and "__exit__" on your classes, you can give them the ability to work inside of "with" blocks, doing things automatically at the start and finish.  And you can even have them trap exceptions in a semi-automated way, without needing "try" and "except" anywhere around.
class mycontextmanager(object):
	def __enter__(self):
		print("I'm in enter!")
	def __exit__(self, type, value, traceback):
		print("I'm in exit!")
with mycontextmanager() as variablename:
	print("Hello") #print I'm in enter!\n Hello\n I'm in exit!
# with mycontextmanager() as errormessage:
# 	print(10/0) #print I'm in enter!\n I'm in exit!\n ZeroDivisionError: division by zero
class mycontextmanager2(object):
	def __enter__(self):
		print("I'm in enter!")
	def __exit__(self, type, value, traceback):
		print("I'm in exit!")
		print(self)
		print("type={}".format(type))
		print("value={}".format(value))
		print("traceback={}".format(traceback))
# with mycontextmanager2() as errormessage:
# 	print(10/0)
	'''
	I'm in enter!
	I'm in exit!
	<__main__.mycontextmanager2 object at 0x7f9c092ff8d0>
	type=<class 'ZeroDivisionError'>
	value=division by zero
	traceback=<traceback object at 0x7f41748a6588>
	Traceback (most recent call last):
	  File "yywork.py", line 19, in <module>
	    print(10/0) #print I'm in enter!\n I'm in exit!\n ZeroDivisionError: division by zero
	ZeroDivisionError: division by zero
	'''
class mycontextmanagertrue(object):
	def __enter__(self):
		print("I'm in enter!")
	def __exit__(self, type, value, traceback):		
		print("I'm in exit!")
		print(self)
		print("type={}".format(type))
		print("value={}".format(value))
		print("traceback={}".format(traceback))
		return True
with mycontextmanagertrue() as errormessage:
	print(10/0)
	'''
	I'm in enter!
	I'm in exit!
	<__main__.mycontextmanagertrue object at 0x7f828c04a470>
	type=<class 'ZeroDivisionError'>
	value=division by zero
	traceback=<traceback object at 0x7f828c053988>
	'''
#Calling the class and a function
class Chooseafunction():
    def __init__(self, name, singer=""):
        self.name = name
        self.singer = singer
    def runfunctioninsideclass(self, number=""):
        print("runfunctioninsideclass is ran.  self. is the prefix before the functionname.")
        if number:
            print("runfunctioninsideclass is ran has function04 entered {}.".format(number))
    def function04(self):
        print(self.name + " choose function04 fourth function.")
        number = int(input("Choose a number? "))
        print(number)
        self.runfunctioninsideclass(number)
    def function03(self):
        print(self.name + " choose function03 third function.")
        toyvariable = "stickers"
        print("{}'s toy for today is {}.".format(self.name, toyvariable))
    def function02(self):
        print(self.name + " choose function02 second function.")
    def function01(self):
        print(self.name + " choose function01 first function.")
        self.runfunctioninsideclass()
    def function05(self):
        print(self.name + " choose function05 fifth function.")
        self.singerfunction()
    def singerfunction(self):
        print(self.name + " included a singer's name in function05.  self.singerfunction is ran.")
        print(self.singer + " is the singer.")


raymondfunction = Chooseafunction("Raymond")
raymondfunction.function01() #return Raymond choose function01 first function.\n  runfunctioninsideclass is ran.  self. is the prefix before the functionname.
jamesfunction = Chooseafunction("James") #return James choose function02 second function.
jamesfunction.function02()
michellefunction = Chooseafunction("Michelle")
michellefunction.function03() #return Michelle choose function03 third function.\n Michelle's toy for today is stickers.
dadfunction = Chooseafunction("Dad")
dadfunction.function04()
'''
Dad choose function04 fourth function.
Choose a number? 4897
4897
runfunctioninsideclass is ran.  self. is the prefix before the functionname.
runfunctioninsideclass is ran has function04 entered 4897.
'''
momfunction = Chooseafunction("Mom", "Celine Dion")
momfunction.function05() #return Mom choose function05 fifth function.\n Mom included a singer's name in function05.  self.singerfunction is ran.\n Celine Dion is the singer.
paulfunction = Chooseafunction(name="", singer="Paul McCartney")
paulfunction.singerfunction() #return  included a singer's name in function05.  self.singerfunction is ran.\n Paul McCartney is the singer.

class Fruit():
    """A class that makes various tasty fruits."""
    def __init__(self, fruitname, color, flavor, poisonous):
        self.name = fruitname
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
        print("I'm a {} {} and I taste {}.".format(self.color, self.name, self.flavor))
        print("I'm a " + self.color + " " + self.name + " and I taste " + self.flavor)
    def isedible(self):
        if self.poisonous:
            print("Don't eat me!  I'm super poisonous.")
        else:
            print("Yep! I'm edible.")


lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
'''
I'm a yellow lemon and I taste sour.
I'm a yellow lemon and I taste sour.
I'm a yellow lemon and I taste sour
'''
lemon.isedible() #return Yep! I'm edible.

class Animal():
    isalive = True
    addlovescale = 5
    health = "good"
    def __init__(self, name, age, ishungry):
        self.name = name
        self.age = age
        self.ishungry = ishungry
    def classvariables(self):
        print("The lovescale is {} and the health is {} for which self. is required in variables defined in class".format(self.addlovescale, self.health))
    def description(self):
        print(self.name + " is age", self.age)


classvariables = Animal(age=14, ishungry=True, name="Arthur")
classvariables.classvariables() #print The lovescale is 5 and the health is good for which self. is required in variables defined in class
zebra = Animal("Jeffry", 2, True)
zebra.description() #return Jeffry is age 2
print(zebra.name) #print Jeffry
print(zebra.age) #print 2
giraffe = Animal("Bruce", ishungry=False, age=2)
giraffe.description() #return Bruce is age 2
print(giraffe.ishungry) #print False
hippo = Animal("Rebecca", 3, False)
hippo.description() #return Rebecca is age 3
print("Class Animal local variables", hippo.isalive) #print Class Animal local variables True
print("Class Animal local variables", hippo.addlovescale) #print Class Animal local variables 5
print("Class Animal local variables " + hippo.health) #print Class Animal local variables good

class AddItemsInShoppingCart():
    itemsincart = {}
    def __init__(self, customername):
        self.customername = customername
    def additem(self, product, price):
        self.itemsincart[product] = price


rockycart = AddItemsInShoppingCart("Rocky")
rockycart.additem("broccoli", 50)
rockycart.additem("coffee", 10.20)
print(rockycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2}
mapopcart = AddItemsInShoppingCart("Ma")
mapopcart.additem("chocolate", 10)
mapopcart.additem("peas and carrots", 15)
mapopcart = AddItemsInShoppingCart("Pa")
mapopcart.additem("comic book", 1)
print(mapopcart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2, 'chocolate': 10, 'peas and carrots': 15, 'comic book': 1}

class AddItemsInShoppingCart2():
    def __init__(self, customername):
        self.customername = customername
        self.itemsincart = {}
    def additem(self, product, price):
        self.itemsincart[product] = price


rockycart = AddItemsInShoppingCart2("Rocky")
rockycart.additem("broccoli", 50)
rockycart.additem("coffee", 10.20)
print(rockycart.itemsincart) #print {'broccoli': 50, 'coffee': 10.2}
mapopcart = AddItemsInShoppingCart2("Ma")
mapopcart.additem("chocolate", 10)
mapopcart.additem("peas and carrots", 15)
print(mapopcart.itemsincart) #print {'chocolate': 10, 'peas and carrots': 15}
mapopcart = AddItemsInShoppingCart2("Pa")
mapopcart.additem("comic book", 1)
print(mapopcart.itemsincart) #print {'comic book': 1}

#Inheritance