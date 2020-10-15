#Common Modules Python Combine All Lessons Learned One Stop Book One Stop Documentation
#Category:  *topic*
#Categories:  math, random
#williamfisetallvideos

#Category:  math
import math
print(dir(math)) #print ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
number = 5.6
print(math.ceil(number)) #print 6
print(math.floor(number)) #print 5
print(math.factorial(4)) #print 24
print(math.exp(2)) #print 7.38905609893065
print(math.pow(2, 4)) #print 16.0
print(int(math.pow(2, 4))) #print 16
print(math.log(16, 2)) #print 4.0
print(math.pi) #print 3.141592653589793
print(math.sqrt(25)) #print 5.0
print(math.fsum([4, 5, 6, 7])) #print 22.0

#Category:  random
import random
singledigitrandomnumber = random.randint(1, 10)
print(singledigitrandomnumber) #print 6
fiverandomnumbers = random.sample(range(1, 21), 5) #random.sample takes a population and a sample size k and returns k random members of the population no duplicates.  An error message appears if the number of returns exceed the number of sample range.
print(fiverandomnumbers) #print [7, 9, 3, 4, 10]
givemenumbernorepeats1, givemenumbernorepeats2, givemenumbernorepeats3 = random.sample(range(1, 31), 3)
print(givemenumbernorepeats1, givemenumbernorepeats2, givemenumbernorepeats3) #print 5 2 16

#Category:  statistics
import statistics
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print(statistics.mean(grades)) #print 80.42307692307692
print("%.2f" % (statistics.mean(grades))) #print 80.42
#A large variance indicates that the data is spread out; a small variance indicates it is clustered closely around the mean.
print(statistics.pvariance(grades)) #print 334.07100591715977.  Population variance.
#Use variance() function when your data is a sample from a population. To calculate the variance from the entire population, see pvariance().  A large variance indicates that the data is spread out; a small variance indicates it is clustered closely around the mean.
gradessample = [100, 100, 90, 100]
print(statistics.variance(gradessample)) #print 25.0
gradessample2 = [100, 100, 90, 40]
print(statistics.variance(gradessample2)) #print 825.0
#The standard deviation is the square root of the variance. You can calculate the square root by raising the number to the one-half power.
print(statistics.stdev(grades)) #print 19.02393903507516
print(statistics.stdev(gradessample)) #print 5.0
