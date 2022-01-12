#Python Itertools.pdf
#Iterate over a collection of items.  Implement the iterator protocol.  Define the __iter__ and __next__ methods.
#Python's standard library provides a module called itertools.  It provides implementations for many iterators.
#Iteration works in Python:  Python asks if the object is iterable by invoking the iter builtin.  It invokes the __iter__ method.  If iterable, it returns an iterator object.  The object implements __next__.  __next__ method invoked repeatedly until it raises a StopIteration exception.
#The example class AllPeople() below assumes every element in args is iterable.  We iterate each element in args one value at a time.  We increase counterindex by one and reset counterindexcurrentlist when we get to the end of a list.

employees = ["Tom", "Dick", "Harry", "Joe", "Lo", "Dibbs"]
managers = ["Mary", "Jane", "Naomi", "John", "Drake", "Blake"]

class AllPeople():
    def __init__(self, *args):
        self.iterables = args
        self.counterindex = 0
        self.counterindexcurrentlist = 0
    def __iter__(self):
        print("__iter__ self.iterables", self.iterables)
        print("__iter__ self.iterables type", type(self.iterables))
        return self
    def __next__(self):
        print("__next__ self.iterables", self.iterables)
        print("__next__ self.counterindex", self.counterindex)
        print("__next__ self.counterindexcurrentlist", self.counterindexcurrentlist)
        if self.counterindexcurrentlist >= len(self.iterables[self.counterindex]):
            print("self.counterindexcurrentlist >= len(self.iterables[self.counterindex]):", self.counterindexcurrentlist, ">=", len(self.iterables[self.counterindex]))
            self.counterindexcurrentlist = 0
            self.counterindex += 1
        if self.counterindex >= len(self.iterables):
            print("self.counterindex >= len(self.iterables) StopIteration now", self.counterindex, ">=", len(self.iterables))
            raise StopIteration
        value = self.iterables[self.counterindex][self.counterindexcurrentlist]
        print("value to return", value)
        self.counterindexcurrentlist += 1
        return value


company = AllPeople(employees, managers)
for eachcompany in company:
    print(eachcompany)
    '''
    __iter__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __iter__ self.iterables type <class 'tuple'>
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 0
    __next__ self.counterindexcurrentlist 0
    value to return Tom
    Tom
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 0
    __next__ self.counterindexcurrentlist 1
    value to return Dick
    Dick
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 0
    __next__ self.counterindexcurrentlist 2
    value to return Harry
    Harry
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 0
    __next__ self.counterindexcurrentlist 3
    value to return Joe
    Joe
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 0
    __next__ self.counterindexcurrentlist 4
    value to return Lo
    Lo
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 0
    __next__ self.counterindexcurrentlist 5
    value to return Dibbs
    Dibbs
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 0
    __next__ self.counterindexcurrentlist 6
    self.counterindexcurrentlist >= len(self.iterables[self.counterindex]): 6 >= 6
    value to return Mary
    Mary
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 1
    __next__ self.counterindexcurrentlist 1
    value to return Jane
    Jane
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 1
    __next__ self.counterindexcurrentlist 2
    value to return Naomi
    Naomi
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 1
    __next__ self.counterindexcurrentlist 3
    value to return John
    John
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 1
    __next__ self.counterindexcurrentlist 4
    value to return Drake
    Drake
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 1
    __next__ self.counterindexcurrentlist 5
    value to return Blake
    Blake
    __next__ self.iterables (['Tom', 'Dick', 'Harry', 'Joe', 'Lo', 'Dibbs'], ['Mary', 'Jane', 'Naomi', 'John', 'Drake', 'Blake'])
    __next__ self.counterindex 1
    __next__ self.counterindexcurrentlist 6
    self.counterindexcurrentlist >= len(self.iterables[self.counterindex]): 6 >= 6
    self.counterindex >= len(self.iterables) StopIteration now 2 >= 2
    '''

class AllPeopleGeneratorFunction():
    def __init__(self, *args):
        self.iterables = args
    def __iter__(self):
        for eachiterable in self.iterables:
            for eachitem in eachiterable:
                yield eachitem


companygeneratorfunction = AllPeopleGeneratorFunction(employees, managers)
print(companygeneratorfunction) #print <__main__.AllPeopleGeneratorFunction object at 0x7fbf7d7db1f0>
for eachcompanygeneratorfunction in companygeneratorfunction:
    print(eachcompanygeneratorfunction)
    '''
    Tom
    Dick
    Harry
    Joe
    Lo
    Dibbs
    Mary
    Jane
    Naomi
    John
    Drake
    Blake
    '''

import itertools

class AllPeopleItertoolsChain():
    def __init__(self, *args):
        self.iterables = args
    def __iter__(self):
        return itertools.chain(*self.iterables)


companyitertoolschain = AllPeopleItertoolsChain(employees, managers)
print(companyitertoolschain) #print <__main__.AllPeopleItertoolsChain object at 0x7f8cedd95eb0>
for eachcompanyitertoolschain in companyitertoolschain:
    print(eachcompanyitertoolschain)
    '''
    Tom
    Dick
    Harry
    Joe
    Lo
    Dibbs
    Mary
    Jane
    Naomi
    John
    Drake
    Blake
    '''

#Infinite Iterators Itertools Python.pdf
#The itertools library provides ready-made iterators which is better than writing iterators ourselves.
#Three itertools Python describes as infinite iterators:  count, cycle, repeat.

#Count.  The count iterator counts.  count(start, increment default is 1).  You indicate where the counter starts and how much increase with each iteration.
from itertools import count
for i in count(10, 100):
    if i > 1500:
        break
    print(i, end=", ") #print 10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010, 1110, 1210, 1310, 1410,  RM:  It's not range() function.
usernames = ["Tom", "Dick", "Harry", "Mar", "Jane", "Naomi"]
for eachusername, idnumber in zip(usernames, count(500)):
    print(f"{eachusername}: {idnumber}")
    '''
    Tom: 500
    Dick: 501
    Harry: 502
    Mar: 503
    Jane: 504
    Naomi: 505
    '''
for i in count(10, -100):
    if i < -1500:
        break
    print(i, end=", ") #print 10, -90, -190, -290, -390, -490, -590, -690, -790, -890, -990, -1090, -1190, -1290, -1390, -1490,
usernames = ["Tom", "Dick", "Harry", "Mar", "Jane", "Naomi"]
for eachusername, idfloatingnumber in zip(usernames, count(500, 0.1)):
    print(f"{eachusername}: {idfloatingnumber}")
    '''
    Tom: 500
    Dick: 500.1
    Harry: 500.20000000000005
    Mar: 500.30000000000007
    Jane: 500.4000000000001
    Naomi: 500.5000000000001
    '''

#Cycle.  The cycle iterator starts from the front to the back and repeats.
from itertools import cycle
mylist = [10, 20, 30, 40]
total = 0
for eachmylist in cycle(mylist):
    if total > 650:
        break
    print(eachmylist, total, "+", eachmylist)
    '''
    10 0 + 10
    20 10 + 20
    30 30 + 30
    40 60 + 40
    10 100 + 10
    20 110 + 20
    30 130 + 30
    40 160 + 40
    10 200 + 10
    20 210 + 20
    30 230 + 30
    40 260 + 40
    10 300 + 10
    20 310 + 20
    30 330 + 30
    40 360 + 40
    10 400 + 10
    20 410 + 20
    30 430 + 30
    40 460 + 40
    10 500 + 10
    20 510 + 20
    30 530 + 30
    40 560 + 40
    10 600 + 10
    20 610 + 20
    30 630 + 30
    '''
    total += eachmylist

#Repeat.  The repeat iterator repeats a set number of times or infinitely.  The Python documentation says repeat is useful if you want to give constant values to map or zip.  Instructor never seen repeat used in practice.
from itertools import repeat
for eachrepeat in repeat(100, 5):
    print(eachrepeat, end=", ") #print 100, 100, 100, 100, 100,

#Python Iterating Predicates Itertools Module.pdf
#Iterators filter the elements of another iterable.  Use an iterator to filter something that's already iterable.  For example, reading a file, which is iterable, to exclude some lines by using the built-in filter function.  Or a modern approach is use a list comprehension or generator comprehension.

#filterfalse.  The built-in filter function returns an iterable object based on the combination of a predicate or a function which returns True or False and an iterable.  The filter function applies the predicate to each element of the iterable.  Objects are returned when the predicate returns True.
mylist = [10, 20, 25, 30, 35, 36, 40, 42, 45]
filterfalsevariable = filter(lambda x: x % 2, mylist)
print(filterfalsevariable) #print <filter object at 0x7fb5cacd5a00>
print(list(filterfalsevariable)) #print [25, 35, 45].  The code returns a filter list consisting of numbers in mylist which are odd.  Returns True for odd numbers.  Returns False for even numbers.
filterfalsevariableevenumbers = filter(lambda x: not x % 2, mylist)
print(list(filterfalsevariableevenumbers)) #print [10, 20, 30, 36, 40, 42].  The code returns a filter list consisting of numbers in mylist which are even.  Returns True for even numbers.  Returns False for odd numbers.
import itertools
filterfalseevenumbers = itertools.filterfalse(lambda x: x % 2, mylist)
print(list(filterfalseevenumbers)) #print [10, 20, 30, 36, 40, 42].  The code returns a filter list consisting of numbers in mylist which are odd.  Returns True for odd numbers.  Returns False for even numbers.

#takewhile.  Takewhile iterators needs a predicate and an iterable.  Returns elements from the iterable as long as the predicate returns True.  The iterable stops when the predicate returns False.
import itertools
stopwhenfalseoddnumber = list(itertools.takewhile(lambda x: not x % 2, mylist))
print(stopwhenfalseoddnumber) #print [10, 20].  Returns True when even number.  Returns False when odd number and iterator stops.

#dropwhile.  Dropwhile iterators needs a predicate and an iterable.  Returns elements from the iterable when the predicate returns the first False.  The iterable stops filtering when the predicate returns True.  All iterables are returned True or False.
import itertools
stopfilteringtrueoddnumber = list(itertools.dropwhile(lambda x: not x % 2, mylist))
print(stopfilteringtrueoddnumber) #print [25, 30, 35, 36, 40, 42, 45]  #Ignores True when even number.  False when odd number. and returns the first false number and returns all numbers thereafter True or False.

#Itertools More Examples Python.pdf
#Three more itertools compress, accumulate, and tee

#compress.  We provide two iterables of equal lengths.  We get the elements from the first iterable whenever the corresponding elements from the second iterable is True.  However, the iterator stops when it finishes the shorter of the two iterable.
from itertools import compress, accumulate
tenletterstentrues = list(compress("abcdefghij", [True] * 10))
print(tenletterstentrues) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
tenletterstenfalses = list(compress("abcdefghij", [False] * 10))
print(tenletterstenfalses) #print []
tenlettersfivetruesfivefalses = list(compress("abcdefghij", [True, False] * 5))
print(tenlettersfivetruesfivefalses) #print ['a', 'c', 'e', 'g', 'i']

#accumulate.  Provides a running total on the numbers.  Running sum.
classicfunctionmap = "This is a bunch of words".split()
print(classicfunctionmap) #print ['This', 'is', 'a', 'bunch', 'of', 'words']
print(list(map(len, classicfunctionmap))) #print [4, 2, 1, 5, 2, 5]
print(accumulate(list(map(len, classicfunctionmap)))) #print <itertools.accumulate object at 0x7f1a8817f2c0>
print(list(accumulate(list(map(len, classicfunctionmap))))) #print [4, 6, 7, 12, 14, 19]
runningtotaltentofifty = list(accumulate([10, 20, 30, 40, 50]))
print(runningtotaltentofifty) #print [10, 30, 60, 100, 150]
from operator import mul
runningmultiplicationtentofifty = list(accumulate([10, 20, 30, 40, 50], mul))
print(runningmultiplicationtentofifty) #print [10, 200, 6000, 240000, 12000000]  RM:  12000000 is 10*20*30*40*50.

#tee.  Takes a single iterable and returns multiple iterators for it.  RM:  skipped.

#Permutations Combinations Scrabble Itertools Python.pdf
#product, permutations and combinations
from itertools import product, permutations, combinations, combinations_with_replacement

#product.  Takes any number of iterables as arguments.  Returns a tuple containing one element from each of the arguments.  The iterator stops after returning all possible tuples.
letters = "abcd"
numbers = [10, 20, 30, 40]
print(list(product(letters, numbers))) #print [('a', 10), ('a', 20), ('a', 30), ('a', 40), ('b', 10), ('b', 20), ('b', 30), ('b', 40), ('c', 10), ('c', 20), ('c', 30), ('c', 40), ('d', 10), ('d', 20), ('d', 30), ('d', 40)]
print(list(product(letters, numbers, repeat=2))) #print [('a', 10, 'a', 10), ('a', 10, 'a', 20), ('a', 10, 'a', 30), ('a', 10, 'a', 40), ('a', 10, 'b', 10), ('a', 10, 'b', 20), ('a', 10, 'b', 30), ('a', 10, 'b', 40), ('a', 10, 'c', 10), ('a', 10, 'c', 20), ('a', 10, 'c', 30), ('a', 10, 'c', 40), ('a', 10, 'd', 10), ('a', 10, 'd', 20), ('a', 10, 'd', 30), ('a', 10, 'd', 40), ('a', 20, 'a', 10), ('a', 20, 'a', 20), ('a', 20, 'a', 30), ('a', 20, 'a', 40), ('a', 20, 'b', 10), ('a', 20, 'b', 20), ('a', 20, 'b', 30), ('a', 20, 'b', 40), ('a', 20, 'c', 10), ('a', 20, 'c', 20), ('a', 20, 'c', 30), ('a', 20, 'c', 40), ('a', 20, 'd', 10), ('a', 20, 'd', 20), ('a', 20, 'd', 30), ('a', 20, 'd', 40), ('a', 30, 'a', 10), ('a', 30, 'a', 20), ('a', 30, 'a', 30), ('a', 30, 'a', 40), ('a', 30, 'b', 10), ('a', 30, 'b', 20), ('a', 30, 'b', 30), ('a', 30, 'b', 40), ('a', 30, 'c', 10), ('a', 30, 'c', 20), ('a', 30, 'c', 30), ('a', 30, 'c', 40), ('a', 30, 'd', 10), ('a', 30, 'd', 20), ('a', 30, 'd', 30), ('a', 30, 'd', 40), ('a', 40, 'a', 10), ('a', 40, 'a', 20), ('a', 40, 'a', 30), ('a', 40, 'a', 40), ('a', 40, 'b', 10), ('a', 40, 'b', 20), ('a', 40, 'b', 30), ('a', 40, 'b', 40), ('a', 40, 'c', 10), ('a', 40, 'c', 20), ('a', 40, 'c', 30), ('a', 40, 'c', 40), ('a', 40, 'd', 10), ('a', 40, 'd', 20), ('a', 40, 'd', 30), ('a', 40, 'd', 40), ('b', 10, 'a', 10), ('b', 10, 'a', 20), ('b', 10, 'a', 30), ('b', 10, 'a', 40), ('b', 10, 'b', 10), ('b', 10, 'b', 20), ('b', 10, 'b', 30), ('b', 10, 'b', 40), ('b', 10, 'c', 10), ('b', 10, 'c', 20), ('b', 10, 'c', 30), ('b', 10, 'c', 40), ('b', 10, 'd', 10), ('b', 10, 'd', 20), ('b', 10, 'd', 30), ('b', 10, 'd', 40), ('b', 20, 'a', 10), ('b', 20, 'a', 20), ('b', 20, 'a', 30), ('b', 20, 'a', 40), ('b', 20, 'b', 10), ('b', 20, 'b', 20), ('b', 20, 'b', 30), ('b', 20, 'b', 40), ('b', 20, 'c', 10), ('b', 20, 'c', 20), ('b', 20, 'c', 30), ('b', 20, 'c', 40), ('b', 20, 'd', 10), ('b', 20, 'd', 20), ('b', 20, 'd', 30), ('b', 20, 'd', 40), ('b', 30, 'a', 10), ('b', 30, 'a', 20), ('b', 30, 'a', 30), ('b', 30, 'a', 40), ('b', 30, 'b', 10), ('b', 30, 'b', 20), ('b', 30, 'b', 30), ('b', 30, 'b', 40), ('b', 30, 'c', 10), ('b', 30, 'c', 20), ('b', 30, 'c', 30), ('b', 30, 'c', 40), ('b', 30, 'd', 10), ('b', 30, 'd', 20), ('b', 30, 'd', 30), ('b', 30, 'd', 40), ('b', 40, 'a', 10), ('b', 40, 'a', 20), ('b', 40, 'a', 30), ('b', 40, 'a', 40), ('b', 40, 'b', 10), ('b', 40, 'b', 20), ('b', 40, 'b', 30), ('b', 40, 'b', 40), ('b', 40, 'c', 10), ('b', 40, 'c', 20), ('b', 40, 'c', 30), ('b', 40, 'c', 40), ('b', 40, 'd', 10), ('b', 40, 'd', 20), ('b', 40, 'd', 30), ('b', 40, 'd', 40), ('c', 10, 'a', 10), ('c', 10, 'a', 20), ('c', 10, 'a', 30), ('c', 10, 'a', 40), ('c', 10, 'b', 10), ('c', 10, 'b', 20), ('c', 10, 'b', 30), ('c', 10, 'b', 40), ('c', 10, 'c', 10), ('c', 10, 'c', 20), ('c', 10, 'c', 30), ('c', 10, 'c', 40), ('c', 10, 'd', 10), ('c', 10, 'd', 20), ('c', 10, 'd', 30), ('c', 10, 'd', 40), ('c', 20, 'a', 10), ('c', 20, 'a', 20), ('c', 20, 'a', 30), ('c', 20, 'a', 40), ('c', 20, 'b', 10), ('c', 20, 'b', 20), ('c', 20, 'b', 30), ('c', 20, 'b', 40), ('c', 20, 'c', 10), ('c', 20, 'c', 20), ('c', 20, 'c', 30), ('c', 20, 'c', 40), ('c', 20, 'd', 10), ('c', 20, 'd', 20), ('c', 20, 'd', 30), ('c', 20, 'd', 40), ('c', 30, 'a', 10), ('c', 30, 'a', 20), ('c', 30, 'a', 30), ('c', 30, 'a', 40), ('c', 30, 'b', 10), ('c', 30, 'b', 20), ('c', 30, 'b', 30), ('c', 30, 'b', 40), ('c', 30, 'c', 10), ('c', 30, 'c', 20), ('c', 30, 'c', 30), ('c', 30, 'c', 40), ('c', 30, 'd', 10), ('c', 30, 'd', 20), ('c', 30, 'd', 30), ('c', 30, 'd', 40), ('c', 40, 'a', 10), ('c', 40, 'a', 20), ('c', 40, 'a', 30), ('c', 40, 'a', 40), ('c', 40, 'b', 10), ('c', 40, 'b', 20), ('c', 40, 'b', 30), ('c', 40, 'b', 40), ('c', 40, 'c', 10), ('c', 40, 'c', 20), ('c', 40, 'c', 30), ('c', 40, 'c', 40), ('c', 40, 'd', 10), ('c', 40, 'd', 20), ('c', 40, 'd', 30), ('c', 40, 'd', 40), ('d', 10, 'a', 10), ('d', 10, 'a', 20), ('d', 10, 'a', 30), ('d', 10, 'a', 40), ('d', 10, 'b', 10), ('d', 10, 'b', 20), ('d', 10, 'b', 30), ('d', 10, 'b', 40), ('d', 10, 'c', 10), ('d', 10, 'c', 20), ('d', 10, 'c', 30), ('d', 10, 'c', 40), ('d', 10, 'd', 10), ('d', 10, 'd', 20), ('d', 10, 'd', 30), ('d', 10, 'd', 40), ('d', 20, 'a', 10), ('d', 20, 'a', 20), ('d', 20, 'a', 30), ('d', 20, 'a', 40), ('d', 20, 'b', 10), ('d', 20, 'b', 20), ('d', 20, 'b', 30), ('d', 20, 'b', 40), ('d', 20, 'c', 10), ('d', 20, 'c', 20), ('d', 20, 'c', 30), ('d', 20, 'c', 40), ('d', 20, 'd', 10), ('d', 20, 'd', 20), ('d', 20, 'd', 30), ('d', 20, 'd', 40), ('d', 30, 'a', 10), ('d', 30, 'a', 20), ('d', 30, 'a', 30), ('d', 30, 'a', 40), ('d', 30, 'b', 10), ('d', 30, 'b', 20), ('d', 30, 'b', 30), ('d', 30, 'b', 40), ('d', 30, 'c', 10), ('d', 30, 'c', 20), ('d', 30, 'c', 30), ('d', 30, 'c', 40), ('d', 30, 'd', 10), ('d', 30, 'd', 20), ('d', 30, 'd', 30), ('d', 30, 'd', 40), ('d', 40, 'a', 10), ('d', 40, 'a', 20), ('d', 40, 'a', 30), ('d', 40, 'a', 40), ('d', 40, 'b', 10), ('d', 40, 'b', 20), ('d', 40, 'b', 30), ('d', 40, 'b', 40), ('d', 40, 'c', 10), ('d', 40, 'c', 20), ('d', 40, 'c', 30), ('d', 40, 'c', 40), ('d', 40, 'd', 10), ('d', 40, 'd', 20), ('d', 40, 'd', 30), ('d', 40, 'd', 40)]
print(list(permutations(letters, 2))) #print [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')].  Permutations order is important.  a, b and b, a are returned.
print(list(combinations(letters, 2))) #print [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')].  Combinations order is unimportant.  a, b is returned.  b, a is not returned because there is an a, b tuple.
moreletters = "abcdefg"
print(list(permutations(moreletters, 4))) #print [('a', 'b', 'c', 'd'), ('a', 'b', 'c', 'e'), ('a', 'b', 'c', 'f'), ('a', 'b', 'c', 'g'), ('a', 'b', 'd', 'c'), ('a', 'b', 'd', 'e'), ('a', 'b', 'd', 'f'), ('a', 'b', 'd', 'g'), ('a', 'b', 'e', 'c'), ('a', 'b', 'e', 'd'), ('a', 'b', 'e', 'f'), ('a', 'b', 'e', 'g'), ('a', 'b', 'f', 'c'), ('a', 'b', 'f', 'd'), ('a', 'b', 'f', 'e'), ('a', 'b', 'f', 'g'), ('a', 'b', 'g', 'c'), ('a', 'b', 'g', 'd'), ('a', 'b', 'g', 'e'), ('a', 'b', 'g', 'f'), ('a', 'c', 'b', 'd'), ('a', 'c', 'b', 'e'), ('a', 'c', 'b', 'f'), ('a', 'c', 'b', 'g'), ('a', 'c', 'd', 'b'), ('a', 'c', 'd', 'e'), ('a', 'c', 'd', 'f'), ('a', 'c', 'd', 'g'), ('a', 'c', 'e', 'b'),  . . .
scrabble = list(permutations(moreletters, 4))
for eachscrabble in scrabble:
    print("".join(eachscrabble))
    '''
    abcd
    abce
    abcf
    abcg
    abdc
    abde
    abdf
    abdg
    abec
    abed
    abef
    abeg
    abfc
    abfd
    abfe
    abfg
    abgc
    abgd
    abge
    abgf
    acbd
    acbe
    acbf
    acbg
    acdb
    acde
    acdf
    acdg
    aceb
    '''
letters = "abcd"
print(list(combinations_with_replacement(letters, 3))) #print [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'a', 'd'), ('a', 'b', 'b'), ('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'c'), ('a', 'c', 'd'), ('a', 'd', 'd'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'b', 'd'), ('b', 'c', 'c'), ('b', 'c', 'd'), ('b', 'd', 'd'), ('c', 'c', 'c'), ('c', 'c', 'd'), ('c', 'd', 'd'), ('d', 'd', 'd')].  Each element can appear more than once in a tuple; for example, a tuple with two a's, another tuple with three b's.'
print(list(combinations(letters, 3))) #print [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]
