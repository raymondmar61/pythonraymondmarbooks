#Advanced Guide To Python 3 Programming by John Hunt Chapter 34 Concurrency With AsyncIO
#Asynchronous IO or Async IO is a language agnostic concurrent programming model or paradigm.  You build concurrent applications.  An alternative to the Threading library.  Async IO runs with a singular process instead of separate processes.  An alternate way of implementing concurrent solutions to problems.  It's not built on either Treading or Multi Processing.  Async IO is cooperative multitasking.  It operates separately from other tasks, wait for another task to return a result when required, and allow other tasks to run while they're waiting.  Async IO is best for Input and Output bound tasks.  Specifically, in an I/O bound task, a program spends most of its time sending data to, or reading data from, some form of external device.  The communication is time consuming and means the program spends most of its time waiting for a response from the external device.  I/O bound applications can speed up is to overlap the execution of differente tasks.  While one task is waiting for a database to respond with some data, another task can be writing data to a log file.
import asyncio
import time

async def workerfunction(timernumber3):
    print("workerfunction start.  timenumber3 is", timernumber3)
    time.sleep(timernumber3)
    print("workerfunction done")
    return 42

async def dosomethingfunction(timernumber2): #Run a separate Task.  Use keyword await to wait for another function or behaviour to complete.  dosomethingfunction must wait for workerfunction to complete.
    print("dosomethingfunction start. Waits for workerfunction")
    result = await workerfunction(timernumber2) #The await keyword indicates dosomething function must wait for the workerfunction to complete.  It trigers another task to be created to execute workerfunction function and releases the processor allowing the Event Loop to select the next task to execute.  The status of the dosomething task waits while the status of the workerfunction task is ready to run.
    print("dosomethingfunction done.  Result is here", result)

def mainsimpleasyncio(timernumber1): #The mainsimpleasyncio() function is the entry point for the program and calls asyncio.run(dosomethingfunction())
    print("mainsimpleasyncio() function start")
    asyncio.run(dosomethingfunction(timernumber1))
    print("mainsimpleasyncio() function done")


mainsimpleasyncio(3)
'''
mainsimpleasyncio() function start
dosomethingfunction start. Waits for workerfunction
workerfunction start.  timenumber3 is 3
workerfunction done
dosomethingfunction done.  Result is here 42
mainsimpleasyncio() function done
'''
print("\n")
mainsimpleasyncio(1)
mainsimpleasyncio(2)
'''
mainsimpleasyncio() function start
dosomethingfunction start. Waits for workerfunction
workerfunction start.  timenumber3 is 1
workerfunction done
dosomethingfunction done.  Result is here 42
mainsimpleasyncio() function done
mainsimpleasyncio() function start
dosomethingfunction start. Waits for workerfunction
workerfunction start.  timenumber3 is 2
workerfunction done
dosomethingfunction done.  Result is here 42
mainsimpleasyncio() function done
'''
import asyncio
async def workerfunction(number):
    print(number, "workerfunction start")
    await asyncio.sleep(1)
    print(number, "workerfunction end")
    return 43
def printitfunction(task):
    print("printitfunction start.  Result:", task.result())
async def dosomethingfunction(number):
    print(number, "dosomethingfunction start.  Create a task for workerfunction.")
    task = asyncio.create_task(workerfunction(number))
    print(number, "dosomethingfunction.  Add a callback.")
    task.add_done_callback(printitfunction)
    await task
    #Information on task
    print(number, "dosomethingfunction information on task.  task.cancelled():", task.cancelled())
    print(number, "dosomethingfunction information on task.  task.done():", task.done())
    print(number, "dosomethingfunction information on task.  task.result():", task.result())
    print(number, "dosomethingfunction information on task.  task.exception():", task.exception())
    print(number, "dosomethingfunction end")
def mainfunction(number):
    print(number, "mainfunction start")
    asyncio.run(dosomethingfunction(number))
    print(number, "mainfunction end")


mainfunction(1)
'''
1 mainfunction start
1 dosomethingfunction start.  Create a task for workerfunction.
1 dosomethingfunction.  Add a callback.
1 workerfunction start
1 workerfunction end
printitfunction start.  Result: 43
1 dosomethingfunction information on task.  task.cancelled(): False
1 dosomethingfunction information on task.  task.done(): True
1 dosomethingfunction information on task.  task.result(): 43
1 dosomethingfunction information on task.  task.exception(): None
1 dosomethingfunction end
1 mainfunction end
'''
import random
async def workerfunction():
    print("workerfunction start")
    await asyncio.sleep(1)
    result = random.randint(1, 10)
    print("workerfunction end.  return the result random integer between 1 and 10")
    return result
async def dosomethingfunction():
    print("dosomethingfunction start")
    resultsthreecallsconcurrently = await asyncio.gather(workerfunction(), workerfunction(), workerfunction()) #run three invocations of the workerfunction() in three separate Tasks.  Wait for the results of all three before the three Tasks are returned as a list of values stored in resultsthreecallsconcurrently variable.
    print("print the resultsthreecallsconcurrently list:", resultsthreecallsconcurrently)
def mainfunctionmultipletasks():
    print("mainfunctionmultipletasks start")
    asyncio.run(dosomethingfunction())
    print("mainfunctionmultipletasks end")


mainfunctionmultipletasks()
'''
mainfunctionmultipletasks start
dosomethingfunction start
workerfunction start
workerfunction start
workerfunction start
workerfunction end.  return the result random integer between 1 and 10
workerfunction end.  return the result random integer between 1 and 10
workerfunction end.  return the result random integer between 1 and 10
print the resultsthreecallsconcurrently list: [9, 2, 1]
mainfunctionmultipletasks end
'''
#The three workerfunction invocations resultsthreecallsconcurrently = await asyncio.gather(workerfunction(), workerfunction(), workerfunction()) are started and then release the processor when sleeping.  After the sleep, the three tasks wake up and complete before the results are collected together and printed out.
#Use the asyncio.as_completed() for multiple Tasks handling the results are they become available instead of waiting for all the results to be provided before continuing.  asyncio.as_completed() returns an interator of async functions serving up as soon as the async functions completed their work.
async def dosomethingfunction():
    print("dosomethingfunction start.  Wait for workerfunction.  Run three calls to workerfunction concurrently and collect results.")
    for asyncfunction in asyncio.as_completed((workerfunction("A"), workerfunction("B"), workerfunction("C"))): #asyncio.as_completed takes a container such as a tuple of async functions
        result = await asyncfunction
        print("dosomethingfunction result:", result)
async def workerfunction(label):
    print("workerfunction start.  Wait one second.")
    await asyncio.sleep(1)
    result = random.randint(1, 10)
    print("workerfunction end.")
    return label + str(result)
def mainfunctionhandleresultsavailablenow():
    print("mainfunctionhandleresultsavailablenow start")
    asyncio.run(dosomethingfunction())
    print("mainfunctionhandleresultsavailablenow end")


mainfunctionhandleresultsavailablenow()
'''
mainfunctionhandleresultsavailablenow start
dosomethingfunction start.  Wait for workerfunction.  Run three calls to workerfunction concurrently and collect results.
workerfunction start.  Wait one second.
workerfunction start.  Wait one second.
workerfunction start.  Wait one second.
workerfunction end.
workerfunction end.
workerfunction end.
dosomethingfunction result: C2
dosomethingfunction result: A4
dosomethingfunction result: B5
mainfunctionhandleresultsavailablenow end
'''
