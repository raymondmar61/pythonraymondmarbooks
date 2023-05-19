#The Quick Python Book by Naomi Ceder Chapter 10 Modules And Scoping Rules
#A module is a file containing code.  A module defines a group of Python functions or other objects.  The name of the module is derived from the name of the file.
import mymath #import mymath is from the file mymath.py in the same directory.
mymathmodulepivariable = mymath.pi
print(mymathmodulepivariable) #print 3.14159
print(mymath.area(2)) #print 12.56636
print(mymath.__doc__) #print my math our example math module
print(mymath.area.__doc__) #print area(r):  returns the area of a circle with radius r.
import importlib
print(importlib.reload(mymath)) #print <module 'mymath' from '/home/mar/python/mymath.py'>
from mymath import area
print(area(2)) #print 12.56636
print(area(20)) #print 1256.636
from mymath import *
print(area(10)) #print 314.159
import sys
print(sys.path) #print ['/home/mar/python', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/mar/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages'] #A list of directories Python searches in the list order to execute an import statement.  Python looks for modules in the directories returned.

#The Quick Python Book by Naomi Ceder Chapter 11 Python Programs
import sys
def main():
    print("This is our first test script file")
    print(sys.argv)


main() #return This is our first test script file\n ['yytest.py']

def mainfilereplace():
    contents = sys.stdin.read()
    sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2])) #replaces first argument with second argument


#mainfilereplace()