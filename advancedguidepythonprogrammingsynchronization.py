#Advanced Guide To Python 3 Programming by John Hunt Chapter 32 Inter Thread/Process Synchronization
#Most libraries are mirrored between threading and multiprocessing.  The same ideas apply.  Don't mix and match threads and processes.  If you use threads, then use facilities from the threading library.  If you use processes, then use facilities in the multiprocessing library.  The chapter uses threading or multiprocessing.  Each are relevant for both.
#Use a threading.Barrier or multiprocessing.Barrier is a simple way to execute a set of Threads or Processes.  The threads or processes involved in the barrier are parties.  Each parties work independently.  The barrier represents an end point which all parties must reach before any further behavior can be triggered.  All parties reach the barrier it's possible to optionally trigger a post-phase action or barrier callback.  The post-phase action represents some behavior which is run when all parties reach the barrier and before allowing those parties to continue.  The post-phase action or the callback executes in a single thread or process.  Once it is completed then all the parties are unblocked and may continue.  For instance, three threads.  When the third thread reaches the barrier, the callback is invoked.  When the callback is completed, the barrier releases all three threads to continue.
from threading import Barrier, Thread
from time import sleep
from random import randint
def printit(message, barrier, sleeptimer):
    print("printit for:", message, end="\n")
    for i in range(1, 10):
        print(message + "-" + str(i), end="|", flush=True)
        sleep(sleeptimer)
    #sleep(randint(1, 6))
    print("Waiting for barrier with:", message)
    barrier.wait()
    print("Returning from printit:", message)
def callbackfunction():
    print("Execute callbackfunction() function")


#parties are the number of individual parties participating in the Barrier.  action is a callable object such as a function called after all the parties enter the barrier and before releasing the parties.  timeout is used as the default for all subsequent wait() calls on the barrier.
#The example can be changed to run using Process.  Change from threading import Barrier, Thread to from multiprocessing import Barrier, Process.  Change thread1 = Thread(target=printit, args=("A thread1", bbarrierobject, 0)) to process1 = Process(target=printit, args=("A process1", bbarrierobject, 0)).
print("Start main timeout 0")
bbarrierobject = Barrier(3, callbackfunction) #three parties.  callbackfunction invoked when all three parties reach the barrier.  The default timeout is None if no timeout specify.  RM:  I can't figure out the timeout.  The example is created outside of the Threads.
thread1 = Thread(target=printit, args=("A thread1", bbarrierobject, 0))
thread2 = Thread(target=printit, args=("B thread2", bbarrierobject, 0))
thread3 = Thread(target=printit, args=("C thread3", bbarrierobject, 0))
thread1.start()
thread2.start()
thread3.start()
print("End main timeout 0")
#The printit() function is ran three times concurrently.  All three invocations reach the barrier.wait() statement in a different order which they were started.  Once the three invocations reached barrier.wait(), the callbackfunction() is executed before the printit() function invocations can proceed.
'''
Start main timeout 0
printit for: A thread1
A thread1-1|A thread1-2|A thread1-3|A thread1-4|A thread1-5|A thread1-6|A thread1-7|A thread1-8|A thread1-9|Waiting for barrier with: A thread1
printit for: B thread2
B thread2-1|B thread2-2|B thread2-3|B thread2-4|B thread2-5|B thread2-6|B thread2-7|B thread2-8|B thread2-9|Waiting for barrier with: B thread2
printit for: C thread3
C thread3-1|C thread3-2|C thread3-3|C thread3-4|C thread3-5|C thread3-6|C thread3-7|C thread3-8|C thread3-9|Waiting for barrier with: C thread3
Execute callbackfunction() function
Returning from printit: C thread3
Returning from printit: A thread1
End main timeout 0
Returning from printit: B thread2
'''
#another result
'''
Start main timeout 0
printit for: A thread1
A thread1-1|A thread1-2|A thread1-3|A thread1-4|A thread1-5|A thread1-6|A thread1-7|A thread1-8|A thread1-9|Waiting for barrier with: A thread1
printit for: B thread2
B thread2-1|B thread2-2|B thread2-3|B thread2-4|B thread2-5|B thread2-6|B thread2-7|B thread2-8|B thread2-9|Waiting for barrier with: B thread2
printit for: C thread3
C thread3-1|C thread3-2|C thread3-3|C thread3-4|C thread3-5|C thread3-6|C thread3-7|C thread3-8|C thread3-9|Waiting for barrier with: C thread3
Execute callbackfunction() function
Returning from printit: C thread3
End main timeout 0
Returning from printit: B thread2
Returning from printit: A thread1
'''
print("Start main sleeptimer 1")
bbarrierobject = Barrier(3, callbackfunction)
thread1 = Thread(target=printit, args=("A thread1", bbarrierobject, 1))
thread2 = Thread(target=printit, args=("B thread2", bbarrierobject, 1))
thread3 = Thread(target=printit, args=("C thread3", bbarrierobject, 1))
thread1.start()
thread2.start()
thread3.start()
print("End main sleeptimer 1")
'''
Start main sleeptimer 1
printit for: A thread1
A thread1-1|printit for: B thread2
B thread2-1|printit for: C thread3
C thread3-1|End main sleeptimer 1
A thread1-2|B thread2-2|C thread3-2|A thread1-3|B thread2-3|C thread3-3|A thread1-4|B thread2-4|C thread3-4|A thread1-5|B thread2-5|C thread3-5|A thread1-6|B thread2-6|C thread3-6|A thread1-7|B thread2-7|C thread3-7|A thread1-8|B thread2-8|C thread3-8|A thread1-9|B thread2-9|C thread3-9|Waiting for barrier with: A thread1
Waiting for barrier with: B thread2
Waiting for barrier with: C thread3
Execute callbackfunction() function
Returning from printit: C thread3
Returning from printit: A thread1
Returning from printit: B thread2
'''
#another result
'''
Start main sleeptimer 1
printit for: A thread1
A thread1-1|printit for: B thread2
B thread2-1|printit for: C thread3
C thread3-1|End main sleeptimer 1
A thread1-2|C thread3-2|B thread2-2|A thread1-3|C thread3-3|B thread2-3|A thread1-4|B thread2-4|C thread3-4|C thread3-5|B thread2-5|A thread1-5|A thread1-6|C thread3-6|B thread2-6|C thread3-7|A thread1-7|B thread2-7|C thread3-8|A thread1-8|B thread2-8|A thread1-9|C thread3-9|B thread2-9|Waiting for barrier with: A thread1
Waiting for barrier with: C thread3
Waiting for barrier with: B thread2
Execute callbackfunction() function
Returning from printit: B thread2
Returning from printit: A thread1
Returning from printit: C thread3
'''
#Two or more Threads or Processes to cooperate on the timing of their behavior.  Use threading.Event or multiprocessing.Event.  An Event manages an internal flag which callers can either set() or clear().  Other threads can wait() for the flag to be set() blocking their own progress until allowed to continue by the Event.  The internal flag is set to False which ensures if a task gets to the Event, before it is set then it must wait.  Invoke wait with an optional timeout.  If you don't include the optional timeout, then wait() waits forever while wait(timeout) wait up to the timeout given in seconds.  If the timeout is reached, then the wait method returns False; otherwise wait returns True.
#The example is two processes sharing an event object.  The first process runs a function waiting for the event to be set.  The second process runs a function which sets the event and release the waiting process.
#The example can be changed to run using Threads.  Change from multiprocessing import Process, Event from threading import Thread, Event.  Change p1process = Process(target=waitforevent, args=[eventobject]) to t1thread = Thread(target=waitforevent, args=[eventobject]).
from multiprocessing import Process, Event
from time import sleep
def waitforevent(event):
    print("Entered and waiting in waitforevent() function")
    eventisset = event.wait()
    print("Event is set in waitforevent() function", eventisset)
def setevent(event, sleeptimer):
    print("Entered setevent() function.  Sleeping for", sleeptimer, "seconds")
    sleep(sleeptimer)
    print("Waking up and setting event in setevent() function")
    event.set()
    print("Event is set in setevent() function")


print("Start main sleeptimer 5")
eventobject = Event()
p1process = Process(target=waitforevent, args=[eventobject]) #Start a process to wait for event notification
p1process.start()
p2process = Process(target=setevent, args=[eventobject, 5]) #Set up a process to set the event
p2process.start()
p1process.join() #Wait for the first process to complete
print("Finsh main sleeptimer 5")
'''
Start main sleeptimer 5
Entered and waiting in waitforevent() function
Entered setevent() function.  Sleeping for 5 seconds
Waking up and setting event in setevent() function
Event is set in setevent() function
Event is set in waitforevent() function True
Finsh main sleeptimer 5
'''
print("Start main sleeptimer 0")
eventobject = Event()
p1process = Process(target=waitforevent, args=[eventobject]) #Start a process to wait for event notification
p1process.start()
p2process = Process(target=setevent, args=[eventobject, 0]) #Set up a process to set the event
p2process.start()
p1process.join() #Wait for the first process to complete
print("Finsh main sleeptimer 0")
'''
Start main sleeptimer 0
Entered and waiting in waitforevent() function
Entered setevent() function.  Sleeping for 0 seconds
Waking up and setting event in setevent() function
Event is set in setevent() function
Event is set in waitforevent() function True
Finsh main sleeptimer 0
'''
#The Lock class provides a mechanism for synchronizing access to a block of code.  The Lock object can be locked and unlocked.  The initial state being unlocked.  The Lock grants access to a single thread at a time.  Other threads must wait for the Lock to become free before progressing.  The acquire() method acquires the lock.  The release() method releases the lock.  The acquire() method changes a Lock object unlocked to locked.  acquire() method is blocked until a call to release() in another thread changes it to unlock.  Then the acquire() call resets it to lock.  The release() method should be called in the locked state.  release() method changes the state to unlocked.  If an attempt to release an unlocked lock, a RuntimeError is raised.
#The SharedData class uses locks to control access to readvalue() method and the changevalue() method.  The Lock object is held internally to the SharedData object.  Both methods attempt to acquire the lock before performing their behavior.  The lock is released after use.
#The readvalue() method locks and unlocks explicitly.  The changevalue() method uses a with statement to lock and unlock.  Both methods use a lock to control access to the methods.  One thread can gain access to the lock area at a time.  The reader() function may start to read data before the updater() function changes the data or vice versa.  For instance, the reader thread accesses the value 0 more than once before the updater update the self.value adding one.  The updater() function runs a second time before the reader gains access to locked block of code which is why the value 2 or another number is missed.
from threading import Thread, Lock
class SharedData(object):
    def __init__(self):
        self.value = 0
        self.lock = Lock()
    def readvalue(self):
        try:
            print("readvalue() function Acquiring Lock")
            self.lock.acquire()
            return self.value
        finally:
            print("readvalue() function Releasing Lock")
            self.lock.release()
    def changevalue(self):
        print("changevalue() function acquiring lock")
        with self.lock:
            self.value = self.value + 1
        print("changevalue() function lock released")


sharedataobject = SharedData()
def reader(counter=0):
    while counter <= 20:
        print(sharedataobject.readvalue())
        counter += 1
def updater(counter=0):
    while counter <= 20:
        sharedataobject.changevalue()
        counter += 1


print("Start main")
t1thread = Thread(target=reader)
t2thread = Thread(target=updater)
t1thread.start()
t2thread.start()
print("Finish main")
'''
Start main
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
0
Finish main
changevalue() function acquiring lock
changevalue() function lock released
...
changevalue() function acquiring lock
changevalue() function lock released
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
21
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
21
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
21
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
21
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
21
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
21
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
21
readvalue() function Acquiring Lock
readvalue() function Releasing Lock
21
'''
#Lock objects can be acquired once.  If a thread attempts to acquiare a lock on the same Lock object more than once, then a RuntimeError is thrown.  If it is necessary to reacquire a lock on a Lock object, then the threading.RLock class should be used which is a re-entrant Lock allowing the same Thread or Process to acquire a lock multiple times.  The code, however, release the lock as many times as it has acqure it.