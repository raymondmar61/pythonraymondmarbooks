#Learn Python - Full Course for Beginners [Tutorial] [rfscVS0vtbw] https://www.youtube.com/watch?v=rfscVS0vtbw
print("Hello World") #print Hello World
stringvariable = "a container which stores data values"
print("The explanation of a variable is " + stringvariable + ".") #print The explanation of a variable is A container which stores data values.
numericalvariable = 99
print("Use a comma for a number or numerical variable", numericalvariable, ".") #print Use a comma for a number or numerical variable 99 .
booleanvariable = True
print("Also use a comma for True or False booleans", booleanvariable) #print Use True or False for booleans True
print("An escape character is a backslash \". I want the one double quote.") #print An escape character is a backslash ". I want the one double quote.
phrase = "Giraffe Academy"
print(phrase) #print Giraffe Academy
print(phrase.lower()) #print giraffe academy
print(phrase.upper()) #print GIRAFFE ACADEMY
print(phrase.isupper()) #print False
print(phrase.upper().isupper()) #print True
print(len(phrase)) #print 15
print(phrase[0]) #print G
print(phrase[3]) #print a
print(phrase.index("G")) #print 0 #Find index position of a string
print(phrase.index("a")) #print 3
print(phrase.index("Acad")) #print 8
print(phrase.replace("Giraffe", "Elephant")) #print Elephant Academy
print(2.0987)
print(10 % 3) #print 1.  Modulo operator returns the remainder
number = -5
print(abs(number)) #print 5
print(pow(3, 2)) #print 9
print(max(4, 6, number)) #print 6
print(min(4, 6, number)) #print -5
print(round(3.2)) #print 3
print(round(3.7)) #print 4
import math #RM:  Save time import the math module with the asterisk from math import *.  I choose import math to emphasize the math module for these methods.
print(math.floor(3.2)) #print 3
print(math.ceil(3.2)) #print 4
print(math.floor(3.7)) #print 3
print(math.ceil(3.7)) #print 4
print(math.sqrt(36)) #print 6
# userinputname = input("Input prompt Enter your name: ")
# userinputage = int(input("Input prompt Enter your age: "))
# print("Hello " + userinputname + "!  You're", userinputage) #print Hello userinputname!  You're 25
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
datatypeslist = ["Kevin", 2, True]
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
print(datatypeslist) #print ['Kevin', 2, True]
print(friendslist[2]) #print Jim
print(friendslist[-1]) #print Toby
print(friendslist[1]) #print Karen
print(friendslist[-2]) #print Oscar
print(friendslist[1:]) #print ['Karen', 'Jim', 'Oscar', 'Toby']
print(friendslist[1:3]) #print ['Karen', 'Jim']
friendslist[1] = "Change from Karen to Mike"
print(friendslist) #print ['Kevin', 'Change from Karen to Mike', 'Jim', 'Oscar', 'Toby']
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
luckynumbers = [4, 8, 15, 16, 23, 42]
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
friendslist.extend(luckynumbers) #append lists
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friendslist.append("Creed")
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 'Creed']
friendslist.insert(1, "Add at index one Kelly")
print(friendslist) #print ['Kevin', 'Add at index one Kelly', 'Karen', 'Jim', 'Oscar', 'Toby', 'Creed']
friendslist.remove("Jim")
print(friendslist) #print ['Kevin', 'Add at index one Kelly', 'Karen', 'Oscar', 'Toby', 'Creed']
friendslist.clear()
print(friendslist) #print []
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friendslist.pop() #delete the item on the furthest right of a list or last itme in a list
print(friendslist) #print ['Kevin', 'Karen', 'Jim', 'Oscar']
print(friendslist.index("Kevin")) #print 0
friendslist = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friendslist.count("Jim")) #print 2
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friendslist.sort()
print(friendslist) #print ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']
friendslist.reverse()
print(friendslist) #print ['Toby', 'Oscar', 'Kevin', 'Karen', 'Jim']
friendslist = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
copyfriendslist = friendslist.copy()
print(copyfriendslist) #print ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
