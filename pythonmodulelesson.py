#Modules provide separate namespaces for which variables are defined.  Modules provide separate files for which we can divide our work.  We put class, function, and variable definitions into a separate file.  A module is a file containing Python variable, function, and class definitions.
#Type x=100 in Python file module100.py.  Type import module100 in pythonmodulelesson.py.  The import module100 define a new variable of type module named module100 in the current namespace.  In the module module100.py x=100 creates a global variable named x.  Import module100.py into pythonmodulelesson.py, no such variable exists.  We have an attribute x attached to our variable module100.py.  Global variables defined inside a module are visible as attributes outside the module.  Global is misleading.  Global refers to a variable visible everywhere within a file, not necessarily everywhere within a program.

import module100 as m

print(m.x) #print 100
print(m) #print <module 'moduleonehundred' from '/home/mar/python/moduleonehundred.py'>
