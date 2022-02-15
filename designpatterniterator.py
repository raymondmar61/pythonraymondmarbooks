#Design Patterns Python Data Structures.pdf
class IterableDesignPattern:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        print("Here is the __iter__ method")
        return self
    def __next__(self):
        print("Here is the  __next__ method")
        if self.index >= len(self.data):
            print("Stop the iteration")
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value, self.index - 1


instance01 = IterableDesignPattern("abcde")
for eachinstance01 in instance01:
    print(eachinstance01)
    '''
    Here is the __iter__ method
    Here is the  __next__ method
    ('a', 0)
    Here is the  __next__ method
    ('b', 1)
    Here is the  __next__ method
    ('c', 2)
    Here is the  __next__ method
    ('d', 3)
    Here is the  __next__ method
    ('e', 4)
    Here is the  __next__ method
    Stop the iteration
    '''
instance02 = IterableDesignPattern("raymond")
for eachinstance02 in instance02:
    print(eachinstance02)
    '''
    Here is the __iter__ method
    Here is the  __next__ method
    ('r', 0)
    Here is the  __next__ method
    ('a', 1)
    Here is the  __next__ method
    ('y', 2)
    Here is the  __next__ method
    ('m', 3)
    Here is the  __next__ method
    ('o', 4)
    Here is the  __next__ method
    ('n', 5)
    Here is the  __next__ method
    ('d', 6)
    Here is the  __next__ method
    Stop the iteration
    '''
#Classes have other responsibilities.  It's a good idea to separate the iteration from the class itself.
class SeparateIteration:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __next__(self):
        print("In SeparateIteration class.  Here is the  __next__ method")
        if self.index >= len(self.data):
            print("In SeparateIteration class.  Stop the iteration")
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value, self.index - 1
class IterationItself:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        print("In IterationItself class.  Here is the __iter__ method")
        return SeparateIteration(self.data)


instance01 = IterationItself("abcde")
for eachinstance01 in instance01:
    print(eachinstance01)
    '''
    In IterationItself class.  Here is the __iter__ method
    In SeparateIteration class.  Here is the  __next__ method
    ('a', 0)
    In SeparateIteration class.  Here is the  __next__ method
    ('b', 1)
    In SeparateIteration class.  Here is the  __next__ method
    ('c', 2)
    In SeparateIteration class.  Here is the  __next__ method
    ('d', 3)
    In SeparateIteration class.  Here is the  __next__ method
    ('e', 4)
    In SeparateIteration class.  Here is the  __next__ method
    In SeparateIteration class.  Stop the iteration
    '''
instance02 = IterationItself("raymond")
for eachinstance02 in instance02:
    print(eachinstance02)
    '''
    In IterationItself class.  Here is the __iter__ method
    In SeparateIteration class.  Here is the  __next__ method
    ('r', 0)
    In SeparateIteration class.  Here is the  __next__ method
    ('a', 1)
    In SeparateIteration class.  Here is the  __next__ method
    ('y', 2)
    In SeparateIteration class.  Here is the  __next__ method
    ('m', 3)
    In SeparateIteration class.  Here is the  __next__ method
    ('o', 4)
    In SeparateIteration class.  Here is the  __next__ method
    ('n', 5)
    In SeparateIteration class.  Here is the  __next__ method
    ('d', 6)
    In SeparateIteration class.  Here is the  __next__ method
    In SeparateIteration class.  Stop the iteration
    '''
#Iterate differently over the data.  For example, iterate the vowels in the data or iterate the data backwards.  Python allows each object to be iterable in one way.  We can have methods which return other iterable objects.
class SeparateIteration2:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __next__(self):
        print("In SeparateIteration2 class.  Here is the  __next__ method")
        if self.index >= len(self.data):
            print("In SeparateIteration2 class.  Stop the iteration")
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value, self.index - 1
class VowelIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        print("In VowelIterator class.  Here is the  __iter__ method")
        return self
    def __next__(self):
        while True:
            print("In VowelIterator class.  Here is the  __next__ method")
            if self.index >= len(self.data):
                print("In VowelIterator class.  Stop the iteration")
                raise StopIteration
            value = self.data[self.index]
            self.index += 1
            if value in "aeiou":
                return value, self.index - 1
class BackwardIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(self.data) - 1
    def __iter__(self):
        print("In BackwardIterator class.  Here is the  __iter__ method")
        return self
    def __next__(self):
        print("In BackwardIterator class.  Here is the  __next__ method")
        if self.index < 0:
            print("In BackwardIterator class.  Stop the iteration")
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value, self.index - 1

class IterateMultipleMethods:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        print("In IterateMultipleMethods class.  Here is the  __iter__ method")
        return SeparateIteration2(self.data)
    def vowels(self):
        print("In IterateMultipleMethods class.  Here is the vowels method")
        return VowelIterator(self.data)
    def backward(self):
        print("In IterateMultipleMethods class.  Here is the backward method")
        return BackwardIterator(self.data)


instance01 = IterateMultipleMethods("abcde")
for eachinstance01 in instance01:
    print(eachinstance01)
    '''
    In IterateMultipleMethods class.  Here is the  __iter__ method
    In SeparateIteration2 class.  Here is the  __next__ method
    ('a', 0)
    In SeparateIteration2 class.  Here is the  __next__ method
    ('b', 1)
    In SeparateIteration2 class.  Here is the  __next__ method
    ('c', 2)
    In SeparateIteration2 class.  Here is the  __next__ method
    ('d', 3)
    In SeparateIteration2 class.  Here is the  __next__ method
    ('e', 4)
    In SeparateIteration2 class.  Here is the  __next__ method
    In SeparateIteration2 class.  Stop the iteration
    '''
print("\n")
instance02 = IterateMultipleMethods("raymond")
for eachinstance02vowels in instance02.vowels():
    print(eachinstance02vowels)
    '''
    In IterateMultipleMethods class.  Here is the vowels method
    In VowelIterator class.  Here is the  __iter__ method
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    ('a', 1)
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    ('o', 4)
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Stop the iteration
    '''
instance03 = IterateMultipleMethods("edwardelric")
for eachinstance03backward in instance03.backward():
    print(eachinstance03backward)
    '''
    In IterateMultipleMethods class.  Here is the backward method
    In BackwardIterator class.  Here is the  __iter__ method
    In BackwardIterator class.  Here is the  __next__ method
    ('c', 8)
    In BackwardIterator class.  Here is the  __next__ method
    ('i', 7)
    In BackwardIterator class.  Here is the  __next__ method
    ('r', 6)
    In BackwardIterator class.  Here is the  __next__ method
    ('l', 5)
    In BackwardIterator class.  Here is the  __next__ method
    ('e', 4)
    In BackwardIterator class.  Here is the  __next__ method
    ('d', 3)
    In BackwardIterator class.  Here is the  __next__ method
    ('r', 2)
    In BackwardIterator class.  Here is the  __next__ method
    ('a', 1)
    In BackwardIterator class.  Here is the  __next__ method
    ('w', 0)
    In BackwardIterator class.  Here is the  __next__ method
    ('d', -1)
    In BackwardIterator class.  Here is the  __next__ method
    ('e', -2)
    In BackwardIterator class.  Here is the  __next__ method
    In BackwardIterator class.  Stop the iteration
    '''
instance04 = VowelIterator("raymond")
for eachinstance04 in instance04:
    print(eachinstance04)
    '''
    In VowelIterator class.  Here is the  __iter__ method
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    ('a', 1)
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    ('o', 4)
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Here is the  __next__ method
    In VowelIterator class.  Stop the iteration
    '''
instance05 = BackwardIterator("edwardelric")
for eachinstance05 in instance05:
    print(eachinstance05)
    '''
    In BackwardIterator class.  Here is the  __iter__ method
    In BackwardIterator class.  Here is the  __next__ method
    ('c', 8)
    In BackwardIterator class.  Here is the  __next__ method
    ('i', 7)
    In BackwardIterator class.  Here is the  __next__ method
    ('r', 6)
    In BackwardIterator class.  Here is the  __next__ method
    ('l', 5)
    In BackwardIterator class.  Here is the  __next__ method
    ('e', 4)
    In BackwardIterator class.  Here is the  __next__ method
    ('d', 3)
    In BackwardIterator class.  Here is the  __next__ method
    ('r', 2)
    In BackwardIterator class.  Here is the  __next__ method
    ('a', 1)
    In BackwardIterator class.  Here is the  __next__ method
    ('w', 0)
    In BackwardIterator class.  Here is the  __next__ method
    ('d', -1)
    In BackwardIterator class.  Here is the  __next__ method
    ('e', -2)
    In BackwardIterator class.  Here is the  __next__ method
    In BackwardIterator class.  Stop the iteration
    '''
