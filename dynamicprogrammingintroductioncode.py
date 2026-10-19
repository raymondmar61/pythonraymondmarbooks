#Mastering Dynamic Programming - How to solve any interview problem [Hdr64lKQ3e4]
memocalculatedfib = {}
def fibonacciyesrecursion(n):
    if n in memocalculatedfib:
        return memocalculatedfib[n]
    if n <= 2:
        result = 1
    else:
        result = fibonacciyesrecursion(n - 2) + fibonacciyesrecursion(n - 1)
    memocalculatedfib[n] = result
    return result


print(fibonacciyesrecursion(7)) #print 13
print(memocalculatedfib) #print {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13}
print(fibonacciyesrecursion(50)) #print 12586269025
print(memocalculatedfib) #print {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55, 11: 89, 12: 144, 13: 233, 14: 377, 15: 610, 16: 987, 17: 1597, 18: 2584, 19: 4181, 20: 6765, 21: 10946, 22: 17711, 23: 28657, 24: 46368, 25: 75025, 26: 121393, 27: 196418, 28: 317811, 29: 514229, 30: 832040, 31: 1346269, 32: 2178309, 33: 3524578, 34: 5702887, 35: 9227465, 36: 14930352, 37: 24157817, 38: 39088169, 39: 63245986, 40: 102334155, 41: 165580141, 42: 267914296, 43: 433494437, 44: 701408733, 45: 1134903170, 46: 1836311903, 47: 2971215073, 48: 4807526976, 49: 7778742049, 50: 12586269025}

def fibonaccinorecursion(n):
    memocalculatedfib = {}
    for i in range(1, n + 1):
        if i <= 2:
            result = 1
        else:
            result = memocalculatedfib[i - 2] + memocalculatedfib[i - 1]
        memocalculatedfib[i] = result
    return (memocalculatedfib, memocalculatedfib[n])


print(fibonaccinorecursion(7)) #print ({1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13}, 13)
print(fibonaccinorecursion(50)) #print ({1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55, 11: 89, 12: 144, 13: 233, 14: 377, 15: 610, 16: 987, 17: 1597, 18: 2584, 19: 4181, 20: 6765, 21: 10946, 22: 17711, 23: 28657, 24: 46368, 25: 75025, 26: 121393, 27: 196418, 28: 317811, 29: 514229, 30: 832040, 31: 1346269, 32: 2178309, 33: 3524578, 34: 5702887, 35: 9227465, 36: 14930352, 37: 24157817, 38: 39088169, 39: 63245986, 40: 102334155, 41: 165580141, 42: 267914296, 43: 433494437, 44: 701408733, 45: 1134903170, 46: 1836311903, 47: 2971215073, 48: 4807526976, 49: 7778742049, 50: 12586269025}, 12586269025)

#m is the total value of the coins.  Find the lowest count of coins to sum m.
def minignorenone(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


memocoins = {}
def minimumcoinsyesrecursion(m, coins):
    if m in memocoins:
        return memocoins[m]
    if m == 0:
        answer = 0
    else:
        answer = None
        for eachcoin in coins:
            subproblem = m - eachcoin
            if subproblem < 0:
                #Skip solution where we try to reach [m] from a negative subproblem.
                continue
            answer = minignorenone(answer, minimumcoinsyesrecursion(subproblem, coins) + 1)
    memocoins[m] = answer
    return answer


print(minimumcoinsyesrecursion(13, [1, 4, 5])) #print 3
print(memocoins) #print {0: 0, 1: 1, 2: 2, 3: 3, 4: 1, 5: 1, 6: 2, 7: 3, 8: 2, 9: 2, 10: 2, 11: 3, 12: 3, 13: 3}
print(minimumcoinsyesrecursion(150, [1, 4, 5])) #print 30
print(memocoins) #print {0: 0, 1: 1, 2: 2, 3: 3, 4: 1, 5: 1, 6: 2, 7: 3, 8: 2, 9: 2, 10: 2, 11: 3, 12: 3, 13: 3, 14: 3, 15: 3, 16: 4, 17: 4, 18: 4, 19: 4, 20: 4, 21: 5, 22: 5, 23: 5, 24: 5, 25: 5, 26: 6, 27: 6, 28: 6, 29: 6, 30: 6, 31: 7, 32: 7, 33: 7, 34: 7, 35: 7, 36: 8, 37: 8, 38: 8, 39: 8, 40: 8, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 10, 47: 10, 48: 10, 49: 10, 50: 10, 51: 11, 52: 11, 53: 11, 54: 11, 55: 11, 56: 12, 57: 12, 58: 12, 59: 12, 60: 12, 61: 13, 62: 13, 63: 13, 64: 13, 65: 13, 66: 14, 67: 14, 68: 14, 69: 14, 70: 14, 71: 15, 72: 15, 73: 15, 74: 15, 75: 15, 76: 16, 77: 16, 78: 16, 79: 16, 80: 16, 81: 17, 82: 17, 83: 17, 84: 17, 85: 17, 86: 18, 87: 18, 88: 18, 89: 18, 90: 18, 91: 19, 92: 19, 93: 19, 94: 19, 95: 19, 96: 20, 97: 20, 98: 20, 99: 20, 100: 20, 101: 21, 102: 21, 103: 21, 104: 21, 105: 21, 106: 22, 107: 22, 108: 22, 109: 22, 110: 22, 111: 23, 112: 23, 113: 23, 114: 23, 115: 23, 116: 24, 117: 24, 118: 24, 119: 24, 120: 24, 121: 25, 122: 25, 123: 25, 124: 25, 125: 25, 126: 26, 127: 26, 128: 26, 129: 26, 130: 26, 131: 27, 132: 27, 133: 27, 134: 27, 135: 27, 136: 28, 137: 28, 138: 28, 139: 28, 140: 28, 141: 29, 142: 29, 143: 29, 144: 29, 145: 29, 146: 30, 147: 30, 148: 30, 149: 30, 150: 30}

def minignorenone(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def minimumcoinsnorecursion(m, coins):
    memocoins = {}
    memocoins[0] = 0
    for i in range(1, m + 1):
        for eachcoin in coins:
            subproblem = i - eachcoin
            if subproblem < 0:
                #Skip solution where we try to reach [m] from a negative subproblem.
                continue
            memocoins[i] = minignorenone(memocoins.get(i), memocoins.get(subproblem) + 1)
    return memocoins[m]


print(minimumcoinsnorecursion(13, [1, 4, 5])) #print 3
print(memocoins) #print {0: 0, 1: 1, 2: 2, 3: 3, 4: 1, 5: 1, 6: 2, 7: 3, 8: 2, 9: 2, 10: 2, 11: 3, 12: 3, 13: 3}
print(minimumcoinsnorecursion(150, [1, 4, 5])) #print 30
print(memocoins) #print {0: 0, 1: 1, 2: 2, 3: 3, 4: 1, 5: 1, 6: 2, 7: 3, 8: 2, 9: 2, 10: 2, 11: 3, 12: 3, 13: 3, 14: 3, 15: 3, 16: 4, 17: 4, 18: 4, 19: 4, 20: 4, 21: 5, 22: 5, 23: 5, 24: 5, 25: 5, 26: 6, 27: 6, 28: 6, 29: 6, 30: 6, 31: 7, 32: 7, 33: 7, 34: 7, 35: 7, 36: 8, 37: 8, 38: 8, 39: 8, 40: 8, 41: 9, 42: 9, 43: 9, 44: 9, 45: 9, 46: 10, 47: 10, 48: 10, 49: 10, 50: 10, 51: 11, 52: 11, 53: 11, 54: 11, 55: 11, 56: 12, 57: 12, 58: 12, 59: 12, 60: 12, 61: 13, 62: 13, 63: 13, 64: 13, 65: 13, 66: 14, 67: 14, 68: 14, 69: 14, 70: 14, 71: 15, 72: 15, 73: 15, 74: 15, 75: 15, 76: 16, 77: 16, 78: 16, 79: 16, 80: 16, 81: 17, 82: 17, 83: 17, 84: 17, 85: 17, 86: 18, 87: 18, 88: 18, 89: 18, 90: 18, 91: 19, 92: 19, 93: 19, 94: 19, 95: 19, 96: 20, 97: 20, 98: 20, 99: 20, 100: 20, 101: 21, 102: 21, 103: 21, 104: 21, 105: 21, 106: 22, 107: 22, 108: 22, 109: 22, 110: 22, 111: 23, 112: 23, 113: 23, 114: 23, 115: 23, 116: 24, 117: 24, 118: 24, 119: 24, 120: 24, 121: 25, 122: 25, 123: 25, 124: 25, 125: 25, 126: 26, 127: 26, 128: 26, 129: 26, 130: 26, 131: 27, 132: 27, 133: 27, 134: 27, 135: 27, 136: 28, 137: 28, 138: 28, 139: 28, 140: 28, 141: 29, 142: 29, 143: 29, 144: 29, 145: 29, 146: 30, 147: 30, 148: 30, 149: 30, 150: 30}

#What Is Dynamic Programming and How To Use It [vYquumk4nWw]
def fibonaccibottomupapproach(n):
    if n == 1 or n == 2:
        return 1
    bottomup = [None] * (n + 1)
    bottomup[1] = 1
    bottomup[2] = 1
    for i in range(3, n + 1):
        bottomup[i] = bottomup[i - 1] + bottomup[i - 2]
    return (bottomup, bottomup[n])


print(fibonaccibottomupapproach(5)) #print ([None, 1, 1, 2, 3, 5], 5)
print(fibonaccibottomupapproach(35)) #print ([None, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465], 9227465)
print(fibonaccibottomupapproach(100)) #print ([None, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, . . ., 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026, 354224848179261915075], 354224848179261915075)

#Dynamic Programming is not difficult [bPbuCAzzmUs]
#Given x stairs.  Each move going up one step or two steps.  Count the number of distinct ways to reach the top of the stairs.  For example, if there are three stairs, then the answer is 3:  1 step, 2 steps; 2 steps, 1 step; 1,1,1.
def reachtopofstairstopdown(n, memosteps=None):
    if memosteps is None:
        memosteps = {}
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memosteps:
        return memosteps[n]
    memosteps[n] = reachtopofstairstopdown(n - 1, memosteps) + reachtopofstairstopdown(n - 2, memosteps)
    return memosteps[n]


print(reachtopofstairstopdown(1)) #print 1
print(reachtopofstairstopdown(2)) #print 2
print(reachtopofstairstopdown(3)) #print 3
print(reachtopofstairstopdown(5)) #print 8

def reachtopofstairsbottomup(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    numberofways = [0] * (n + 1)
    numberofways[1] = 1
    numberofways[2] = 2
    for i in range(3, n + 1):
        numberofways[i] = numberofways[i - 1] + numberofways[i - 2]
    return numberofways[n]


print(reachtopofstairsbottomup(1)) #print 1
print(reachtopofstairsbottomup(2)) #print 2
print(reachtopofstairsbottomup(3)) #print 3
print(reachtopofstairsbottomup(5)) #print 8
