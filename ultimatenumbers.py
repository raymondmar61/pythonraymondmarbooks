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
print(math.log(16, 2)) #print 4.0
print(math.pi) #print 3.141592653589793
squareroot = math.sqrt(25)
iterablesequencesum = math.fsum([4, 5, 600, 10]) #fsum(seq, /) Return an accurate floating point sum of values in the iterable seq.
print(iterablesequencesum) #print 619.0

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
print(fiverandomnumbersnoduplicates) #print #print [14, 6, 20, 1, 8]
print(type(fiverandomnumbersnoduplicates)) #print <class 'list'>
fiverandomnumbersnoduplicates1, fiverandomnumbersnoduplicates2, fiverandomnumbersnoduplicates3, fiverandomnumbersnoduplicates4, fiverandomnumbersnoduplicates5 = random.sample(range(1, 21), 5)
print(fiverandomnumbersnoduplicates1) #print 5
print(fiverandomnumbersnoduplicates2) #print 16
print(fiverandomnumbersnoduplicates3) #print 3
print(fiverandomnumbersnoduplicates4) #print 1
print(fiverandomnumbersnoduplicates5) #print 20
print(type(fiverandomnumbersnoduplicates5)) #print <class 'int'>


#Statistics module
import statistics
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
averagenumber = statistics.mean(grades)
print(averagenumber) #print 80.42307692307692
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