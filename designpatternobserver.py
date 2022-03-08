#Python Observer Design Pattern.pdf
#You have an object whose state changes.  Other objects want to know when the state changes.  An Observer object looks at the subject and informs whoever wants to be updated.
#For example, a Person object with a name attribute.  We want to know each time the user changes their name.  Log the change to a file.  Example uses a settler method which is unpythonic.
#The class introduces a tight coupling between the Person object and the logfile.  Why is the logfile in the Person class?  Why is the person needs to update the logfile each time?  What if I want to write things to two different logfiles and services?
class Personsettlermethod:
    def __init__(self, name, logfile):
        self.name = name
        self.logfile = logfile
    def getname(self):
        print("getname method")
        return self.name
    def setname(self, newname):
        print("setname method")
        oldname = self.name
        self.name = newname
        with open(self.logfile, "a") as fileobject:
            fileobject.write(f"updated {oldname} to {newname}\n")

#The Observer pattern solves the problem.  The Person class no longer hardcodes a logfile attribute.  The logfile has an attribute observers which is a list of objects which want to be notified when something changed.  We create a notify method which invokes notify on each attached object.  Each observer object implements a notify method and accepts a message object.
class Personobserver:
    def __init__(self, name):
        self.name = name
        self.observers = []
        print(self.name)
        print(self.observers)
    def getname(self):
        print("1get getname method in Person class")
        self.notify(f"get name returned {self.name} from getname method in Person class")
        return self.name
    def setname(self, newname):
        print("1set setname method in Person class")
        oldname = self.name
        self.name = newname
        self.notify(f"set name from {oldname} to {newname}")
    def notify(self, message):
        print("2 notify method in Person class")
        for oneobserver in self.observers:
            oneobserver.notify(message)
class FileLogger:
    def __init__(self, filename):
        self.filename = filename
    def notify(self, message):
        print("3 notify method in FileLogger class")
        with open(self.filename, "a") as fileobject:
            fileobject.write(f"{message}\n")
class ScreenLogger:
    def notify(self, message):
        print("4a notify method in ScreenLogger class")
        print(f"4b ScreenLogger: {message}")


personone = Personobserver("Raymond")
personone.observers.append(FileLogger("personlog.txt"))
personone.observers.append((ScreenLogger()))
print("print getname method " + personone.getname())
personone.setname("Haku")
print("print setname method " + personone.getname())
'''
[]
1get getname method in Person class
2 notify method in Person class
3 notify method in FileLogger class
4a notify method in ScreenLogger class
4b ScreenLogger: get name returned Raymond from getname method in Person class
print getname method Raymond
1set setname method in Person class
2 notify method in Person class
3 notify method in FileLogger class
4a notify method in ScreenLogger class
4b ScreenLogger: set name from Raymond to Haku
1get getname method in Person class
2 notify method in Person class
3 notify method in FileLogger class
4a notify method in ScreenLogger class
4b ScreenLogger: get name returned Haku from getname method in Person class
print setname method Haku
'''

#Add register and deregister method for additional observers.
class Personregisterderegister:
    def __init__(self, name):
        self.name = name
        self.observers = []
        print(self.name)
        print(self.observers)
    def getname(self):
        print("1get getname method in Person class")
        self.notify(f"get name returned {self.name} from getname method in Person class")
        return self.name
    def setname(self, newname):
        print("1set setname method in Person class")
        oldname = self.name
        self.name = newname
        self.notify(f"set name from {oldname} to {newname}")
    def notify(self, message):
        print("2 notify method in Person class")
        for oneobserver in self.observers:
            oneobserver.notify(message)
    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
class FileLogger:
    def __init__(self, filename):
        self.filename = filename
    def notify(self, message):
        print("3 notify method in FileLogger class")
        with open(self.filename, "a") as fileobject:
            fileobject.write(f"{message}\n")
class ScreenLogger:
    def notify(self, message):
        print("4a notify method in ScreenLogger class")
        print(f"4b ScreenLogger: {message}")


persontwo = Personregisterderegister("Buster")
filelogtwo = FileLogger("personlog.txt")
persontwo.attach(filelogtwo)
print("print getname method " + persontwo.getname())
persontwo.attach(ScreenLogger())
persontwo.setname("Posey")
persontwo.detach(persontwo)
print("print getname method after setname " + persontwo.getname())
'''
Buster
[]
1get getname method in Person class
2 notify method in Person class
3 notify method in FileLogger class
print getname method Buster
1set setname method in Person class
2 notify method in Person class
3 notify method in FileLogger class
4a notify method in ScreenLogger class
4b ScreenLogger: set name from Buster to Posey
1get getname method in Person class
2 notify method in Person class
3 notify method in FileLogger class
4a notify method in ScreenLogger class
4b ScreenLogger: get name returned Posey from getname method in Person class
print getname method after setname Posey
'''