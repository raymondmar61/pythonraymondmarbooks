#Python Threading Tutorial Run Code Concurrently Using the Threading Module
import threading
import time
start = time.perf_counter()

def dosomething():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping")


# dosomething()
# dosomething()
#create two thread objects like dosomething()\n dosomething()
threadone = threading.Thread(target=dosomething)
threadtwo = threading.Thread(target=dosomething)
threadone.start()
threadtwo.start()
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
'''
Sleeping 1 second...
Sleeping 1 second...
Finished in 0.0 second(s).
Done sleeping
Done sleeping
'''
#create two thread objects like dosomething()\n dosomething() joined
threadone = threading.Thread(target=dosomething)
threadtwo = threading.Thread(target=dosomething)
threadone.start()
threadtwo.start()
threadone.join()
threadtwo.join()
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
'''
Sleeping 1 second...
Sleeping 1 second...
Done sleeping
Done sleeping
Finished in 1.0 second(s).
'''
#create ten threads using a loop
threadslist = []
for _ in range(0, 10):
    thethread = threading.Thread(target=dosomething)
    thethread.start()
    threadslist.append(thethread)
for thread in threadslist:
    thread.join()
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
'''
Sleeping 1 second...
Sleeping 1 second...
Sleeping 1 second...
Sleeping 1 second...
Sleeping 1 second...
Sleeping 1 second...
Sleeping 1 second...
Sleeping 1 second...
Sleeping 1 second...
Sleeping 1 second...
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Finished in 1.02 second(s).
'''
#pass an argument
def dosomethingargument(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping")


threadslist = []
for _ in range(0, 10):
    thethread = threading.Thread(target=dosomethingargument, args=[1.5])  #args is a list type
    thethread.start()
    threadslist.append(thethread)
for thread in threadslist:
    thread.join()
finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
'''
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Sleeping 1.5 second(s)...
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Finished in 1.51 second(s).
'''
#Use concurrent.futures less code
import concurrent.futures
def dosomethingargument(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done sleeping"


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(dosomethingargument, 1)
    f2 = executor.submit(dosomethingargument, 1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
'''
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Done sleeping
Done sleeping
Finished in 1.02 second(s).
'''
#Use concurrent.futures less code run multiple times
import concurrent.futures
def dosomethingargument(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done sleeping"


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(dosomethingargument, 1) for _ in range(0, 10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
'''
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Done sleeping
Finished in 1.02 second(s).
'''
#Use concurrent.futures less code run multiple times submit a list
import concurrent.futures
def dosomethingargument(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping {seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secondslist = [5, 4, 3, 2, 1]
    results = [executor.submit(dosomethingargument, eachsecondslist) for eachsecondslist in secondslist]
    for f in concurrent.futures.as_completed(results):  #The as_completed(results) as_completed method printed the results in order of completion
        print(f.result())


finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
'''
Sleeping 5 second(s)...
Sleeping 4 second(s)...
Sleeping 3 second(s)...
Sleeping 2 second(s)...
Sleeping 1 second(s)...
Done sleeping 1
Done sleeping 2
Done sleeping 3
Done sleeping 4
Done sleeping 5
Finished in 5.02 second(s).
'''
#map method with the results prints or returns the object when completed
import concurrent.futures
def dosomethingargument(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping {seconds}"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secondslist = [5, 4, 3, 2, 1]
    results = executor.map(dosomethingargument, secondslist)
    for eachresults in results:
        print(eachresults)


finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
'''
Sleeping 5 second(s)...
Sleeping 4 second(s)...
Sleeping 3 second(s)...
Sleeping 2 second(s)...
Sleeping 1 second(s)...
Done sleeping 5
Done sleeping 4
Done sleeping 3
Done sleeping 2
Done sleeping 1
Finished in 5.02 second(s).
'''
#download images one at a time without threading
import requests
import time
imageurlslist = ["image1", "image2", "image3", "image4", "image5"]
starttimer = time.perf_counter()
for eachimageurlslist in imageurlslist:
    imagebytes = requests.get(eachimageurlslist).content
    imagename = eachimageurlslist + ".jpg"
    with open(imagename, "wb") as imagefileobject:
        imagefileobject.write(imagebytes)
        print(imagename + "was downloaded.")
endtimer = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")
#download images multiple times with threading
import requests
import time
import concurrent.futures
imageurlslist = ["image1", "image2", "image3", "image4", "image5"]
starttimer = time.perf_counter()
def downloadimages(imageurl):
    imagebytes = requests.get(imageurl).content
    imagename = imageurl + ".jpg"
    with open(imagename, "wb") as imagefileobject:
        imagefileobject.write(imagebytes)
        print(imagename + "was downloaded.")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(downloadimages, imageurlslist)


endtimer = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s).")

#Reuven Lerner lerner.co.il Python Deadlock Threads.pdf or Python Threads Deadlock.pdf
#deadlocks happen when two or more threads get intertwined resulting in stop progressing.  It's like a busy intersection.  A car to progress other cars must move out of the way.  They can't move out of the way because other cars are blocking them.  Cars eventually pull out of the intersection in time through negotiation to get traffic moving again.
#Not easy in software.  Thread A waiting for thread B and thread B waiting for thread A, you could wait forever.  Or one thread moves out to let the other thread progress.  Or Python stops because there is a deadlock.

import threading
import time
import random
lock = threading.Lock()
def lockfunction1():
    with threading.Lock():
        print("I'm lockfunction1")
def lockfunction2():
    with threading.Lock():
        print("I'm lockfunction2")


threading.Thread(target=lockfunction1).start()
threading.Thread(target=lockfunction2).start()
#Create two functions lockfuntion1 and lockfunction2 to print.  The print is inside the "with" block.  The "with" turns to the object threading.Lock() asking if threading.Lock() wants to do anything.  Answer is yes.  threading.Lock() invokes the acquire method which ensures one and only one thread is currently lock with threading.Lock().  Only one function enters its "with" block at a time and the other waits.  The "with" block exits and invokes its release method.  Then the other function enter its "with" block.  There shouldn't be any deadlocks.
#What if we have several locks.  It's possible we want to acquire more locks.
# import threading
# import time
# lock1 = threading.Lock()
# lock2 = threading.Lock()
# def secondlockfunction1():
#     with lock1:
#         time.sleep(3)
#         with lock2:
#             print("I'm in secondlockfunction1")
# def secondlockfunction2():
#     with lock2:
#         time.sleep(3)
#         with lock1:
#             print("I'm in secondlockfunction2")


# threading.Thread(target=secondlockfunction1).start()
# threading.Thread(target=secondlockfunction2).start()
#We run each functions in a separate thread.  Each function starts acquire a lock lock1 for secondlookfunction1 and lock2 for secondloookfunction2.  We don't know when each function starts.  We assume each acquires the lock and then sleep for three seconds.  secondlookfunction1 acquires lock1, sleep, and acquires lock2.  secondlookfunction1 can't acquire lock2 because secondlookfunction2 acquires lock2.  secondlookfunction2 releases lock2 after it completes the outer "with" block.  secondlookfunction2 releases lock2 after releasing lock1.  secondlookfunction2 can't release lock1 because secondlookfunction1 is progressing with lock1.  In other words, a deadlock.
#The solution is acquire multiple locks in the same order.# import threading
import threading
import time
lock1 = threading.Lock()
lock2 = threading.Lock()
def correctlockfunction1():
    with lock1:
        time.sleep(3)
        with lock2:
            print("I'm in correctlockfunction1")
def correctlockfunction2():
    with lock1:
        time.sleep(3)
        with lock2:
            print("I'm in correctlockfunction2")


threading.Thread(target=correctlockfunction1).start()
threading.Thread(target=correctlockfunction2).start()

#Reuven Lerner lerner.co.il Python Different Tasks In Different Threads
#Threads communicate with each other using a queue.  Queues are the only Python objects whoese operations are guaranteed to be thread-safe.  For example, a program with a GUI runs in one thread.  Press a button on the GUI spawns a new thread allowing the GUI to continue to function while the calculations happen.
#Python's Global Interpreter Lock (GIL) means doing calculations in parallel using multiple threads don't get you anywhere.  Doing I/O tasks using the disk or network is handled well by threads.
spacesinstring = "abc def ghi jkl"
print(spacesinstring.count(" ")) #print 3
#Open file, iterate file line by line totaling number of space characters found on each line, print total.
dummyfiledoesntexsit = "pretendtextfile.txt"
total = 0
for eachline in open(dummyfiledoesntexsit):
    total += eachline.count(" ")
print(total) #print 284
#Open file, iterate file line by line totaling number of space characters found on each line, print total using a function.
def countspaces(filename):
    total = 0
    for eachline in open(filename):
        total += eachline.count(" ")
    return total


countspaces("pretendtextfile.txt") #return 284
#Open files in a directory, iterate files line by line totaling number of space characters found on each line, print total using a function.
import glob
def countspaces(filename):
    total = 0
    for eachline in open(filename):
        total += eachline.count(" ")
    return total


for eachtextfile in glob.glob("*.txt"):
    print(countspaces(eachtextfile)) #print 105\n 16280\n 4\n 1\n 6145\n 0\n 4206\n 0\n 0\n 0  RM:  total sum is 26,741

#Wrap the count inside a function.  countspacesglob is a function to count spaces in what type of file.  The countspacesglob calls another function countspaces to count the spaces in the files.
def countspaces(filename):
    total = 0
    for eachline in open(filename):
        total += eachline.count(" ")
    return total
def countspacesglob(pattern):
    total = 0
    for eachtextfile in glob.glob(pattern):
        total += countspaces(eachtextfile)
    return total


print(countspacesglob("*.txt")) #print 26741

#We can calculate the number of spaces in text files.  What if you have a large number of text files.  Use threads.  How?  Instead of invoking countspaces function on a file in the main thread,we launch our call to the function in its own thread.  One thread per file.
import threading
from queue import Queue, Empty
qisforqueuing = Queue()
def countspaces2(filename):
    total = 0
    for eachline in open(filename):
        total += eachline.count(" ")
    qisforqueuing.put(total)
#We invoke countspaces in a new thread each time function is invoked.  We create a new thread object instead of creating a new instance of threading.Thread.  After starting all of the threads, we run a while loop for which we wait for all of the threads to be done.  We iterate over threading.enumerate returning each of the threads in sequence.  If the thread cannot be joined within 0.1 seconds, we move onto the next thread from threading.enumerate.  When we're done going through all threads, we either exit the while loop or go through it again trying to join with each remaining thread.  Once all threads are joined, we go through the queue retrieving each totals we got.
def countspacesglob2(pattern):
    for eachtextfile in glob.glob(pattern):
        threading.Thread(target=countspaces2, args=(eachtextfile,)).start()
    while len(threading.enumerate()) > 1:
        for t in threading.enumerate():
            if threading.current_thread() == t:
                continue
            t.join(0.1)
    print("All threads are done")
    total = 0
    while True:
        try:
            total += qisforqueuing.get(True, 0.01)
        except Empty as e:
            break
    return total


print(countspacesglob2("*.txt")) #print 26741

#Reuven Lerner lerner.co.il Python Exceptions in Threads.pdf
#Technically, Python didn't crash.  Python exited with an unhandled exception.
x = 10
y = 0
#z = x / y #ZeroDivisionError: division by zero
#Write code in a function because it's the only way to start code in a new thread putting the code in a function or a method.  Create a new instance of threading.Thread to run baddivision function and start baddivisionfunction in a new thread.  Result is an exception.
# import threading
# def baddivision():
#     x = 10
#     y = 0
#     z = x / y


# threading.Thread(target=baddivision).start()
#A unhanlded exception stops one thread and the other threads continue.  An exception in one thread doesn't bring down the entire program.  Invoke a division function several times in a loop.
#Spawn five threads invoking baddivision2 with a different value for y.  The thread which the exception takes place exists with an unhandled exception.  The rest of the threads continue.
import threading
import time
import random
def baddivision2(y):
    print("Thread {}".format(threading.get_ident()))
    time.sleep(random.randint(1, 5))
    x = 10
    z = x / y
    print("\t{}".format(z))


for i in range(0, 5):
    threading.Thread(target=baddivision2, args=(i,)).start()
'''
Thread 140364226017024
Thread 140364217624320
Thread 140364209231616
Thread 140364200838912
Thread 140364192446208
    3.3333333333333335
    5.0
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "yywork.py", line 23, in baddivision2
    z = x / y
ZeroDivisionError: division by zero

    10.0
    2.5
'''
#What if we want to capture the exception or inform another part of the program the exception was raised.  We want to trap the exception raised within the thread.  The try except clause must be within the thread.
def baddivisiontryexceptwithinthread(y):
    print("Thread {}".format(threading.get_ident()))
    time.sleep(random.randint(1, 5))
    try:
        x = 10
        z = x / y
        print("\t{}".format(z))
    except ZeroDivisionError as errorvariable:
        print("Exception {} in thread {}".format(errorvariable, threading.get_ident()))


for i in range(0, 5):
    threading.Thread(target=baddivisiontryexceptwithinthread, args=(i,)).start()
'''
Thread 139699728750336
Thread 139699381335808
Thread 139699372943104
Thread 139699364550400
Thread 139699356157696
    2.5
    10.0
Exception division by zero in thread 139699728750336
    5.0
    3.3333333333333335
'''
#What if our function wants to communicate to the main thread there was a problem.  We want to keep track of which threads ended with exceptions as opposed to threads which ended.  One solution is use Queues.  Exceptions are Python objects which can be added and removed from queues.  Queues are thread-safe data structures allowing us to pass information among threads.  Create a queue called failuequeues which put all exceptions occurred.
import threading
import time
import random
from queue import Queue
failuequeues = Queue()
def baddivisiontryexceptqueue(y):
    print("Thread {}".format(threading.get_ident()))
    time.sleep(random.randint(1, 5))
    try:
        x = 10
        z = x / y
        print("\t{}".format(z))
    except ZeroDivisionError as errorvariable:
        failuequeues.put((errorvariable, threading.get_ident(), x, y))


threadlist = []
for i in range(0, 5):
    #threading.Thread(target=baddivisiontryexceptqueue, args=(i,)).start()
    t = threading.Thread(target=baddivisiontryexceptqueue, args=(i,))
    t.start()
    threadlist.append(t)
for eachthreadlist in threadlist:
    eachthreadlist.join()
print("All done!")
print("Now showing {} failures(s):".format(failuequeues.qsize()))
while not failuequeues.empty():
    errorvariable, threadid, x, y = failuequeues.get()
    print("\tThread {}, exception {}: {} / {}".format(threadid, errorvariable, x, y))
'''
Thread 140305503917824
Thread 140305495525120
Thread 140305487132416
Thread 140305478739712
Thread 140305470347008
    2.5
    3.3333333333333335
    5.0
    10.0
All done!
Now showing 1 failures(s):
    Thread 140305503917824, exception division by zero: 10 / 0
'''

#Reuven Lerner lerner.co.il Python Threading Multiprocessing.pdf
#This program demonstrates the double-edged sword of shared data within threads: The global "mylist" variable is shared by all of the threads, meaning that when we invoke"mylist.append" from within a thread, each of the threads is actually modifying the samelist.
import threading
mylist = [10, 20, 30]
def addonethreading(x):
    mylist.append(x)


threadslist = []
for i in range(5):
    threadingvariable = threading.Thread(target=addonethreading, args=(i,))
    threadslist.append(threadingvariable)
    threadingvariable.start()
for eachthreadslist in threadslist:
    threadingvariable.join()
print(mylist) #print [10, 20, 30, 0, 1, 2, 3, 4]