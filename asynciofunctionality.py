#Generators Python Asyncio Functionality.pdf
#A normal function run it.  A value is returned.  Run the function returns a value.  Function finished executing.  If you run the function again, then you get a new stack frame.  Local variables are reset.  No memory of the previous run.
#Generator functions return a value via "yield" keyword each time the "next" function is run using a for loop.  The first time you invoke "next", you get everything until the first "yield".  The second time you invoke "next", you get everything until the second "yield".   The generator function raises StopIteration at the end.
def normalfunction():
    yield "yield 1"
    yield "yield 2"
    yield "yield 3"


for oneitem in normalfunction():
    print(oneitem) #print yield1\n yield2\n yield3.  When the "for" loop implicitly invokes "next", the function executes through the first "yield" statement. We get "yield 1" back from the generator, which then goes to sleep. When we invoke "next" a second time -- again, implicitly via the "for" loop -- the function runs through the next "yield", returning "yield 2". And then again, it goes to sleep.
allgenerators = [normalfunction(), normalfunction(), normalfunction(), normalfunction()]
waitingfor = len(allgenerators)
print(waitingfor) #print 4
while allgenerators:
    for onegenerateor in list(allgenerators):
        print(onegenerateor)
        try:
            print(next(onegenerateor))
        except StopIteration:
            print("StopIteration")
            allgenerators.remove(onegenerateor)
'''
#RM:  Double click a generator object ID.  Notice it goes through yield 1, yield 2, yield 3, and StopIteration.
<generator object normalfunction at 0x7fe031986360>
yield 1
<generator object normalfunction at 0x7fe0303609e8>
yield 1
<generator object normalfunction at 0x7fe030360a40>
yield 1
<generator object normalfunction at 0x7fe030360a98>
yield 1
<generator object normalfunction at 0x7fe031986360>
yield 2
<generator object normalfunction at 0x7fe0303609e8>
yield 2
<generator object normalfunction at 0x7fe030360a40>
yield 2
<generator object normalfunction at 0x7fe030360a98>
yield 2
<generator object normalfunction at 0x7fe031986360>
yield 3
<generator object normalfunction at 0x7fe0303609e8>
yield 3
<generator object normalfunction at 0x7fe030360a40>
yield 3
<generator object normalfunction at 0x7fe030360a98>
yield 3
<generator object normalfunction at 0x7fe031986360>
StopIteration
<generator object normalfunction at 0x7fe0303609e8>
StopIteration
<generator object normalfunction at 0x7fe030360a40>
StopIteration
<generator object normalfunction at 0x7fe030360a98>
StopIteration
'''
#Invoke normalfunction() four times.  Each time I get a separate generator object.  allgenerators contains four generator objects.  Each know how to respond to the "next" function via a "for" loop.  If we get to the end, we trap the StopIteration exception.  We "remove" the current generator.  We stop the "while" loop when the list is empty.

#Python Generator Functions Coroutines.pdf
#Generator functions return generators or iterable objects.  A generator function in a for loop is executed as written.  It stops at a yield statement.  The generator sleeps while keeping its state.  When the function restarts because of the next iteration, the generator function resumes and executes.  The "yield" pauses the function's execution at a point.

def fibonaccigeneratorfunction():
    firstnumber = 0
    secondnumber = 1
    while True:
        print("yield %d" % (firstnumber))
        yield firstnumber
        print("firstnumber %d, secondnumber %d" % (firstnumber, secondnumber))
        firstnumber, secondnumber = secondnumber, firstnumber + secondnumber
        if firstnumber > 10000:
            break


for i in fibonaccigeneratorfunction():
    print("for loop i:", i)
    '''
    yield 0
    for loop i: 0
    firstnumber 0, secondnumber 1
    yield 1
    for loop i: 1
    firstnumber 1, secondnumber 1
    yield 1
    for loop i: 1
    firstnumber 1, secondnumber 2
    yield 2
    for loop i: 2
    firstnumber 2, secondnumber 3
    yield 3
    for loop i: 3
    firstnumber 3, secondnumber 5
    yield 5
    for loop i: 5
    firstnumber 5, secondnumber 8
    yield 8
    for loop i: 8
    firstnumber 8, secondnumber 13
    yield 13
    for loop i: 13
    firstnumber 13, secondnumber 21
    yield 21
    for loop i: 21
    firstnumber 21, secondnumber 34
    yield 34
    for loop i: 34
    firstnumber 34, secondnumber 55
    yield 55
    for loop i: 55
    firstnumber 55, secondnumber 89
    yield 89
    for loop i: 89
    firstnumber 89, secondnumber 144
    yield 144
    for loop i: 144
    firstnumber 144, secondnumber 233
    yield 233
    for loop i: 233
    firstnumber 233, secondnumber 377
    yield 377
    for loop i: 377
    firstnumber 377, secondnumber 610
    yield 610
    for loop i: 610
    firstnumber 610, secondnumber 987
    yield 987
    for loop i: 987
    firstnumber 987, secondnumber 1597
    yield 1597
    for loop i: 1597
    firstnumber 1597, secondnumber 2584
    yield 2584
    for loop i: 2584
    firstnumber 2584, secondnumber 4181
    yield 4181
    for loop i: 4181
    firstnumber 4181, secondnumber 6765
    yield 6765
    for loop i: 6765
    firstnumber 6765, secondnumber 10946
    '''

def fibonaccigeneratorfunctionforloop():
    firstnumber = 0
    secondnumber = 1
    for i in range(20):
        yield firstnumber
        firstnumber, secondnumber = secondnumber, firstnumber + secondnumber

def communication():
    x = 100
    while True:
        print(f"At the top of loop, x={x}")
        x = yield x
        print(f"Just got {x} from yield")
        x = x * 5


generatorg = communication()
next(generatorg) #return At the top of loop, x=100.  start the generator.  RM:  I think it's the first line in communcation() function x = 100.
#The generatorg generator is paused.  It's waiting for another value.  I provide a value sending number seven to it.
generatorg.send(7) #return Just got 7 from yield\n At the top of loop, x=35
#The generatorg generator stopped when it reaches the "yield".  Anything we send to generatorg becomes the right-side of the assignment.
generatorg.send(9) #return Just got 9 from yield\n At the top of loop, x=45
'''
If I had a bunch of coroutines, each retrieve data from the stock market, via the Internet. It might make sense, after we have made a request, for the function to go to sleep, waking up later on to check if there's an answer waiting.
You could further imagine a loop of such coroutines, with a Python program going through each of them in turn, re-awakening each coroutine and checking if it got anything from the network. If so, then great. And if not, then we can put this coroutine back to sleep, and try someone else.
If you read asyncio, then you know that we no longer explicitly use generators and coroutines. And yet, the functionality is still tied to this sort of idea. And while the modern syntax hides some of this from us, the fact is that a loop is still there, going to sleep is st

#Python Await Async Keywords Asyncio.pdf
#Asyncio uses cooperative multitasking which means a task can't give up the CPU.  The task voluntarily gives up control.  A Python generator can voluntarily suspend itself,remembering its state, and where it should restart via the "yield" statement.  In the past, we use regular generator functions and "yield" statement to indicate a task was ready to hand control to another task.
#Today, we use the "await" statement.  Python lets another task runs in its place on an event loop when Python encounters the "await" statement.  For instance, a task waits for data.  While waiting, another tasks is run.  When the event loop reteurns to our task and the network provided the data requested, then Python continues the task.
#It's asyncio.  Working with any I/O means waiting for the hardware to provide the data requested.  We take advantage of the wait periods by having tasks suspend themselves every time they ask for I/O.  Python's threads do something similar.
#We use "await" to get I/O and to give up control of the CPU.  You can't use "await" inside a normal Python function because it expects to be run directly.  In contrast, tasks are run indirectly via the asyncio event loop.  An asyncio tasks function is defined with async def instead of def.
#SUMMARY SO FAR:  Asyncio don't run functions themselves; rather, asyncio functions are defined async def.  An async function can be turned into a task attached to the event loop.  Async functions can't be run on its own; rather it can only run in the event loop.  A task indicates it gives up the CPU in favor of another task with "await".  Use "await" to indicate we wait for something which takes time, typically I/O.