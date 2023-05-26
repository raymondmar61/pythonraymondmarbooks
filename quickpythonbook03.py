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

#Advanced Guide To Python 3 Programming by John Hunt Chapter 30 Threading
#Threading allows you to write programs that multitask.  It appears to do more than one thing at a time.
#The Thread class from the threading module represents an activity which is run in a separate thread of execution within a single process.  These threads of execution are lightweight, pre-emptive execution threads.  A thread is lightweight because it doesn't possess its own address space.  It's not treated as a separate entity by the host operating system.  It's not a process.  Threads exist within a single machine process using the same address space as other threads.
#A thread object created must be started.  A thread object is runnable once the thread object is started.  A thread object may switch back and forth between running and being runnable under the control of the scheduler.  The scheduler is responsible for managing multiple threads which want execution time.
#A thread object remains runnable or running until the run() method terminates.  A Thread may be in a waiting state when a thread is waiting for another thread to finish its work before continuing.  It's possible a thread is waiting because a thread is waiting for the results from another thread to continue.  The results from another thread to continue is achieved using the join() method.  Once the second thread completes the waiting thread becomes runnable.
#The thread currently executing is the active thread.
#A thread is considered to be alive unless its run() method terminates after which a thread is considered dead.  A live thread can be running, runable, waiting, etc.
#The runnable state indicates the thread can be executed by the processor not currently executing because an equal or higher priority process is executing.  The thread must wait until the processor becomes free.  The scheduler can move a thread between the running state and runnable state.
'''
There are two ways in which to initiate a new thread of execution:
1 Pass a reference to a callable object (such as a function or method) into the Thread class constructor. This reference acts as the target for the Thread to execute.
2 Create a subclass of the Thread class and redefine the run() method to perform the set of actions that the thread is intended to do.
'''
'''
Instantiating the Thread Class.  The Thread class can be found in the threading module and therefore must be imported prior to use. The class Thread defines a single constructor that takes up to six optional arguments:  class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)

1 group should be None; reserved for future extension when a ThreadGroup class is implemented.
2 target is the callable object to be invoked by the run() method. Defaults to None, meaning nothing is called.
3 name is the thread name. By default, a unique name is constructed of the form "Thread-N" where N is an integer.
4 args is the argument tuple for the target invocation. Defaults to (). If a single argument is provided the tuple is not required. If multiple arguments are provided then each argument is an element within the tuple.
5 kwargs is a dictionary of keyword arguments for the target invocation.  Defaults to {}.
6 daemon indicates whether this thread runs as a daemon thread or not. If not None, daemon explicitly sets whether the thread is daemonic. If None (the default), the daemonic property is inherited from the current thread.
'''
from threading import Thread
def simpleworker():
    print("Hello")


createnewthread1 = Thread(target=simpleworker) #createnewthread1 executes the function simpleworker.  The main code is executed by the main thread present when the program starts.  There are two threads used which are main and createnewthread1.
createnewthread1.start() #return Hello
'''
The Thread class defines all the facilities required to create an object that can execute within its own lightweight process. The key methods are:
1 start() Start the thread's activity. It must be called at most once per thread object. It arranges for the object's run() method to be invoked in a separate thread of control. This method will raise a RuntimeError if called more than once on the same thread object.
2 run() Method representing the thread's activity. You may override this method in a subclass. The standard run() method invokes the callable object passed to the object’s constructor as the target argument, if any, with positional and keyword arguments taken from the args and kwargs arguments, respectively. You should not call this method directly.
3 join(timeout = None) Wait until the thread sent this message terminates. This blocks the calling thread until the thread whose join()method is called terminates. When the timeout argument is present and not None, it should be a floating-point number specifying a timeout for the operation in seconds (or fractions thereof). A thread can be join()ed many times.
4 name A string used for identification purposes only. It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor. Giving a thread a name can be useful for debugging purposes.
5 ident The "thread identifier" of this thread or None if the thread has not been started. This is a nonzero integer.
6 is_alive() Return whether the thread is alive. This method returns True just before the run() method starts until just after the run() method terminates. The module function threading.enumerate() returns a list of all alive threads.
7 daemon A boolean value indicating whether this thread is a daemon thread (True) or not (False). This must be set before start() is called, otherwise a RuntimeError is raised. Its default value is inherited from the creating thread. The entire Python program exits when no alive non-daemon threads are left.
'''
createnewthread2 = Thread(target=simpleworker) #createnewthread2 executes the function simpleworker.  The main code is executed by the main thread present when the program starts.  There are two threads used which are main and createnewthread2.
createnewthread2.start() #return Hello
print(createnewthread2.getName()) #print Thread-2
print(createnewthread2.ident) #print 139858093799168
print(createnewthread2.is_alive()) #print False
#The join() method causes one thread to wait for another to complete.
from time import sleep
def workerfunction():
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(1)


print("Start")
readobject = Thread(target=workerfunction)
readobject.start()
readobject.join() #return ..........
print("\nDone")
def workerfunction(sleepnumber):
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(sleepnumber)


print("Start")
readobject1 = Thread(target=workerfunction(1))
readobject1.start()
readobject1.join() #return ..........
print("\nDone")
print("Start")
readobject0 = Thread(target=workerfunction(0))
readobject0.start()
readobject0.join() #return ..........
print("\nDone")
'''
The Threading Module Functions.  There are a set of threading module functions which support working with
threads; these functions include:
1 threading.active_count() Return the number of Thread objects currently alive. The returned count is equal to the length of the list returned by enumerate().
2 threading.current_thread() Return the current Thread object, corresponding to the caller’s thread of control. If the caller’s thread of control was not created through the threading module, a dummy thread object with limited functionality is returned.
3 threading.get_ident() Return the "thread identifier" of the current thread. This is a nonzero integer. Thread identifiers may be recycled when a thread exits and another thread is created.
4 threading.enumerate() Return a list of all Thread objects currently alive. The list includes daemon threads, dummy thread objects created by current_thread() and the main thread. It excludes terminated threads and threads that have not yet been started.
5 threading.main_thread()Return the main Thread object.
'''
def workerfunctionarguments(sleepnumber, letter):
    for i in range(0, 10):
        print(letter, end="", flush=True)
        sleep(sleepnumber)


print("Start")
thread1A = Thread(target=workerfunctionarguments, args=[1, "A"])
thread0B = Thread(target=workerfunctionarguments(0, "B"))
thread1C = Thread(target=workerfunctionarguments, args=[1, "C"])
thread2D = Thread(target=workerfunctionarguments(2, "D"))
thread1A.start()
thread0B.start()
thread1C.start()
thread2D.start()
print("Done")
'''
Start
BBBBBBBBBBDDDDDDDDDDACDone
CAACACACACACCAACA
#or
Start
BBBBBBBBBBDDDDDDDDDDACDone
CACACACAACACCACACA
'''
#The main thread is finished after the worker threads have only printed out a single letter each; however as long as there is at least one non-daemon thread running the program will not terminate; as none of these threads are marked as a daemon thread the program continues until the last thread has finished printing out the tenth of its letters. Also notice how each of the threads gets a chance to run on the processor before it sleeps again; thus we can see the letters A, B and C [and D] all mixed in together.
#Daemon Thread used for housekeeping tasks such as background data and backups.
def workerfunctiondaemon(sleepnumber, letter):
    for i in range(0, 10):
        print(letter, end="", flush=True)
        sleep(sleepnumber)


print("Start daemon")
daemonthread1A = Thread(daemon=True, target=workerfunctiondaemon, args=[1, "A"])
daemonthread0B = Thread(daemon=True, target=workerfunctiondaemon, args=[0, "B"])
daemonthread1C = Thread(daemon=True, target=workerfunctiondaemon, args=[1, "C"])
daemonthread1A.start()
daemonthread0B.start()
daemonthread1C.start()
print("Done daemon")
'''
Start daemon
ABBBBBBBBBBCDone daemon
'''
#Naming Threads assign a name to a thread
def workerfunctionnaming(sleepnumber, letter):
    for i in range(0, 10):
        print(letter, end="", flush=True)
        sleep(sleepnumber)


print("Start naming")
namingthread1A = Thread(name="1A", target=workerfunctionnaming, args=[1, "A"])
namingthread0B = Thread(name="0B", target=workerfunctionnaming, args=[0, "B"])
namingthread1C = Thread(name="1C", target=workerfunctionnaming, args=[1, "C"])
namingthread1A.start()
namingthread0B.start()
namingthread1C.start()
print("Done naming")
'''
Start naming
ABBBBBBBBBBCDone naming
CAACAACCCAACACCAACCAACCAACCACACAAACC
'''
#Each Thread requires its own copy of the data.  The shared memory or heap is difficiult to use as it's inherently shared between all threads.  Python provides a concept known as Thread-Local data whose values are associated with a thread instead of shared memory.  To create a thread-local data, create an instance of threading.local and store attributes into it.  The instances are thread specific.  One thread doesn't see the values stored by another thread.
from threading import Thread, local, currentThread
from random import randint
def showvaluefunction(data):
    """Access a value in the thread local data object value is present or not present with the try except"""
    try:
        valuevariable = data.value
    except AttributeError:
        print(currentThread().name, "no value yet.")
    else:
        print(currentThread().name, "yes there is a value which is", valuevariable)
def workerfunction(data):
    """Calls showvaluefunction() twice.  Once before it sets a data.value in the local data object and after it sets a data.value in the local data object."""
    showvaluefunction(data)
    data.value = randint(1, 100)
    print(currentThread().name, "at workerfunction random number is", data.value)
    showvaluefunction(data)
print("Start", currentThread().name)
localdata = local() #Create a local data object using local() function
showvaluefunction(localdata) #Call showvaluefunction().  Create two threads to execute the worker function passing the localdata object into the two threads.  Each thread is started.
for i in range(0, 4):
    threadobject = Thread(name="Thread name" + str(i), target=workerfunction, args=[localdata])
    threadobject.start()
showvaluefunction(localdata)
print("Done", currentThread().name)
'''
Start MainThread
MainThread no value yet.
Thread name0 no value yet.
Thread name0 at workerfunction random number is 92
Thread name0 yes there is a value which is 92
Thread name1 no value yet.
Thread name1 at workerfunction random number is 23
Thread name1 yes there is a value which is 23
Thread name2 no value yet.
Thread name2 at workerfunction random number is 58
Thread name2 yes there is a value which is 58
Thread name3 no value yet.
Thread name3 at workerfunction random number is 78
Thread name3 yes there is a value which is 78
MainThread no value yet.
Done MainThread
'''
#The Global Interpreter Lock or GIL protects access to Python objects by preventing multiple threads from executing at the same time.  No need to worry about the GIL when running low level programs.  GIL prevents multithreaded Python programs from taking full advantage of multiprocessor systems.  Python acts like a single CPU machine running one thing at a time.  It's impossible for standard Python threads to take advantage of multiple CPUs.  A solution is to use Python multiprocessing library.