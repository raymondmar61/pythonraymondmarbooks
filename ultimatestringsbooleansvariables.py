#Boolean
print(bool("return true" > "or return false using bool()")) #print True
print(bool("v" > "a")) #print True
print(bool(1 == 1)) #print True
print(any([True, False, 0, 1 < 0])) #print True
print(any([True, False, 0, 1 > 0])) #print True
print(any([False, True])) #print True
print(any([False])) #print False
print(any([])) #print False
print(all([True, False, 0, 1 < 0])) #print False
print(all([True, False, 0, 1 > 0])) #print False
print(all([True, True])) #print True
print(all([True, 34 < 5])) #print False
print(True and True) #print True
print(True and False) #print False
print(False and False) #print False
print(True, True) #print True True
print(True, False) #print True False
print(False, False) #print False False
intnumber = 80
floatnumber = 55.70
checkinteger = isinstance(intnumber, (int, float))
print(checkinteger) #print True
checkfloat = isinstance(floatnumber, (int, float))
print(checkfloat) #print True
print(intnumber is floatnumber) #print False

#Variables
assignvariablenone = None
print(assignvariablenone) #print None
x = "string variable attributes"
print(x) #print string variable attributes
print(globals()["x"]) #print string variable attributes
y = "a second string variable attributes"
print(globals())
'''
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fa125ad5b80>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'yytest.py', '__cached__': None, 'x': 'string variable attributes', 'y': 'a second string variable attributes'}
'''
print(type(globals())) #print <class 'dict'>
print(globals()["__cached__"]) #print None
attributevariable = "upper() is the attribute for attributevariable"
print(attributevariable) #print upper() is the attribute for attributevariable
uppermethod = attributevariable.upper() #Python finds the upper() method and executes upper() thanks to the parentheses
print(uppermethod) #print UPPER() IS THE ATTRIBUTE FOR ATTRIBUTEVARIABLE
variable1, variable2, variable3, variable4 = "four variables", "separated by", "four commas", "in one line"
print(variable1) #print four variables
print(variable2) #print separated by
print(variable3) #print four commas
print(variable4) #print in one line
[variable1, variable2, variable3, variable4] = ["four variables contained in a list", "separated by four", "commas all", "in one list"]
print(variable1) #print four variables contained in a list
print(variable2) #print separated by four
print(variable3) #print commas all
print(variable4) #print in one list
print(type(variable4)) #print <class 'str'>
(variable1, variable2, variable3, variable4) = ("four variables contained in a tuple", "separated", "by four commas all", "in one tuple")
print(variable1) #print four variables contained in a tuple
print(variable2) #print separated
print(variable3) #print by four commas all
print(variable4) #print in one tuple
print(type(variable4)) #print <class 'str'>
variable1, variable2, variable3, variable4 = ["assign me to four different variables"] * 4
print(variable1) #print assign me to four different variables
print(variable2) #print assign me to four different variables
print(variable3) #print assign me to four different variables
print(variable4) #print assign me to four different variables
print(type(variable4)) #print <class 'str'>
variable1 = variable2 = variable3 = variable4 = "four variables all equal to each other"
print(variable1) #print four variables all equal to each other
print(variable2) #print four variables all equal to each other
print(variable3) #print four variables all equal to each other
print(variable4) #print four variables all equal to each other
print(variable4 is variable1) #print True
variable1 = variable2 = variable3 = variable4 = ["list", "contains", "three entries"]
print(variable1) #print ["list", "contains", "three entries"]
print(variable2) #print ["list", "contains", "three entries"]
print(variable3) #print ["list", "contains", "three entries"]
print(variable4) #print ["list", "contains", "three entries"]
print(variable4 is variable1) #print True
dictionaryvaluea, dictionaryvalueb, dictionaryvaluec = ({"a key": "a value"}, {"b key": "b value"}, {"c key": "c value"})
print(dictionaryvaluea) #print {'a key': 'a value'}
print(dictionaryvalueb) #print {'b key': 'b value'}
print(dictionaryvaluec) #print {'c key': 'c value'}
#A stackoverflow says don't do the following any other object
dontdothis = {}
dontdothistoo = {}
dontdothis = dontdothistoo = {} #same dictionary object assigned to dontdothis, dontdothistoo.  Should not do this.
lista = listb = []
lista.append("append me to the lista and listb")
print(lista) #print ['append me to the lista and listb']
print(listb) #print ['append me to the lista and listb']
lista = listb = ["first entry already inside"]
lista.append("append me to the lista and listb")
print(lista) #print ['first entry already inside', 'append me to the lista and listb']
print(listb) #print ['first entry already inside', 'append me to the lista and listb']
leftlist, middlelist, rightlist = [[], [], []] #leftlist, middlelist, rightlist = [[] for _ in range(0, 3)] using lists or tuples also works
print(leftlist) #print []
print(middlelist) #print []
print(rightlist) #print []
leftlist.append("add text to the blank left list")
print(leftlist) #print ['add text to the blank left list']
print(middlelist) #print []
print(rightlist) #print []
rightlist.append("add text to the blank right list")
print(middlelist) #print []
print(rightlist) #print ['add text to the blank right list']
