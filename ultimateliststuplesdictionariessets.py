#Lists
listitemscontainedinbrackets = ["Multiple data types", 55, True, "contained in list", -1, 3.50]
print(listitemscontainedinbrackets) #print ['Multiple data types', 55, True, 'contained in list', -1, 3.5]
print(list("Convert string to list 491")) #print ['C', 'o', 'n', 'v', 'e', 'r', 't', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 't', 'o', ' ', 'l', 'i', 's', 't', ' ', '4', '9', '1']
convertnumberstostring = list(map(str, [29, 58, -5, 210, 985]))
print(convertnumberstostring) #print ['29', '58', '-5', '210', '985']
insertitemsinlist = [29, 58, 66, 71, 87]
combinelistsplussign = [90, 91, 98]
insertitemsinlist = insertitemsinlist + combinelistsplussign
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98]
insertitemsinlist.append(120) #append item to list
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98, 120]
numberofitemsinlist = len(insertitemsinlist)
print(numberofitemsinlist) #print 9
insertitemsinlist[numberofitemsinlist + 1:] = [-1, -10, -54] #insert multiple items to list
print(insertitemsinlist) #print [29, 58, 66, 71, 87, 90, 91, 98, 120, -1, -10, -54]


extractfromlistslice = [29, 58, 66, 71, 87]
print(extractfromlistslice[2]) #print 66
