#Basics Python Classes Combine All Lessons Learned One Stop Book One Stop Documentation
#thenewbostonallvideos
#williamfisetallvideos
#next video

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

