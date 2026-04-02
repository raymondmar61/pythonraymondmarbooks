#sort() method changes the object itself.  sorted() function returns a sorted copy of the list.
threetuplesnumbers = [(1, 4, 3), (1, 5, 7), (1, 0, 1)]
print(threetuplesnumbers) #print [(1, 4, 3), (1, 5, 7), (1, 0, 1)]
print(sorted(threetuplesnumbers)) #print [(1, 0, 1), (1, 4, 3), (1, 5, 7)]
threetuplesnumbers.sort()
print(threetuplesnumbers) #print [(1, 0, 1), (1, 4, 3), (1, 5, 7)]
sortlisttuples = [(1, "a", "apple"), (3, "b", "ball"), (2, "a", "ankle"), (4, "c", "cookie")]
print(sortlisttuples) #print [(1, "a", "apple"), (3, "b", "ball"), (2, "a", "ankle"), (4, "c", "cookie")]
sortlisttuples.sort(key=lambda x: (x[2])) #sort by third item in the list of tuples
print(sortlisttuples) #print [(1, 'a', 'apple'), (2, 'a', 'ankle'), (3, 'b', 'ball'), (4, 'c', 'cookie')]
solution = [(4, 'a', '1:aaaa'), (2, 'd', '2:dd'), (2, 'e', '=:ee'), (2, 'f', '2:ff'), (3, 'h', '1:hhh'), (2, 'i', '2:ii'), (3, 'm', '2:mmm'), (5, 'n', '2:nnnnn'), (2, 'r', '2:rr'), (2, 's', '=:ss'), (3, 'y', '2:yyy')]
print(solution) #print [(4, 'a', '1:aaaa'), (2, 'd', '2:dd'), (2, 'e', '=:ee'), (2, 'f', '2:ff'), (3, 'h', '1:hhh'), (2, 'i', '2:ii'), (3, 'm', '2:mmm'), (5, 'n', '2:nnnnn'), (2, 'r', '2:rr'), (2, 's', '=:ss'), (3, 'y', '2:yyy')]
solution.sort(key=lambda x: (-x[0], x[1], x[2])) #negate or negative is sort descending
print(solution) #print [(5, 'n', '2:nnnnn'), (4, 'a', '1:aaaa'), (3, 'h', '1:hhh'), (3, 'm', '2:mmm'), (3, 'y', '2:yyy'), (2, 'd', '2:dd'), (2, 'e', '=:ee'), (2, 'f', '2:ff'), (2, 'i', '2:ii'), (2, 'r', '2:rr'), (2, 's', '=:ss')]
solution.sort(key=lambda x: (-x[0], x[2][0], x[1])) #negate or negative is sort descending
print(solution) #print [(5, 'n', '2:nnnnn'), (4, 'a', '1:aaaa'), (3, 'h', '1:hhh'), (3, 'm', '2:mmm'), (3, 'y', '2:yyy'), (2, 'd', '2:dd'), (2, 'f', '2:ff'), (2, 'i', '2:ii'), (2, 'r', '2:rr'), (2, 'e', '=:ee'), (2, 's', '=:ss')]
finalsolutionsubstring = ""
for eachsolution in solution:
    finalsolutionsubstring = finalsolutionsubstring + eachsolution[2] + "/"
print(finalsolutionsubstring[:-1]) #print 2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss
from operator import itemgetter
fruitnumbers = [("cherry", 5), ("apple", 10), ("banana", 5)]
print(fruitnumbers) #print [('cherry', 5), ('apple', 10), ('banana', 5)]
fruitnumbers.sort(key=itemgetter(1, 0)) #sort number first, fruit second
print(fruitnumbers) #print [('banana', 5), ('cherry', 5), ('apple', 10)]
#Multiple sorts stable sorting.  Sort by second key first.  Sort by first key second.
fruitnumbers = [("cherry", 5), ("apple", 10), ("banana", 5)]
print(fruitnumbers) #print [('cherry', 5), ('apple', 10), ('banana', 5)]
sortbystringlength = [("Hyperion", 3500), ("Hadoop", 2500), ("Spark", 2200), ("Python", 3000)]
print(sortbystringlength) #print [('Hyperion', 3500), ('Hadoop', 2500), ('Spark', 2200), ('Python', 3000)]
print(sorted(sortbystringlength, key=lambda x: (len(x[0])))) #print [('Spark', 2200), ('Hadoop', 2500), ('Python', 3000), ('Hyperion', 3500)]
fruitnumbers.sort(key=lambda x: (x[1]))
fruitnumbers.sort(key=lambda x: (x[0]))
print(fruitnumbers) #print [('apple', 10), ('banana', 5), ('cherry', 5)]
newlist = [("p", 3, 5), ("i", 2, 7), ("d", 1, 8), ("b", 7, 4), ("v", 4, 9), ("t", 8, 2), ("i", 4, 1), ("d", 1, 9), ("p", 3, 7), ("c", 7, 1), ("f", 7, 5), ("x", 4, 1), ("e", 1, 9), ("h", 7, 4), ("a", 7, 4), ("k", 8, 2), ("c", 8, 2), ("r", 8, 1), ]
print(newlist) #print [('p', 3, 5), ('i', 2, 7), ('d', 1, 8), ('b', 7, 4), ('v', 4, 9), ('t', 8, 2), ('i', 4, 1), ('d', 1, 9), ('p', 3, 7), ('c', 7, 1), ('f', 7, 5), ('x', 4, 1), ('e', 1, 9), ('h', 7, 4), ('a', 7, 4), ('k', 8, 2), ('c', 8, 2), ('r', 8, 1)]
sortdescendingmiddlerightleft = sorted(newlist, key=lambda item: (item[1], item[2], item[0]), reverse=True)
print(sortdescendingmiddlerightleft) #print [('t', 8, 2), ('k', 8, 2), ('c', 8, 2), ('r', 8, 1), ('f', 7, 5), ('h', 7, 4), ('b', 7, 4), ('a', 7, 4), ('c', 7, 1), ('v', 4, 9), ('x', 4, 1), ('i', 4, 1), ('p', 3, 7), ('p', 3, 5), ('i', 2, 7), ('e', 1, 9), ('d', 1, 9), ('d', 1, 8)]
def functionsortdata(datalist):
    return datalist[1]


sortmiddlenumber = [(1, 7, 3), (4, 9, 6), (7, 3, 9)]
print(sortmiddlenumber) #print [(1, 7, 3), (4, 9, 6), (7, 3, 9)]
sortmiddlenumber.sort(key=functionsortdata)
print(sortmiddlenumber) #print [(7, 3, 9), (1, 7, 3), (4, 9, 6)]

#Breakdown Lambda
coordinates = [(1, 2), (5, 1), (-1, -1), (16, 2)] #Sort ascending order second number, descending order first number
print(coordinates) #print [(1, 2), (5, 1), (-1, -1), (16, 2)]
print(sorted(coordinates, key=lambda x: (x[1], -x[0]))) #print [(-1, -1), (5, 1), (16, 2), (1, 2)]
def sortfunction(numbers):
    print(numbers)
    x, y = numbers
    print(f"x is {x}, y is {y}-->y is {y}, -x is {x}")
    '''
    (1, 2)
    x is 1, y is 2-->y is 2, -x is 1
    (5, 1)
    x is 5, y is 1-->y is 1, -x is 5
    (-1, -1)
    x is -1, y is -1-->y is -1, -x is -1
    (16, 2)
    x is 16, y is 2-->y is 2, -x is 16
    '''
    return y, -x


print(sorted(coordinates, key=sortfunction)) #print [(-1, -1), (5, 1), (16, 2), (1, 2)]


#https://forum.codewithmosh.com/t/double-sorting-list-of-tuples/13546
#If you only need to reverse one of the sort keys, then you would use a different approach. For example, suppose you had a list of strings and you wanted them sorted by length (shortest to longest) and reverse alphabetical (after sorting by length).  We can use this reversor class to reverse any comparable keys (I think you need the __gt__ method as well, not sure why that answer did not include it),
class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj

    def __gt__(self, other):
        return other.obj > self.obj


listofstrings = ["just", "some", "simple", "strings", "here"]
print(listofstrings) #print ['just', 'some', 'simple', 'strings', 'here']
result = sorted(listofstrings, key=lambda item: (len(item), reversor(item)))
print(result) #print ['some', 'just', 'here', 'simple', 'strings']
