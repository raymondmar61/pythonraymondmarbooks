import collections
listofwords = ['call', 'me', 'ishmael', 'some', 'years', 'ago', 'never', 'mind', 'how', 'long', 'precisely', 'having', 'little', 'or', 'no', 'money', 'in', 'my', 'purse', 'and', 'nothing', 'particular', 'to', 'interest', 'me', 'on', 'shore', 'i', 'thought', 'i', 'would', 'sail', 'about', 'a', 'little', 'and', 'see', 'the', 'watery', 'part', 'of', 'the', 'world', 'it', 'is', 'a', 'way', 'i', 'have', 'of', 'driving', 'off', 'the', 'spleen', 'and', 'regulating', 'the', 'circulation', 'whenever', 'i', 'find', 'myself', 'growing', 'grim', 'about', 'the', 'mouth', 'whenever', 'it', 'is', 'a', 'damp', 'drizzly', 'november', 'in', 'my', 'soul', 'whenever', 'i', 'find', 'myself', 'involuntarily', 'pausing', 'before', 'coffin', 'warehouses', 'and', 'bringing', 'up', 'the', 'rear', 'of', 'every', 'funeral', 'i', 'meet', 'and', 'especially', 'whenever', 'my', 'hypos', 'get', 'such', 'an', 'upper', 'hand', 'of', 'me', 'that', 'it', 'requires', 'a', 'strong', 'moral', 'principle', 'to', 'prevent', 'me', 'from', 'deliberately', 'stepping', 'into', 'the', 'street', 'and', 'methodically', 'knocking', 'people', 's', 'hats', 'off', 'then', 'i', 'account', 'it', 'high', 'time', 'to', 'get', 'to', 'sea', 'as', 'soon', 'as', 'i', 'can', 'this', 'is', 'my', 'substitute', 'for', 'pistol', 'and', 'ball', 'with', 'a', 'philosophical', 'flourish', 'cato', 'throws', 'himself', 'upon', 'his', 'sword', 'i', 'quietly', 'take', 'to', 'the', 'ship', 'there', 'is', 'nothing', 'surprising', 'in', 'this', 'if', 'they', 'but', 'knew', 'it', 'almost', 'all', 'men', 'in', 'their', 'degree', 'some', 'time', 'or', 'other', 'cherish', 'very', 'nearly', 'the', 'same', 'feelings', 'towards', 'the', 'ocean', 'with', 'me', 'there', 'now', 'is', 'your', 'insular', 'city', 'of', 'the', 'manhattoes', 'belted', 'round', 'by', 'wharves', 'as', 'indian', 'isles', 'by', 'coral', 'reefs', 'commerce', 'surrounds', 'it', 'with', 'her', 'surf', 'right', 'and', 'left', 'the', 'streets', 'take', 'you', 'waterward', 'its', 'extreme', 'downtown', 'is', 'the', 'battery', 'where', 'that', 'noble', 'mole', 'is', 'washed', 'by', 'waves', 'and', 'cooled', 'by', 'breezes', 'which', 'a', 'few', 'hours', 'previous', 'were', 'out', 'of', 'sight', 'of', 'land', 'look', 'at', 'the', 'crowds', 'of', 'water', 'gazers', 'there']
wordcounttopten = collections.Counter(listofwords).most_common(10)
print(wordcounttopten) #print [('the', 14), ('and', 9), ('i', 9), ('of', 8), ('is', 7), ('a', 6), ('it', 6), ('me', 5), ('to', 5), ('in', 4)]

import copy
letterslist = ["a", "b", "c", "d"]
print(letterslist) #print ['a', 'b', 'c', 'd']
cheeseletterslist = copy.copy(letterslist) #copy.copy makes a duplicate copy of a mutable value such as a list or dictionary
print(cheeseletterslist) #print ['a', 'b', 'c', 'd']
print(letterslist) #print ['a', 'b', 'c', 'd']
cheeseletterslist[1] = "cheese"
print(cheeseletterslist) #print ['a', 'cheese', 'c', 'd']
print(letterslist) #print ['a', 'b', 'c', 'd']
letterslist = ["a", "b", "c", "d"]
cheeseletterslist = letterslist
print(cheeseletterslist) #print ['a', 'b', 'c', 'd']
print(letterslist) #print ['a', 'b', 'c', 'd']

import csv
with open("csvmodule.csv", "w") as fileobject:
    columnheaders = "columnheader1,columnheader2,columnheader3"
    fileobject.write(str(columnheaders) + "\n")
    newrecord = "Brian,73,Taurus\n"
    aplacementrow = "Name,Age,Star sign"
    fileobject.write(str(aplacementrow) + "\n")
    fileobject.write("Sandra,48,Virgo" + "\n")
    fileobject.write("Zoe,25,Scorpio" + "\n")
    fileobject.write("Keith,43,Leo" + "\n")
    fileobject.write("Raymond,74,Leo")
with open("csvmodule.csv", "r") as fileobject:
    usereadmethod = fileobject.read()
    print(usereadmethod)
    '''
    columnheader1,columnheader2,columnheader3
    Name,Age,Star sign
    Sandra,48,Virgo
    Zoe,25,Scorpio
    Keith,43,Leo
    Raymond,74,Leo
    '''
openfiletolist = list(csv.reader(open("csvmodule.csv")))
print(openfiletolist) #print [['columnheader1', 'columnheader2', 'columnheader3'], ['Name', 'Age', 'Star sign'], ['Sandra', '48', 'Virgo'], ['Zoe', '25', 'Scorpio'], ['Keith', '43', 'Leo'], ['Raymond', '74', 'Leo']]
for eachopenfiletolist in openfiletolist:
    listtostring = ",".join(map(str, eachopenfiletolist))
    print(listtostring)
    '''
    columnheader1,columnheader2,columnheader3
    Name,Age,Star sign
    Sandra,48,Virgo
    Zoe,25,Scorpio
    Keith,43,Leo
    Raymond,74,Leo
    '''
seachterm = "Leo"
for eachopenfiletolist in openfiletolist:
    listtostring = ",".join(map(str, eachopenfiletolist))
    if seachterm in listtostring:
        print("Found searchterm: " + listtostring)
        '''
        Found searchterm: Keith,43,Leo
        Found searchterm: Raymond,74,Leo
        '''

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

import itertools
#Iterate over a collection of items.  Implement the iterator protocol.  Define the __iter__ and __next__ methods.
#Iteration works in Python:  Python asks if the object is iterable by invoking the iter builtin.  It invokes the __iter__ method.  If iterable, it returns an iterator object.  The object implements __next__.  __next__ method invoked repeatedly until it raises a StopIteration exception.
#Count.  The count iterator counts.  count(start, increment default is 1).  You indicate where the counter starts and how much increase with each iteration.
for i in itertools.count(1):
    if i >= 20:
        print("Count from 1 to 19 break now")
        break
    print(i)
    '''
    1
    2
    3
    4
    5
    ...
    18
    19
    Count from 1 to 19 break now
    '''
for i in itertools.count(-10, 4):
    if i >= 20:
        print("Count from -10 to 19 by fours break now")
        break
    print(i)
    '''
    -10
    -6
    -2
    2
    6
    10
    14
    18
    Count from -10 to 19 by fours break now
    '''
#Cycle.  The cycle iterator starts from the front to the back and repeats.
cyclestartsfromfronttobackrepeating = ["Giants", "Warriors", "49ers", "A's", "Sharks", "Earthquakes"]
counter = 1
for needcountertostopcycle in itertools.cycle(cyclestartsfromfronttobackrepeating):
    if counter > 20:
        break
    else:
        print(counter, needcountertostopcycle)
        counter += 1
        '''
        1 Giants
        2 Warriors
        3 49ers
        4 A's
        5 Sharks
        6 Earthquakes
        7 Giants
        ...
        19 Giants
        20 Warriors
        '''
#Repeat.  The repeat iterator repeats a set number of times or infinitely.  The Python documentation says repeat is useful if you want to give constant values to map or zip.  Instructor never seen repeat used in practice.
for eachrepeat in itertools.repeat(100, 5):
    print(eachrepeat, end=", ") #print 100, 100, 100, 100, 100,
print("\n")

#Filterfalse.  The built-in filter function returns an iterable object based on the combination of a predicate or a function which returns True or False and an iterable.  The filter function applies the predicate to each element of the iterable.  Objects are returned when the predicate returns True.
mylist = [10, 20, 25, 30, 35, 36, 40, 42, 45]
for eachmylist in mylist:
    print(eachmylist % 2) #RM:  0 is False, 1 is True
    '''
    0
    0
    1
    0
    1
    0
    0
    0
    1
    '''
mylist = [10, 20, 25, 30, 35, 36, 40, 42, 45]
filterfalsevariable = filter(lambda x: x % 2, mylist)
print(filterfalsevariable) #print <filter object at 0x7fb5cacd5a00>
print(list(filterfalsevariable)) #print [25, 35, 45].  The code returns a filter list consisting of numbers in mylist which are odd.  Returns True for odd numbers x % 2 is 1.  Returns False for even numbers x % 2 is 0.
filterfalsevariableevenumbers = filter(lambda x: not x % 2, mylist)
print(list(filterfalsevariableevenumbers)) #print [10, 20, 30, 36, 40, 42].  The code returns a filter list consisting of numbers in mylist which are even.  Returns True for even numbers x % 2 is not 0.  Returns False for odd numbers x % 2 is not 1.
filterfalseevenumbers = itertools.filterfalse(lambda x: x % 2, mylist)
print(list(filterfalseevenumbers)) #print [10, 20, 30, 36, 40, 42].  The code returns a filter list consisting of numbers in mylist which are odd.  Returns True for odd numbers x % 2 is 1.  Returns False for even numbers x % 2 is 0.
#Takewhile.  Takewhile iterators needs a predicate and an iterable.  Returns elements from the iterable as long as the predicate returns True.  The iterable stops when the predicate returns False.
stopwhenfalseoddnumber = list(itertools.takewhile(lambda x: not x % 2, mylist))
print(stopwhenfalseoddnumber) #print [10, 20].  Returns True when even number.  Returns False when odd number and iterator stops which is 25.
#Dropwhile.  Dropwhile iterators needs a predicate and an iterable.  Returns elements from the iterable when the predicate returns the first False.  The iterable stops filtering when the predicate returns True.  All iterables are returned True or False.
stopfilteringtrueoddnumber = list(itertools.dropwhile(lambda x: not x % 2, mylist))
print(stopfilteringtrueoddnumber) #print [25, 30, 35, 36, 40, 42, 45]  #Ignores True when even number.  False when odd number. and returns the first false number and returns all numbers thereafter True or False.  In other words, the interator starts returning results from the first false to the end of the elements.

#Compress.  We provide two iterables of equal lengths.  We get the elements from the first iterable whenever the corresponding elements from the second iterable is True.  However, the iterator stops when it finishes the shorter of the two iterable.\
print([True] * 8) #print [True, True, True, True, True, True, True, True]
tenlettersonestring = "abcdefghij"
eightletterseighttrues = itertools.compress(tenlettersonestring, [True] * 8)
print(eightletterseighttrues) #print <itertools.compress object at 0x7f262e1f5b50>
print(list(eightletterseighttrues)) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
threefalses = [True, False, True, False, False, True]
threelettersthreefalses = itertools.compress(tenlettersonestring, threefalses)
print(list(threelettersthreefalses)) #print ['a', 'c', 'f']
combinationtruefalses = [False, False, "c", False, "e", True, "G", "HH", ""]
print(list(itertools.compress(tenlettersonestring, combinationtruefalses))) #print ['c', 'e', 'f', 'g', 'h']
#Accumulate.  Provides a running total on the numbers.  Running sum.
runningtotaltentofifty = list(itertools.accumulate([10, 20, 30, 40, 50]))
print(runningtotaltentofifty) #print [10, 30, 60, 100, 150]

#Product.  Takes any number of iterables as arguments.  Returns a tuple containing one element from each of the arguments.  The iterator stops after returning all possible tuples.
#Combinations and permutations.  Combinations can be used once in an area.  Permutations all possibilities are returned.  Simple example (a, b) and (b, a) can't be used in a permutation because they're the same in combination.
fourletterscombinewith = "abcd"
fournumberstobecombinedwith = [10, 20, 30, 40]
print(list(itertools.product(fourletterscombinewith, fournumberstobecombinedwith))) #print [('a', 10), ('a', 20), ('a', 30), ('a', 40), ('b', 10), ('b', 20), ('b', 30), ('b', 40), ('c', 10), ('c', 20), ('c', 30), ('c', 40), ('d', 10), ('d', 20), ('d', 30), ('d', 40)]
print(list(itertools.product(fourletterscombinewith, fournumberstobecombinedwith, repeat=2))) #print [('a', 10, 'a', 10), ('a', 10, 'a', 20), ('a', 10, 'a', 30), ('a', 10, 'a', 40), ('a', 10, 'b', 10), ('a', 10, 'b', 20), ('a', 10, 'b', 30), ('a', 10, 'b', 40), ('a', 10, 'c', 10), ('a', 10, 'c', 20), ('a', 10, 'c', 30), ('a', 10, 'c', 40), ('a', 10, 'd', 10), ('a', 10, 'd', 20), ('a', 10, 'd', 30), ('a', 10, 'd', 40), ('a', 20, 'a', 10), ('a', 20, 'a', 20), ('a', 20, 'a', 30), ('a', 20, 'a', 40), ('a', 20, 'b', 10), ('a', 20, 'b', 20), ('a', 20, 'b', 30), ('a', 20, 'b', 40), ('a', 20, 'c', 10), ('a', 20, 'c', 20), ('a', 20, 'c', 30), . . .]
print(list(itertools.combinations(fourletterscombinewith, 4))) #print [('a', 'b', 'c', 'd')]
print(list(itertools.combinations(fourletterscombinewith, 2))) #print [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
print(list(itertools.permutations(fourletterscombinewith))) #print [('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ('a', 'c', 'b', 'd'), ('a', 'c', 'd', 'b'), ('a', 'd', 'b', 'c'), ('a', 'd', 'c', 'b'), ('b', 'a', 'c', 'd'), ('b', 'a', 'd', 'c'), ('b', 'c', 'a', 'd'), ('b', 'c', 'd', 'a'), ('b', 'd', 'a', 'c'), ('b', 'd', 'c', 'a'), ('c', 'a', 'b', 'd'), ('c', 'a', 'd', 'b'), ('c', 'b', 'a', 'd'), ('c', 'b', 'd', 'a'), ('c', 'd', 'a', 'b'), ('c', 'd', 'b', 'a'), ('d', 'a', 'b', 'c'), ('d', 'a', 'c', 'b'), ('d', 'b', 'a', 'c'), ('d', 'b', 'c', 'a'), ('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')]
print(list(itertools.permutations(fourletterscombinewith, 2))) #print [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]
minigymfiveworkouts = itertools.combinations(range(1, 6), 2)
print(list(minigymfiveworkouts)) #print [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
print(list(itertools.combinations_with_replacement(fourletterscombinewith, 3))) #print [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'a', 'd'), ('a', 'b', 'b'), ('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'c'), ('a', 'c', 'd'), ('a', 'd', 'd'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'b', 'd'), ('b', 'c', 'c'), ('b', 'c', 'd'), ('b', 'd', 'd'), ('c', 'c', 'c'), ('c', 'c', 'd'), ('c', 'd', 'd'), ('d', 'd', 'd')]
print(list(itertools.combinations_with_replacement(fournumberstobecombinedwith, 2))) #print [(10, 10), (10, 20), (10, 30), (10, 40), (20, 20), (20, 30), (20, 40), (30, 30), (30, 40), (40, 40)]

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

import pprint
mobydicktext = "Call me Ishmael. Some years ago--never mind how long precisely-- having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off--then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.\n There now is your insular city of the Manhattoes, belted round by wharves as Indian isles by coral reefs--commerce surrounds it with her surf. Right and left, the streets take you waterward. Its extreme downtown is the battery, where that noble mole is washed by waves, and cooled by breezes, which a few hours previous were out of sight of land.  Look at the crowds of water - gazers there."
cleanoutput = pprint.pprint(mobydicktext) #RM:  I don't understand from the tutorial file automatetheboringstuffpythonbasics.py
print(cleanoutput)
'''
('Call me Ishmael. Some years ago--never mind how long precisely-- having '
 'little or no money in my purse, and nothing particular to interest me on '
 'shore, I thought I would sail about a little and see the watery part of the '
 'world. It is a way I have of driving off the spleen and regulating the '
 'circulation. Whenever I find myself growing grim about the mouth; whenever '
 'it is a damp, drizzly November in my soul; whenever I find myself '
 'involuntarily pausing before coffin warehouses, and bringing up the rear of '
 'every funeral I meet; and especially whenever my hypos get such an upper '
 'hand of me, that it requires a strong moral principle to prevent me from '
 "deliberately stepping into the street, and methodically knocking people's "
 'hats off--then, I account it high time to get to sea as soon as I can. This '
 'is my substitute for pistol and ball. With a philosophical flourish Cato '
 'throws himself upon his sword; I quietly take to the ship. There is nothing '
 'surprising in this. If they but knew it, almost all men in their degree, '
 'some time or other, cherish very nearly the same feelings towards the ocean '
 'with me.\n'
 ' There now is your insular city of the Manhattoes, belted round by wharves '
 'as Indian isles by coral reefs--commerce surrounds it with her surf. Right '
 'and left, the streets take you waterward. Its extreme downtown is the '
 'battery, where that noble mole is washed by waves, and cooled by breezes, '
 'which a few hours previous were out of sight of land.  Look at the crowds of '
 'water - gazers there.')
None
'''
print(type(cleanoutput)) #print <class 'NoneType'>
print(pprint.pformat(mobydicktext))
'''
('Call me Ishmael. Some years ago--never mind how long precisely-- having '
 'little or no money in my purse, and nothing particular to interest me on '
 'shore, I thought I would sail about a little and see the watery part of the '
 'world. It is a way I have of driving off the spleen and regulating the '
 'circulation. Whenever I find myself growing grim about the mouth; whenever '
 'it is a damp, drizzly November in my soul; whenever I find myself '
 'involuntarily pausing before coffin warehouses, and bringing up the rear of '
 'every funeral I meet; and especially whenever my hypos get such an upper '
 'hand of me, that it requires a strong moral principle to prevent me from '
 "deliberately stepping into the street, and methodically knocking people's "
 'hats off--then, I account it high time to get to sea as soon as I can. This '
 'is my substitute for pistol and ball. With a philosophical flourish Cato '
 'throws himself upon his sword; I quietly take to the ship. There is nothing '
 'surprising in this. If they but knew it, almost all men in their degree, '
 'some time or other, cherish very nearly the same feelings towards the ocean '
 'with me.\n'
 ' There now is your insular city of the Manhattoes, belted round by wharves '
 'as Indian isles by coral reefs--commerce surrounds it with her surf. Right '
 'and left, the streets take you waterward. Its extreme downtown is the '
 'battery, where that noble mole is washed by waves, and cooled by breezes, '
 'which a few hours previous were out of sight of land.  Look at the crowds of '
 'water - gazers there.')
'''
print(type(pprint.pformat(mobydicktext))) #print <class 'str'>

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
while True:
    response = input("Terminate a program or exit calling sys.exit() function.  Type exit to exit. ")
    if response == "exit":
        sys.exit()
    else:
        continue

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
