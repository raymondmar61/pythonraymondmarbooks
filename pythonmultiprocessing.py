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