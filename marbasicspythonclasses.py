#Basics Python Classes Combine All Lessons Learned One Stop Book One Stop Documentation
#thenewbostonallvideos
#williamfisetallvideos
#pythoncrashcourse

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