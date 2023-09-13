#Lists
listitemscontainedinbrackets = ["Multiple data types", 55, True, "contained in list", -1, 3.50]
print(listitemscontainedinbrackets) #print ['Multiple data types', 55, True, 'contained in list', -1, 3.5]
copylistitemscontainedinbrackets = listitemscontainedinbrackets.copy()
print(copylistitemscontainedinbrackets) #print ['Multiple data types', 55, True, 'contained in list', -1, 3.5]
listvariable1, listvariable2, listvariable3 = ["multiple variables", "one list", "separate list entry"]
print(listvariable2) #print one list
nest1 = ["a list of lists", "numbers", 1, 5, 7]
nest2 = ["nested lists sublists", "fruit", "apple", "orange", "banana"]
nestedlists = [nest1, nest2]
print(nestedlists) #print [['a list of lists', 'numbers', 1, 5, 7], ['nested lists sublists', 'fruit', 'apple', 'orange', 'banana']]
print(nestedlists[0][2]) #print 1
print(nestedlists[1][-1]) #print banana
concatenatelist = nest1 + nest2 #Concatenate lists or combine lists
print(concatenatelist) #print ['a list of lists', 'numbers', 1, 5, 7, 'nested lists sublists', 'fruit', 'apple', 'orange', 'banana']
replicatelist = ["multiply", "a", "list", "multiple lists"] * 3
print(replicatelist) #print ['multiply', 'a', 'list', 'multiple lists', 'multiply', 'a', 'list', 'multiple lists', 'multiply', 'a', 'list', 'multiple lists']
appendlistinsidelist = []
leftlist = "sublist append"
rightlist = "inside main list"
appendlistinsidelist.append([leftlist, rightlist])
print(appendlistinsidelist) #print [['sublist append', 'inside main list']]
leftlist = "A second append sublist"
rightlist = "the second sublist inside main list"
appendlistinsidelist.append([leftlist, rightlist])
print(appendlistinsidelist) #print [['sublist append', 'inside main list'], ['A second append sublist', 'the second sublist inside main list']]
print(list("Convert string to list 491")) #print ['C', 'o', 'n', 'v', 'e', 'r', 't', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 't', 'o', ' ', 'l', 'i', 's', 't', ' ', '4', '9', '1']
convertnumberstostring = list(map(str, [29, 58, -5, 210, 985]))
print(convertnumberstostring) #print ['29', '58', '-5', '210', '985']
duplicateitems = ["cat", "dog", "moon", "shoe", "cat", "dog", "cat"]
print(duplicateitems) #print ['cat', 'dog', 'moon', 'shoe', 'cat', 'dog', 'cat']
countitemsinlist = duplicateitems.count("cat")
print(countitemsinlist) #print 3
print(sorted(duplicateitems, reverse=False)) #print ['cat', 'cat', 'cat', 'dog', 'dog', 'moon', 'shoe']
duplicateitems.sort(reverse=True)
print(duplicateitems) #print ['shoe', 'moon', 'dog', 'dog', 'cat', 'cat', 'cat']
duplicateitems = ["cat", "dog", "moon", "shoe", "cat", "dog", "cat"]
print(duplicateitems) #print ['cat', 'dog', 'moon', 'shoe', 'cat', 'dog', 'cat']
duplicateitems.reverse() #print list backwards
print(duplicateitems) #print ['cat', 'dog', 'cat', 'shoe', 'moon', 'dog', 'cat']
sortcaseinsensitive = "This is a bunch of words in a Python string With No Period".split() #string to list
print(sortcaseinsensitive) #print ['This', 'is', 'a', 'bunch', 'of', 'words', 'in', 'a', 'Python', 'string', 'With', 'No', 'Period']
sortcaseinsensitive.sort(key=str.lower) #no key=str.lower sortcaseinsensitive sorted case sensitive uppercase letters first
print(sortcaseinsensitive) #print ['a', 'a', 'bunch', 'in', 'is', 'No', 'of', 'Period', 'Python', 'string', 'This', 'With', 'words']
sortcaseinsensitive = "This is a bunch of words in a Python string With No Period".split() #string to list
def functionsortlastletteroftheword(word):
    return word[::-1]


wordlist = ["Python", "is", "better", "than", "C"]
print(wordlist) #print ['Python', 'is', 'better', 'than', 'C']
wordlist.sort(key=len)
print(wordlist) #print ['C', 'is', 'than', 'Python', 'better']
sortcaseinsensitive.sort(key=functionsortlastletteroftheword)
print(sortcaseinsensitive) #print ['a', 'a', 'Period', 'of', 'string', 'bunch', 'With', 'in', 'Python', 'No', 'words', 'is', 'This']
from operator import itemgetter #https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
sortlistwithinalist = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
print(sortlistwithinalist) #print [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
sortlistwithinalist.sort(key=itemgetter(1)) #Sort the second element or index number one in the sublists
print(sortlistwithinalist) #print [[4, 0, 1], [2, 1, 3], [1, 2, 3]]
joinitemsinlist = ["convert", "list", "to", "string"] #list to string
print(joinitemsinlist) #print ['convert', 'list', 'to', 'string']
print(" ".join(joinitemsinlist)) #print convert list to string
print("-".join(joinitemsinlist)) #print convert-list-to-string
print("\n".join(joinitemsinlist)) #print convert\n list\n to\n string
threepipes = ["|||"]
fourthreepipes = threepipes * 4
print(fourthreepipes) #print ['|||', '|||', '|||', '|||']
joinfourthreepipes = "".join(fourthreepipes)
print(joinfourthreepipes) #print ||||||||||||
usernumbers = "1 2 3 1 2 3 1 2 3 4"
print(usernumbers.split()) #print ['1', '2', '3', '1', '2', '3', '1', '2', '3', '4'].  .split separates number string by spaces create a list
initializetotal = 0
for eachusernumbers in usernumbers.split():
    initializetotal += int(eachusernumbers)
print(initializetotal) #print 22
usernumberslistcomprehension = [int(eachusernumbers) for eachusernumbers in usernumbers.split()]
print(usernumberslistcomprehension) #print [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
print(sum(usernumberslistcomprehension)) #print 22
sumusernumberslistcomprehension = sum([int(eachusernumbers) for eachusernumbers in usernumbers.split()])
print(sumusernumberslistcomprehension) #print 22
#enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
firstname = ["Bucky", "Tom", "Taylor"]
lastname = ["Roberts", "Hanks", "Swift"]
print(enumerate(firstname)) #print <enumerate object at 0x7f01d25b5708>
print(list(enumerate(firstname))) #print [(0, 'Bucky'), (1, 'Tom'), (2, 'Taylor')]
print(list(enumerate(lastname))) #print [(0, 'Roberts'), (1, 'Hanks'), (2, 'Swift')]
for index, value in list(enumerate(lastname)):
    print(index, value)
    '''
    0 Roberts
    1 Hanks
    2 Swift
    '''
for anyindexvariable, anyvaluevariable in list(enumerate(lastname)):
    print(anyindexvariable, anyvaluevariable)
    '''
    0 Roberts
    1 Hanks
    2 Swift
    '''
print(tuple(enumerate(firstname))) #print ((0, 'Bucky'), (1, 'Tom'), (2, 'Taylor'))
names = zip(firstname, lastname)
print(names) #print <zip object at 0x7f7c3a3eeb48>
nameslistcomprehension = list(names)
print(nameslistcomprehension) #print []
nameslistcomprehension = list(zip(names))
print(nameslistcomprehension) #print []
nameslistcomprehension = list(zip(firstname, lastname))
print(nameslistcomprehension) #print [('Bucky', 'Roberts'), ('Tom', 'Hanks'), ('Taylor', 'Swift')]
print(list(zip(firstname, lastname))) #print [('Bucky', 'Roberts'), ('Tom', 'Hanks'), ('Taylor', 'Swift')]
print(list(zip(firstname, lastname))[1]) #print ('Tom', 'Hanks')
print(list(zip(firstname, lastname))[1][1]) #print Hanks
print(tuple(zip(firstname, lastname))) #print (('Bucky', 'Roberts'), ('Tom', 'Hanks'), ('Taylor', 'Swift'))
insertitemsinlist = [29, 58, 66, 71, 87]
combinelistsplussign = [90, 91, 98]
insertitemsinlist = insertitemsinlist + combinelistsplussign
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98]
insertitemsinlist.append(120) #append item to list
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98, 120]
# insertitemsinlist.append(6594, 3799) #TypeError: append() takes exactly one argument (2 given)
insertitemsinlist.append([6594, 3799])
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98, 120, [6594, 3799]]
insertitemsinlist.pop() #delete last item in list
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98, 120]
insertitemsinlist.extend([6594, 3799]) #insert multiple items to list
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98, 120, 6594, 3799]
insertitemsinlist.insert(3, "Insert at index number 3")
print(insertitemsinlist) #print [29, 58, 66, 'Insert at index number 3', 71, 87, 90, 91, 98, 120, 6594, 3799, -1, -10, -54]
insertitemsinlist.insert(5, insertitemsinlist.extend([98453, 87990]))
print(insertitemsinlist) #print [29, 58, 66, 'Insert at index number 3', 71, None, 87, 90, 91, 98, 120, 6594, 3799, 98453, 87990]
numberofitemsinlist = len(insertitemsinlist)
print(numberofitemsinlist) #print 15
insertitemsinlist[numberofitemsinlist + 1:] = [-1, -10, -54] #insert multiple items to list
print(insertitemsinlist) #print [29, 58, 66, 'Insert at index number 3', 71, None, 87, 90, 91, 98, 120, 6594, 3799, 98453, 87990, -1, -10, -54]
insertitemsinlist.pop(5) #delete specific index position.  Can save to a variable to be used later.
print(insertitemsinlist) #print [29, 58, 66, 'Insert at index number 3', 71, 87, 90, 91, 98, 120, 6594, 3799, 98453, 87990, -1, -10, -54]
insertitemsinlist.remove("Insert at index number 3") #delete specific item
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98, 120, 6594, 3799, 98453, 87990, -1, -10, -54]
savedeletedlistitemvariable = insertitemsinlist.pop(2)
print(insertitemsinlist) #print [29, 58, 71, 87, 90, 91, 98, 120, 6594, 3799, 98453, 87990, -1, -10, -54]
print(savedeletedlistitemvariable) #print 66
savedeletedlistitemvariable = insertitemsinlist.remove(6594)
print(insertitemsinlist) #print [29, 58, 71, 87, 90, 91, 98, 120, 3799, 98453, 87990, -1, -10, -54]
insertitemsinlist[4] = 9090 #replace item in list
print(insertitemsinlist) #print [29, 58, 71, 87, 9090, 91, 98, 120, 3799, 98453, 87990, -1, -10, -54]
print(savedeletedlistitemvariable) #print None
del insertitemsinlist[6] #delete item in list which is sixth index position 98
print(insertitemsinlist) #print [29, 58, 71, 87, 9090, 91, 120, 3799, 98453, 87990, -1, -10, -54]
del insertitemsinlist[2:4] #delete item in list which is second and third index positions 71 and 87
print(insertitemsinlist) #print [29, 58, 9090, 91, 120, 3799, 98453, 87990, -1, -10, -54]
insertitemsinlist.sort(key=abs) #Sort by absolute value ignore negatives; all numbers are positive.  The .sort method must be stand alone.  No assigned variable.  No inside a print function.
print(insertitemsinlist) #print [-1, -10, 29, -54, 58, 91, 120, 3799, 9090, 87990, 98453]
insertitemsinlist.clear()
print(insertitemsinlist) #print [].  Delete all items in a list.
grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(grades) #print [32, 43, 654, 34, 132, 66, 99, 532]
sortedfunction = sorted(grades, reverse=False)
print(sortedfunction) #print [32, 34, 43, 66, 99, 132, 532, 654].  Sorted function also works for a list.
print(min(grades)) #print 32
print(max(grades)) #print 654
print(sum(grades)) #print 1592
import heapq
print(heapq.nlargest(1, grades)) #print [654]
print(heapq.nlargest(3, grades)) #print [654, 532, 132]
print(heapq.nsmallest(2, grades)) #print [32, 34]
stocks = [{"Ticker": "AAPL", "Price": 201}, {"Ticker": "GOOG", "Price": 800}, {"Ticker": "F", "Price": 54}, {"Ticker": "MSFT", "Price": 313}, {"Ticker": "TUNA", "Price": 68}]
print(stocks) #print [{'Ticker': 'AAPL', 'Price': 201}, {'Ticker': 'GOOG', 'Price': 800}, {'Ticker': 'F', 'Price': 54}, {'Ticker': 'MSFT', 'Price': 313}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nsmallest(2, stocks, key=lambda stock: stock["Price"])) #print [{'Ticker': 'F', 'Price': 54}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nsmallest(2, stocks, key=lambda anyvariable: anyvariable["Price"])) #print [{'Ticker': 'F', 'Price': 54}, {'Ticker': 'TUNA', 'Price': 68}]
print(heapq.nlargest(2, stocks, key=lambda anyvariable: anyvariable["Ticker"])) #print [{'Ticker': 'TUNA', 'Price': 68}, {'Ticker': 'MSFT', 'Price': 313}]
extractfromlistslice = [11, 22, 33, 44, 55, 66, 77, 88]
print(len(extractfromlistslice)) #print 8
print(extractfromlistslice) #print [11, 22, 33, 44, 55, 66, 77, 88]
print(extractfromlistslice[2]) #print 33
print(extractfromlistslice[-1]) #print 88
print(extractfromlistslice[-4]) #print 55
print(extractfromlistslice[2:7]) #print [33, 44, 55, 66, 77]
print(extractfromlistslice[6:1]) #print []
print(extractfromlistslice[6:1:-1]) #print [77, 66, 55, 44, 33]
print(extractfromlistslice[:4]) #print [11, 22, 33, 44]
print(extractfromlistslice[5:]) #print [66, 77, 88]
print(extractfromlistslice[-3:]) #print [66, 77, 88].  #a negative index returns an element a certain distance beginning from the end of a list
print(extractfromlistslice[-5:-2]) #print [44, 55, 66].  #a negative index returns an element a certain distance beginning from the end of a list
print(extractfromlistslice[0:-1]) #print [11, 22, 33, 44, 55, 66, 77]
print(extractfromlistslice[1:-1]) #print [22, 33, 44, 55, 66, 77]
print(extractfromlistslice[::2]) #print [11, 33, 55, 77]
print(extractfromlistslice[::-1]) #print [88, 77, 66, 55, 44, 33, 22, 11]
print(extractfromlistslice[::-3]) #print [88, 55, 22]
print(extractfromlistslice[-3::2]) #print [66, 88]
print(extractfromlistslice[-1::-3]) #print [88, 55, 22]
print(extractfromlistslice[-4::-2]) #print [55, 33, 11]
print(extractfromlistslice[3::2]) #print [44, 66, 88]
print(extractfromlistslice[0::-3]) #print [11]
print(extractfromlistslice[6::-3]) #print [77, 44, 11]
print(extractfromlistslice[5:9:]) #print [66, 77, 88]
print(extractfromlistslice[5:10:]) #print [66, 77, 88]
print(extractfromlistslice[5:9:-1]) #print []
print(extractfromlistslice[7:4:-1]) #print [88, 77, 66]
print(extractfromlistslice[-1:-4:-1]) #print [88, 77, 66]
print(extractfromlistslice[1:4:]) #print [22, 33, 44]
print(extractfromlistslice[1:4:-1]) #print []
print(extractfromlistslice[3:0:-1]) #print [44, 33, 22]
print(extractfromlistslice[-5:-8:-1]) #print [44, 33, 22]
slicetoreplacelistnumbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(slicetoreplacelistnumbers) #print [2, 3, 5, 7, 11, 13, 17, 19]
slicetoreplacelistnumbers[::2] = ["Every second number with 100 start index 0", "Every second number with 100 start index 0", "Every second number with 100 start index 0", "Every second number with 100 start index 0"]
print(slicetoreplacelistnumbers) #print ['Every second number with 100 start index 0', 3, 'Every second number with 100 start index 0', 7, 'Every second number with 100 start index 0', 13, 'Every second number with 100 start index 0', 19]
slicetoreplacelistnumbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(slicetoreplacelistnumbers) #print [2, 3, 5, 7, 11, 13, 17, 19]
slicetoreplacelistnumbers[::3] = ["Every third number 555 start index 0", "Every third number 555 start index 0", "Every third number 555 start index 0"]
print(slicetoreplacelistnumbers) #print ['Every third number 555 start index 0', 3, 5, 'Every third number 555 start index 0', 11, 13, 'Every third number 555 start index 0', 19]
searchlistelement = ["dog", "cat", "bird", "butterfly", "squarrel", "lady bug", "fish", "cat", "squarrel", "parrot", "snake"]
print(searchlistelement.index("bird")) #print 2.  Print index number return index.
print(searchlistelement.index("cat", 3)) #print 7.  Start search for cat at index number 3.
print(searchlistelement.index("squarrel", 0, 5)) #print 4.  Start search for squarrel at index number 0 and end at index 4.
alphabeticalanimals = ["zebra", "aardvark", "cat", "dog", "fish", "duck", "aligator"]
print(min(alphabeticalanimals)) #print aardvark
print(max(alphabeticalanimals)) #print zebra
if alphabeticalanimals in ("cat", "dog"):
    print("If statement True included items in tuple.")
else:
    print("What's going on here?") #print What's going on here?
if alphabeticalanimals in ["cat", "dog"]:
    print("If statement True included items in list.")
else:
    print("What's going on here?") #print What's going on here?
if ["cat", "dog"] in alphabeticalanimals:
    print("If statement True included items in list.")
else:
    print("What's going on here?") #print What's going on here?
if ("cat", "dog") in alphabeticalanimals:
    print("If statement True included items in tuple.")
else:
    print("What's going on here?") #print What's going on here?
if "cat" in alphabeticalanimals:
    print("If statement True included the animal.") #print If statement True included the animal.
else:
    print("What's going on here?")
for eachalphabeticalanimals in alphabeticalanimals:
    if eachalphabeticalanimals in ("cat", "dog"):
        print("These animals are in the list [] or tuple().")
    else:
        print("Items in list not in the if statement.")
'''
Items in list not in the if statement.
Items in list not in the if statement.
These animals are in the list.
These animals are in the list.
Items in list not in the if statement.
Items in list not in the if statement.
Items in list not in the if statement.
'''
singlea = [1, 2, 3, 4, 5]
doubleb = [10, 11, 12, 13, 14]
for eachsinglea in singlea:
    print(eachsinglea)
    '''
    1
    2
    3
    4
    5
    '''
for eachsinglea in zip(singlea):
    print(eachsinglea)
    '''
    (1,)
    (2,)
    (3,)
    (4,)
    (5,)
    '''
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachsinglea) #print 1\n 2\n 3\n 4\n 5
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachdoubleb) #print 10\n 11\n 12\n 13\n 14
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    print(eachsinglea, eachdoubleb) #print 1 10\n 2 11\n 3 12\n 4 13\n 5 14
numbers = zip(singlea, doubleb)
numbervariable = 1
for a, b in numbers:
    print("line", numbervariable, end=": ")
    print(a, end="/")
    print(b, end="; ")
    print(a, b)
    numbervariable += 1
    '''
    line 1: 1/10; 1 10
    line 2: 2/11; 2 11
    line 3: 3/12; 3 12
    line 4: 4/13; 4 13
    line 5: 5/14; 5 14
    '''
singleadoubleb = []
for eachsinglea, eachdoubleb in zip(singlea, doubleb):
    singleadoubleb.append(eachsinglea + eachdoubleb)
print(singleadoubleb) #print [11, 13, 15, 17, 19]
print(appendlistinsidelist) #print [['sublist append', 'inside main list'], ['A second append sublist', 'the second sublist inside main list']]
for eachappendlistinsidelist in appendlistinsidelist:
    print(eachappendlistinsidelist[0], eachappendlistinsidelist[1])
    '''
    sublist append inside main list
    A second append sublist the second sublist inside main list
    '''
ordinalnumbers = list(range(1, 10))
for eachordinalnumbers in ordinalnumbers:
    if eachordinalnumbers == 1: #in (1) error message
        print(str(eachordinalnumbers) + "st")
    elif eachordinalnumbers in (2, 3):
        print(str(eachordinalnumbers) + "nd")
    else:
        print(str(eachordinalnumbers) + "th")
        '''
        1st
        2nd
        3nd
        4th
        5th
        6th
        7th
        8th
        9th
        '''
randomnumbers = [5, 8, 9, 1]
if randomnumbers in (5, 9):
    print("There are fives and nines")
else:
    print("What's going on here.") #print What's going on here.
for eachrandomnumbers in randomnumbers:
    if eachrandomnumbers in (5, 9):
        print("There are fives and nines")
    else:
        print("What's going on here.")
        '''
        There are fives and nines
        What's going on here.
        There are fives and nines
        What's going on here.
        '''
unconfirmedusers = ["Alice", "Brian", "Candace"]
confirmedusers = []
while unconfirmedusers:
    moveunconfirmeduserstoconfirmed = unconfirmedusers.pop()  #.pop() removes the last items in the list
    confirmedusers.append(moveunconfirmeduserstoconfirmed)
print("Confirmedusers list populated", confirmedusers) #print Confirmedusers list populated ['Candace', 'Brian', 'Alice']
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
while "cat" in pets:
    pets.remove("cat")
print("Cat is removed", pets) #print Cat is removed ['dog', 'dog', 'goldfish', 'rabbit']
numbers = list(range(0, 10))
squares = []
for onenumber in numbers:
    squares.append(onenumber * onenumber)
print(squares) #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squareslistcomprehension = [onenumber * onenumber for onenumber in numbers] #list comprehension
print(squareslistcomprehension) #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
listsquared = [n**2 for n in range(0, 10)]
print(listsquared) #print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Tuples
print(tuple("Tuples are immutable")) #print ('T', 'u', 'p', 'l', 'e', 's', ' ', 'a', 'r', 'e', ' ', 'i', 'm', 'm', 'u', 't', 'a', 'b', 'l', 'e')
print(tuple((1, 2, 3))) #print (1, 2, 3)
print(tuple((1, 2, 3)) * 3) #print (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(tuple(["A", "tuple", "can't", "change", "what", "is", "stored"])) #print ('A', 'tuple', "can't", 'change', 'what', 'is', 'stored')
print(tuple(list("Tuples are for menu items which don't change."))) #print ('T', 'u', 'p', 'l', 'e', 's', ' ', 'a', 'r', 'e', ' ', 'f', 'o', 'r', ' ', 'm', 'e', 'n', 'u', ' ', 'i', 't', 'e', 'm', 's', ' ', 'w', 'h', 'i', 'c', 'h', ' ', 'd', 'o', 'n', "'", 't', ' ', 'c', 'h', 'a', 'n', 'g', 'e', '.')
slicetuple = ("a", "b", "c", "d", "e", "f", "g", "h")
print(slicetuple.index("e")) #print 4.  Return index position.
print(slicetuple[2]) #print C
print(slicetuple[-1]) #print h
print(slicetuple[1:5]) #print ('b', 'c', 'd', 'e')
print(slicetuple[1:7:2]) #print ('b', 'd', 'f')
numbersintuple = (1, 54565, -22)
listoftuples = [slicetuple, numbersintuple]
print(listoftuples) #print [('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'), (1, 54565, -22)]
tupleoftuples = (slicetuple, numbersintuple)
print(tupleoftuples) #print (('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'), (1, 54565, -22))
combinetuplesnumbers = tuple([x for x in range(1, 8)])
print(combinetuplesnumbers) #print (1, 2, 3, 4, 5, 6, 7)
combinetupleswords = ("run", "shoe", "tree", "door", "hive", "six", "heaven")
print(combinetupleswords) #print ('run', 'shoe', 'tree', 'door', 'hive', 'six', 'heaven')
from itertools import product
combinealltuples = product(combinetuplesnumbers, combinetupleswords)
print(combinealltuples) #print <itertools.product object at 0x7faf0671ea40>
print(tuple(combinealltuples)) #print ((1, 'run'), (1, 'shoe'), (1, 'tree'), (1, 'door'), (1, 'hive'), (1, 'six'), (1, 'heaven'), (2, 'run'), (2, 'shoe'), (2, 'tree'), (2, 'door'), (2, 'hive'), (2, 'six'), (2, 'heaven'), (3, 'run'), (3, 'shoe'), (3, 'tree'), (3, 'door'), (3, 'hive'), (3, 'six'), (3, 'heaven'), (4, 'run'), (4, 'shoe'), (4, 'tree'), (4, 'door'), (4, 'hive'), (4, 'six'), (4, 'heaven'), (5, 'run'), (5, 'shoe'), (5, 'tree'), (5, 'door'), (5, 'hive'), (5, 'six'), (5, 'heaven'), (6, 'run'), (6, 'shoe'), (6, 'tree'), (6, 'door'), (6, 'hive'), (6, 'six'), (6, 'heaven'), (7, 'run'), (7, 'shoe'), (7, 'tree'), (7, 'door'), (7, 'hive'), (7, 'six'), (7, 'heaven'))
print(list(combinealltuples)) #print []
listcombinealltuples = list(product(combinetuplesnumbers, combinetupleswords))
print(listcombinealltuples) #print [(1, 'run'), (1, 'shoe'), (1, 'tree'), (1, 'door'), (1, 'hive'), (1, 'six'), (1, 'heaven'), (2, 'run'), (2, 'shoe'), (2, 'tree'), (2, 'door'), (2, 'hive'), (2, 'six'), (2, 'heaven'), (3, 'run'), (3, 'shoe'), (3, 'tree'), (3, 'door'), (3, 'hive'), (3, 'six'), (3, 'heaven'), (4, 'run'), (4, 'shoe'), (4, 'tree'), (4, 'door'), (4, 'hive'), (4, 'six'), (4, 'heaven'), (5, 'run'), (5, 'shoe'), (5, 'tree'), (5, 'door'), (5, 'hive'), (5, 'six'), (5, 'heaven'), (6, 'run'), (6, 'shoe'), (6, 'tree'), (6, 'door'), (6, 'hive'), (6, 'six'), (6, 'heaven'), (7, 'run'), (7, 'shoe'), (7, 'tree'), (7, 'door'), (7, 'hive'), (7, 'six'), (7, 'heaven')]
listcombinealltuples.sort() #Sort a list of tuples or tuples inside a list
print(listcombinealltuples) #print [(1, 'door'), (1, 'heaven'), (1, 'hive'), (1, 'run'), (1, 'shoe'), (1, 'six'), (1, 'tree'), (2, 'door'), (2, 'heaven'), (2, 'hive'), (2, 'run'), (2, 'shoe'), (2, 'six'), (2, 'tree'), (3, 'door'), (3, 'heaven'), (3, 'hive'), (3, 'run'), (3, 'shoe'), (3, 'six'), (3, 'tree'), (4, 'door'), (4, 'heaven'), (4, 'hive'), (4, 'run'), (4, 'shoe'), (4, 'six'), (4, 'tree'), (5, 'door'), (5, 'heaven'), (5, 'hive'), (5, 'run'), (5, 'shoe'), (5, 'six'), (5, 'tree'), (6, 'door'), (6, 'heaven'), (6, 'hive'), (6, 'run'), (6, 'shoe'), (6, 'six'), (6, 'tree'), (7, 'door'), (7, 'heaven'), (7, 'hive'), (7, 'run'), (7, 'shoe'), (7, 'six'), (7, 'tree')]
numberletter = [("c", 3), ("a", 1), ("b", 2), ("a", 2), ("c", 2)]
print(numberletter) #print [('c', 3), ('a', 1), ('b', 2), ('a', 2), ('c', 2)]
numberletter.sort()
print(numberletter) #print [('a', 1), ('a', 2), ('b', 2), ('c', 2), ('c', 3)]

#Dictionaries
blankdictionary = {}
blankdictionary["Insert key in brackets"] = "Insert item right of equal sign"
blankdictionary["Insert key left of colon"] = "Insert value to blankdictionary dictionary"
blankdictionary["Number key"] = 721
blankdictionary["Use len function"] = "to return the number of entries"
print(blankdictionary) #print {'Insert key in brackets': 'Insert item right of equal sign', 'Insert key left of colon': 'Insert value to blankdictionary dictionary', 'Number key': 721, 'Use len function': 'to return the number of entries'}
print(blankdictionary["Number key"]) #print 721
print(len(blankdictionary)) #print 4
for keysonly in blankdictionary.keys(): #RM:  Looping a dictionary default is key; for example for defaultgetkey in blankdictionary the for loop returns the keys.
    print(keysonly, end=", ") #print Insert key in brackets, Insert key left of colon, Number key, Use len function,
for sortedkeys in sorted(blankdictionary.keys()):
    print(sortedkeys, end=", ") #print Insert key in brackets, Insert key left of colon, Number key, Use len function,
for valuesonly in blankdictionary.values():
    print(valuesonly, end=", ") #print Insert item right of equal sign, Insert value to blankdictionary dictionary, 721, to return the number of entries,
for key, value in blankdictionary.items():
    print(key + ": " + str(value))
    '''
    Insert key in brackets: Insert item right of equal sign
    Insert key left of colon: Insert value to blankdictionary dictionary
    Number key: 721
    Use len function: to return the number of entries
    '''
for key in blankdictionary:
    print(key + ": " + str(blankdictionary[key]))
    '''
    Insert key in brackets: Insert item right of equal sign
    Insert key left of colon: Insert value to blankdictionary dictionary
    Number key: 721
    Use len function: to return the number of entries
    '''
blankdictionary.update({"Number key": "Change value update dictionary value to a string here."})  #The updates from the update dictionary or second dictionary overrides matching key-value pairs in the first dictionary.  Same values are not duplicated.
print(blankdictionary["Number key"]) #print Change value update dictionary value to a string here.
blankdictionary["Use len function"] = "Change dictionary value works, too"
print(blankdictionary) #print {'Insert key in brackets': 'Insert item right of equal sign', 'Insert key left of colon': 'Insert value to blankdictionary dictionary', 'Number key': 'Change value update dictionary value to a string here.', 'Use len function': 'Change dictionary value works, too'}
blankdictionary.update({"Use update method to": "insert a new item"})
print(blankdictionary) #print {'Insert key in brackets': 'Insert item right of equal sign', 'Insert key left of colon': 'Insert value to blankdictionary dictionary', 'Number key': 'Change value update dictionary value to a string here.', 'Use len function': 'Change dictionary value works, too', 'Use update method to': 'insert a new item'}
del blankdictionary["Number key"] #delete entry delete dictionary
print(blankdictionary) #print {'Insert key in brackets': 'Insert item right of equal sign', 'Insert key left of colon': 'Insert value to blankdictionary dictionary', 'Use len function': 'to return the number of entries'}
basicfunctionsforadictionary = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 306.21, "AAPL": 99.76}
print(basicfunctionsforadictionary) #print {'GOOG': 520.54, 'FB': 76.45, 'YHOO': 39.28, 'AMZN': 306.21, 'AAPL': 99.76}
print(min(basicfunctionsforadictionary)) #print AAPL
print(max(basicfunctionsforadictionary)) #print YHOO
print(zip(basicfunctionsforadictionary.keys(), basicfunctionsforadictionary.values())) #print <zip object at 0x7fac3c8975c0>
print(min(zip(basicfunctionsforadictionary.keys(), basicfunctionsforadictionary.values()))) #print ('AAPL', 99.76)
print(max(zip(basicfunctionsforadictionary.keys(), basicfunctionsforadictionary.values()))) #print ('YHOO', 39.28)
print(max(zip(basicfunctionsforadictionary.values(), basicfunctionsforadictionary.keys()))) #print (520.54, 'GOOG')
print(list(zip(basicfunctionsforadictionary.keys(), basicfunctionsforadictionary.values()))) #print [('GOOG', 520.54), ('FB', 76.45), ('YHOO', 39.28), ('AMZN', 306.21), ('AAPL', 99.76)]
print(sorted(zip(basicfunctionsforadictionary.keys(), basicfunctionsforadictionary.values()))) #print [('AAPL', 99.76), ('AMZN', 306.21), ('FB', 76.45), ('GOOG', 520.54), ('YHOO', 39.28)]
dictionarycomprehension = {stocksymbolkey: stockpricevalue for stocksymbolkey, stockpricevalue in basicfunctionsforadictionary.items()} #dictionary comprehension
print(dictionarycomprehension) #print {'GOOG': 520.54, 'FB': 76.45, 'YHOO': 39.28, 'AMZN': 306.21, 'AAPL': 99.76}
print("get() method get value for FB stock price " + str(basicfunctionsforadictionary.get("FB", "default value if there's no FB ticker symbol")) + ".") #print get() method get value for FB stock price 76.45.
print("get() method get value for APPL stock price " + str(basicfunctionsforadictionary.get("APPL", "default value if there's no APPL ticker symbol")) + ".") #print get() method get value for APPL stock price default value if there's no APPL ticker symbol.
copydictionary = basicfunctionsforadictionary.copy() #copy dictionary
print(copydictionary) #print {'GOOG': 520.54, 'FB': 76.45, 'YHOO': 39.28, 'AMZN': 306.21, 'AAPL': 99.76}
basicfunctionsforadictionary.clear()
print(basicfunctionsforadictionary) #print {}
valueislist = {"listvalues": ["a", "list", "is", "a", "value"], "dictionarydefinition": "Use a list as a definition", "luck": "good"}
print(valueislist) #print {'listvalues': ['a', 'list', 'is', 'a', 'value'], 'dictionarydefinition': 'Use a list as a definition', 'luck': 'good'}
print(valueislist.items()) #print dict_items([('listvalues', ['a', 'list', 'is', 'a', 'value']), ('dictionarydefinition', 'Use a list as a definition'), ('luck', 'good')])
print(valueislist.keys()) #print dict_keys(['listvalues', 'dictionarydefinition', 'luck'])
print(valueislist.values()) #print dict_values([['a', 'list', 'is', 'a', 'value'], 'Use a list as a definition', 'good'])
print(list(valueislist.values())) #print [['a', 'list', 'is', 'a', 'value'], 'Use a list as a definition', 'good']
print(list(valueislist.values())[1]) #print Use a list as a definition
valueislistprintlistvalues = list(valueislist.values())
print(valueislistprintlistvalues) #print [['a', 'list', 'is', 'a', 'value'], 'Use a list as a definition', 'good']
valueislistprintkeyvalues = list(valueislist.keys())
print(valueislistprintkeyvalues) #print ['listvalues', 'dictionarydefinition', 'luck']
print("list" in valueislist.values()) #print False
print(["a", "list", "is", "a", "value"] in valueislist.values()) #print True
print("good" in valueislist.values()) #print True
print("listvalues" in valueislist.keys()) #print True
print("luck" in valueislist) #print True
print(valueislist["listvalues"]) #print ['a', 'list', 'is', 'a', 'value']
print(valueislist["listvalues"][1]) #print list
valueislist["insertnewlist"] = ["insert", "new value", "in dictionary", "as a list"]
print(valueislist) #print {'listvalues': ['a', 'list', 'is', 'a', 'value'], 'dictionarydefinition': 'Use a list as a definition', 'luck': 'good', 'insertnewlist': ['insert', 'new value', 'in dictionary', 'as a list']}
valueislist["listvalues"].sort() #sort valueislist dictionary listvalues key values
print(valueislist) #print {'listvalues': ['a', 'a', 'is', 'list', 'value'], 'dictionarydefinition': 'Use a list as a definition', 'luck': 'good', 'insertnewlist': ['insert', 'new value', 'in dictionary', 'as a list']}
valueislist["listvalues"].remove("is") #remove valueislist dictionary listvalues key value is
print(valueislist) #print {'listvalues': ['a', 'a', 'list', 'value'], 'dictionarydefinition': 'Use a list as a definition', 'luck': 'good', 'insertnewlist': ['insert', 'new value', 'in dictionary', 'as a list']}
for loopvalueislist in valueislist["insertnewlist"]:
    print(loopvalueislist)
    '''
    insert
    new value
    in dictionary
    as a list
    '''
for eachvalueislist in valueislist.values():
    print(eachvalueislist)
    '''
    ['a', 'a', 'list', 'value']
    Use a list as a definition
    good
    ['insert', 'new value', 'in dictionary', 'as a list']
    '''
missingvalue = {"name": "Pooka", "age": 5}
print(missingvalue) #print {'name': 'Pooka', 'age': 5}
missingvalue.setdefault("color", "add key and default value if key and value doesn't exist")
print(missingvalue) #print {'name': 'Pooka', 'age': 5, 'color': "add key and default value if key and value doesn't exist"}
missingvalue.setdefault("color", "I want to change the default value.  I actually can't change because color key is already in missingvalue dictionary")
print(missingvalue) #print {'name': 'Pooka', 'age': 5, 'color': "add key and default value if key and value doesn't exist"}
missingvalue["color"] = "Change default white color"
print(missingvalue) #print {'name': 'Pooka', 'age': 5, 'color': 'Change default white color'}
#Individual dictionaries, variable dictionaries, assign dictionaries
lloyd = {"name": "Lloyd", "homework": [0.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0]}
alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]}
tyler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]}
print(lloyd) #print {'name': 'Lloyd', 'homework': [0.0, 97.0, 75.0, 92.0], 'quizzes': [88.0, 40.0, 94.0], 'tests': [75.0, 90.0]}
combinedictionaries = [lloyd, alice, tyler]
print(combinedictionaries) #print [{'name': 'Lloyd', 'homework': [0.0, 97.0, 75.0, 92.0], 'quizzes': [88.0, 40.0, 94.0], 'tests': [75.0, 90.0]}, {'name': 'Alice', 'homework': [100.0, 92.0, 98.0, 100.0], 'quizzes': [82.0, 83.0, 91.0], 'tests': [89.0, 97.0]}, {'name': 'Tyler', 'homework': [0.0, 87.0, 75.0, 22.0], 'quizzes': [0.0, 75.0, 78.0], 'tests': [100.0, 100.0]}]
print(combinedictionaries[1]) #print {'name': 'Alice', 'homework': [100.0, 92.0, 98.0, 100.0], 'quizzes': [82.0, 83.0, 91.0], 'tests': [89.0, 97.0]}
print(combinedictionaries[1]["name"]) #print Alice
print(combinedictionaries[1]["quizzes"]) #print [82.0, 83.0, 91.0]
print(combinedictionaries[1]["quizzes"][2]) #print 91
#Nested dictionary.  Notice the information value in for loop reference it's nested dictionary keys such as information["country"]
nesteddictionarycities = {"springdale": {"country": "usa", "population": 3000, "fact": "zion national park", }, "anaheim": {"country": "usa", "population": 50000, "fact": "disneyland"}, "london": {"country": "great britian", "population": 500000, "fact": "london bridge"}}
for city, information in nesteddictionarycities.items():
    print("City: " + city)
    print("Country: " + information["country"] + " population: ", information["population"])
    print("fact: " + information["fact"])
'''
City: springdale
Country: usa population:  3000
fact: zion national park
City: anaheim
Country: usa population:  50000
fact: disneyland
City: london
Country: great britian population:  500000
fact: london bridge
'''
from operator import itemgetter
dictionaryinsidealist = [{"fname": "Bucky", "lname": "Roberts"}, {"fname": "Tom", "lname": "Roberts"}, {"fname": "Bernie", "lname": "Zunks"}, {"fname": "Jenna", "lname": "Hayes"}, {"fname": "Sally", "lname": "Jones"}, {"fname": "Amanda", "lname": "Roberts"}, {"fname": "Tom", "lname": "Williams"}, {"fname": "Dean", "lname": "Hayes"}, {"fname": "Bernie", "lname": "Barbie"}, {"fname": "Tom", "lname": "Jones"}]
print(dictionaryinsidealist) #print [{'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Tom', 'lname': 'Jones'}]
sortfname = sorted(dictionaryinsidealist, key=itemgetter("fname"))
print(sortfname) #print [{'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}, {'fname': 'Tom', 'lname': 'Jones'}]
sortfnamelname = sorted(dictionaryinsidealist, key=itemgetter("fname", "lname"))
print(sortfnamelname) #print [{'fname': 'Amanda', 'lname': 'Roberts'}, {'fname': 'Bernie', 'lname': 'Barbie'}, {'fname': 'Bernie', 'lname': 'Zunks'}, {'fname': 'Bucky', 'lname': 'Roberts'}, {'fname': 'Dean', 'lname': 'Hayes'}, {'fname': 'Jenna', 'lname': 'Hayes'}, {'fname': 'Sally', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Jones'}, {'fname': 'Tom', 'lname': 'Roberts'}, {'fname': 'Tom', 'lname': 'Williams'}]
#Order lists order dictionary keeps track of order.  Ordered lists.  Ordered dictionary.
from collections import OrderedDict
nameandcolor = OrderedDict()
nameandcolor["Jen"] = "Red"
nameandcolor["Ben"] = "Brown"
nameandcolor["Ren"] = "Blue"
nameandcolor["Ten"] = "White"
print(nameandcolor) #print OrderedDict([('Jen', 'Red'), ('Ben', 'Brown'), ('Ren', 'Blue'), ('Ten', 'White')])
for key, value in nameandcolor.items():
    print(key + "'s name as key favorite color is as value " + value + ".")
    '''
    Jen's name as key favorite color is as value Red.
    Ben's name as key favorite color is as value Brown.
    Ren's name as key favorite color is as value Blue.
    Ten's name as key favorite color is as value White.
    '''

#Sets
setvariable = set([10, 20, 30, 10, 20, 30, 40, "abc", "abcabcabc", "printed sets items printed in random order"])
print(setvariable) #print {'abc', 40, 10, 'printed sets items printed in random order', 20, 'abcabcabc', 30}
usesetsremoveduplicates = [1, 1, 1, 2, 3, 4, 4, 4, 5]
print(usesetsremoveduplicates) #print [1, 1, 1, 2, 3, 4, 4, 4, 5]
print(set(usesetsremoveduplicates)) #print {1, 2, 3, 4, 5}
print(list(set(usesetsremoveduplicates))) #print {1, 2, 3, 4, 5}.  Convert set to list.
blankset = set()
print(blankset) #print set()
blankset.add("insert item to set")
blankset.add("insert item to set")
blankset.add("number")
blankset.add(5)
blankset.add("there is a duplicate")
blankset.add("there is a duplicate")
blankset.add("there is a duplicate")
blankset.add("set items returned in random order")
print(blankset) #print {'insert item to set', 5, 'number', 'there is a duplicate', 'set items returned in random order'}
print("\n")
blankset.update(["New Updates", "a list of updates", "added to blankset", "set", "set", "set is a duplicate"])
print(blankset) #print {'a list of updates', 'New Updates', 'set is a duplicate', 5, 'insert item to set', 'set items returned in random order', 'set', 'added to blankset', 'there is a duplicate', 'number'}
blankset.remove("set items returned in random order")
print(blankset) #print {5, 'a list of updates', 'insert item to set', 'set', 'there is a duplicate', 'added to blankset', 'number', 'set is a duplicate', 'New Updates'}
setone = {1, 2, 3, 4, 1000}
settwo = {3, 4, 5, 6, 2222}
uniontwosets = setone | settwo #Combine two sets all items printed once no duplicates.  TThe union of two sets is a set consisting of all unique elements for both sets.  The binary set operators must be be sets.
print(uniontwosets) #print {1, 2, 3, 4, 5, 6, 1000, 2222}
#or
print(setone.union(settwo)) #print {1, 2, 3, 4, 5, 6, 1000, 2222}
intersecttwosets = setone & settwo #Combine two sets all duplicate items.  The intersection of two sets is a set consisting of all the unqiue elements the two sets have in common.
print(intersecttwosets) #print {3, 4}
#or
print(setone.intersection(settwo)) #print {3, 4}
differencetwosets = setone - settwo
print(differencetwosets) #print {1000, 1, 2}.  The difference between two sets is a set consisting of the elements in the left which are not in the right.
#or
print(setone.difference(settwo)) #print {1000, 1, 2}
symmetricdifferencetwosets = setone ^ settwo #Combine two sets no duplicates
print(symmetricdifferencetwosets) #print {1, 2, 5, 6, 1000, 2222}.  The symmetric difference between two sets is a set consisting of the elments of both sets not in common which each other.
#or
print(setone.symmetric_difference(settwo)) #print {1, 2, 5, 6, 1000, 2222}
print(setone.isdisjoint(settwo)) #print False.  The disjoint returns True if both sets don't have any common elements.  Returns False if both sets do have any common elements.
subsetcheck = {5, 6}
print(subsetcheck) #print {5, 6}
print(subsetcheck < settwo) #print True.  subsetcheck is a subset of settwo
print(subsetcheck > settwo) #print False.  settwo is not a subset of subsetcheck
print(1000 in setone) #print True
print({1, 3, 5} == {3, 5, 1}) #print True
print({1, 3, 5} != {3, 5, 1}) #print False
print({1, 3, 5} < {3, 5, 1}) #print False.  #The less than < operator tests all the elements in the left are in the right.  A proper subset.
print({1, 3, 5} < {7, 3, 5, 1}) #print True
print({1, 3, 5} < {1, 3, 5, 7}) #print True
print({1, 3, 5} <= {3, 5, 1}) #print True.  #The less than or equal to <= operator tests all the elements in the left are in the right and the sets might be equal.  An improper subset.
print({1, 3} <= {3, 5, 1}) #print True.
print({1, 3, 5}.issubset({3, 5, 1})) #print True.  #Use method issubset().  The less than or equal to <= operator tests all the elements in the left are in the right and the sets might be equal.  An improper subset.
print({1, 3}.issubset({3, 5, 1})) #print True.
print({1, 3, 5} > {3, 5, 1}) #print False.  #The greater than > operator tests all the elements in the right are in the left and the left has more elements.  A proper superubset.
print({1, 3, 5, 7} > {3, 5, 1}) #print True.  #The greater than > operator tests all the elements in the right are in the left and the left has more elements.  A proper supersubset.
print({1, 3, 5} >= {3, 5, 1}) #print True.  #The greater than or equal to >= operator tests all the elements in the right are in the left and the sets might be equal.  An improper superset.
print({1, 3, 5, 7} >= {3, 1}) #print True
print({1, 3} >= {3, 1, 7}) #print False
print({1, 3, 5}.issuperset({3, 5, 1})) #print True.  #Use method isupserset().  The greater than or equal to >= operator tests all the elements in the right are in the left and the sets might be equal.  An improper superset.
print({1, 3, 5, 7}.issuperset({3, 2})) #print False
numbersset = {0, 1, 2, 4, 5, 6, 7, 8, 9, 17}
setcomprehension = {eachnumbersset for eachnumbersset in numbersset if eachnumbersset % 2 == 0}
print(setcomprehension) #print {0, 2, 4, 6, 8}
