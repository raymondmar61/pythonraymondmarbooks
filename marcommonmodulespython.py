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
print(math.pow(2,4)) #print 16.0
print(int(math.pow(2,4))) #print 16
print(math.log(16,2)) #print 4.0
print(math.pi) #print 3.141592653589793

#Category:  random
import random
singledigitrandomnumber = random.randint(1,10)
print(singledigitrandomnumber) #print 6
fiverandomnumbers = random.sample(range(1,21),5) #random.sample takes a population and a sample size k and returns k random members of the population no duplicates.  An error message appears if the number of returns exceed the number of sample range.
print(fiverandomnumbers) #print [7, 9, 3, 4, 10]
givemenumbernorepeats1, givemenumbernorepeats2, givemenumbernorepeats3 = random.sample(range(1,31),3)
print(givemenumbernorepeats1, givemenumbernorepeats2, givemenumbernorepeats3) #print 5 2 16
