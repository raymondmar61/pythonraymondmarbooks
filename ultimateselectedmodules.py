import importfile
#import a file with objects; import python file importfile.py
xis4 = importfile.x
yis5 = importfile.y
print(xis4) #print 4
print(yis5) #print 5
from importfile import *
print(x) #print 4
print(y) #print 5
import importfile as ifxy
print(ifxy.x) #print 4
print(ifxy.y) #print 5

import pickle
#Pickle module write to a file and read from a file
studentsgradesdictionarylist = {"andy": ["A", "A", "B"], "laura": ["B", "B", "A"], "sam": ["A", "B", "C"]}
print(studentsgradesdictionarylist) #print {'andy': ['A', 'A', 'B'], 'laura': ['B', 'B', 'A'], 'sam': ['A', 'B', 'C']}
filename = "writetotextfile.txt"
with open(filename, "wb") as writefileobject: #wb write binary
    pickle.dump(studentsgradesdictionarylist, writefileobject) #create text file filename with studentsgradesdictionarylist
    '''
    8004 953e 0000 0000 0000 007d 9428 8c04
    616e 6479 945d 9428 8c01 4194 6803 8c01
    4294 658c 056c 6175 7261 945d 9428 6804
    6804 6803 658c 0373 616d 945d 9428 6803
    6804 8c01 4394 6575 2e
    '''
with open(filename, "rb") as readfileobject: #rb read binary
    #pickle.load(readfileobject)
    print(pickle.load(readfileobject)) #print {'andy': ['A', 'A', 'B'], 'laura': ['B', 'B', 'A'], 'sam': ['A', 'B', 'C']}
with open(filename, "wb") as editfileobject:
    studentsgradesdictionarylist["andy"][1] = "A*"
    pickle.dump(studentsgradesdictionarylist, editfileobject)
with open(filename, "rb") as readfileobject: #rb read binary
    loadfilepickle = pickle.load(readfileobject)
    print(loadfilepickle) #print {'andy': ['A', 'A*', 'B'], 'laura': ['B', 'B', 'A'], 'sam': ['A', 'B', 'C']}
#Open text file with pickle returns an error MemoryError
# with open("moby01.txt", "rb") as readmoby01object:
#     print(pickle.load(readmoby01object)) #print MemoryError
studentsgradesdictionarylist = {"andy": ["A", "A", "B"], "laura": ["B", "B", "A"], "sam": ["A", "B", "C"]}
with open("savepicklefile.pickle", "wb") as writefileobject:
    pickle.dump(studentsgradesdictionarylist, writefileobject) #create pickle file savepicklefile.pickle
    '''
    8004 953e 0000 0000 0000 007d 9428 8c04
    616e 6479 945d 9428 8c01 4194 6803 8c01
    4294 658c 056c 6175 7261 945d 9428 6804
    6804 6803 658c 0373 616d 945d 9428 6803
    6804 8c01 4394 6575 2e
    '''
with open("savepicklefile.pickle", "rb") as readfileobject:
    print(pickle.load(readfileobject)) #print {'andy': ['A', 'A', 'B'], 'laura': ['B', 'B', 'A'], 'sam': ['A', 'B', 'C']}
studentsgradespkldictionarylist = {"andypkl": ["A", "A", "B"], "laurapkl": ["B", "B", "A"], "sampkl": ["A", "B", "C"]}
with open("savepklfile.pkl", "wb") as writefileobject:
    pickle.dump(studentsgradespkldictionarylist, writefileobject) #create pickle file savepklfile.pickle
    '''
    8004 953e 0000 0000 0000 007d 9428 8c04
    616e 6479 945d 9428 8c01 4194 6803 8c01
    4294 658c 056c 6175 7261 945d 9428 6804
    6804 6803 658c 0373 616d 945d 9428 6803
    6804 8c01 4394 6575 2e
    '''
with open("savepklfile.pkl", "rb") as readfileobject:
    print(pickle.load(readfileobject)) #print {'andypkl': ['A', 'A', 'B'], 'laurapkl': ['B', 'B', 'A'], 'sampkl': ['A', 'B', 'C']}
#Storing and retrieving Python objects with pickle
dictionarynumber = {"a": 1, "b": 2, "c": 3}
serializationstring = pickle.dumps(dictionarynumber)
print(serializationstring) #print b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.'
deserializationstring = pickle.loads(serializationstring)
print(deserializationstring) #print {'a': 1, 'b': 2, 'c': 3}
with open("dictionarynumberpklfile.pkl", "wb") as writefileobject:
    pickle.dump(dictionarynumber, writefileobject)
    '''
    8004 9517 0000 0000 0000 007d 9428 8c01
    6194 4b01 8c01 6294 4b02 8c01 6394 4b03
    752e 
    '''
with open("dictionarynumberpklfile.pkl", "rb") as readfileobject:
    openpicklefile = pickle.load(readfileobject)
    print(openpicklefile) #print {'a': 1, 'b': 2, 'c': 3}

import subprocess
listfiles = subprocess.run(["ls", "-l"]) #type and execute ls -l in terminal
listfilesneedprintfunction = subprocess.run(["ls", "-l"], capture_output=True)
print(listfilesneedprintfunction) #print CompletedProcess(args=['ls', '-l'], returncode=0, stdout=b'total 215520\n-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf\n-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt\n-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv\n-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json\n-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv\n-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py\n-rw-rw-rw- 1 mar mar . . .
print(listfilesneedprintfunction.stdout) #print b'total 215520\n-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf\n-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt\n-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv\n-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json\n-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv\n-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py\n-rw-rw-rw- 1 mar mar . . .
print(listfilesneedprintfunction.stdout.decode())
'''
total 215520
-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf
-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt
-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv
-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json
-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv
-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py
...
'''
listfilesneedprintfunction = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(listfilesneedprintfunction.stdout)
'''
total 215520
-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf
-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt
-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv
-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json
-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv
-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py
...
'''
listfilesneedprintfunction = subprocess.run(["ls", "-l"], shell=True, capture_output=True, text=True)
print(listfilesneedprintfunction.stdout)
'''
56_power_query_tutorials.pdf
accountscreatetextfile.txt
accountscsvfile.csv
accountsjson.json
Admission_Predict_Ver1.1.csv
advancedguidepythonprogrammingasyncio.py
'''
listfilesneedprintfunction = subprocess.run(["ls", "-l"], shell=True, text=True)
print(listfilesneedprintfunction.stdout) #print None
listfilesneedprintfunctionpipe = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
print(listfilesneedprintfunctionpipe.stdout)
'''
56_power_query_tutorials.pdf                      generatepasswords.py                      pythondataanalyticsvisualization05timeseries.py
 accountscreatetextfile.txt                   Im1.jpg                               pythondataanalyticsvisualization06interactingwithdatabases.py
 accountscsvfile.csv                          Im2.png                               pythondataanalyticsvisualization07dataanalysisapplicationexamples.py
 accountsjson.json                        imagename1.jpeg                           pythonforprogrammersbasics02.py
 Admission_Predict_Ver1.1.csv                     imagename2.png                            pythonforprogrammersbasics.py
 advancedguidepythonprogrammingasyncio.py             imdbratings.csv                           pythonforprogrammersregularexpressions.py
 ...
total 215520
-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf
-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt
-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv
-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json
-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv
-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py
...
'''
unsuccessfullinuxcommand = subprocess.run(["ls", "-l", "doesnotexist"], capture_output=True, text=True)
print(unsuccessfullinuxcommand.stdout) #print *nothing*
print(unsuccessfullinuxcommand.returncode) #print 2
print(unsuccessfullinuxcommand.stderr) #print ls: cannot access 'doesnotexist': No such file or directory
unsuccessfullinuxcommand = subprocess.run(["ls", "-l", "doesnotexist"], capture_output=True)
print(unsuccessfullinuxcommand.stdout) #print b''
print(unsuccessfullinuxcommand.returncode) #print 2
print(unsuccessfullinuxcommand.stderr) #print b"ls: cannot access 'doesnotexist': No such file or directory\n"
printworkingdirectory = subprocess.run(["pwd"]) #type and execute pwd in terminal
historytrivia = subprocess.run(["calendar"]) #type and execute calendar in terminal
#openfirefox = subprocess.run(["firefox"]) #type and execute firefox in terminal.  Opens Firefox browser.
readtextfile = subprocess.run(["cat", "moby01.txt"], capture_output=True, text=True)
print(readtextfile.stdout)
'''
Call me Ishmael. Some years ago--never mind how long precisely--
having little or no money in my purse, and nothing particular
to interest me on shore, I thought I would sail about a little
and see the watery part of the world. It is a way I have
of driving off the spleen and regulating the circulation.
...
'''
readtextfilemorecommand = subprocess.run(["more", "moby01.txt"], capture_output=True, text=True)
catviewfile = subprocess.run(["cat"], capture_output=True, text=True, input=readtextfilemorecommand.stdout)
print(catviewfile.stdout)
'''
Call me Ishmael. Some years ago--never mind how long precisely--
having little or no money in my purse, and nothing particular
to interest me on shore, I thought I would sail about a little
and see the watery part of the world. It is a way I have
of driving off the spleen and regulating the circulation.
...
'''

#https://stackoverflow.com/questions/20810366/executing-shell-script-using-subprocess-popen-in-python
subprocess.call("echo Hello world", shell=True) #executes echo to print Hello world
#subprocess.call("firefox &", shell=True) #executes open program Firefox
subprocess.call("calendar", shell=True) #executes calendar Linux command
#typehelloworld = subprocess.run(["echo Hello world"]) #FileNotFoundError: [Errno 2] No such file or directory: 'echo Hello world'
subprocess.call("echo Hello world", shell=True) #executes echo to print Hello world

subprocess.call("ls *.txt", shell=True) #return text files in present directory
listoutput = subprocess.check_output("ls *.txt", shell=True)
print(listoutput) #print b'accountscreatetextfile.txt\nbasicreadwritefile.txt\ncombinedatatitaniclowercasecolumns.txt\ncombinedatatitanic.txt\ncopytemp.txt\nCreate Test File On My Windows.txt\n . . .
print(type(listoutput)) #print <class 'bytes'>
print(listoutput.decode()) #print text files in present directory
print(type(listoutput.decode())) #print <class 'str'>

import sys
sys.stderr.write("pronounced s-t-err for errors\n") #return pronounced s-t-err for errors
sys.stderr.flush()
sys.stdout.write("pronounced s-t-out for output\n") #return pronounced s-t-out for output
print(sys.argv) #print ['yytest.py', 'Type a sentence after python3.8 yytest.py'].  Returns file name and more.  Typed python3.8 yytest.py "Type a sentence after python3.8 yytest.py" on prompt mar@mar-VirtualBox:~/python$.  mar@mar-VirtualBox:~/python$ python3.8 yytest.py "Type a sentence after python3.8 yytest.py"  Pronounced arg-v.
print(type(sys.argv)) #print <class 'list'>
print(sys.argv[1]) #print Type a sentence after python3.8 yytest.py
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
Copyright (c) 2001-2021 Python Software Foundation.
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
3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0]
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

pythoninterpreterfilelocation = sys.executable
print(pythoninterpreterfilelocation) #print /usr/bin/python3.8
pythonbuiltinmodules = sys.builtin_module_names #Python modules builtin modules
# print(pythonbuiltinmodules) #print ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_csv', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_socket', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zlib')
pythonsystemmodules = sys.modules #Python system modules
print(pythonsystemmodules) #print {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>,. . .}
print(pythonsystemmodules.keys()) #print dict_keys(['sys', 'builtins', '_frozen_importlib', '_imp', '_warnings', '_io', 'marshal', 'posix', '_frozen_importlib_external', '_thread', '_weakref', 'time', 'zipimport', '_codecs', 'codecs', 'encodings.aliases', 'encodings', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', '_abc', 'abc', 'io', '_stat', 'stat', '_collections_abc', 'genericpath', 'posixpath', 'os.path', 'os', '_sitebuiltins', '_locale', '_bootlocale', 'types', 'importlib._bootstrap', 'importlib._bootstrap_external', 'warnings', 'importlib', 'importlib.machinery', 'importlib.abc', '_operator', 'operator', 'keyword', '_heapq', 'heapq', 'itertools', 'reprlib', '_collections', 'collections', '_functools', 'functools', 'contextlib', 'importlib.util', 'mpl_toolkits', 'apport_python_hook', 'sitecustomize', 'site'])
