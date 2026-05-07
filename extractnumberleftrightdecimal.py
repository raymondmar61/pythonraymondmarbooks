#Extract decimal numbers to the right of decimal point
#Use Modulo and divide by 1 to isolate the numbers right of decimal point.  Extract fraction extract fractional.
decimalnumber = 12.345
numbersrightdecimal = decimalnumber % 1
print(numbersrightdecimal) #print 0.34500000000000064.  You may get small trailing artifacts because of floating point precision problems.
#Use integer function rounds off the float to the nearest integer value.  Converts float numbers to integers.
decimalnumber = 12.345
print(int(decimalnumber)) #print 12
decimalnumber = 12.987
print(int(decimalnumber)) #print 12
decimalnumber = 34.49
print(int(decimalnumber)) #print 34
decimalnumber = 34.51
print(int(decimalnumber)) #print 34
#Use modf from math module to return the whole number or integer left of decimal and fractional number right of decimal as a tuple.
import math
decimalnumber = 12.345
fractionnumber, integernumber = math.modf(12.345)
print(fractionnumber) #print 0.34500000000000064.  You may get small trailing artifacts because of floating point precision problems.
print(integernumber)  #print 12.0
#quicker
decimaldigits = decimalnumberstring.split(".")[1] if "." in decimalnumberstring else ""
print(decimaldigits) #print 345
#Convert float number to string
decimalnumber = 12.345
decimalnumberstring = str(decimalnumber)
numbersrightdecimal = decimalnumberstring.split(".")
print(numbersrightdecimal) #print ['12', '345']
print(numbersrightdecimal[1]) #print 345
forloopmultiplenumbers = [998.99, 56.8, 25.6, -52.0]
integerlist = []
for eachdecimalnumber in forloopmultiplenumbers:
    integerlist.append(str(eachdecimalnumber).split(".")[0]) #Want the first entry in the split which is the integer part
print(integerlist) #print ['998', '56', '25', '-52']
integerlistconvertinteger = [int(i) for i in integerlist]
print(integerlistconvertinteger) #print [998, 56, 25, -52]
#Regular expression extract all decimal numbers right of decimal in a text
import re
text = "The price is 12.34 and the weight is 0.567"
alldecimalnumbersrightofdecimal = re.findall(r"\.(\d+)", text)
print(alldecimalnumbersrightofdecimal) #print ['34', '567']
#Decimal module for precision accuracy
from decimal import Decimal
number = Decimal("12.345")
numbersrightdecimalexact = number % 1
print(numbersrightdecimalexact) #print 0.345

#Extract decimal numbers to the left of decimal point
#Round function.  Rounds numbers to the nearest integer and rounds up.
print(round(12.345)) #print 12
print(round(12.675)) #print 13
#Truncate the number return integer only.  Remove decimal.  No rounding.
import math
print(math.trunc(2.77)) #print 2
print(math.trunc(8.32)) #print 8
print(math.trunc(8.999)) #print 8
print(math.trunc(-99.29)) #print -99
print(math.trunc(999998.99999)) #print 999998
