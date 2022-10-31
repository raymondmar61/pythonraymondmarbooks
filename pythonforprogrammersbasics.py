#Python For Programmers by Paul Deitel Chapter 03 Control Statements
grade = 77
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C") #print C
elif grade >= 60:
    print("D")
else:
    print("F")
product = 3
while product <= 50:
    print(product)
    '''
    3
    9
    27
    '''
    product = product * 3
print(product) #print 81
for eachcharacter in "Programming":
    print(eachcharacter, end="") #print Programming
print("\b")
print("Use a line break after a print(, end=\"\")")
print(10, 20, 30) #print 10 20 30
print(10, 20, 30, sep=", ") #print 10, 20, 30
formattedstringvariable = 81.7
print(f"Class average is {formattedstringvariable}.") #print Class average is 81.7.
print(f"Class average is {formattedstringvariable:.2f}.") #print Class average is 81.70.
fieldwidth10with2totheright = 1050
print(f"Compound interest {fieldwidth10with2totheright:10.2f}") #print Compound interest    1050.00.  RM:  exclude the space from the total count 10
print(f"Compound interest right align {fieldwidth10with2totheright:>10.2f}") #print Compound interest right align ***1050.00
print(f"Compound interest left align {fieldwidth10with2totheright:<10.2f}") #print Compound interest left align 1050.00***
from statistics import mean, median, mode
grades = [85, 93, 45, 89, 85]
print(mean(grades)) #print 79.4
print(median(grades)) #print 85
print(mode(grades)) #print 85
