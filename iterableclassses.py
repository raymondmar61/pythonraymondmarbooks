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
