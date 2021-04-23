#Reuven Lerner lerner.co.il Python Threading Multiprocessing.pdf
#Python's Global Interpreter Lock (GIL) ensures only one thread runs at a time.  Sometimes process can be better.  Processes are easier to deal with than threads because processes don't share data, safer, and less likely to corrupt things.  Processes don't worry about deadlocks, mutexes, and semaphores, making writing process-based programs far easier to understand and debut, and are more predictable.
#There are objections to using processes.  Processes are larger than threads consuming more resources and more overhead.  Processes are independent for program stability.  Processes are not good if you want to let different pieces communicate.  For example, someone presses a button on GUI to send a message in the background to update a text box.  With threads, one thread handles the request and display in the background.  The other thread shows the GUI in the background.  With processes, its harder for which the background or calculating process doesn't have access to the GUI.
#Python's subprocess module allows us to work with external processes.  The module is used to launch external programs in separate processes.  Run code in a separate process.  We use the multiprocessing module.  Multiprocessing looks and feels like threads which actually uses processes.  Multiprocessing let you share data in controlled and specified ways.  If your programs are CPU-bound or need parallelism and independence of processes, use multiprocessing.
#This program demonstrates the double-edged sword of shared data within threads: The global "mylist" variable is shared by all of the threads, meaning that when we invoke"mylist.append" from within a thread, each of the threads is actually modifying the same list.
import threading
mylist = [10, 20, 30]
def addonethreading(x):
    mylist.append(x)
    print(mylist)
    '''
    [10, 20, 30, 0]
    [10, 20, 30, 0, 1]
    [10, 20, 30, 0, 1, 2]
    [10, 20, 30, 0, 1, 2, 3]
    [10, 20, 30, 0, 1, 2, 3, 4]
    '''


threadslist = []
for i in range(5):
    threadingvariable = threading.Thread(target=addonethreading, args=(i,))
    threadslist.append(threadingvariable)
    threadingvariable.start()
for eachthreadslist in threadslist:  #RM:  the threadslist for loop doesn't affect the mylist result
    print("eachthreadslist", eachthreadslist)
    '''
    eachthreadslist <Thread(Thread-1, stopped 140112488040192)>
    eachthreadslist <Thread(Thread-2, stopped 140112477452032)>
    eachthreadslist <Thread(Thread-3, stopped 140112477452032)>
    eachthreadslist <Thread(Thread-4, stopped 140112477452032)>
    eachthreadslist <Thread(Thread-5, stopped 140112477452032)>
    '''
    threadingvariable.join()
print(threadingvariable) #print <Thread(Thread-5, stopped 140112477452032)>
print(mylist) #print [10, 20, 30, 0, 1, 2, 3, 4]

#Use multiprocessing. The global variable "mylist" didn't change.  The function addonemultiprocessing is running in separate processes. Each process is modifying its own copy of "mylist", but none is modifying the copy of "mylist" in our original process.  I added the print("In add_one({0}), mylist is {1}".format(x, mylist)) code in the addonemultiprocessing function to demonstrate separate processes.
import multiprocessing
mylist = [10, 20, 30]
def addonemultiprocessing(x):
    mylist.append(x)
    print("In addonemultiprocessing function({0}), mylist is {1}".format(x, mylist))
    '''
    In addonemultiprocessing function(0), mylist is [10, 20, 30, 0]
    In addonemultiprocessing function(1), mylist is [10, 20, 30, 1]
    In addonemultiprocessing function(2), mylist is [10, 20, 30, 2]
    In addonemultiprocessing function(4), mylist is [10, 20, 30, 4]
    In addonemultiprocessing function(3), mylist is [10, 20, 30, 3]
    '''


multiprocessinglist = []
for i in range(5):
    multiprocessingvariable = multiprocessing.Process(target=addonemultiprocessing, args=(i,))
    multiprocessinglist.append(multiprocessingvariable)
    multiprocessingvariable.start()
for eachthreadslist in multiprocessinglist:  #RM:  the multiprocessinglist for loop doesn't affect the mylist result
    print("eachthreadslist", eachthreadslist)
    multiprocessingvariable.join()
'''
In addonemultiprocessing function(0), mylist is [10, 20, 30, 0]
In addonemultiprocessing function(1), mylist is [10, 20, 30, 1]
In addonemultiprocessing function(2), mylist is [10, 20, 30, 2]
eachthreadslist <Process(Process-1, stopped)>
In addonemultiprocessing function(4), mylist is [10, 20, 30, 4]
In addonemultiprocessing function(3), mylist is [10, 20, 30, 3]
eachthreadslist <Process(Process-2, stopped)>
eachthreadslist <Process(Process-3, stopped)>
eachthreadslist <Process(Process-4, started)>
eachthreadslist <Process(Process-5, stopped)>
'''
print(multiprocessinglist) #print [<Process(Process-1, stopped)>, <Process(Process-2, stopped)>, <Process(Process-3, stopped)>, <Process(Process-4, stopped)>, <Process(Process-5, stopped)>]
print(mylist) #print [10, 20, 30]

#Python Sharing Data Across Processes Multiprocessing.pdf

#Multiprocessing gives us an interface which looks and feels we're using threads even though we're using processes.  Multiprocessing removes the issues of thread safety and frees us from the constraints of the Global Interpreter Lock (GIL).  The variables are running in their own containers.  The containers don't affect other processes.
#How can processes contribute to the creation of a larger data structure or a more complex calculation like threads contributing to the creation of a larger data structure or a more complext calculation?
def sumthenumbers(numbers):
    total = 0
    for eachnumber in numbers:
        total += eachnumber
    return total


for i in range(10):
    print(i, sumthenumbers(range(i)), list(range(i)))
    '''
    0 0 []
    1 0 [0]
    2 1 [0, 1]
    3 3 [0, 1, 2]
    4 6 [0, 1, 2, 3]
    5 10 [0, 1, 2, 3, 4]
    6 15 [0, 1, 2, 3, 4, 5]
    7 21 [0, 1, 2, 3, 4, 5, 6]
    8 28 [0, 1, 2, 3, 4, 5, 6, 7]
    9 36 [0, 1, 2, 3, 4, 5, 6, 7, 8]
    '''

#I want to run each function in its own process.
import multiprocessing
for i in range(10):
    print(i, multiprocessing.Process(target=sumthenumbers, args=(range(i),)).start(), list(range(i))) #we're creating a new instance of multiprocessing.Process, telling it that we want to run "sumthenumbers" and giving it the appropriate argument to do so. We then take that new instance of multiprocessing.Process and invoke the "start" method on it, so that it runs.
    '''
    0 None []
    1 None [0]
    2 None [0, 1]
    3 None [0, 1, 2]
    4 None [0, 1, 2, 3]
    5 None [0, 1, 2, 3, 4]
    6 None [0, 1, 2, 3, 4, 5]
    7 None [0, 1, 2, 3, 4, 5, 6]
    8 None [0, 1, 2, 3, 4, 5, 6, 7]
    9 None [0, 1, 2, 3, 4, 5, 6, 7, 8]
    '''

import multiprocessing
from multiprocessing import Queue
q = Queue()
def mysumqueue(i, numbers):
    total = 0
    for eachnumber in numbers:
        total += eachnumber
    q.put((i, total)) #Instead of returning the total, we'll now put a two-element tuple on the "q" queue. We can "put" any object we want (within reason) on that queue, and it'll wait until someone retrieves it.  However, we don't want to retrieve the values right after creating all of those processes. That's because it takes time (if only a bit) for each process to calculate and then return its values. So we first put all of the processes in a list named processeslist, and then iterate over that list for loop processeslist, guaranteeing that each of the subprocesses has finished.


processeslist = []
for i in range(10):
    print(list(range(i)))
    '''
    []
    [0]
    [0, 1]
    [0, 1, 2]
    [0, 1, 2, 3]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4, 5]
    [0, 1, 2, 3, 4, 5, 6]
    [0, 1, 2, 3, 4, 5, 6, 7]
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    '''
    p = multiprocessing.Process(target=mysumqueue, args=(i, range(i)),)
    processeslist.append(p)
    p.start()
for eachprocesseslist in processeslist:
    p.join()
while not q.empty():  #The while loop retrieves and prints each tuple from mysumqueue function
    print(q.get())
    '''
    (0, 0)
    (1, 0)
    (3, 3)
    (2, 1)
    (5, 10)
    (6, 15)
    (4, 6)
    (7, 21)
    (9, 36)
    (8, 28)
    '''

#Python Locking With Multiprocessing.pdf

#Locks allow us the different processes to use only one resource.
#The function is running with a new process
import multiprocessing
import time
import random

def writethreeletters(filename, i):
    print("Writing to {} with i= {}".format(filename, i))
    with open(filename, "a") as fileobject:
        for word in "abc def ghi jkl mno".split():
            time.sleep(random.randint(1, 3))
            fileobject.write("{}: {}\n".format(i, word))
            fileobject.flush()


for i in range(5):
    print(i)
    multiprocessing.Process(target=writethreeletters, args=("tempwritethreeletters.txt", i)).start()
'''
0
1
2
Writing to tempwritethreeletters.txt with i= 0
3
Writing to tempwritethreeletters.txt with i= 1
4
Writing to tempwritethreeletters.txt with i= 2
Writing to tempwritethreeletters.txt with i= 3
Writing to tempwritethreeletters.txt with i= 4
'''
'''
tempwritethreeletters.txt
2: abc
3: abc
4: abc
3: def
0: abc
2: def
1: abc
3: ghi
4: def
2: ghi
0: def
4: ghi
0: ghi
2: jkl
1: def
3: jkl
0: jkl
4: jkl
3: mno
4: mno
1: ghi
2: mno
0: mno
1: jkl
1: mno
'''

#We want to make sure the words from each writethreeletters function doesn't get interference.  Use a lock.  When one process acquires the lock, the others have to wait.  We synchronize the processes ensuring each process use a resource exclusively despite time.sleep and fileobject.flush()
#The downside is not letting processes write to the logfile freely means the processes stack up waiting for their chance to use that locked section of code which can lead to slow downs.  If you let the procedures write to the logfile whenever they want, you end up with chaos.
from multiprocessing import Lock
lock = Lock()
def writethreeletters(filename, i):
    print("Writing to {} with i= {}".format(filename, i))
    with open(filename, "a") as fileobject:
        lock.acquire()
        for word in "abc def ghi jkl mno".split():
            time.sleep(random.randint(1, 3))
            fileobject.write("{}: {}\n".format(i, word))
            fileobject.flush()
        lock.release()


for i in range(5):
    print(i)
    multiprocessing.Process(target=writethreeletters, args=("tempwritethreeletters.txt", i)).start()
'''
0
1
2
Writing to tempwritethreeletters.txt with i= 0
3
4
Writing to tempwritethreeletters.txt with i= 2
Writing to tempwritethreeletters.txt with i= 1
Writing to tempwritethreeletters.txt with i= 3
Writing to tempwritethreeletters.txt with i= 4
'''

#Python Multiprocessing Sharing Data Share Data Shared Memory.pdf
#Multiprocessing uses processes to share data using a Queue.
#The shared memory feature of the multiprocessing module relies on shared memory capabilities allowing the processes to communicate with one another.  We're restricted to several low-level data types corresponding to individual values and arrays at the C level.
#The program below counts the size of a number of files.  We launch a new process from multiprocessing to open a file and get its size.  We place each file's size in a queue.  When all the processes are done, we retrieve and add all of the values from the queue.  Using shared memory, each process increment the value.  No counting necessary.  We want to join the processes in order to ensure all of them finished.
#I created a new "Value" object in the main process that launches everything. The "Value" object needs to be given a type and a value.  I've given it an "i" integer value and an initial value of 0. To us, "wordcount" is an integer. However, "multiprocessing" keeps track of it across processes, such that it's visible elsewhere.
from multiprocessing import Process, Value
import glob

def countwordsinfile(counter, filename):
    try:
        counter.value += len(open(filename).read())
    except IOError:
        print("Problem with ()".format(filename))


wordcount = Value("i", 0) #RM:  Value comes from the multiprocessing module.

processeslist = []
for filename in glob.glob("*.txt"):
    print(filename)
    '''
    pokemon_data.txt
    favoritetweetstext.txt
    savetextarray.txt
    tempdelete.txt
    temptwitter.txt
    arraytextfilename.txt
    sampleinin61tweets.txt
    fremontweather.txt
    oneminutedeletetemp.txt
    arraytextfile.txt
    '''
    p = Process(target=countwordsinfile, args=(wordcount, filename))
    p.start()
    processeslist.append(p)
for eachprocesseslist in processeslist:
    print(eachprocesseslist)
    '''
    <Process(Process-1, stopped)>
    <Process(Process-2, stopped)>
    <Process(Process-3, stopped)>
    <Process(Process-4, stopped)>
    <Process(Process-5, stopped)>
    <Process(Process-6, stopped)>
    <Process(Process-7, stopped)>
    <Process(Process-8, started)>
    <Process(Process-9, started)>
    <Process(Process-10, started)>
    '''
    eachprocesseslist.join()
print(processeslist) #print [<Process(Process-1, stopped)>, <Process(Process-2, stopped)>, <Process(Process-3, stopped)>, <Process(Process-4, stopped)>, <Process(Process-5, stopped)>, <Process(Process-6, stopped)>, <Process(Process-7, stopped)>, <Process(Process-8, stopped)>, <Process(Process-9, stopped)>, <Process(Process-10, stopped)>]
print("Total = {}".format(wordcount.value)) #print Total = 306076  RM:  the Total = number changes everytime the code is run


#Add with counter.get_lock() to start countwordsinfile.  The get_lock() method makes sure no one else uses the variable, then update it atomically [RM:  automatically(?)], and then release the lock.
from multiprocessing import Process, Value
import glob

def countwordsinfile(counter, filename):
    with counter.get_lock():
        try:
            counter.value += len(open(filename).read())
        except IOError:
            print("Problem with ()".format(filename))


wordcount = Value("i", 0) #RM:  Value comes from the multiprocessing module.

processeslist = []
for filename in glob.glob("*.txt"):
    print(filename)
    '''
    pokemon_data.txt
    favoritetweetstext.txt
    savetextarray.txt
    tempdelete.txt
    temptwitter.txt
    arraytextfilename.txt
    sampleinin61tweets.txt
    fremontweather.txt
    oneminutedeletetemp.txt
    arraytextfile.txt
    '''
    p = Process(target=countwordsinfile, args=(wordcount, filename))
    p.start()
    processeslist.append(p)
for eachprocesseslist in processeslist:
    print(eachprocesseslist)
    '''
    <Process(Process-11, stopped)>
    <Process(Process-12, stopped)>
    <Process(Process-13, stopped)>
    <Process(Process-14, stopped)>
    <Process(Process-15, stopped)>
    <Process(Process-16, stopped)>
    <Process(Process-17, stopped)>
    <Process(Process-18, started)>
    <Process(Process-19, started)>
    <Process(Process-20, started)>
    '''
    eachprocesseslist.join()
print(processeslist) #print [<Process(Process-11, stopped)>, <Process(Process-12, stopped)>, <Process(Process-13, stopped)>, <Process(Process-14, stopped)>, <Process(Process-15, stopped)>, <Process(Process-16, stopped)>, <Process(Process-17, stopped)>, <Process(Process-18, stopped)>, <Process(Process-19, stopped)>, <Process(Process-20, stopped)>]
print("Total = {}".format(wordcount.value)) #print Total = 307197  RM:  the Total = number is the same everytime the code is run

#Working With Process Pools Python.pdf
#Open each file and read it into memory.  Every file opened and counted is a separate process.  We open 1,000 files we're opening 1,000 processes.
#A better solution is use process pool; in other words, we start up 10 Python processes like Python servers and ask multiprocessing to execute the code on those 10 Python processes.  If there are more files to count than available processes, then some files wait.
import multiprocessing
import glob
from multiprocessing import Queue

def filesize(filename):
    try:
        q.put(len(open(filename).read()))
    except:
        pass


q = Queue()
processeslist = []
for onefilename in glob.glob("*.txt"):
    print(onefilename)
    '''
    pokemon_data.txt
    favoritetweetstext.txt
    savetextarray.txt
    tempdelete.txt
    temptwitter.txt
    arraytextfilename.txt
    sampleinin61tweets.txt
    fremontweather.txt
    oneminutedeletetemp.txt
    arraytextfile.txt
    '''
    p = multiprocessing.Process(target=filesize, args=(onefilename, ))
    p.start()
    processeslist.append(p)
for eachprocesseslist in processeslist:
    print(eachprocesseslist)
    '''
    <Process(Process-1, stopped)>
    <Process(Process-2, started)>
    <Process(Process-3, stopped)>
    <Process(Process-4, stopped)>
    <Process(Process-5, started)>
    <Process(Process-6, started)>
    <Process(Process-7, started)>
    <Process(Process-8, stopped)>
    <Process(Process-9, started)>
    <Process(Process-10, stopped)>
    '''
    eachprocesseslist.join()
total = 0
while not q.empty():
    total += q.get()
print("Total: {}".format(total)) #print Total: 307197

#Use a process pool.  Apply a function to each element in a list like a for loop or a list comprehension.  We expect to get output from the function.
#The function prints its process ID and returns its value instead of putting the value in a queue.  We create a pool of 8 processes.  We use pool.map to invoke our funciton once for each element returned by glob.glob.  The result of pool.map is a list which is summed to get the total size.
#The code below we turned it into a functional-style programming problem.  We can raise or lower the number of processes in the pool go up or go down.
from multiprocessing import Pool
import glob
import os
def filesizepoolprocessing(filename):
    print("I'm in PID {}".format(os.getpid()))
    '''
    I'm in PID 3348
    I'm in PID 3349
    I'm in PID 3350
    I'm in PID 3351
    I'm in PID 3350
    I'm in PID 3353
    I'm in PID 3348
    I'm in PID 3351
    I'm in PID 3354
    I'm in PID 3355
    '''
    try:
        return len(open(filename).read())
    except IOError:
        return 0


with Pool(processes=8) as pool:
    result = pool.map(filesizepoolprocessing, glob.glob("*.txt"))
    print(sum(result)) #print 307197

#Python Multiprocessing Tutorial Run Code in Parallel Using the Multiprocessing Module
import time
start = time.perf_counter()

def dosomethingnonmultiprocessing():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping")


dosomethingnonmultiprocessing()
dosomethingnonmultiprocessing()
finish = time.perf_counter()
print(f"dosomethingnomultiprocessing Finished in {round(finish-start,2)} second(s)")
'''
RM:  without multiprocessing
Sleeping 1 second...
Done sleeping
Sleeping 1 second...
Done sleeping
dosomethingnomultiprocessing Finished in 2.08 second(s)
'''

import multiprocessing
import time
start = time.perf_counter()

def dosomething():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping")


process01 = multiprocessing.Process(target=dosomething)
process02 = multiprocessing.Process(target=dosomething)
process01.start()
process02.start()
finish = time.perf_counter()
print(f"multiprocessing Finished in {round(finish-start,2)} second(s)")
'''
RM:  with multiprocessing
multiprocessing Finished in 0.0 second(s)
Sleeping 1 second...
Sleeping 1 second...
Done sleeping
Done sleeping
'''

start = time.perf_counter()
def dosomethinginorder():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping")


process01 = multiprocessing.Process(target=dosomethinginorder)
process02 = multiprocessing.Process(target=dosomethinginorder)
process01.start()
process02.start()
process01.join() #join a process means wait to finish to continue with rest of script.
process02.join() #join a process means wait to finish to continue with rest of script.
finish = time.perf_counter()
print(f"multiprocessing processed in order Finished in {round(finish-start,2)} second(s)")
'''
RM:  with multiprocessing
Sleeping 1 second...
Sleeping 1 second...
Done sleeping
Done sleeping
multiprocessing processed in order Finished in 1.0 second(s)
'''

start = time.perf_counter()
def dosomethingforloop():
    print("Sleeping wait and order 1 second...")
    time.sleep(1)
    print("Done wait and order sleeping")


processseslist = []
for _ in range(10):
    process = multiprocessing.Process(target=dosomethingforloop)
    process.start()
    processseslist.append(process)
for eachprocesseslist in processseslist:
    process.join() #join a process means wait to finish to continue with rest of script.  Finish the multiprocess script before going to finish = time.perf_counter()

finish = time.perf_counter()
print(f"multiprocessing processing and waiting in order Finished in {round(finish-start,2)} second(s)")
'''
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Sleeping wait and order 1 second...
Done wait and order sleeping
Done wait and order sleeping
Done wait and order sleeping
Done wait and order sleeping
Done wait and order sleeping
Done wait and order sleeping
Done wait and order sleeping
Done wait and order sleeping
Done wait and order sleeping
Done wait and order sleeping
multiprocessing processing and waiting in order Finished in 1.01 second(s)
'''

start = time.perf_counter()
def dosomethingforloopargument(seconds):
    print(f"Sleeping argument {seconds} second(s)...")
    time.sleep(seconds)
    print("Done argument sleeping")


processseslist = []
for _ in range(10):
    process = multiprocessing.Process(target=dosomethingforloopargument, args=[1.5])
    process.start()
    processseslist.append(process)
for eachprocesseslist in processseslist:
    process.join() #join a process means wait to finish to continue with rest of script.  Finish the multiprocess script before going to finish = time.perf_counter()

finish = time.perf_counter()
print(f"multiprocessing processing and waiting in order arguments Finished in {round(finish-start,2)} second(s)")
'''
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Sleeping argument 1.5 second(s)...
Done argument sleeping
Done argument sleeping
Done argument sleeping
Done argument sleeping
Done argument sleeping
Done argument sleeping
Done argument sleeping
Done argument sleeping
Done argument sleeping
Done argument sleeping
multiprocessing processing and waiting in order arguments Finished in 1.51 second(s)
'''

import concurrent.futures

start = time.perf_counter()
def dosomethingmanual(seconds):
    print(f"Sleeping concurrent.futures {seconds} second(s)...")
    time.sleep(seconds)
    return "Return done concurrent.futures sleeping"


with concurrent.futures.ProcessPoolExecutor() as executor: #ProcessPoolExecutor is in concurrent.futures module.  Use with context text manager.
    executefunction1 = executor.submit(dosomethingmanual, 1)
    print(executefunction1.result())
    executefunction2 = executor.submit(dosomethingmanual, 2)
    print(executefunction2.result())
    '''
    Sleeping concurrent.futures 1 second(s)...
    Return done concurrent.futures sleeping
    Sleeping concurrent.futures 2 second(s)...
    Return done concurrent.futures sleeping
    '''

finish = time.perf_counter()
print(f"multiprocessing concurent.futures Finished in {round(finish-start,2)} second(s)") #print multiprocessing concurent.futures Finished in 3.01 second(s)

import concurrent.futures

start = time.perf_counter()
def dosomethinglistcomprehensiontorunmultipletimes(seconds):
    print(f"Sleeping concurrent.futures list comprehension run multiple times {seconds} second(s)...")
    time.sleep(seconds)
    return "Return done concurrent.futures list comprehension run multiple times sleeping"


with concurrent.futures.ProcessPoolExecutor() as executor: #ProcessPoolExecutor is in concurrent.futures module.  Use with context text manager.
    results = [executor.submit(dosomethinglistcomprehensiontorunmultipletimes, 1) for _ in range(10)]  #RM:  for loop instead of list comprehension is valid
    for f in concurrent.futures.as_completed(results):
        print(f.result())
        '''
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Return done concurrent.futures list comprehension run multiple times sleeping
        Return done concurrent.futures list comprehension run multiple times sleeping
        Return done concurrent.futures list comprehension run multiple times sleeping
        Return done concurrent.futures list comprehension run multiple times sleeping
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Sleeping concurrent.futures list comprehension run multiple times 1 second(s)...
        Return done concurrent.futures list comprehension run multiple times sleeping
        Return done concurrent.futures list comprehension run multiple times sleeping
        Return done concurrent.futures list comprehension run multiple times sleeping
        Return done concurrent.futures list comprehension run multiple times sleeping
        Return done concurrent.futures list comprehension run multiple times sleeping
        Return done concurrent.futures list comprehension run multiple times sleeping
        '''
finish = time.perf_counter()
print(f"multiprocessing concurent.futures list comprehension run multiple times Finished in {round(finish-start,2)} second(s)") #print multiprocessing concurent.futures list comprehension run multiple times Finished in 3.05 second(s)

start = time.perf_counter()
def dosomethinglistcomprehensiontorunmultipletimesvariousseconds(nseconds):
    print(f"Sleeping concurrent.futures list comprehension run multiple times nseconds {nseconds} nsecond(s)...")
    time.sleep(nseconds)
    return f"Return done concurrent.futures list comprehension run multiple times sleeping {nseconds} nseconds(s)"


with concurrent.futures.ProcessPoolExecutor() as executor: #ProcessPoolExecutor is in concurrent.futures module.  Use with context text manager. The end result printed in order starting with Return done concurrent.futures . . .
    results = [executor.submit(dosomethinglistcomprehensiontorunmultipletimesvariousseconds, nseconds) for nseconds in range(10)]  #RM:  for loop instead of list comprehension is valid
    for f in concurrent.futures.as_completed(results):
        print(f.result())
        '''
        Sleeping concurrent.futures list comprehension run multiple times nseconds 0 nsecond(s)...
        Sleeping concurrent.futures list comprehension run multiple times nseconds 1 nsecond(s)...
        Sleeping concurrent.futures list comprehension run multiple times nseconds 3 nsecond(s)...
        Sleeping concurrent.futures list comprehension run multiple times nseconds 4 nsecond(s)...
        Return done concurrent.futures list comprehension run multiple times sleeping 0 nseconds(s)
        Sleeping concurrent.futures list comprehension run multiple times nseconds 2 nsecond(s)...
        Sleeping concurrent.futures list comprehension run multiple times nseconds 5 nsecond(s)...
        Return done concurrent.futures list comprehension run multiple times sleeping 1 nseconds(s)
        Return done concurrent.futures list comprehension run multiple times sleeping 2 nseconds(s)
        Sleeping concurrent.futures list comprehension run multiple times nseconds 6 nsecond(s)...
        Sleeping concurrent.futures list comprehension run multiple times nseconds 7 nsecond(s)...
        Return done concurrent.futures list comprehension run multiple times sleeping 3 nseconds(s)
        Sleeping concurrent.futures list comprehension run multiple times nseconds 8 nsecond(s)...
        Return done concurrent.futures list comprehension run multiple times sleeping 4 nseconds(s)
        Sleeping concurrent.futures list comprehension run multiple times nseconds 9 nsecond(s)...
        Return done concurrent.futures list comprehension run multiple times sleeping 5 nseconds(s)
        Return done concurrent.futures list comprehension run multiple times sleeping 6 nseconds(s)
        Return done concurrent.futures list comprehension run multiple times sleeping 7 nseconds(s)
        Return done concurrent.futures list comprehension run multiple times sleeping 8 nseconds(s)
        Return done concurrent.futures list comprehension run multiple times sleeping 9 nseconds(s)
        '''
finish = time.perf_counter()
print(f"multiprocessing concurent.futures list comprehension run multiple times nseconds Finished in {round(finish-start,2)} second(s)") #print multiprocessing concurent.futures list comprehension run multiple times nseconds Finished in 15.03 second(s)

start = time.perf_counter()
def dosomethinglistcomprehensiontorunmultipletimesmapmethod(nseconds):
    print(f"Sleeping concurrent.futures map method run multiple times nseconds {nseconds} nsecond(s)...")
    time.sleep(nseconds)
    return f"Return done concurrent.futures map method run multiple times sleeping {nseconds} nseconds(s)"


with concurrent.futures.ProcessPoolExecutor() as executor: #ProcessPoolExecutor is in concurrent.futures module.  Use with context text manager. The end result printed in order starting with Return done concurrent.futures . . .
    secondslist = [n for n in range(10)]
    results = executor.map(dosomethinglistcomprehensiontorunmultipletimesmapmethod, secondslist)
    for eachresult in results:
        print(eachresult)
        '''
        Sleeping concurrent.futures map method run multiple times nseconds 0 nsecond(s)...
        Sleeping concurrent.futures map method run multiple times nseconds 1 nsecond(s)...
        Sleeping concurrent.futures map method run multiple times nseconds 2 nsecond(s)...
        Sleeping concurrent.futures map method run multiple times nseconds 4 nsecond(s)...
        Sleeping concurrent.futures map method run multiple times nseconds 3 nsecond(s)...
        Return done concurrent.futures map method run multiple times sleeping 0 nseconds(s)
        Sleeping concurrent.futures map method run multiple times nseconds 5 nsecond(s)...
        Return done concurrent.futures map method run multiple times sleeping 1 nseconds(s)
        Sleeping concurrent.futures map method run multiple times nseconds 6 nsecond(s)...
        Return done concurrent.futures map method run multiple times sleeping 2 nseconds(s)
        Sleeping concurrent.futures map method run multiple times nseconds 7 nsecond(s)...
        Return done concurrent.futures map method run multiple times sleeping 3 nseconds(s)
        Sleeping concurrent.futures map method run multiple times nseconds 8 nsecond(s)...
        Return done concurrent.futures map method run multiple times sleeping 4 nseconds(s)
        Sleeping concurrent.futures map method run multiple times nseconds 9 nsecond(s)...
        Return done concurrent.futures map method run multiple times sleeping 5 nseconds(s)
        Return done concurrent.futures map method run multiple times sleeping 6 nseconds(s)
        Return done concurrent.futures map method run multiple times sleeping 7 nseconds(s)
        Return done concurrent.futures map method run multiple times sleeping 8 nseconds(s)
        Return done concurrent.futures map method run multiple times sleeping 9 nseconds(s)
        '''
finish = time.perf_counter()
print(f"multiprocessing concurent.futures map method run multiple times nseconds Finished in {round(finish-start,2)} second(s)") #print multiprocessing concurent.futures map method run multiple times nseconds Finished in 15.05 second(s)

start = time.perf_counter()
def dosomethinglistcomprehensiontorunmultipletimesmapmethod(nseconds):
    print(f"Sleeping concurrent.futures map method run multiple times no for loop results nseconds {nseconds} nsecond(s)...")
    time.sleep(nseconds)


with concurrent.futures.ProcessPoolExecutor() as executor: #ProcessPoolExecutor is in concurrent.futures module.  Use with context text manager. The end result printed in order
    secondslist = [n for n in range(10)]
    results = executor.map(dosomethinglistcomprehensiontorunmultipletimesmapmethod, secondslist)
    '''
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 0 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 1 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 2 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 3 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 4 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 5 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 6 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 7 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 8 nsecond(s)...
    Sleeping concurrent.futures map method run multiple times no for loop results nseconds 9 nsecond(s)...
    '''
finish = time.perf_counter()
print(f"multiprocessing concurent.futures map method run multiple times no for loop results nseconds Finished in {round(finish-start,2)} second(s)") #print multiprocessing concurent.futures map method run multiple times no for loop results nseconds Finished in 15.03 second(s)

#Multiprocessing in Python - Introduction (Part 1)-RR4SoktDQAw
# def square(number):
#     result = number * number
#     print(f"The number {number} squares to {result}.")


# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4]
#     for number in numbers:
#         square(number)
#         '''
#         The number 1 squares to 1.
#         The number 2 squares to 4.
#         The number 3 squares to 9.
#         The number 4 squares to 16.
#         '''

import os
def squareprocess(number):
    result = number * number
    #OS module to print out the Process ID assigned to the call of squareprocess function assigned by the operating system
    processid = os.getpid()
    print(f"Process ID:  {processid}")
    #Get the name of the Process object
    processname = current_process().name
    print(f"Process Name: {processname}")
    print(f"squareprocess functionn The number {number} squares to {result}.")
    '''
    Process ID:  2090
    Process Name: Process-1
    squareprocess functionn The number 1 squares to 1.
    Process ID:  2091
    Process Name: Process-2
    squareprocess functionn The number 2 squares to 4.
    Process ID:  2093
    Process Name: Process-4
    squareprocess functionn The number 4 squares to 16.
    Process ID:  2092
    Process Name: Process-3
    squareprocess functionn The number 3 squares to 9.
    '''


from multiprocessing import Process, current_process
if __name__ == "__main__":
    processes = []
    numbers = [1, 2, 3, 4]
    for number in numbers:
        #Processes are spawned by creating a Process object
        process = Process(target=squareprocess, args=(number,)) #stylistically one argument to function end the args with a comma inside the tuple
        processes.append(process)
        #Call its start() method
        process.start()

#Multiprocessing in Python - Introduction (Part 2)-itbx_hDX7z8

import os
import time
from multiprocessing import Process, current_process
def squareprocess(numberslist):
    for eachnumberslist in numberslist:
        time.sleep(3)
        result = eachnumberslist * eachnumberslist
        processid = os.getpid()
        print(f"Process ID:  {processid}")
        #Get the name of the Process object
        processname = current_process().name
        print(f"Process Name: {processname}")
        print(f"squareprocess functionn The number {eachnumberslist} squares to {result}.")
        '''
        Process ID:  2194
        Process Name: Process-1
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2199
        Process Name: Process-6
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2196
        Process Name: Process-3
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2197
        Process Name: Process-4
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2195
        Process ID:  2198
        Process ID:  2200
        Process ID:  2201
        Process ID:  2202
        Process Name: Process-8
        Process Name: Process-7
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-5
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-2
        squareprocess functionn The number 0 squares to 0.
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-9
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2204
        Process Name: Process-11
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2203
        Process ID:  2205
        Process ID:  2206
        Process ID:  2208
        Process ID:  2209
        Process ID:  2210
        Process Name: Process-15
        Process Name: Process-16
        Process Name: Process-13
        Process Name: Process-17
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-12
        Process Name: Process-10
        squareprocess functionn The number 0 squares to 0.
        squareprocess functionn The number 0 squares to 0.
        squareprocess functionn The number 0 squares to 0.
        squareprocess functionn The number 0 squares to 0.
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2212
        Process ID:  2213
        Process ID:  2207
        Process ID:  2217
        Process Name: Process-24
        Process Name: Process-14
        Process Name: Process-20
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-19
        squareprocess functionn The number 0 squares to 0.
        squareprocess functionn The number 0 squares to 0.
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2223
        Process Name: Process-30
        Process ID:  2211
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2219
        Process Name: Process-18
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-26
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2214
        Process Name: Process-21
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2218
        Process Name: Process-25
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2220
        Process Name: Process-27
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2215
        Process Name: Process-22
        Process ID:  2216
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-23
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2225
        Process Name: Process-32
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2224
        Process Name: Process-31
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2226
        Process Name: Process-33
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2233
        Process Name: Process-40
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2227
        Process Name: Process-34
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2235
        Process ID:  2228
        Process Name: Process-42
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-35
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2222
        Process ID:  2229
        Process Name: Process-29
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-36
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2221
        Process ID:  2230
        Process Name: Process-28
        squareprocess functionn The number 0 squares to 0.
        Process Name: Process-37
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2231
        Process Name: Process-38
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2232
        Process Name: Process-39
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2234
        Process Name: Process-41
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2236
        Process Name: Process-43
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2238
        Process Name: Process-45
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2237
        Process Name: Process-44
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2239
        Process Name: Process-46
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2240
        Process Name: Process-47
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2241
        Process Name: Process-48
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2243
        Process Name: Process-50
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2242
        Process Name: Process-49
        squareprocess functionn The number 0 squares to 0.
        Process ID:  2197
        Process Name: Process-4
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2196
        Process Name: Process-3
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2204
        Process Name: Process-11
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2194
        Process Name: Process-1
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2199
        Process Name: Process-6
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2198
        Process ID:  2201
        Process ID:  2195
        Process Name: Process-8
        Process ID:  2200
        Process Name: Process-7
        Process Name: Process-2
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2202
        Process Name: Process-9
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-5
        squareprocess functionn The number 1 squares to 1.
        squareprocess functionn The number 1 squares to 1.
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2218
        Process Name: Process-25
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2214
        Process Name: Process-21
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2211
        Process Name: Process-18
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2220
        Process Name: Process-27
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2215
        Process Name: Process-22
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2216
        Process Name: Process-23
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2209
        Process Name: Process-16
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2208
        Process Name: Process-15
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2206
        Process Name: Process-13
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2210
        Process Name: Process-17
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2207
        Process ID:  2226
        Process ID:  2217
        Process ID:  2203
        Process Name: Process-33
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-10
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2213
        Process ID:  2235
        Process Name: Process-42
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2229
        Process Name: Process-36
        Process ID:  2205
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-12
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-20
        Process ID:  2227
        Process Name: Process-34
        Process ID:  2224
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-24
        Process ID:  2219
        Process Name: Process-26
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2222
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2233
        Process ID:  2223
        Process Name: Process-40
        squareprocess functionn The number 1 squares to 1.
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2228
        Process Name: Process-35
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2231
        Process Name: Process-38
        Process ID:  2232
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-39
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-14
        Process ID:  2234
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-41
        Process ID:  2212
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-19
        Process ID:  2225
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-32
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-31
        Process Name: Process-29
        squareprocess functionn The number 1 squares to 1.
        Process Name: Process-30
        squareprocess functionn The number 1 squares to 1.
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2230
        Process Name: Process-37
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2221
        Process Name: Process-28
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2238
        Process Name: Process-45
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2236
        Process Name: Process-43
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2237
        Process Name: Process-44
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2239
        Process Name: Process-46
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2240
        Process Name: Process-47
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2241
        Process Name: Process-48
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2243
        Process Name: Process-50
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2242
        Process Name: Process-49
        squareprocess functionn The number 1 squares to 1.
        Process ID:  2196
        Process Name: Process-3
        squareprocess functionn The number 2 squares to 4.
        '''


if __name__ == "__main__":
    processes = []
    numbers = range(100)
    for _ in range(50):
        #Processes are spawned by creating a Process object
        process = Process(target=squareprocess, args=(numbers,)) #stylistically one argument to function end the args with a comma inside the tuple
        processes.append(process)
        #Call its start() method
        process.start()
    #Wait for all processes started to be completed before we run any subsequent code
    for process in processes:
        process.join()
    print("Multiprocessing complete")
