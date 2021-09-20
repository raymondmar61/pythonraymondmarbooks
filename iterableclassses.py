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

#Python Two Class Iterators.pdf
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


letters = ClassIterationMultipleIterations("abcd")
for eachletters in letters:
    print(eachletters)
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

objectlettersforloop1 = iter(letters)
print(next(objectlettersforloop1)) #print Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.\n Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration. ('a', '1')
print(next(objectlettersforloop1)) #print Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration. ('b', '2')
objectlettersforloop2 = iter(letters)
print(next(objectlettersforloop2)) #print Now in ClassIterationMultipleIterations.__iter__ self.  Iterator method like an iterator function.  Object iterator gets a different object back.  Check instance is iterable.\n Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration. ('a', '1')
print(next(objectlettersforloop2)) #print Now in ClassIterationMultipleIterations.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration. ('b', '2')
print(objectlettersforloop1 is objectlettersforloop2) #print True RM:  objectlettersforloop1 and objectlettersforloop2 are aliases for each other.  objectlettersforloop2 sets self.index to zero also sets objectlettersforloop1 to zero.  We're unable to have the same object in multiple for loops simultaneously.
print(objectlettersforloop1 == objectlettersforloop2) #print True RM:  objectlettersforloop1 and objectlettersforloop2 are aliases for each other.  objectlettersforloop2 sets self.index to zero also sets objectlettersforloop1 to zero.  We're unable to have the same object in multiple for loops simultaneously.

class ClassIterationMultipleIterationsBringObject(object):
    def __init__(self, stringinput):
        print("Now in ClassIterationMultipleIterationsBringObject.__init__ self,stringinput.  Class initiation create the instance.")
        self.stringinput = stringinput
    def __iter__(self):
        print("Now in ClassIterationMultipleIterationsBringObject.__iter__ self.  Create and return a new instance ClassIterationMultipleIterationsBringObjectIterator.")
        return ClassIterationMultipleIterationsBringObjectIterator(self.stringinput)
class ClassIterationMultipleIterationsBringObjectIterator(object):
    def __init__(self, stringinput):
        print("Now in ClassIterationMultipleIterationsBringObjectIterator.__init__ self,stringinput.")
        self.stringinput = stringinput
        self.index = 0
        print("Starting index number", str(self.index))
    def __next__(self):
        print("Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self.")
        if self.index >= len(self.stringinput):
            print("End of iterations")
            print("self.index value is", str(self.index))
            raise StopIteration
        value = self.stringinput[self.index]
        self.index += 1
        return value, str(self.index)


lettersiterator = ClassIterationMultipleIterationsBringObject("abcd") #return Now in ClassIterationMultipleIterationsBringObject.__init__ self,stringinput.  Class initiation create the instance.
print("\n")
for eachlettersiterator in lettersiterator:
    print(eachlettersiterator)
    '''
    Now in ClassIterationMultipleIterationsBringObject.__iter__ self.  Create and return a new instance ClassIterationMultipleIterationsBringObjectIterator.
    Now in ClassIterationMultipleIterationsBringObjectIterator.__init__ self,stringinput.
    Starting index number 0
    Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self.
    ('a', '1')
    Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self.
    ('b', '2')
    Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self.
    ('c', '3')
    Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self.
    ('d', '4')
    Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self.
    End of iterations
    self.index value is 4
    '''
objectlettersiteratorforloop1 = iter(lettersiterator)
print(next(objectlettersiteratorforloop1)) #print Starting index number 0\n Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self. ('a', '1')
print(next(objectlettersiteratorforloop1)) #print Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self. ('b', '2')
objectlettersiteratorforloop2 = iter(lettersiterator)
print(next(objectlettersiteratorforloop2)) #print Starting index number 0\n Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self. ('a', '1')
print(next(objectlettersiteratorforloop2)) #print Now in ClassIterationMultipleIterationsBringObjectIterator.__next__ self. ('b', '2')
print(objectlettersiteratorforloop1 is objectlettersiteratorforloop2) #print False RM:  objectlettersiteratorforloop1 and objectlettersiteratorforloop2 are independent.  Two differente objects.
print(objectlettersiteratorforloop1 == objectlettersiteratorforloop2) #print False RM:  objectlettersiteratorforloop1 and objectlettersiteratorforloop2 are independent.  Two differente objects.

#Python Iteration Iterators Protocol.pdf
class FibonacciImplementIterationProtocol(object):
    def __iter__(self):
        print("Now in FibonacciImplementIterationProtocol.__iter__.  Send object to FibonacciIterator")
class FibonacciIterator(object):
    def __init__(self):
        print("Now in FibonacciIterator.__init__ self.  Define the first two numbers to add.")
        self.firstnumber = 0
        self.secondnumber = 1
    def __next__(self):
        print("Now in FibonacciIterator.__next__ self.")
        answer = self.firstnumber
        self.firstnumber, self.secondnumber = self.secondnumber, self.firstnumber + self.secondnumber
        return answer


#print(list(FibonacciImplementIterationProtocol()))
print("The above code creates a new instance of FibonacciImplementIterationProtocol, and then hands that to list. In order to create a list, the list class invokes the iteration protocol, stopping when it sees StopIteration. The FibonacciIterator class never raises StopIteration, so it'll continue forever. It's less good if you want your computer to do something else.")

class BookSingleClassObjectNorepr(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def titleandbook(self):
        return self.title + " wrote the book " + self.author + "."
class BookSingleClassObject(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __repr__(self):
        return f"{self.title}, by {self.author}"
class Bookshelf(object):
    def __init__(self):
        print("Now in Bookshelf__init__ self.  Class initiation create the instance.")
        self.books = []
        print("Print self.books ", self.books)
    def add_books(self, *books):
        print("Now in Bookshelf add_books.")
        self.books += books
        print("Print self.books ", self.books)
    def __iter__(self):
        print("Now in Bookshelf__iter.  Create and return a new instance BookshelfIterator.  Go to BookshelfIterator.")
        return BookshelfIterator(self.books)
class BookshelfIterator(object):
    def __init__(self, books):
        print("Now in BookshelfIterator__init__ self, books.")
        self.books = books
        self.index = 0
        print("__init__ self.books", self.books)
        print("__init__ self.index", self.index)
    def __next__(self):
        print("Now in BookshelfIterator.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.")
        if self.index >= len(self.books):
            print("End of iterations")
            print("self.index books is", str(self.index))
            raise StopIteration
        books = self.books[self.index]
        self.index += 1
        return books, str(self.index)


harrypotter = BookSingleClassObjectNorepr("JK Rowling", "HP")
print(harrypotter) #print <__main__.BookSingleClassObjectNorepr object at 0x7fcb86e7b668>
print(harrypotter.titleandbook()) #print JK Rowling wrote the book HP.
stevejobs = BookSingleClassObject("Walter Isaacson", "Steve Jobs")
print(stevejobs) #print Walter Isaacson, by Steve Jobs
harperlee = BookSingleClassObject("Harper Lee", "To Kill A Mockingbird")
shelf = Bookshelf()
shelf.add_books(stevejobs, harperlee)
'''
Now in Bookshelf__init__ self.  Class initiation create the instance.
Print self.books  []
Now in Bookshelf add_books.
Print self.books  [Walter Isaacson, by Steve Jobs, Harper Lee, by To Kill A Mockingbird]
'''
for iterateshelf in shelf:
    print(iterateshelf)
    '''
    Now in Bookshelf__iter.  Create and return a new instance BookshelfIterator.  Go to BookshelfIterator.
    Now in BookshelfIterator__init__ self, books.
    __init__ self.books [Walter Isaacson, by Steve Jobs, Harper Lee, by To Kill A Mockingbird]
    __init__ self.index 0
    Now in BookshelfIterator.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.
    (Walter Isaacson, by Steve Jobs, '1')
    Now in BookshelfIterator.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.  Start the iteration.
    (Harper Lee, by To Kill A Mockingbird, '2')
    Now in BookshelfIterator.__next__ self.  Object next function gets the next item from the iterator which should return a value.  __next__ is invoked.
    End of iterations
    self.index books is 2
    '''

#Python Being Creative With Iteration Protocol.pdf
import time
import random
class FibonacciImplementIterationProtocol(object):
    def __iter__(self):
        print("Now in FibonacciImplementIterationProtocol.__iter__.  Send object to FibonacciIterator")
        return FibonacciIterator()
class FibonacciIterator(object):
    def __init__(self):
        print("Now in FibonacciIterator.__init__ self.  Define the first two numbers to add and previous_time.")
        self.firstnumber = 0
        self.secondnumber = 1
        self.previous_time = None
    def __next__(self):
        print("Now in FibonacciIterator.__next__ self.")
        value = self.firstnumber
        self.firstnumber, self.secondnumber = self.secondnumber, self.firstnumber + self.secondnumber
        current_time = time.time()
        if self.previous_time is None:
            time_value = current_time
            self.previous_time = current_time
        else:
            time_value = current_time - self.previous_time
            self.previous_time = current_time
        return value, time_value


fibonacciinstance = FibonacciImplementIterationProtocol()
for number, time_since in fibonacciinstance:
    print(f"{number}, {time_since} elapsed since previous value")
    time.sleep(random.randint(0, 3))
    '''
    Now in FibonacciImplementIterationProtocol.__iter__.  Send object to FibonacciIterator
    Now in FibonacciIterator.__init__ self.  Define the first two numbers to add and previous_time.
    Now in FibonacciIterator.__next__ self.
    0, 1631133535.5123522 elapsed since previous value
    Now in FibonacciIterator.__next__ self.
    1, 2.007510185241699 elapsed since previous value
    Now in FibonacciIterator.__next__ self.
    1, 3.002793788909912 elapsed since previous value
    Now in FibonacciIterator.__next__ self.
    2, 2.0027008056640625 elapsed since previous value
    Now in FibonacciIterator.__next__ self.
    3, 3.0034291744232178 elapsed since previous value
    Now in FibonacciIterator.__next__ self.
    5, 2.0026378631591797 elapsed since previous value
    Now in FibonacciIterator.__next__ self.
    8, 2.002868413925171 elapsed since previous value
    Now in FibonacciIterator.__next__ self.
    13, 3.0067427158355713 elapsed since previous value
    Now in FibonacciIterator.__next__ self.
    21, 1.0015947818756104 elapsed since previous value
    ^CTraceback (most recent call last):
      File "yywork.py", line 31, in <module>
        time.sleep(random.randint(0, 3))
    KeyboardInterrupt
    '''
#The enumerate function tracks the current index of the object over which it's iterating, and returning the index along with the element itself.

#Python Generator Functions Iteration Iterators.pdf
def functionthreereturnstatements():
    return "First return statement"
    return "Second return statement"
    return "Third return statement"


print(functionthreereturnstatements()) #print First return statement

def functionthreeyieldstatements():
    yield "First return statement"
    yield "Second return statement"
    yield "Third return statement"


print(functionthreeyieldstatements()) #print <generator object functionthreeyieldstatements at 0x7f79f81ec360>
generatoriterableobjecttrueorfalse = functionthreeyieldstatements()
print(iter(generatoriterableobjecttrueorfalse) == generatoriterableobjecttrueorfalse) #print True
print(next(generatoriterableobjecttrueorfalse)) #print First return statement
print(next(generatoriterableobjecttrueorfalse)) #print Second return statement
print(next(generatoriterableobjecttrueorfalse)) #print Third return statement
print(next(generatoriterableobjecttrueorfalse))
'''
Traceback (most recent call last):
  File "yywork.py", line 23, in <module>
    print(next(generatoriterableobjecttrueorfalse)) #print *nothing*
StopIteration
'''

#Python More On Generators Generator.pdf
def fibonaccigeneratorfunction():
    firstnumber = 0
    secondnumber = 1
    #infinite while loop
    while True:
        yield firstnumber
        firstnumber, secondnumber = secondnumber, firstnumber + secondnumber
        if firstnumber == 1000:
            yield ("fibonaccigeneratorfunction while loop firstnumber==1000 break")
            break


print(fibonaccigeneratorfunction()) #print <generator object fibonaccigeneratorfunction at 0x7f01342c5a98>
print(next(fibonaccigeneratorfunction())) #print 0
print(next(fibonaccigeneratorfunction())) #print 0
print(next(fibonaccigeneratorfunction())) #print 0
for i in fibonaccigeneratorfunction():
    print(i, end=" ") #print 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393
    if i > 100000:
        break
print("\n")
print(fibonaccigeneratorfunction.__code__.co_flags) #print 99 which means fibonaccigeneratorfunction is a generator function
def fibonaccifunction():
    firstnumber = 0
    secondnumber = 1
    #infinite while loop
    while True:
        return firstnumber
        firstnumber, secondnumber = secondnumber, firstnumber + secondnumber
        if firstnumber == 1000:
            return ("fibonaccifunction while loop firstnumber==1000 break")
            break


print(fibonaccifunction.__code__.co_flags) #print 67 which means fibonaccifunction is a function

#Python Generator Functions Iteration Iterators.pdf
def functionthreereturnstatements():
    return "First return statement"
    return "Second return statement"
    return "Third return statement"


print(functionthreereturnstatements()) #print First return statement

def functionthreeyieldstatements():
    yield "First return statement"
    yield "Second return statement"
    yield "Third return statement"


print(functionthreeyieldstatements()) #print <generator object functionthreeyieldstatements at 0x7f79f81ec360>
generatoriterableobjecttrueorfalse = functionthreeyieldstatements()
print(iter(generatoriterableobjecttrueorfalse) == generatoriterableobjecttrueorfalse) #print True
print(next(generatoriterableobjecttrueorfalse)) #print First return statement
print(next(generatoriterableobjecttrueorfalse)) #print Second return statement
print(next(generatoriterableobjecttrueorfalse)) #print Third return statement
# print(next(generatoriterableobjecttrueorfalse))
'''
Traceback (most recent call last):
  File "yywork.py", line 23, in <module>
    print(next(generatoriterableobjecttrueorfalse)) #print *nothing*
StopIteration
'''

#Python More On Generators Generator.pdf
def fibonaccigeneratorfunction():
    firstnumber = 0
    secondnumber = 1
    #infinite while loop
    while True:
        yield firstnumber
        firstnumber, secondnumber = secondnumber, firstnumber + secondnumber
        if firstnumber == 1000:
            yield ("fibonaccigeneratorfunction while loop firstnumber==1000 break")
            break


print(fibonaccigeneratorfunction()) #print <generator object fibonaccigeneratorfunction at 0x7f01342c5a98>
print(next(fibonaccigeneratorfunction())) #print 0
print(next(fibonaccigeneratorfunction())) #print 0
print(next(fibonaccigeneratorfunction())) #print 0
for i in fibonaccigeneratorfunction():
    print(i, end=" ") #print 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393
    if i > 100000:
        break
print("\n")
print(fibonaccigeneratorfunction.__code__.co_flags) #print 99 which means fibonaccigeneratorfunction is a generator function
def fibonaccifunction():
    firstnumber = 0
    secondnumber = 1
    #infinite while loop
    while True:
        return firstnumber
        firstnumber, secondnumber = secondnumber, firstnumber + secondnumber
        if firstnumber == 1000:
            return ("fibonaccifunction while loop firstnumber==1000 break")
            break


print(fibonaccifunction.__code__.co_flags) #print 67 which means fibonaccifunction is a function

#Python Implementing Enumerate With A Generator.pdf
for index, item in enumerate("abcd"):
    print(f"{index}: {item}")
    '''
    0: a
    1: b
    2: c
    3: d
    '''
def enumerategeneratorfunction(data):
    index = 0
    for eachdata in data:
        print(f"eachdata in enumerategeneratorfunction {eachdata}, index number {index}")
        yield index, eachdata
        index += 1


for index, item in enumerategeneratorfunction("abcd"):
    print(f"{index}:{item}")
    '''
    eachdata in enumerategeneratorfunction a, index number 0
    0:a
    eachdata in enumerategeneratorfunction b, index number 1
    1:b
    eachdata in enumerategeneratorfunction c, index number 2
    2:c
    eachdata in enumerategeneratorfunction d, index number 3
    3:d
    '''
def notreallyenumeratefunction(data):
    index = 111
    for eachdata in data:
        print(f"eachdata in notreallyenumeratefunction {eachdata}, index number {index}")
        return index, eachdata
        index += 1


for item in notreallyenumeratefunction("abcd"):
    print(item)
    '''
    eachdata in notreallyenumeratefunction a, index number 111
    111
    a
    '''
def notreallyenumeratefunction2(data):
    index = 111
    returninlistformat = []
    for eachdata in data:
        print(f"eachdata in notreallyenumeratefunction2 {eachdata}, index number {index}")
        returninlistformat.append(eachdata + ":" + str(index))
        print(returninlistformat)
        index += 1
    return returninlistformat


for item in notreallyenumeratefunction2("abcd"):
    print(item)
    '''
    eachdata in notreallyenumeratefunction2 a, index number 111
    ['a:111']
    eachdata in notreallyenumeratefunction2 b, index number 112
    ['a:111', 'b:112']
    eachdata in notreallyenumeratefunction2 c, index number 113
    ['a:111', 'b:112', 'c:113']
    eachdata in notreallyenumeratefunction2 d, index number 114
    ['a:111', 'b:112', 'c:113', 'd:114']
    a:111
    b:112
    c:113
    d:114
    '''

for index, item in enumerate("abcd", 111):
    print(f"{index}:{item}")
    '''
    111:a
    112:b
    113:c
    114:d
    '''
def enumerategeneratorfunction2(data, index=0):
    for eachdata in data:
        print(f"eachdata in enumerategeneratorfunction2 {eachdata}, index number {index}")
        yield eachdata, index
        index += 1


for item, index in enumerategeneratorfunction2("abcd", 111):
    print(f"{item}:{index}")
    '''
    eachdata in enumerategeneratorfunction2 a, index number 111
    a:111
    eachdata in enumerategeneratorfunction2 b, index number 112
    b:112
    eachdata in enumerategeneratorfunction2 c, index number 113
    c:113
    eachdata in enumerategeneratorfunction2 d, index number 114
    d:114
    '''
