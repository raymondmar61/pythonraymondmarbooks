#https://pynative.com/python-find-all-divisors-of-number/
#For loop.  Straightforward.  Use modulo operator %.
findalldivisors = 36
divisorslist = []
for divisor in range(1, findalldivisors + 1):
    if findalldivisors % divisor == 0:
        divisorslist.append(divisor)
print(divisorslist) #print [1, 2, 3, 4, 6, 9, 12, 18, 36]

#math.sqrt() function.  math.sqrt() limits the number of iterations.  Iterate up to math.sqrt(findalldivisors) instead of findalldivisors.  The divisor and its complementary divisor n//i are included in the divisorslist.  It reduces the number of iterations.
#math.sqrt(findalldivisors) determines the range to check for divisors.  int() converts the square root value to a whole number.
#All divisors are pairs.  For example, for 100, the pairs are (1, 100), (2, 50), (4, 25), (5, 20), and (10, 10).  (10, 10) is both divisors are equal or a perfect square.  Include perfect squares once.  Iterate from 1 to the square root of n.  For any factor a of n, the corresponding factor b = n/a forms a pair (a,b).  At least one of the two values in the pair must be between 1 and the square root of n.
import math
findalldivisors = 36
divisorslist = []
for divisor in range(1, int(math.sqrt(findalldivisors)) + 1):
    if findalldivisors % divisor == 0:
        divisorslist.append(divisor)
        #Add the corresponding divisor which is divisor and findalldivisor//divisor
        if divisor != findalldivisors // divisor:
            print("findalldivisors // divisor", findalldivisors // divisor)
            '''
            findalldivisors // divisor 36
            findalldivisors // divisor 18
            findalldivisors // divisor 12
            findalldivisors // divisor 9
            '''
            divisorslist.append(findalldivisors // divisor)
print(divisorslist) #print [1, 36, 2, 18, 3, 12, 4, 9, 6]
#also.  From https://www.geeksforgeeks.org/dsa/find-all-factors-of-a-natural-number/
import math
findalldivisors = 36
divisorslist = []
for divisor in range(1, int(math.sqrt(findalldivisors)) + 1):
    if findalldivisors % divisor == 0:
        #If both divisors are the same or a perfect square, then add once.
        if findalldivisors // divisor == divisor:
            divisorslist.append(divisor)
        else:
            divisorslist.append(divisor)
            divisorslist.append(findalldivisors // divisor)
print(divisorslist) #print [1, 36, 2, 18, 3, 12, 4, 9, 6]

#List comprehension
findalldivisors = 36
divisorslist = [divisor for divisor in range(1, findalldivisors + 1) if findalldivisors % divisor == 0]
print(divisorslist) #print [1, 2, 3, 4, 6, 9, 12, 18, 36]

#Function to create a generator.  Yields values one at a time as they are produced instead of returning values all at once.  The generator function yield divisors one by one.  More memory efficient for large numbers.  Avoids storing all divisors in memory at once.
#The yield keyword produces each divisor one at a time instead of storing all divisors in memory.
def findalldivisorsgenerator(n):
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor
            if divisor != n // divisor:
                yield n // divisor


findalldivisors = 36
divisors = list(findalldivisorsgenerator(findalldivisors))
print(divisors) #print [1, 36, 2, 18, 3, 12, 4, 9, 6]


'''
# Source - https://stackoverflow.com/a/171784
# Posted by Greg Hewgill, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-17, License - CC BY-SA 4.0
def divisorGen(n):
    factors = list(factorGenerator(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x * y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


print(divisorGen(100000000)) #print <generator object divisorGen at 0x7c1a18146420>

# Source - https://stackoverflow.com/a/171779
# Posted by Matthew Scharley, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-17, License - CC BY-SA 4.0
import math
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


print(list(divisorGenerator(100))) #print [1, 2, 4, 5, 10, 20.0, 25.0, 50.0, 100.0]
print(list(divisorGenerator(100000000))) #print [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100, 125, 128, 160, 200, 250, 256, 320, 400, 500, 625, 640, 800, 1000, 1250, 1280, 1600, 2000, 2500, 3125, 3200, 4000, 5000, 6250, 6400, 8000, 10000, 12500.0, 15625.0, 16000.0, 20000.0, 25000.0, 31250.0, 32000.0, 40000.0, 50000.0, 62500.0, 78125.0, 80000.0, 100000.0, 125000.0, 156250.0, 160000.0, 200000.0, 250000.0, 312500.0, 390625.0, 400000.0, 500000.0, 625000.0, 781250.0, 800000.0, 1000000.0, 1250000.0, 1562500.0, 2000000.0, 2500000.0, 3125000.0, 4000000.0, 5000000.0, 6250000.0, 10000000.0, 12500000.0, 20000000.0, 25000000.0, 50000000.0, 100000000.0]
'''
