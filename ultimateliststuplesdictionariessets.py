#Lists
listitemscontainedinbrackets = ["Multiple data types", 55, True, "contained in list", -1, 3.50]
print(listitemscontainedinbrackets) #print ['Multiple data types', 55, True, 'contained in list', -1, 3.5]
listvariable1, listvariable2, listvariable3 = ["multiple variables", "one list", "separate list entry"]
print(listvariable2) #print one list
nest1 = ["a list of lists"]
nest2 = ["nested lists sublists"]
nestedlists = [nest1, nest2]
print(nestedlists) #print [['a list of lists'], ['nested lists sublists']]
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


sortcaseinsensitive.sort(key=functionsortlastletteroftheword)
print(sortcaseinsensitive) #print ['a', 'a', 'Period', 'of', 'string', 'bunch', 'With', 'in', 'Python', 'No', 'words', 'is', 'This']
joinitemsinlist = ["convert", "list", "to", "string"] #list to string
print(joinitemsinlist) #print ['convert', 'list', 'to', 'string']
print(" ".join(joinitemsinlist)) #print convert list to string
print("-".join(joinitemsinlist)) #print convert-list-to-string
threepipes = ["|||"]
fourthreepipes = threepipes * 4
print(fourthreepipes) #print ['|||', '|||', '|||', '|||']
joinfourthreepipes = "".join(fourthreepipes)
print(joinfourthreepipes) #print ||||||||||||
#enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
firstname = ["Bucky", "Tom", "Taylor"]
lastname = ["Roberts", "Hanks", "Swift"]
print(enumerate(firstname)) #print <enumerate object at 0x7f01d25b5708>
print(list(enumerate(firstname))) #print [(0, 'Bucky'), (1, 'Tom'), (2, 'Taylor')]
print(list(enumerate(lastname))) #print [(0, 'Roberts'), (1, 'Hanks'), (2, 'Swift')]
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
insertitemsinlist.pop(5) #delete specific index position
print(insertitemsinlist) #print [29, 58, 66, 'Insert at index number 3', 71, 87, 90, 91, 98, 120, 6594, 3799, 98453, 87990, -1, -10, -54]
insertitemsinlist.remove("Insert at index number 3") #delete specific item
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98, 120, 6594, 3799, 98453, 87990, -1, -10, -54]
savedeletedlistitemvariable = insertitemsinlist.pop(2)
print(insertitemsinlist) #print [29, 58, 71, 87, 90, 91, 98, 120, 6594, 3799, 98453, 87990, -1, -10, -54]
print(savedeletedlistitemvariable) #print 66
savedeletedlistitemvariable = insertitemsinlist.remove(6594)
print(insertitemsinlist) #print [29, 58, 71, 87, 90, 91, 98, 120, 3799, 98453, 87990, -1, -10, -54]
print(savedeletedlistitemvariable) #print None
del insertitemsinlist[6]
print(insertitemsinlist) #print [29, 58, 71, 87, 90, 91, 120, 3799, 98453, 87990, -1, -10, -54]
insertitemsinlist.sort(key=abs) #sort by absolute value ignore negatives; all numbers are positive
print(insertitemsinlist) #print [-1, -10, 29, -54, 58, 71, 87, 90, 91, 120, 3799, 87990, 98453]
grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(grades) #print [32, 43, 654, 34, 132, 66, 99, 532]
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
listindexnumber = extractfromlistslice.index(55)
print(listindexnumber) #print 4
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
