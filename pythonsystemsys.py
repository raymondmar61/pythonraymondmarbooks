import sys

#Python 3 Programming Tutorial - Sys Module-rLG7Tz6db0w
sys.stderr.write("pronounced s-t-err for errors\n") #return pronounced s-t-err for errors
sys.stderr.flush()
sys.stdout.write("pronounced s-t-out for output\n") #return pronounced s-t-out for output
print(sys.argv)  #print ['yytest.py', 'Sentence typed on terminal.']  Returns file name and more.  Typed python3.8 yytest.py "Sentence typed on terminal." on prompt mar@mar-VirtualBox:~/python$.  mar@mar-VirtualBox:~/python$ python3.8 yytest.py "Sentence typed on terminal."   Pronounced arg-v.
print(type(sys.argv)) #print <class 'list'>
print(len(sys.argv)) #print 2
if len(sys.argv) > 1:
    print(sys.argv[1]) #print Sentence typed on terminal.
    sys.argv[1] = 5.67 #change Sentence typed on terminal. to number 5 for math problem (float(sys.argv[1]) + 5)
    print(float(sys.argv[1]) + 5) #print 10.67
def returnarv(argument):
    print(argument) #print 5.67 RM:  I changed sys.argv[1] from Sentence typed on terminal. to 5.67.


returnarv(sys.argv[1])

#Python modules  - sys-qZy9pb5BCsU
'''
sys.platform Platform type.  Prints the platform Python code is running.
sys.copyright Interpreter copyright.  Prints the copyrights like copyrights from books, movies, food names.
sys.version Interpreter Python version.  Prints Python version, build number, and compiler.
sys.stdout.write(string) Print a statement.  Output a statement.  It's like a print statement.
sys.stderr.write(string) Print an error.  Output a standard error.
sys.getsizeof(variable) Get variable size in bytes
sys.argv List of command CMD line arguments passed to a Python script.  The file name is the first argument in sys.argv.
'''

print(sys.platform) #print linux
print(sys.copyright)
'''
Copyright (c) 2001-2020 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
'''
print(sys.version)
'''
3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0]
'''
sys.stdout.write("No print statement for sys.stdout.write()\n")
sys.stderr.write("No print statement for sys.stderr.write()\n")
variableinteger = 15
variablefloat = 12.78
variablestring = "Hello there"
variablelist = ["list", 123, 123.456]
print(sys.getsizeof(variableinteger)) #print 28
print(sys.getsizeof(variablefloat)) #print 24
print(sys.getsizeof(variablestring)) #print 60
print(sys.getsizeof(variablelist)) #print 80
print(sys.argv) #mar@mar-VirtualBox:~/python$ python3.8 yytest.py argument2 argument3 argument4 159 print ['yytest.py', 'argument2', 'argument3', 'argument4', '159']
sysargvargumentslist = sys.argv
print("Hello file name " + sysargvargumentslist[0] + " the arguments two to four are " + sysargvargumentslist[1] + " " + sysargvargumentslist[2] + " and " + sysargvargumentslist[3] + ".  The number is " + sysargvargumentslist[4] + ".") #print Hello file name yytest.py the arguments two to four are argument2 argument3 and argument4.  The number is 159.

#Python [sys] 01 Basic Information-7OrSEpv26D8
print(sys.executable) #print /usr/bin/python3.8.  Python interpreter file location.
print(sys.builtin_module_names) #print ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_csv', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_socket', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zlib').  A tuple of modules or libraries built-in.

#Python [sys] 02 Module Madness-RNOuiYYgPSU
print(sys.modules)
'''
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'posix': <module 'posix' (built-in)>, '_thread': <module '_thread' (built-in)>, '_weakref': <module '_weakref' (built-in)>, 'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' from '/usr/lib/python3.8/codecs.py'>, 'encodings.aliases': <module 'encodings.aliases' from '/usr/lib/python3.8/encodings/aliases.py'>, 'encodings': <module 'encodings' from '/usr/lib/python3.8/encodings/__init__.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/usr/lib/python3.8/encodings/utf_8.py'>, '_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' from 'yytest.py'>, 'encodings.latin_1': <module 'encodings.latin_1' from '/usr/lib/python3.8/encodings/latin_1.py'>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' from '/usr/lib/python3.8/abc.py'>, 'io': <module 'io' from '/usr/lib/python3.8/io.py'>, . . .}.  Every module you can import from your Python script.  It's a dictionary.
'''
print(sys.modules.keys) #print <built-in method keys of dict object at 0x7fa0f80ebd00>
print(sys.modules.keys()) #print dict_keys(['sys', 'builtins', '_frozen_importlib', '_imp', '_warnings', '_frozen_importlib_external', '_io', 'marshal', 'posix', '_thread', '_weakref', 'time', 'zipimport', '_codecs', 'codecs', 'encodings.aliases', 'encodings', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', '_abc', 'abc', 'io', '_stat', 'stat', '_collections_abc', 'genericpath', 'posixpath', 'os.path', 'os', '_sitebuiltins', '_locale', '_bootlocale', 'types', 'importlib._bootstrap', 'importlib._bootstrap_external', 'warnings', 'importlib', 'importlib.machinery', 'importlib.abc', '_operator', 'operator', 'keyword', '_heapq', 'heapq', 'itertools', 'reprlib', '_collections', 'collections', '_functools', 'functools', 'contextlib', 'importlib.util', 'mpl_toolkits', 'apport_python_hook', 'sitecustomize', 'site'])
#print(sys.modules.has_key("time")) #print AttributeError: 'dict' object has no attribute 'has_key'.  Must run Python2.7
import xyvariables  #Python file xyvariables.py created
#print(sys.modules.has_key("xyvariables")) #print True.  Must run Python2.7
print(xyvariables.x) #print 4
print(xyvariables.y) #print 5
from xyvariables import *
print(x) #print 4
print(y) #print 5
import xyvariables as xy
print(xy.x) #print 4
print(xy.y) #print 5

#Python [sys] 03 Platform-ebxzI7f55tw

#Python [sys] 04 Windows Version-Zc3O7wsVeXw

#Python [sys] 05 Exit Codes-uWEiep-ksDo
print("Hello")
name = input("What is your name? ")
print(name)
if name == "Raymond":
    print("I have the same name as you")
    sys.exit(2)
else:
    print("Our names don't match")
    sys.exit(0)
'''
marmar-VirtualBox:~/python$ python3.8 yytest.py 
Hello
What is your name? adsfasd
adsfasd
Our names don't match
mar@mar-VirtualBox:~/python$ echo $?
0
mar@mar-VirtualBox:~/python$ python3.8 yytest.py 
Hello
What is your name? Raymond
Raymond
I have the same name as you
mar@mar-VirtualBox:~/python$ echo $?
2
'''
print("No sys.exit")
name = input("What is your name? ")
print(name)
if name == "Operation":
    print("I have the same name as you")
    exit(2)
else:
    print("Our names don't match")
    exit(0)
'''
mar@mar-VirtualBox:~/python$ python3.8 yytest.py 
No sys.exit
What is your name? Operation
Operation
I have the same name as you
mar@mar-VirtualBox:~/python$ echo $?
2
mar@mar-VirtualBox:~/python$ python3.8 yytest.py 
No sys.exit
What is your name? qpeoiruqwpeirowr
qpeoiruqwpeirowr
Our names don't match
mar@mar-VirtualBox:~/python$ echo $?
0
'''

#Python [sys] 06 Streams-C6CfFNsJ0Sg
import sys
import string

name = input("What is your name? ")
print(name)
for digit in string.digits:
    if digit in name:
        sys.stderr.write("You have numbers in your name.\n")
        sys.stderr.flush()  #flush standard error
        exit(2)
        '''
        Type echo $? to get the exit code or error status:
        mar@mar-VirtualBox:~/python$ python3.8 yytest.py
        What is your name? 23
        23
        You have numbers in your name.
        mar@mar-VirtualBox:~/python$ echo $?
        2
        '''
print(name + ", you have a good name")
exit(0)
#exit("Zero is a number I see if a string is error outputted")  #RM:  it seems if exit is a string, then the string is outputted immediately.
'''
Type echo $? to get the exit code or error status:
mar@mar-VirtualBox:~/python$ python3.8 yytest.py
What is your name? Raymond
Raymond
Raymond, you have a good name
mar@mar-VirtualBox:~/python$ echo $?
0
'''

#Python [sys] 07 Command-line Arguments-DCxYAYzTWOI
#arg is arguments. v is values.
print(sys.argv) #print [yytest.py]  RM:  print filename
print(type(sys.argv)) #print <class 'list'>
'''
mar@mar-VirtualBox:~/python$ python3.8 yytest.py what youtube
['yytest.py', 'what', 'youtube']
<class 'list'>
'''
if len(sys.argv) < 3:
    sys.stderr.write("Error:  usage " + sys.argv[0] + " <input filename> <input word to search in filename>\n")
    sys.stderr.flush() #flush standard error
    exit(22)
    '''
    mar@mar-VirtualBox:~/python$ python3.8 yytest.py findtheneedle.txt
    ['yytest.py', 'findtheneedle.txt']
    <class 'list'>
    Error:  usage yytest.py <input filename> <input word to search in filename>
    mar@mar-VirtualBox:~/python$ echo $?
    22
    '''
else:
    filename = sys.argv[1]
    needleorfindtheword = sys.argv[2]
counter = 0
filehandle = open(filename)
for line in filehandle.readlines():
    line = line.replace("\n", " ") #replace paragraph mark with single space
    words = line.split(" ")
    for eachwords in words:
        if eachwords == needleorfindtheword:
            counter += 1
print(counter)
'''
mar@mar-VirtualBox:~/python$ python3.8 yytest.py findtheneedle.txt done
['yytest.py', 'findtheneedle.txt', 'done']
<class 'list'>
3
'''

#Python [sys] 08 Conclusion-OmngfOjyzJc
'''
Instructor says I taught the basics.  Rest user can learn.
The sys module is getting information, learning your environment, knowing where you code is actually running, platform running executed, python version being used, where modules stored, python interpreter is located.
'''

#Command Line Arguments in Python programming language (sys module, sys.argv[] string list)-R2_beoINHe4
number = 1
if len(sys.argv) == 2:
    print("Python file name first argument " + sys.argv[0])
    print("Number inputted second argument " + sys.argv[1])
    number = int(sys.argv[1])
for i in range(number):
    print("Hello world " + str(i))
'''
mar@mar-VirtualBox:~/python$ python3.8 yytest.py
Hello world 0
mar@mar-VirtualBox:~/python$ python3.8 yytest.py 3
Python file name first argument yytest.py
Number inputted second argument 3
Hello world 0
Hello world 1
Hello world 2
'''

#01 sys argv-K0gEgFy3Q9A
print(sys.argv)
print(type(sys.argv))
'''
mar@mar-VirtualBox:~/python$ python3.8 yytest.py 1 2 3
['yytest.py', '1', '2', '3']
<class 'list'>
mar@mar-VirtualBox:~/python$ python3.8 yytest.py
['yytest.py']
<class 'list'>
'''
year = sys.argv[1]
sortdirection = sys.argv[2]
print(year)
print(sortdirection)
'''
mar@mar-VirtualBox:~/python$ python3.8 yytest.py 1927 ascending
['yytest.py', '1927', 'ascending']
<class 'list'>
1927
ascending
'''
#error message arguments are null #return IndexError: list index out of range
#year = sys.argv[1]
#sortdirection = sys.argv[2]
'''
mar@mar-VirtualBox:~/python$ python3.8 yytest.py
['yytest.py']
<class 'list'>
Traceback (most recent call last):
  File "yytest.py", line 14, in <module>
    year = sys.argv[1]
IndexError: list index out of range
'''
