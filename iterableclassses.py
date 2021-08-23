#Python Making A Class Iterable.pdf
class ClassIteration(object):
    def __init__(self, stringinput):
        print("Now in ClassIteration.__init__ self,stringinput.  Class initiation create the instance.")
        self.stringinput = stringinput
    def __iter__(self):
        print("Now in ClassIteration.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.")
        print(self.stringinput)
        return self
    def __next__(self):
        print("Now in ClassIteration.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.")
        print(self.stringinput + "the quick brown fox jumped over the lazy dog.")
        raise StopIteration

class ClassIterationMultipleIterations(object):
    def __init__(self, stringinput):
        print("Now in ClassIterationMultipleIterations.__init__ self,stringinput.  Class initiation create the instance.")
        self.stringinput = stringinput
        self.index = 0
    def __iter__(self):
        print("Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.")
        return self
    def __next__(self):
        print("Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.")
        if self.index >= len(self.stringinput):
            print("End of iterations")
            raise StopIteration
        value = self.stringinput[self.index]
        self.index += 1
        return value


for item in ClassIteration("abcd"):
    print(item)
    '''
    Now in ClassIteration.__init__ self,stringinput.  Class initiation create the instance.
    Now in ClassIteration.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
    abcd
    Now in ClassIteration.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    abcdthe quick brown fox jumped over the lazy dog.
    '''
for item in ClassIterationMultipleIterations("abcdefg"):
    print(item)
    '''
    Now in ClassIterationMultipleIterations.__init__ self,stringinput.  Class initiation create the instance.
    Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    a
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    b
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    c
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    d
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    e
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    f
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    g
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    End of iterations
    '''

#Python Why Some Iterators Can Restart.pdf
#ClassIterationMultipleIterations("abcdefg") is unnecessary because strings know how to iterate themselves.
noclass = "abcdefg"
for item in noclass:
    print(item)
    '''
    a
    b
    c
    d
    e
    f
    g
    '''
class ClassIterationOneIterations(object):
    def __init__(self, stringinput):
        print("Now in ClassIterationOneIterations.__init__ self,stringinput.  Class initiation create the instance.")
        self.stringinput = stringinput
        self.index = len(stringinput) - 1
        print("Starting index number", str(self.index))
    def __iter__(self):
        print("Now in ClassIterationOneIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.")
        return self
    def __next__(self):
        print("Now in ClassIterationOneIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.")
        if self.index < 0:
            print("End of iterations")
            print("self.index value is", str(self.index))
            raise StopIteration
        value = self.stringinput[self.index]
        self.index -= 1
        return value, str(self.index)


classinstance = ClassIterationOneIterations("abcd")
for eachclassinstance in classinstance:
    print(eachclassinstance)
    '''
    Now in ClassIterationOneIterations.__init__ self,stringinput.  Class initiation create the instance.
    Starting index number 3
    Now in ClassIterationOneIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
    Now in ClassIterationOneIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('d', '2')
    Now in ClassIterationOneIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('c', '1')
    Now in ClassIterationOneIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('b', '0')
    Now in ClassIterationOneIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('a', '-1')
    Now in ClassIterationOneIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    End of iterations
    self.index value is -1
    '''
for eachclassinstance in classinstance:
    print(eachclassinstance)
    '''
    Now in ClassIterationOneIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
    Now in ClassIterationOneIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    End of iterations
    self.index value is -1
    '''
print("The second time classinstance stopped being iterable after the first run or after the first for eachclassinstance loop.  __next__ sees the self.index number is lower than len(self.stringinput) stopping the iterations and raises StopIteration.  classinstance is theoretically iterable many times as we want, realistically it stops being iterable after the first run.")
for adifferentclassinstance in classinstance:
    print(adifferentclassinstance)
    '''
    Now in ClassIterationOneIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
    Now in ClassIterationOneIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    End of iterations
    self.index value is -1
    '''

#Python Making A Restartable Iterator Restart.pdf
class ClassIterationMultipleIterations(object):
    def __init__(self, stringinput):
        print("Now in ClassIterationMultipleIterations.__init__ self,stringinput.  Class initiation create the instance.")
        self.stringinput = stringinput
        self.index = 0
        print("Starting index number", str(self.index))
    def __iter__(self):
        print("Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.")
        self.index = 0
        return self
    def __next__(self):
        print("Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.")
        if self.index >= len(self.stringinput):
            print("End of iterations")
            print("self.index value is", str(self.index))
            raise StopIteration
        value = self.stringinput[self.index]
        self.index += 1
        return value, str(self.index)


#Some people suggest that the way to do this is by having "__iter__" reset whateveriteration count is in our object. Perhaps this is a good idea in some cases, but it seemsquite dangerous to me, and I don't recommend it for most objects.
classinstance = ClassIterationMultipleIterations("abcd")
for eachclassinstance in classinstance:
    print(eachclassinstance)
    '''
    Now in ClassIterationMultipleIterations.__init__ self,stringinput.  Class initiation create the instance.
    Starting index number 0
    Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('a', '1')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('b', '2')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('c', '3')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('d', '4')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    End of iterations
    self.index value is 4
    '''
print("\n")
for eachclassinstance in classinstance:
    print(eachclassinstance)
    '''
    Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('a', '1')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('b', '2')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('c', '3')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('d', '4')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    End of iterations
    self.index value is 4
    '''
print("\n")
for adifferentclassinstance in classinstance:
    print(adifferentclassinstance)
    '''
    Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('a', '1')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('b', '2')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('c', '3')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    ('d', '4')
    Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    End of iterations
    self.index value is 4
    '''
print("\n")
quickinstance1 = iter(classinstance)
print(quickinstance1)
'''
Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
<__main__.ClassIterationMultipleIterations object at 0x7ff9b1c74a90>
'''
print(next(quickinstance1))
'''
Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
('a', '1')
'''
print(next(quickinstance1))
'''
Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
('b', '2')
'''
print("\n")
quickinstance2 = iter(classinstance)
print(next(quickinstance2))
'''
Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.
Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
('a', '1')
'''
print(next(quickinstance1)) #RM  quickinstance1 not quickinstance2
'''
Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
('b', '2')
'''
print(quickinstance1 is quickinstance2) #print True  RM:  quickinstance2 sets self.index to 0 which is also setting quickinstance1 self.index to 0.  We're unable to have the same object be in multiple for loops simultaneously.  Each invocation of __iter__ ruins it for the others.  The solution is a completely separate object.  The objects don't return themselves from __iter__.  The separate object implements __next__ and upon which next is called; in other words, we get a new instance of a different class each time we invoke __iter__.
class ClassGetInput(object):
    def __init__(self, stringinput):
        print("Now in ClassGetInput.__init__ self,stringinput.  Class initiation create the instance.")
        self.stringinput = stringinput
    def __iter__(self):
        print("Now in ClassGetInput.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.  Creates and returns a new ClassGetInputMultipleIterators instance.")
        return ClassGetInputMultipleIterators(self.stringinput)
class ClassGetInputMultipleIterators(object):
    def __init__(self, data):
        print("Now in ClassGetInputMultipleIterators.__init__ self,data.  Class initiation create the instance.  The self.index is no longer needed in ClassGetInput.")
        self.data = data
        self.index = 0
    def __next__(self):
        print("Now in ClassGetInputMultipleIterators.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.")
        if self.index >= len(self.data):
            print("End of iterations")
            print("self.index value is", str(self.index))
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value, str(self.index)


multipleiterator1 = ClassGetInput("abcd") #return Now in ClassGetInput.__init__ self,stringinput.  Class initiation create the instance.
multipleiterator2 = ClassGetInput("abcd") #return Now in ClassGetInput.__init__ self,stringinput.  Class initiation create the instance.
print(multipleiterator1 is multipleiterator2) #print False
