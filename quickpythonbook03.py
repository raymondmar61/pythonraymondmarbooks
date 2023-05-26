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
