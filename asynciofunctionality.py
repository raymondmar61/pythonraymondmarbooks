#Generators Python Asyncio Functionality.pdf
#A normal function run it.  A value is returned.  Run the function returns a value.  Function finished executing.  If you run the function again, then you get a new stack frame.  Local variables are reset.  No memory of the previous run.
#Generator functions return a value via "yield" keyword each time the "next" function is run using a for loop.  The first time you invoke "next", you get everything until the first "yield".  The second time you invoke "next", you get everything until the second "yield".   The generator function raises StopIteration at the end.
def normalfunction():
    yield "yield 1"
    yield "yield 2"
    yield "yield 3"


for oneitem in normalfunction():
    print(oneitem) #print yield1\n yield2\n yield3.  When the "for" loop implicitly invokes "next", the function executes through the first"yield" statement. We get "yield 1" back from the generator, which then goes to sleep. Whenwe invoke "next" a second time -- again, implicitly via the "for" loop -- the function runsthrough the next "yield", returning "yield 2". And then again, it goes to sleep.
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