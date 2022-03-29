#Implementing Template Design Pattern Python Reuven Lerner.pdf
#A design pattern in the behavioral category.

import random
class RandomNumbers:
    def getnumbers(self, start, stop, count):
        return [random.randint(start, stop) for i in range(count)]


listofrandomnumbersinstance = RandomNumbers()
print(listofrandomnumbersinstance.getnumbers(0, 100, 5)) #print [10, 19, 15, 64, 20]
print(listofrandomnumbersinstance.getnumbers(0, 50, 10)) #print [42, 20, 31, 40, 27, 28, 20, 37, 19, 3]

#What if we want floats instead of integers.  What if we want to do something to each integers after the intergers are chosen.  We can write if statements.  A more flexible way is inheritance.  First, break out the getnumbers method into smaller methods.  Second, encourage anyone who wants to customize some or all of our implementation by inheriting from the RandomNumbers class and override one or more methods.

class RandomNumbers2:
    def __init__(self):
        self.start = None
        self.stop = None
        self.count = None
        self.values = None
    def setup(self, start, stop, count):
        self.start = start
        self.stop = stop
        self.count = count
        self.values = []
    def generatevalues(self):
        print("At generatevalues() method")
        self.values = [random.randint(self.start, self.stop) for i in range(self.count)]
    def transform(self):
        pass
    def teardown(self):
        pass
    def getnumbers(self, start, stop, count):
        self.setup(start, stop, count)
        print("getnumbers() method start, stop, count: {} {} {}" .format(self.start, self.stop, self.count))
        self.generatevalues()
        self.transform()
        self.teardown()
        print("getnumbers() method here is self.values", self.values)
        return self.values


listofrandomnumbers2instance = RandomNumbers2()
print(listofrandomnumbers2instance.getnumbers(0, 100, 5)) #print [10, 19, 15, 64, 20]
'''
getnumbers() method start, stop, count: 0 100 5
At generatevalues() method
getnumbers() method here is self.values [76, 35, 10, 95, 17]
[76, 35, 10, 95, 17]
'''
print(listofrandomnumbers2instance.getnumbers(0, 50, 10)) #print [42, 20, 31, 40, 27, 28, 20, 37, 19, 3]
'''
getnumbers() method start, stop, count: 0 50 10
At generatevalues() method
getnumbers() method here is self.values [46, 11, 39, 8, 18, 10, 49, 17, 42, 49]
[46, 11, 39, 8, 18, 10, 49, 17, 42, 49]
'''

class RandomStringNumbers(RandomNumbers2):
    def transform(self):
        print("At transform() method in RandomStringNumbers class.")
        self.values = [str(oneitem) for oneitem in self.values]


listofrandomstringnumbersinstance = RandomStringNumbers()
print(listofrandomstringnumbersinstance.getnumbers(0, 100, 5))
'''
getnumbers() method start, stop, count: 0 100 5
At generatevalues() method
At transform() method in RandomStringNumbers class.
getnumbers() method here is self.values ['84', '17', '91', '74', '34']
['84', '17', '91', '74', '34']
'''
print(listofrandomstringnumbersinstance.getnumbers(0, 50, 10))
'''
getnumbers() method start, stop, count: 0 50 10
At generatevalues() method
At transform() method in RandomStringNumbers class.
getnumbers() method here is self.values ['46', '6', '36', '49', '41', '41', '29', '35', '31', '27']
['46', '6', '36', '49', '41', '41', '29', '35', '31', '27']
'''