#Basics Python Classes Combine All Lessons Learned One Stop Book One Stop Documentation
#thenewbostonallvideos

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
from operator import attrgetter
class User3:
	def __init__(self, name, anumber):
		self.name = name
		self.user_id = anumber
	def __repr__(self):
		return self.name+" : "+str(self.user_id)
users3list = [User3("Bucky", 43),User3("Sally", 5),User3("Tuna", 61),User3("Brian", 2),	User3("Joby", 77),User3("Amanda", 9)]
print(users3list) #print [Bucky : 43, Sally : 5, Tuna : 61, Brian : 2, Joby : 77, Amanda : 9]
print(sorted(users3list,key=attrgetter("name"))) #print [Amanda : 9, Brian : 2, Bucky : 43, Joby : 77, Sally : 5, Tuna : 61]
print(sorted(users3list,key=attrgetter("user_id"))) #print [Brian : 2, Sally : 5, Amanda : 9, Bucky : 43, Tuna : 61, Joby : 77]



