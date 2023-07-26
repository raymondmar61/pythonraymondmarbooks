#Lists
listitemscontainedinbrackets = ["Multiple data types", 55, True, "contained in list", -1, 3.50]
print(listitemscontainedinbrackets) #print ['Multiple data types', 55, True, 'contained in list', -1, 3.5]
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
