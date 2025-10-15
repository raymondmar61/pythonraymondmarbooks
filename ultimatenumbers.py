#Basics
integernumber1 = 9
integernumber2 = 6
basicdivide = integernumber1 / integernumber2
print(basicdivide) #print 1.5
basicdivideinteger = integernumber1 // integernumber2
print(basicdivideinteger) #print 1
moduloreturnstheremainder = 10 % 3
print(moduloreturnstheremainder) #print 1
print(divmod(10, 3)) #print (3, 1).  10/3 is 3 remainder 1.  10 is the dividend.  3 is the divisor.  The 3 in the 3 remainder 1 is the quotient.
floatnumber = 458.21897869
complextnumber = 3 + 2j
exponentsasteriks = 2**4
print(exponentsasteriks) #print 16
print(pow(2, 4)) #print 16
roundthreedecimals = round(floatnumber, 3)
print(roundthreedecimals) #print 458.219
print(42 == 42.0) #print True
print(42.0 == 0042.0000) #print True
print(2 != 3) #print True
integernumber3 = -5
print(abs(integernumber3)) #print 5
print(max(4, 6, integernumber3)) #print 6
print(min(4, 6, integernumber3)) #print -5

#Formatting
stringvariable = "The String"
integervariable = 457
decimalvariable = 3.14159
print("Use plus sign to concatenate string variables.  Integer is " + str(integervariable) + ".  String is " + stringvariable + ".") #print Use plus sign to concatenate string variables.  Integer is 457.  String is The String.
print("use comma to concateante numerical variables.  Integer is", integervariable, ".  Decimal is", decimalvariable, ".") #print use comma to concateante numerical variables.  Integer is 457 .  Decimal is 3.14159 .
print("Use the percent f for an integer as a floating number %f.  Use the percent s for a string %s." % (integervariable, stringvariable)) #print Use the percent f for an integer as a floating number 457.000000.  Use the percent s for a string The String.
print("Use the percent f for a decimal as a floating number %f." % (decimalvariable)) #print Use the percent f for a decimal as a floating number 3.141590.
print("Use the percent period 2 f for a decimal as a floating number two decimals %.2f." % (decimalvariable)) #print Use the percent period 2 f for a decimal as a floating number two decimals 3.14.
print("Use the percent d for a decimal as an integer %d." % (decimalvariable)) #print Use the percent d for a decimal as an integer 3.
print("Pi is %f" % (3.14159)) #print Pi is 3.141590
print("Pi is %.2f" % (3.14159)) #print Pi is 3.14
print("Pi is %8.2f" % (3.14159)) #print Pi is ****3.14
print("Pi is %3f for geometry circles" % (3.14159)) #print Pi is 3.141590 for geometry circles
print("Pi is %-3f for geometry circles" % (3.14159)) #print Pi is 3.141590 for geometry circles
print("Pi is %-8.2f" % (3.14159)) #print Pi is 3.14****
print("Type the colon period and number f for a floating number or decimal number from an integer {:.1f} {:.2f}.".format(integervariable, integervariable)) #print Type the colon period and number f for a floating number or decimal number from an integer 457.0 457.00.
print("Decimal variable return two decimals {:.2f}.".format(decimalvariable)) #print Decimal variable return two decimals 3.14.
print("Decimal variable return five decimals {:.5f}.".format(decimalvariable)) #Decimal variable return five decimals 3.14159.

#Modulo or modulus
#Get the remainder from division.  Written with the percent sign %.  Takes a number and maps the number to a range based on the remainder when you divide the number.  number % modulus = remainder.  The remainder is always less than the modulus number.
#Take the modulus number and calculate how many times the modulus number fits in the first number.  The amount remaining is the answer or the remainder.
#Modular arithmetic.  A group of integers which wrap around when the maximum value is reached.
#Congruence means equivalent.
#Programming languges calculate negative modulus differently.  For example, Python and JavaScript return different answers.
print(10 / 3) #print 3.3333333333333335
pizzaslices = 10
people = 3
print(pizzaslices / people) #print 3.3333333333333335
print(pizzaslices % people) #print 1
print(12 % 3) #print 0.  12 / 3 = 4.  No remainder
print(7 % 2) #print 1.  7 - (3 * 2) = 1 remainder.
print(7 % 6) #print 1
print(6 % 7) #print 6
print(12 % 10) #print 2
print(10 % 12) #print 10
print(15 % 100) #print 15
print(15 % 299) #print 15
print(19 % 5987) #print 19
print(294 % 379654) #print 294
print(13 / 12) #print 1.0833333333333333
print(13 % 12) #print 1
print(divmod(13, 12)) #print (1,1).  Return division result quotient and remainder.
print(15 / 4) #print 3.75
print(15 % 4) #print 3
print(240 / 13) #print 18.46153846153846
print(240 % 13) #print 6
print(37 / 5) #print 7.4
print(37 // 5) #print 7
print(37 % 5) #print 2
print(divmod(37, 5)) #print (7,2).  Return division result quotient and remainder.
print(8 / 3) #print 2.6666666666666665
print(8 % 3) #print 2
print(8 / -3) #print -2.6666666666666665
print(8 % -3) #print -1
print(-20 % 6) #print 4.  Negative dividend and positive divisor.  Add postivie divisor to negative dividend.   Stop the math when the answer is zero or a positive number.  -20+6=-14+6=-8+6=-2+6=+4
print(20 % -6) #print -4.  Positive dividend and negative divisor.  Subtract negative divisor being absolute negative divisor to positive dividend.  Stop the math when the answer is zero or a negative number.  20-6=14-6=8-6=2-6=-4
print(5 % 3) #print 2.
print(-5 % 3) #print 1.  Negative dividend.
print(5 % -3) #print -1.  Negative divisor.
print(-5 % -3) #print -2.  Negative dividend and negative divisor.  Reason is the floor operator when calculating the remainder using the modulus operator.
#Python calculates the remainder.  r = a % n and r = a - (n * math.floor(a / n))
from math import floor
print(13 % 12) #print 1
print(13 - (12 * floor(13 / 12))) #print 1
print(8 % -3) #print -1
print(8 - (-3 * floor(8 / -3))) #print -1
print(-5 - (3 * floor(-5 / 3))) #print 1.  For (-5 % 3)
print(5 - (-3 * floor(5 / -3))) #print -1.  For (5 % -3)
print(-5 - (-3 * floor(-5 / -3))) #print -2.  For (-5 % -3)
print(12.5 % 5.5) #print 1.5.  Floating numbers.
print(17.0 % 12.0) #print 5.0
print(13.3 % 1.1) #print 0.09999999999999964.  Don't use floating value to store money.  Use decimal module.
from math import fmod #Use math.fmod for floating point or decimal remainders.
print(fmod(12.5, 5.5)) #print 1.5.
#Python negative remainders calculate differently
print(8 % -3) #print -1
print(fmod(8, -3)) #print 2.0
#https://www.mathsisfun.com/numbers/division-remainder.html
#7 divided by 2 is 3 with a remainder of 1.  Take remainder 1 and divisor 2; 1 / 2 = 0.5.
print(7 / 2) #print 3.5
print(7 % 2) #print 1
print(16 / 9) #print 1.7777777777777777
print(16 % 9) #print 7
print(7 / 9) #print 0.7777777777777778
print(19 / 5) #print 3.8
print(19 % 5) #print 4
print(4 / 5) #print 0.8
#https://www.mathsisfun.com/numbers/congruence.html
#Congruence.  Numbers are congruent when the numbers have the same remainder after being divided by the same number or the same modulus.  For example, 2 and 14 are congruent with modulus 12.
samemodulus = 12
print(2 % samemodulus) #print 2
print(14 % samemodulus) #print 2
#17 and 134 are congruent with modulus 9
samemodulus = 9
print(17 % samemodulus) #print 8
print(134 % samemodulus) #print 8
#The symbol for congruence is the hamburger icon or triple horizontal lines
print("17 --- 134 mod 9.  17 is congruent to 134 using modulus 9.")
#Subtract the two congruence numbers and divide by the modulus number.  The answer should be a multiple number.
print(134 - 17) #print 117
print((134 - 17) / samemodulus) #print 13.0
print((134 - 17) // samemodulus) #print 13

#Math module
import math
#print(help(math)) #print module help module description function descriptions
print(dir(math)) #print ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc'].  RM:  print module functions list module list
number = 5.6
ceiling = math.ceil(number)
print(ceiling) #print 6
floor = math.floor(number)
print(floor) #print 5
print(math.factorial(4)) #print 24
exponentetothepower = math.exp(2) #Return e raised to the power of x
print(exponentetothepower) #print 7.38905609893065
exponentsxtothepowerofy = math.pow(2, 4)
print(exponentsxtothepowerofy) #print 16.0
squareroot = math.pow(49, 1 / 2)
print(squareroot) #print 7.0
cuberoot = math.pow(27, 1 / 3)
print(cuberoot) #print 3.0
print(math.log(16, 2)) #print 4.0
print(math.pi) #print 3.141592653589793
squareroot = math.sqrt(25)
iterablesequencesum = math.fsum([4, 5, 600, 10]) #fsum(seq, /) Return an accurate floating point sum of values in the iterable seq.
print(iterablesequencesum) #print 619.0
absolutevalue = abs(-5.1)
print(absolutevalue) #print 5.1
absolutevaluealwaysfloat = math.fabs(-700)
print(absolutevaluealwaysfloat) #print 700.0
remainder = 10 % 5
print(remainder) #print 0
remainderalwaysfloat = math.remainder(10, 5)
print(remainderalwaysfloat) #print 0.0
remainderalwaysfloat = math.fmod(10, 5)
print(remainderalwaysfloat) #print 0.0

#Random module
import random
onerandomnumber = random.randint(1, 10)
print(onerandomnumber) #print 9
onerandomintegersincrementsoffive = random.randrange(0, 100, 5)
print(onerandomintegersincrementsoffive) #print 50
bonussixrandomintegersincrementsoffive = [random.randrange(0, 100, 5) for x in range(0, 6)]
print(bonussixrandomintegersincrementsoffive) #print [75, 5, 35, 70, 20, 85]
print(bonussixrandomintegersincrementsoffive[0]) #print 75
print(bonussixrandomintegersincrementsoffive[1]) #print 5
print(bonussixrandomintegersincrementsoffive[2]) #print 35
bonus1, bonus2, bonus3, bonus4, bonus5, bonus6 = bonussixrandomintegersincrementsoffive
print(bonus4) #print 70
print(bonus5) #print 20
print(bonus6) #print 85
choosenumber = random.choice(bonussixrandomintegersincrementsoffive)  #random.choice works for a list of strings
print(choosenumber) #print 5
fiverandomnumbersnoduplicates = random.sample(range(1, 21), 5) #random.sample takes a population and a sample size k and returns k random members of the population no duplicates.  An error message appears if the number of returns exceed the number of sample range.
print(fiverandomnumbersnoduplicates) #print [14, 6, 20, 1, 8]
print(type(fiverandomnumbersnoduplicates)) #print <class 'list'>
fiverandomnumbersnoduplicates1, fiverandomnumbersnoduplicates2, fiverandomnumbersnoduplicates3, fiverandomnumbersnoduplicates4, fiverandomnumbersnoduplicates5 = random.sample(range(1, 21), 5)
print(fiverandomnumbersnoduplicates1) #print 5
print(fiverandomnumbersnoduplicates2) #print 16
print(fiverandomnumbersnoduplicates3) #print 3
print(fiverandomnumbersnoduplicates4) #print 1
print(fiverandomnumbersnoduplicates5) #print 20
print(type(fiverandomnumbersnoduplicates5)) #print <class 'int'>
#The shuffle() is an inbuilt method of the random module. It is used to shuffle a sequence (list). Shuffling a list of objects means changing the position of the elements of the sequence
random.shuffle(fiverandomnumbersnoduplicates)
print(fiverandomnumbersnoduplicates) #print [1, 20, 14, 8, 6]
#Use the random.seed function to guarantee reproducibility of a random sequence such as debugging.
seednumber = 32
random.seed(seednumber) #Define a seed to make random numbers predictable or the same random numbers appear every time
for samerandomnumbers in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 2 2 3 6 2 4 1 6 1
print("\b")
for differentrandomnumbers1 in range(10): #RM:  the differentrandomnumbers*number* generates different values because it continues the pseudorandom number sequence which started at samerandomnumbers
    print(random.randrange(1, 7), end=" ") #print 1 3 5 3 1 5 6 4 3 5
print("\b")
for differentrandomnumbers2 in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 5 2 5 1 4 6 2 3 2
print("\b")
random.seed(seednumber) #start again random.seed(seednumber)
for samerandomnumbers in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 2 2 3 6 2 4 1 6 1
print("\b")
for differentrandomnumbers3 in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 3 5 3 1 5 6 4 3 5
print("\b")
for differentrandomnumbers4 in range(10):
    print(random.randrange(1, 7), end=" ") #print 1 5 2 5 1 4 6 2 3 2
print("\n")
random.seed() #deactivate random.seed or stop random.seed

#Statistics module
import statistics
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
averagenumber = statistics.mean(grades)
print(averagenumber) #print 80.42307692307692
middlenumber = statistics.median(grades)
print(middlenumber) #print 85
mostcommonnumber = statistics.mode(grades)
print(mostcommonnumber) #print 100
print("Two decimal points %.2f" % (averagenumber)) #print Two decimal points 80.42
populationvariance = statistics.pvariance(grades)
print(populationvariance) #print 334.07100591715977
#Use variance() function when your data is a sample from a population.  A large variance indicates that the data is spread out; a small variance indicates it is clustered closely around the mean.
sixrandomgrades = random.sample(grades, 5)
print(sixrandomgrades) #print [100, 100, 40, 50.5, 85]
sixrandomgradesvariance = statistics.variance(sixrandomgrades)
print(sixrandomgradesvariance) #print 793.8000000000001
#The standard deviation is the square root of the variance. You can calculate the square root by raising the number to the one-half power.
print(statistics.stdev(grades)) #print 19.02393903507516
print(statistics.stdev(sixrandomgrades)) #print 28.17445651649735

#Decimal module
import decimal
decimalnumber = 0.00
print(decimal.Decimal(decimalnumber)) #print 0
decimalstring = "0.00"
print(decimal.Decimal(decimalstring)) #print 0.00
print(type(decimal.Decimal(decimalstring))) #print <class 'decimal.Decimal'>
decimalstringcalculations = decimal.Decimal(decimalstring)
print(decimalstringcalculations) #print 0.00
print(decimalstringcalculations + 1) #print 1.00

#Manual counter, manual iterator
generateanumber = iter(range(0, 10))
print(generateanumber) #print <range_iterator object at 0x7f094d6a0b10>
#RM:  the next function must be immediate; otherwise, an error message StopIteration
# print(type(generateanumber)) #print <class 'range_iterator'>
# print(list(generateanumber)) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(next(generateanumber)) #print 0
print(next(generateanumber)) #print 1
print(next(generateanumber)) #print 2
print(type(generateanumber)) #print <class 'range_iterator'>
print(next(generateanumber)) #print 3
print(list(generateanumber)) #print [4, 5, 6, 7, 8, 9]
#print(next(generateanumber)) #Error message StopIteration

#Fractions module
import fractions
print(fractions.Fraction(6, 10)) #print 3/5.  Round fractions rounding fractions.
print(type(fractions.Fraction(6, 10))) #print <class 'fractions.Fraction'>
print(fractions.Fraction(1, 3)) #print 1/3.  1/3 can't be rounded down.
print(fractions.Fraction(20, 8)) #print 5/2.  20/8 can be rounded down.
a = fractions.Fraction(22, 99)
print(a) #print 2/9.  22/99 can be rounded down by 11.
addfraction1 = fractions.Fraction(1, 4)
addfraction2 = fractions.Fraction(1, 2)
print(addfraction1 + addfraction2) #print 3/4
addfraction1 = fractions.Fraction(2, 3)
addfraction2 = fractions.Fraction(2, 3)
print(addfraction1 + addfraction2) #print 4/3.  2/3 is 1/3 + 1/3.  (2/3 + 1/3) + 1/3.  (1) + 1/3 = 4/3.
arithemeticfraction1 = fractions.Fraction(2, 3)
arithemeticfraction2 = fractions.Fraction(2, 9)
print(arithemeticfraction1 - arithemeticfraction2) #print 4/9
print(arithemeticfraction1 * arithemeticfraction2) #print 4/27
decimaltofraction = fractions.Fraction(1.25)
print(decimaltofraction) #print 5/4
decimaltofraction = fractions.Fraction(2.5)
print(decimaltofraction) #print 5/2
decimaltofraction = fractions.Fraction(1.33)
print(decimaltofraction) #print 748723438050345/562949953421312
decimaltofraction = fractions.Fraction("1.33")
print(decimaltofraction) #print 133/100
#limit_denominator() method.  Finds and returns the closest Fraction that has denominator at most max_denominator. This method is useful for finding rational approximations to a given floating-point number.  default max_denominator is 1000000.
decimaltofraction = fractions.Fraction(1.33).limit_denominator()
print(decimaltofraction) #print 133/100
print(type(decimaltofraction)) #print <class 'fractions.Fraction'>
technicallyzero = fractions.Fraction()
print(technicallyzero) #print 0
technicallyzero = fractions.Fraction(0, 1)
print(technicallyzero) #print 0
print(fractions.Fraction(.3)) #print 5404319552844595/18014398509481984
print(fractions.Fraction(".3")) #print 3/10
print(fractions.Fraction(.3).limit_denominator()) #print 3/10
print(fractions.Fraction(2 / 10)) #print 3602879701896397/18014398509481984
print(fractions.Fraction("2/10")) #print 1/5
print(fractions.Fraction(2 / 10).limit_denominator) #print <bound method Fraction.limit_denominator of Fraction(3602879701896397, 18014398509481984)>
print(fractions.Fraction(2 / 10).limit_denominator()) #print 1/5
print(fractions.Fraction(2 / 10).limit_denominator(10)) #print 1/5
print(fractions.Fraction(3.1415937).limit_denominator(30)) #print 22/7
print(fractions.Fraction(3.1415937).limit_denominator(100)) #print 311/99
print(fractions.Fraction(.1)) #print 3602879701896397/36028797018963968
print(fractions.Fraction(.1).limit_denominator()) #print 1/10
print(fractions.Fraction(.1).limit_denominator(30)) #print 1/10
print(fractions.Fraction.from_float(.1)) #print 3602879701896397/36028797018963968
print(fractions.Fraction.from_float(.1).limit_denominator(10)) #print 1/10
print(fractions.Fraction.from_float(.1).limit_denominator(100)) #print 1/10
print(fractions.Fraction.from_float(.3)) #print 5404319552844595/18014398509481984
print(fractions.Fraction.from_float(.3).limit_denominator(10)) #print 3/10
print(fractions.Fraction.from_float(.3).limit_denominator(100)) #print 3/10
print(fractions.Fraction(20 / 40).numerator) #print 1
print(fractions.Fraction(20 / 40).denominator) #print 2
print(fractions.Fraction(20 / 33).numerator) #print 5458908639236965
print(fractions.Fraction(20 / 33).denominator) #print 9007199254740992
#print(fractions.Fraction(20 / 33).denominator.limit_denominator(10)) #print AttributeError: 'int' object has no attribute 'limit_denominator'
print(fractions.Fraction((5 * 4), (30 + 3))) #print 20/33
print(round(fractions.Fraction(3 / 2))) #print 2
print(round(fractions.Fraction(1.5))) #print 2
print(round(fractions.Fraction(5 / 2))) #print 2
print(round(fractions.Fraction(2.5))) #print 2
print(round(fractions.Fraction(6 / 2))) #print 3
print(round(fractions.Fraction(3.25))) #print 3
print(round(fractions.Fraction(3.5))) #print 4

#Convert seconds to hours, minutes, and seconds
totalseconds = 67000
hours = int(totalseconds / 3600)
minutes = int((totalseconds / 60) % 60)
seconds = totalseconds % 60
print(hours, minutes, seconds) #print 18 36 40
print(hours, "hours", minutes, "minutes", seconds, "seconds") #print 18 hours 36 minutes 40 seconds
print(f"{totalseconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds") #print 67000 seconds = 18 hours, 36 minutes, 40 seconds

#Check number is square root or perfect square
import math
def checkperfectsquare(n):
    if n >= 0:
        squareroot = math.isqrt(n) #The isqrt() function calculates the integer square root of a given number.
        #print(squareroot * squareroot == n)
        return (squareroot * squareroot == n)
def issquarenumber(n):
    root = math.sqrt(n)
    return (root % 1 == 0) #return True if square number
def isnotsquarenumber(n):
    root = math.sqrt(n)
    return (root % 1 != 0) #return False if square number


number = 4
print(checkperfectsquare(4)) #print True
print(issquarenumber(4)) #print True
print(isnotsquarenumber(4)) #print  False
number = 100
print(checkperfectsquare(100)) #print True
print(issquarenumber(100)) #print True
print(isnotsquarenumber(100)) #print  False
number = 5
print(checkperfectsquare(5)) #print False
print(issquarenumber(5)) #print False
print(isnotsquarenumber(5)) #print  True

#Check number is cube root
def isperfectcube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x


print(isperfectcube(27)) #print True

#Find cube root
import math
def cubicroot(n):
    return round(math.exp(math.log(n) / 3), 6)


print(cubicroot(41063625)) #print 345.0
print(cubicroot(127035954683)) #print 5027.0

#Itertools module
import itertools
#Iterate over a collection of items.  Implement the iterator protocol.  Define the __iter__ and __next__ methods.
#Iteration works in Python:  Python asks if the object is iterable by invoking the iter builtin.  It invokes the __iter__ method.  If iterable, it returns an iterator object.  The object implements __next__.  __next__ method invoked repeatedly until it raises a StopIteration exception.
#Count.  The count iterator counts.  count(start, increment default is 1).  You indicate where the counter starts and how much increase with each iteration.
for i in itertools.count(1):
    if i >= 20:
        print("Count from 1 to 19 break now")
        break
    print(i)
    '''
    1
    2
    3
    4
    5
    ...
    18
    19
    Count from 1 to 19 break now
    '''
for i in itertools.count(-10, 4):
    if i >= 20:
        print("Count from -10 to 19 by fours break now")
        break
    print(i)
    '''
    -10
    -6
    -2
    2
    6
    10
    14
    18
    Count from -10 to 19 by fours break now
    '''
#Repeat.  The repeat iterator repeats a set number of times or infinitely.  The Python documentation says repeat is useful if you want to give constant values to map or zip.  Instructor never seen repeat used in practice.
for eachrepeat in itertools.repeat(100, 5):
    print(eachrepeat, end=", ") #print 100, 100, 100, 100, 100,
print("\n")
#Filterfalse.  The built-in filter function returns an iterable object based on the combination of a predicate or a function which returns True or False and an iterable.  The filter function applies the predicate to each element of the iterable.  Objects are returned when the predicate returns True.
mylist = [10, 20, 25, 30, 35, 36, 40, 42, 45]
for eachmylist in mylist:
    print(eachmylist % 2) #RM:  0 is False, 1 is True
    '''
    0
    0
    1
    0
    1
    0
    0
    0
    1
    '''
mylist = [10, 20, 25, 30, 35, 36, 40, 42, 45]
filterfalsevariable = filter(lambda x: x % 2, mylist)
print(filterfalsevariable) #print <filter object at 0x7fb5cacd5a00>
print(list(filterfalsevariable)) #print [25, 35, 45].  The code returns a filter list consisting of numbers in mylist which are odd.  Returns True for odd numbers x % 2 is 1.  Returns False for even numbers x % 2 is 0.
filterfalsevariableevenumbers = filter(lambda x: not x % 2, mylist)
print(list(filterfalsevariableevenumbers)) #print [10, 20, 30, 36, 40, 42].  The code returns a filter list consisting of numbers in mylist which are even.  Returns True for even numbers x % 2 is not 0.  Returns False for odd numbers x % 2 is not 1.
filterfalseevenumbers = itertools.filterfalse(lambda x: x % 2, mylist)
print(list(filterfalseevenumbers)) #print [10, 20, 30, 36, 40, 42].  The code returns a filter list consisting of numbers in mylist which are odd.  Returns True for odd numbers x % 2 is 1.  Returns False for even numbers x % 2 is 0.
#Takewhile.  Takewhile iterators needs a predicate and an iterable.  Returns elements from the iterable as long as the predicate returns True.  The iterable stops when the predicate returns False.
stopwhenfalseoddnumber = list(itertools.takewhile(lambda x: not x % 2, mylist))
print(stopwhenfalseoddnumber) #print [10, 20].  Returns True when even number.  Returns False when odd number and iterator stops which is 25.
#Dropwhile.  Dropwhile iterators needs a predicate and an iterable.  Returns elements from the iterable when the predicate returns the first False.  The iterable stops filtering when the predicate returns True.  All iterables are returned True or False.
stopfilteringtrueoddnumber = list(itertools.dropwhile(lambda x: not x % 2, mylist))
print(stopfilteringtrueoddnumber) #print [25, 30, 35, 36, 40, 42, 45]  #Ignores True when even number.  False when odd number. and returns the first false number and returns all numbers thereafter True or False.  In other words, the interator starts returning results from the first false to the end of the elements.
#Product.  Takes any number of iterables as arguments.  Returns a tuple containing one element from each of the arguments.  The iterator stops after returning all possible tuples.
#Combinations and permutations.  Combinations can be used once in an area.  Permutations all possibilities are returned.  Simple example (a, b) and (b, a) can't be used in a permutation because they're the same in combination.
fourletterscombinewith = "abcd"
fournumberstobecombinedwith = [10, 20, 30, 40]
print(list(itertools.product(fourletterscombinewith, fournumberstobecombinedwith))) #print [('a', 10), ('a', 20), ('a', 30), ('a', 40), ('b', 10), ('b', 20), ('b', 30), ('b', 40), ('c', 10), ('c', 20), ('c', 30), ('c', 40), ('d', 10), ('d', 20), ('d', 30), ('d', 40)]
print(list(itertools.product(fourletterscombinewith, fournumberstobecombinedwith, repeat=2))) #print [('a', 10, 'a', 10), ('a', 10, 'a', 20), ('a', 10, 'a', 30), ('a', 10, 'a', 40), ('a', 10, 'b', 10), ('a', 10, 'b', 20), ('a', 10, 'b', 30), ('a', 10, 'b', 40), ('a', 10, 'c', 10), ('a', 10, 'c', 20), ('a', 10, 'c', 30), ('a', 10, 'c', 40), ('a', 10, 'd', 10), ('a', 10, 'd', 20), ('a', 10, 'd', 30), ('a', 10, 'd', 40), ('a', 20, 'a', 10), ('a', 20, 'a', 20), ('a', 20, 'a', 30), ('a', 20, 'a', 40), ('a', 20, 'b', 10), ('a', 20, 'b', 20), ('a', 20, 'b', 30), ('a', 20, 'b', 40), ('a', 20, 'c', 10), ('a', 20, 'c', 20), ('a', 20, 'c', 30), . . .]
print(list(itertools.combinations(fourletterscombinewith, 4))) #print [('a', 'b', 'c', 'd')]
print(list(itertools.combinations(fourletterscombinewith, 2))) #print [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
print(list(itertools.permutations(fourletterscombinewith))) #print [('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ('a', 'c', 'b', 'd'), ('a', 'c', 'd', 'b'), ('a', 'd', 'b', 'c'), ('a', 'd', 'c', 'b'), ('b', 'a', 'c', 'd'), ('b', 'a', 'd', 'c'), ('b', 'c', 'a', 'd'), ('b', 'c', 'd', 'a'), ('b', 'd', 'a', 'c'), ('b', 'd', 'c', 'a'), ('c', 'a', 'b', 'd'), ('c', 'a', 'd', 'b'), ('c', 'b', 'a', 'd'), ('c', 'b', 'd', 'a'), ('c', 'd', 'a', 'b'), ('c', 'd', 'b', 'a'), ('d', 'a', 'b', 'c'), ('d', 'a', 'c', 'b'), ('d', 'b', 'a', 'c'), ('d', 'b', 'c', 'a'), ('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')]
print(list(itertools.permutations(fourletterscombinewith, 2))) #print [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]
minigymfiveworkouts = itertools.combinations(range(1, 6), 2)
print(list(minigymfiveworkouts)) #print [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
print(list(itertools.combinations_with_replacement(fourletterscombinewith, 3))) #print [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'a', 'd'), ('a', 'b', 'b'), ('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'c'), ('a', 'c', 'd'), ('a', 'd', 'd'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'b', 'd'), ('b', 'c', 'c'), ('b', 'c', 'd'), ('b', 'd', 'd'), ('c', 'c', 'c'), ('c', 'c', 'd'), ('c', 'd', 'd'), ('d', 'd', 'd')]
print(list(itertools.combinations_with_replacement(fournumberstobecombinedwith, 2))) #print [(10, 10), (10, 20), (10, 30), (10, 40), (20, 20), (20, 30), (20, 40), (30, 30), (30, 40), (40, 40)]
#Permutate a number.  Number must be a string.
import itertools
testnumber = 56623104
testnumberlength = len(str(testnumber))
cubicpermutation = itertools.permutations(str(testnumber), testnumberlength)
print(testnumberlength) #print 8
print(cubicpermutation) #print <itertools.permutations object at 0x7fdf7a232b80>
for eachcubicpermutation in cubicpermutation:
    integertuple = tuple(map(int, eachcubicpermutation))
    if integertuple == (5, 6, 6, 2, 3, 1, 0, 4) or integertuple == (6, 6, 4, 3, 0, 1, 2, 5):
        print(integertuple)
        '''
        (5, 6, 6, 2, 3, 1, 0, 4)
        (5, 6, 6, 2, 3, 1, 0, 4)
        (6, 6, 4, 3, 0, 1, 2, 5)
        (6, 6, 4, 3, 0, 1, 2, 5)
        '''

#Binary
#https://stackoverflow.com/questions/2451386/what-does-the-caret-operator-do
#The caret ^ is a bitwise XOR; in other words, an exclusive OR.  XOR evalulates to True if and only if its arguments differ; in other words, one is True and the other is False.
#It invokes the __xor__() or __rxor__() method of the object as needed, which for integer types does a bitwise exclusive-or.  It's a bit-by-bit exclusive-or. Binary bitwise operators.
#Whatever data types are placed to the right and left of the symbol must implement this function in a compatible way. For integers, it is the common XOR operation.
print(0 ^ 0) #print 0
print(1 ^ 1) #print 0
print(1 ^ 0) #print 1
print(0 ^ 1) #print 1
print(8 ^ 3) #print 11.  1000 is 8 binary.  0011 is 3 binary.  1011 is 11 binary.
print(0b1000 ^ 0b0011) #print 11.  You can do binary numbers by typing 0bX where X is your binary.
print(8 ^ 4) #print 12
print(8 ^ 1) #print 9
print(8 ^ 0) #print 8
print(7 ^ 1) #print 6
print(7 ^ 2) #print 5
print(7 ^ 7) #print 0
print(7 ^ 8) #print 15
print(9 ^ 1) #print 8
print(16 ^ 1) #print 17
print(15 ^ 1) #print 14
print(3 ^ 4) #print 7
print(5 ^ 6) #print 3
print(1234 ^ 4321) #print 5171
