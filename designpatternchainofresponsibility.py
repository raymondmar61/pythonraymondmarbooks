#Chain Of Responsibility Design Pattern Python.pdf
#The design pattern is a number of objects can handle a situation.  Each object is given a chance in a set order.  The first object to act is also the last object to act.  There are situations we encounter the behavior:  attribute lookup in Python instance, class, parent(s), and object for which Python finds an object with the named attribute retrieving the value and stop looking, exception handling, GUIs, and web pages.  The design pattern is like a big if-then-else decision chain.  The difference is the identities of the objects handling these events and the order in which the objects are registered.

#First, we need handler classes for which each implements the same method.  We want each handler to decide whether it can handle it and stop the chain or can't handle it and invoke the next handle.
# h1.handle()
# h2.handle()
# h3.handle()
#In other words, h1.handle() and know that h1, h2, or h3 completed the Python code.  We don't care which h1, h2, or h3.  Each handler object needs to be told who is the next one in line.  h1 tries to handle the Python code.  If h1 can't, then h1 asks h2 which was set to be next.  If h2 can't handle the Python code, then h2 asks h3 which was set to be next.  The chain stops at h3 because h3 doesn't have any next handler defined.
# h1.setnext(h2)
# h2.setnext(h3)
# h1.handle()
#RM:  or is it
# h1.handle()
# h1.setnext(h2)
# h2.setnext(h3)
#A travel example,  I use the cheapest form of transportation.  Different types of vehicles are appropriate for different distances.  Walk for 2km.  Drive for 30km.  Train for 200km.  Fly for greater than 200km.
# walkhandler = Walk()
# drivehandler = Drive()
# walkhandler.setnext(drivehandler)
# trainhandler = Train()
# drivehandler.setnext(trainhandler)
# planehandler = Plane()
# trainhandler.setnext(planehandler)

class Handler:
    def __init__(self):
        self.nexthandler = None
        print("init self.nexthandler " + str(self.nexthandler))
    def setnext(self, nexthandler):
        self.nexthandler = nexthandler
        print("setnext method self.nexthandler " + str(self.nexthandler))
class Walk(Handler):
    def handle(self, distance):
        print("Walk class Maybe we should walk")
        if distance > 2:
            if self.nexthandler:
                print("if self.nexthandler Walk")
                return self.nexthandler.handle(distance)
            else:
                return "Walk None"
class Drive(Handler):
    def handle(self, distance):
        print("Drive class Maybe we should drive")
        if distance > 30:
            if self.nexthandler:
                print("if self.nexthandler Drive")
                return self.nexthandler.handle(distance)
            else:
                return "Drive None"
class Train(Handler):
    def handle(self, distance):
        print("Train class Maybe we should train")
        if distance > 200:
            if self.nexthandler:
                print("if self.nexthandler Train")
                return self.nexthandler.handle(distance)
            else:
                return "Trane None"
class Plane(Handler):
    def handle(self, distance):
        print("Plane class Maybe we should fly")
        if distance > 200:
            if self.nexthandler:
                print("if self.nexthandler Plane")
                return self.nexthandler.handle(distance)
            else:
                return "Plane None"


walkhandler = Walk()
drivehandler = Drive()
walkhandler.setnext(drivehandler)
trainhandler = Train()
drivehandler.setnext(trainhandler)
planehandler = Plane()
trainhandler.setnext(planehandler)

print(walkhandler.handle(1))
'''
init self.nexthandler None
init self.nexthandler None
setnext method self.nexthandler <__main__.Drive object at 0x7f6517bc6370>
init self.nexthandler None
setnext method self.nexthandler <__main__.Train object at 0x7f6517bcbaf0>
init self.nexthandler None
setnext method self.nexthandler <__main__.Plane object at 0x7f6517c21a90>
Walk class Maybe we should walk
None
'''
print(walkhandler.handle(150))
'''
Walk class Maybe we should walk
if self.nexthandler Walk
Drive class Maybe we should drive
if self.nexthandler Drive
Train class Maybe we should train
None
'''
print(walkhandler.handle(1000))
'''
Walk class Maybe we should walk
if self.nexthandler Walk
Drive class Maybe we should drive
if self.nexthandler Drive
Train class Maybe we should train
if self.nexthandler Train
Plane class Maybe we should fly
Plane None
'''
#Each object has a responsibility to make them easier to write, understand, and debug.  Also, we can modify the chain.  For example, the trains are on strike or it's raining.  We can run drivehandler.setnext(planehandler) while adjust the responsibility at run time.
