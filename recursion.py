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
