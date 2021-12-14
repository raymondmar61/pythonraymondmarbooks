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
'''

#Python Await Async Keywords Asyncio.pdf
#Asyncio uses cooperative multitasking which means a task can't give up the CPU.  The task voluntarily gives up control.  A Python generator can voluntarily suspend itself, remembering its state, and where it should restart via the "yield" statement.  In the past, we use regular generator functions and "yield" statement to indicate a task was ready to hand control to another task.
#Today, we use the "await" statement.  Python lets another task runs in its place on an event loop when Python encounters the "await" statement.  For instance, a task waits for data.  While waiting, another tasks is run.  When the event loop reteurns to our task and the network provided the data requested, then Python continues the task.
#It's asyncio.  Working with any I/O means waiting for the hardware to provide the data requested.  We take advantage of the wait periods by having tasks suspend themselves every time they ask for I/O.  Python's threads do something similar.
#We use "await" to get I/O and to give up control of the CPU.  You can't use "await" inside a normal Python function because it expects to be run directly.  In contrast, tasks are run indirectly via the asyncio event loop.  An asyncio tasks function is defined with async def instead of def.
#SUMMARY SO FAR:  Asyncio don't run functions themselves; rather, asyncio functions are defined async def.  An async function can be turned into a task attached to the event loop.  Async functions can't be run on its own; rather it can only run in the event loop.  A task indicates it gives up the CPU in favor of another task with "await".  Use "await" to indicate we wait for something which takes time, typically I/O.

#Event Loop Python Asyncio.pdf
#Create an event loop
import asyncio
loop = asyncio.get_event_loop() #get_event_loop() function returns an event loop.  Precisely, get_event_loop() function returns the event loop.  A singleton is a single asyncio event loop.  You can invoke get_event_loop() infinitely which always get the same result back.
loop.run_forever() #start the event loop using method run_forever().  However, we didn't indicate when the loop stops.  The loop runs forever.  Also, we didn't add any coroutines.
#An event loop invokes each coroutines in order giving each a chance to use the CPU and other system resources.  Write a coroutine using async def instead of def.
async def hello():
    print("Hello")
    loop.stop()
hello() #invoke async def hello
loop = asyncio.get_event_loop() #get_event_loop() function returns an event loop.
loop.create_task(hello())
loop.run_forever() #start the event loop using method run_forever().  The program hangs.  Kill it with control-C.  The event loop continued to run forever.  We tell it to run_forever.  Type loop.stop() to end after our function runs.
'''
#code when there's no loop.stop() or there's loop.stop()
yywork.py:9: RuntimeWarning: coroutine 'hello' was never awaited
  hello() #invoke async def hello
Hello
'''
async def hello_norun_forever():
    print("Hello no run_forever")
    loopnorun_forever.stop()
hello_norun_forever() #invoke async def hello_norun_forever
loopnorun_forever = asyncio.get_event_loop() #get_event_loop() function returns an event loop.
loopnorun_forever.create_task(hello_norun_forever())
'''
yywork.py:23: RuntimeWarning: coroutine 'hello_norun_forever' was never awaited
  hello_norun_forever() #invoke async def hello_norun_forever
'''

#Python Multiple Tasks With Asyncio Event Loop.pdf
#Asyncio event loop more than one task
import asyncio
async def hello():
    print("Hello")
    loop.stop()
async def goodbye():
    print("Goodbye")
    loop.stop()
loop = asyncio.get_event_loop()
loop.create_task(hello())
loop.create_task(goodbye())
loop.run_forever()
#Each async function is doing only one thing
'''
Hello
Goodbye
'''
#Each task prints more than once.  One function only.  Define async function greetword.  Get our [event] loop.  Create two tasks based on the greet function.
async def greetword(word):
    for i in range(5):
        print(word)
    loopword.stop()
loopword = asyncio.get_event_loop()
loopword.create_task(greetword("Hello"))
loopword.create_task(greetword("Goodbye"))
loopword.run_forever()
'''
Hello
Hello
Hello
Hello
Hello
Goodbye
Goodbye
Goodbye
Goodbye
Goodbye
'''
#No concurrency at all. Rather, we ran the entire "hello" task.  When it completes,  we ran the entire "goodbye" task.  The whole point of using asyncio is that it lets us run tasks concurrently.  What's wrong?
#Asyncio uses a system known as "cooperative multitasking." This means that tasks need to explicitly give up control of the CPU.  Since our tasks didn't have such an explicit statement that they'll give up control, they didn't.
#So far, we've used the "async" keyword to define functions that can be turned into tasks.  Functions are attached to the event loop. The other keyword is "await".  "Await" inside an async function, used only in such a function, tell Python you ask for a value from a source that might take a while to respond, and that's fine to pass control onto another task.
#In other words, "await" calls an "awaitable" to gather data from a slow source such as a file system, network, or the like.  And "await" forces the task to give up control.
#There are a few "awaitables."  The simplest and lease useful in practice is asyncio.sleep which indicates Python move to the next task.
async def greetwithsleep(word):
    for i in range(5):
        await asyncio.sleep(1)
        print(word)
        loopsleep.stop()
loopsleep = asyncio.get_event_loop()
loopsleep.create_task(greetwithsleep("Hello with sleep"))
loopsleep.create_task(greetwithsleep("Goodbye with sleep"))
loopsleep.run_forever()
'''
Hello with sleep
Goodbye with sleep
'''

#Python Async Function Future.pdf
import asyncio
#Create an async function greetwithsleep run by the event loop.  We invoke the function putting the reuslt of its invocation on the loop as a task and tell the loop to run forever; however, loopsleep.stop() stops after every task has indicated it's ready to happen.  The code is ugly.  We started an infinite loop and stop multiple times within the tasks on the loop.
async def greetwithsleep(word):
    for i in range(5):
        await asyncio.sleep(1)
        print(word)
        loopsleep.stop()
loopsleep = asyncio.get_event_loop()
loopsleep.create_task(greetwithsleep("Hello with sleep"))
loopsleep.create_task(greetwithsleep("Goodbye with sleep"))
loopsleep.run_forever()
#Instead of starting the loop with run_forever, we tell the loop to run until all tasks have completed.  We use loop.run_until_complete(group).  Group is the result from running asyncio.gather which is a function which comes from asyncio which takes one or more tasks and turns them into a future.  We pass the resulting future object to run_until_complete.
#Run an async function we get back a coroutine object which can be turned into a task on our event loop with asyncio.create_task.  The task is a type of futur object saying "I promise to come back in the future with a result."  Initially, it doesn't have a result.  It's like a boomerang.  Throw it, some time passes, and it returns with results.  You can be doing other things while the boomerang is out flying.
#Tasks are futures.  We can create a new future with the asyncio.gather function which takes any number of futures and combines them into a single future  For example,
'''
tasksvariable=asyncio.Task.all_tasks(loop=loop) #Return all tasksvariable currently on the event loop.
groupvariable = asyncio.gather(*tasksvariable) #Pass all the tasksvariable to turn the set into a bunch of separate arguments to asyncio.gather.  It returns a new future named groupvariable.  groupvariable is a future which represents many other tasks and futures.
loop.run_until_complete(groupvariable) #Run the function.  Tells asyncio event loop to run forever and stop when all of the futures or all of the tasks finished and exited.  No need for loop.stop().
'''
async def hellotasksgroups():
    for i in range(5):
        print(f"[{i}] Hello tasks groups")
        await asyncio.sleep(1.0)
async def goodbyetasksgroups():
    for i in range(5):
        print(f"[{i}] Goodbye tasks groups")
        await asyncio.sleep(1.0)
looptasksgroups = asyncio.get_event_loop()
looptasksgroups.create_task(hellotasksgroups())
looptasksgroups.create_task(goodbyetasksgroups())
tasksvariable = asyncio.Task.all_tasks(loop=looptasksgroups)
groupvariable = asyncio.gather(*tasksvariable)
looptasksgroups.run_until_complete(groupvariable)
'''
[0] Hello tasks groups
[0] Goodbye tasks groups
[1] Hello tasks groups
[1] Goodbye tasks groups
[2] Hello tasks groups
[2] Goodbye tasks groups
[3] Hello tasks groups
[3] Goodbye tasks groups
[4] Hello tasks groups
[4] Goodbye tasks groups
'''

#Web Scrape Web Scraping Asyncio Part 1 Python.pdf
import asyncio
#We start an event loop, add tasks to the loop, and tell the loop to finish once all the tasks are done.
async def greet(sentence):
    for i in range(5):
        await asyncio.sleep(1.0)
        print(sentence)
loopsentence = asyncio.get_event_loop()
loopsentence.create_task(greet("Hello sentence"))
loopsentence.create_task(greet("Goodbye sentence"))
taskssentence = asyncio.Task.all_tasks(loop=loopsentence)
groupsentence = asyncio.gather(*taskssentence)
loopsentence.run_until_complete(groupsentence)
'''
Hello sentence
Goodbye sentence
Hello sentence
Goodbye sentence
Hello sentence
Goodbye sentence
Hello sentence
Goodbye sentence
Hello sentence
Goodbye sentence
'''
#The idea is each task works on some task broken into pieces, and each piece means waiting an unknown amount of time to get a response.  Asyncio is designed breaking tasks into pieces.  It's not an alternative to threads or processes.
#For example, go to a website to extract the length of the retrieved content or website.  Store the length in a dictionary.
#measureurlcontent is the asynchronous function which takes the URL, retrieves the content, counts the length, and saves to sizes dictionary.  We create a new task with each URL.  The example below Asyncio took too long time wise.  The reason is measureurlcontent was asynchronous in name only.  The idea of an async def is the function runs for a little bit and gives up control in favor of another task saying, "I'm about to do something which might take a long time" using the await keyword.  There is no potential sync benefit without the await keyword.
#What if we replace content = requests.get(oneurl).content with content = await requests.get(one_url).content?  It doesn't work because await works when something becomes awaitable such as another asyncio task or an object designed to work with asyncio.  import requests is not awaitable.
import time
import requests
import asyncio
urls = ['https://nytimes.com', 'https://washingtonpost.com', 'https://python.org', 'https://us.pycon.org']
sizes = {}
async def measureurlcontent(oneurl):
    print(oneurl)
    content = requests.get(oneurl).content
    sizes[oneurl] = len(content)
loopurls = asyncio.get_event_loop()
starttime = time.time()
for eachurls in urls:
    loopurls.create_task(measureurlcontent(eachurls))
tasks = asyncio.Task.all_tasks(loop=loopurls)
group = asyncio.gather(*tasks)
loopurls.run_until_complete(group)
totaltime = time.time() - starttime
print(sizes)
print(f"It took {totaltime} seconds.")
'''
https://nytimes.com
https://washingtonpost.com
https://python.org
https://us.pycon.org
{'https://nytimes.com': 1804910, 'https://washingtonpost.com': 1080202, 'https://python.org': 49777, 'https://us.pycon.org': 17526}
It took 11.457214593887329 seconds.
'''

#Web Scraping Asyncio Part 2 Python.pdf
import asyncio
#The measureurlcontent didn't use asynchronous execution ecause asyncio uses cooperative multitasking or an async function can give up control of the CPU.  An async function gives up control with the await keyword.  The await keyword tells Python it's going to take time to get a response back from the thing to its right.  Python might as well give control to the next async def on the event loop.  The thing we awaited returns an answer by the time we return to our async function.
#The problem is import requests isn't awaitable.  You can't await anything in Python.  You can await something that has been defined to run within the context of an async def.
import time
import requests
import asyncio
urls = ['https://nytimes.com', 'https://washingtonpost.com', 'https://python.org', 'https://us.pycon.org']
sizes = {}
async def measureurlcontent(oneurl):
    print(oneurl)
    content = requests.get(oneurl).content
    sizes[oneurl] = len(content)
loopurls = asyncio.get_event_loop()
starttime = time.time()
for eachurls in urls:
    loopurls.create_task(measureurlcontent(eachurls))
tasks = asyncio.Task.all_tasks(loop=loopurls)
group = asyncio.gather(*tasks)
loopurls.run_until_complete(group)
totaltime = time.time() - starttime
print(sizes)
print(f"It took {totaltime} seconds.")
'''
https://nytimes.com
https://washingtonpost.com
https://python.org
https://us.pycon.org
{'https://nytimes.com': 1804910, 'https://washingtonpost.com': 1080202, 'https://python.org': 49777, 'https://us.pycon.org': 17526}
It took 11.457214593887329 seconds.
'''
#What makes something awaitable?  The answer is it needs to implement the __await__ method which returns an iteraetor when called.  The awaitable can provide one piece of data at a time rather than all at once which allows us to switch from one async def to another to give us the concurrency that asyncio promises.
#The solution of import requests doesn't implement await is use another library called aiohttp.  RM:  I stopped the tutorial.