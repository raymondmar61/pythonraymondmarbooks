#Learn RECURSION in 5 minutes! [ivl5-snqul8]
'''
Recursion.  A function which calls itself from within.  It helps visualize a complex problem in basic steps which can be solved easier iteratively or recursively.  Iteratively is using a for loop or while loop.  Recursively is using if else or adding or subtracting the number of steps.

Recursively is calling the function itself from within; invoke the function from within.  Recursively needs a base condition to avoid a RecursionError.  We create a loop; we involve the function itself.  Invoke a function add a frame to the call stack.  There is a certain order to resolve functions.  It's a stacked data structure.  Start at the top and work down.  It's like a stack of CDs.  Add frames to the call stack.  Stop when the condition is met.  Then undo everything starting at the top going in reverse.  RM:  confusing

If there are too many frames on the call stack, then a maximum error RecursionError: maximum recursion depth exceeded while calling a Python object.  There is a limit to how many frames are on the call stack.  Recursive is slower.  Recursive can be more simple than iterative.  Recursive is good for data structures and algorithms.
'''
def iterativefunctionwalk(steps):
    for eachstep in range(1, steps + 1):
        print(f"You take step #{eachstep}")
def recursivefunctionwalk(steps):
    print(f"You take step #{steps}")
    recursivefunctionwalk(steps - 1) #invoked the function recursivefunctionwalk from within.  Create a loop with the function itself
def recursivefunctionwalkbasecondition(steps):
    print(f"I'm the first line:  You take step #{steps}")
    if steps == 0: #Base condition
        return
    recursivefunctionwalkbasecondition(steps - 1) #invoked the function recursivefunctionwalkbasecondition from within.  Create a loop with the function itself.
    print(f"You take step #{steps}")


iterativefunctionwalk(100)
#recursivefunctionwalk(100)
'''
You take step #-891
You take step #-892
You take step #-893
You take step #-894
You take step #-895
RecursionError: maximum recursion depth exceeded while calling a Python object.  RM:  when do we want to stop.
'''
recursivefunctionwalkbasecondition(100)
'''
I'm the first line:  You take step #100
I'm the first line:  You take step #99
I'm the first line:  You take step #98
I'm the first line:  You take step #97
...
I'm the first line:  You take step #3
I'm the first line:  You take step #2
I'm the first line:  You take step #1
I'm the first line:  You take step #0
You take step #1
You take step #2
You take step #3
You take step #4
You take step #5
You take step #6
...
You take step #97
You take step #98
You take step #99
You take step #100
'''
def factorialiterative(x):
    result = 1
    if x > 0:
        for y in range(1, x + 1):
            result = result * y
        return result
def factorialrecursive(x):
    if x == 1: #Base condition
        return 1
    else:
        print(f"Else statement x value is {x}.")
        return x * factorialrecursive(x - 1)


print(factorialiterative(10)) #print 3628800
print(factorialrecursive(10))
'''
Else statement x value is 10.
Else statement x value is 9.
Else statement x value is 8.
Else statement x value is 7.
Else statement x value is 6.
Else statement x value is 5.
Else statement x value is 4.
Else statement x value is 3.
Else statement x value is 2.
3628800
'''

#Python： RECURSION Explained [wMNrSM5RFMc]
'''
A recursive function breaks the problem to smaller problems.  It calls itself for each of the smaller problems.  There is a base case or terminal case and a recursive case.
Five factorial 5! is 120 = 5*4*3*2*1.  5! is also 5 * 4!.  4! is 4 * 3!.  3! is 3 * 2!.  2! is 2 * 1!.  1! is 1.
Pass the next number to call the function again to factorial.

Function calls:
getfactorial(5) is 5 * getfactorial(4)
getfactorial(4) is 4 * getfactorial(3)
getfactorial(3) is 3 * getfactorial(2)
getfactorial(2) is 2 * getfactorial(1)
getfactorial(1) is return 1

Then work you way back up
getfactorial(1) is return 1 1 GO TO GETFACTORIAL2
getfactorial(2) is 2 * getfactorial(1) 2 GO TO GETFACTORIAL3
getfactorial(3) is 3 * getfactorial(2) 6 GO TO GETFACTORIAL4
getfactorial(4) is 4 * getfactorial(3) 24 GO TO GETFACTORIAL5
getfactorial(5) is 5 * getfactorial(4) 120

First dig in the hole.  Work forwards or work downwards.  Stop digging in the hole when you reach the base case or terminal case.  Then dig out the hole starting from the last answer digging in the hole to the first answer digging in the hole.  Work backwards or work upwards.

A recursion negative is millions of recursive calls may run out of memory because of the million of open function calls.  Requires more memory.  Can be slower to calculate solution.  More abstract or harder to understand than iterative solutions.

A recursive positive is for tree traversals and binary search.
'''
def getfactorial(n):
    print("First sentence", n)
    if n < 2: #Base case or terminal case
        return 1
    else:
        print(f"Digging in the hole {n}")
        return n * getfactorial(n - 1)
        print("Do you see the sentence below the return n * getfactorial(n - 1)?")


print(getfactorial(5)) #print 120
'''
First sentence 5
Digging in the hole 5
First sentence 4
Digging in the hole 4
First sentence 3
Digging in the hole 3
First sentence 2
Digging in the hole 2
First sentence 1
120
'''

#40 Python Tutorial for Beginners ｜ Recursion [XkL3SUioNvo]
#Recursion is calling a function from itself.  Calling a function from the same function.
def samefunctioninfinitecalling():
    print("Hello.  I'm from the function samefunctioninfinitecalling().")
    samefunctioninfinitecalling() #Calling samefunctioninfinitecalling() itself.  Unfortunately, RecursionError: maximum recursion depth exceeded while calling a Python object.  YouTuber said call same function one thousand times by default.  Limit thousand times.  My error message said [Previous line repeated 992 more times].


#samefunctioninfinitecalling() #return Hello.  I'm from the function samefunctioninfinitecalling().
counter = 1
def samefunctioncounter():
    global counter #UnboundLocalError: local variable 'counter' referenced before assignment.
    print("Hello.  I'm from the function samefunctioncounter().  Counter", counter)
    counter += 1
    if counter == 100:
        return True
    samefunctioncounter() #Calling samefunctioncounter() itself.


samefunctioncounter() #return Hello.  I'm from the function samefunctioncounter().  Counter 1
#Change recursion limit
import sys
print(sys.getrecursionlimit()) #print 1000
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit()) #print 2000.  However, YouTuber ran a function which stopped at count 1,996.

#5 Simple Steps for Solving Any Recursive Problem [ngCos392W4w]
#Recursive Leap Of Faith is assuming simpler cases work out.
#Write a recursive function that given an input n sums all nonnegative integers up to n?
def sumiteration(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result


print(sumiteration(50)) #print 1275

def summathematical(n):
    return n * ((n + 1) / 2) #((n + 1) // 2) is incorrect


print(summathematical(50)) #print 1275

def sumrecursion(n):
    if n == 0:
        return 0
    else:
        return n + sumrecursion(n - 1)


print(sumrecursion(50)) #print 1275
print(sumrecursion(5)) #print 15
'''
sumrecursion(5):  5+sumrecursion(4).  Theoretically the answer is 15.  The function is not evaluated yet.  Go back and repeat the process.
sumrecursion(4):  4+sumrecursion(3).  Theoretically the answer is 10.  The function is not evaluated yet.  Go back and repeat the process.
sumrecursion(3):  3+sumrecursion(2).  Theoretically the answer is 6.  The function is not evaluated yet.  Go back and repeat the process.
sumrecursion(2):  2+sumrecursion(1).  Theoretically the answer is 3.  The function is not evaluated yet.  Go back and repeat the process.
sumrecursion(1):  1+sumrecursion(0).  Theoretically the answer is 1.  The function is not evaluated yet.  Go back and repeat the process.
sumrecursion(0):  0.  Base case if n == 0 return 0.  Evaluate the problem sumrecursion() function when n = 1, then n = 2, then n = 3, then n = 4, and then n = 5.
'''
#Write a function that takes two inputs n and m and outputs the number of unique paths from the top left corner to [the] bottom right corner of a nXm grid.  Constraints:  you can only move down or right 1 unit at a time.
def gridpaths(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return gridpaths(n, m - 1) + gridpaths(n - 1, m)
#Write a function that counts the number of ways you can partition n objects using parts up to m (assuming m >= 0).  For example, dots are objects.  Partition 6 dots up to 4 parts.  n=6.  m=4.  4+2; 4+1+1; 3+3; 3+2+1; 3+1+1+1; 2+2+2; 2+2+1+1; 2+1+1+1+1; 1+1+1+1+1+1.  9 partitions.  Partition 5 dots up to 5 parts.  n=5.  m=5.  5+0; 4+1; 3+2; 3+1+1; 2+2+1; 2+1+1+1; 1+1+1+1+1.  7 partitions.
#The simplest partition is n=0 and m=0.  There is 1 parition.  There is always 1 parition when n=0 and m>=0.  Another simplest parition is n>=1 and m=0.  There is 0 parition.
#Another base case is n<0.  There is 0 partition.
def countpartitions(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return countpartitions(n - m, m) + countpartitions(n, m - 1)


print(countpartitions(6, 4)) #print 9
print(countpartitions(5, 5)) #print 7
print(countpartitions(3, 2)) #print 2
print(countpartitions(0, 200)) #print 1
