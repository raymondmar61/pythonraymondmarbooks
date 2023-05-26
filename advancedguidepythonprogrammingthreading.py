#Advanced Guide To Python 3 Programming by John Hunt Chapter 30 Threading
#Threading allows you to write programs that multitask.  It appears to do more than one thing at a time.
#The Thread class from the threading module represents an activity which is run in a separate thread of execution within a single process.  These threads of execution are lightweight, pre-emptive execution threads.  A thread is lightweight because it doesn't possess its own address space.  It's not treated as a separate entity by the host operating system.  It's not a process.  Threads exist within a single machine process using the same address space as other threads.
#A thread object created must be started.  A thread object is runnable once the thread object is started.  A thread object may switch back and forth between running and being runnable under the control of the scheduler.  The scheduler is responsible for managing multiple threads which want execution time.
#A thread object remains runnable or running until the run() method terminates.  A Thread may be in a waiting state when a thread is waiting for another thread to finish its work before continuing.  It's possible a thread is waiting because a thread is waiting for the results from another thread to continue.  The results from another thread to continue is achieved using the join() method.  Once the second thread completes the waiting thread becomes runnable.
#The thread currently executing is the active thread.
#A thread is considered to be alive unless its run() method terminates after which a thread is considered dead.  A live thread can be running, runable, waiting, etc.
#The runnable state indicates the thread can be executed by the processor not currently executing because an equal or higher priority process is executing.  The thread must wait until the processor becomes free.  The scheduler can move a thread between the running state and runnable state.
'''
There are two ways in which to initiate a new thread of execution:
1 Pass a reference to a callable object (such as a function or method) into the Thread class constructor. This reference acts as the target for the Thread to execute.
2 Create a subclass of the Thread class and redefine the run() method to perform the set of actions that the thread is intended to do.
'''
'''
Instantiating the Thread Class.  The Thread class can be found in the threading module and therefore must be imported prior to use. The class Thread defines a single constructor that takes up to six optional arguments:  class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)

1 group should be None; reserved for future extension when a ThreadGroup class is implemented.
2 target is the callable object to be invoked by the run() method. Defaults to None, meaning nothing is called.
3 name is the thread name. By default, a unique name is constructed of the form "Thread-N" where N is an integer.
4 args is the argument tuple for the target invocation. Defaults to (). If a single argument is provided the tuple is not required. If multiple arguments are provided then each argument is an element within the tuple.
5 kwargs is a dictionary of keyword arguments for the target invocation.  Defaults to {}.
6 daemon indicates whether this thread runs as a daemon thread or not. If not None, daemon explicitly sets whether the thread is daemonic. If None (the default), the daemonic property is inherited from the current thread.
'''
from threading import Thread
def simpleworker():
    print("Hello")


createnewthread1 = Thread(target=simpleworker) #createnewthread1 executes the function simpleworker.  The main code is executed by the main thread present when the program starts.  There are two threads used which are main and createnewthread1.
createnewthread1.start() #return Hello
'''
The Thread class defines all the facilities required to create an object that can execute within its own lightweight process. The key methods are:
1 start() Start the thread's activity. It must be called at most once per thread object. It arranges for the object's run() method to be invoked in a separate thread of control. This method will raise a RuntimeError if called more than once on the same thread object.
2 run() Method representing the thread's activity. You may override this method in a subclass. The standard run() method invokes the callable object passed to the object’s constructor as the target argument, if any, with positional and keyword arguments taken from the args and kwargs arguments, respectively. You should not call this method directly.
3 join(timeout = None) Wait until the thread sent this message terminates. This blocks the calling thread until the thread whose join()method is called terminates. When the timeout argument is present and not None, it should be a floating-point number specifying a timeout for the operation in seconds (or fractions thereof). A thread can be join()ed many times.
4 name A string used for identification purposes only. It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor. Giving a thread a name can be useful for debugging purposes.
5 ident The "thread identifier" of this thread or None if the thread has not been started. This is a nonzero integer.
6 is_alive() Return whether the thread is alive. This method returns True just before the run() method starts until just after the run() method terminates. The module function threading.enumerate() returns a list of all alive threads.
7 daemon A boolean value indicating whether this thread is a daemon thread (True) or not (False). This must be set before start() is called, otherwise a RuntimeError is raised. Its default value is inherited from the creating thread. The entire Python program exits when no alive non-daemon threads are left.
'''
createnewthread2 = Thread(target=simpleworker) #createnewthread2 executes the function simpleworker.  The main code is executed by the main thread present when the program starts.  There are two threads used which are main and createnewthread2.
createnewthread2.start() #return Hello
print(createnewthread2.getName()) #print Thread-2
print(createnewthread2.ident) #print 139858093799168
print(createnewthread2.is_alive()) #print False
#The join() method causes one thread to wait for another to complete.
from time import sleep
def workerfunction():
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(1)


print("Start")
readobject = Thread(target=workerfunction)
readobject.start()
readobject.join() #return ..........
print("\nDone")
def workerfunction(sleepnumber):
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(sleepnumber)


print("Start")
readobject1 = Thread(target=workerfunction(1))
readobject1.start()
readobject1.join() #return ..........
print("\nDone")
print("Start")
readobject0 = Thread(target=workerfunction(0))
readobject0.start()
readobject0.join() #return ..........
print("\nDone")
'''
The Threading Module Functions.  There are a set of threading module functions which support working with
threads; these functions include:
1 threading.active_count() Return the number of Thread objects currently alive. The returned count is equal to the length of the list returned by enumerate().
2 threading.current_thread() Return the current Thread object, corresponding to the caller’s thread of control. If the caller’s thread of control was not created through the threading module, a dummy thread object with limited functionality is returned.
3 threading.get_ident() Return the "thread identifier" of the current thread. This is a nonzero integer. Thread identifiers may be recycled when a thread exits and another thread is created.
4 threading.enumerate() Return a list of all Thread objects currently alive. The list includes daemon threads, dummy thread objects created by current_thread() and the main thread. It excludes terminated threads and threads that have not yet been started.
5 threading.main_thread()Return the main Thread object.
'''
def workerfunctionarguments(sleepnumber, letter):
    for i in range(0, 10):
        print(letter, end="", flush=True)
        sleep(sleepnumber)


print("Start")
thread1A = Thread(target=workerfunctionarguments, args=[1, "A"])
thread0B = Thread(target=workerfunctionarguments(0, "B"))
thread1C = Thread(target=workerfunctionarguments, args=[1, "C"])
thread2D = Thread(target=workerfunctionarguments(2, "D"))
thread1A.start()
thread0B.start()
thread1C.start()
thread2D.start()
print("Done")
'''
Start
BBBBBBBBBBDDDDDDDDDDACDone
CAACACACACACCAACA
#or
Start
BBBBBBBBBBDDDDDDDDDDACDone
CACACACAACACCACACA
'''
#The main thread is finished after the worker threads have only printed out a single letter each; however as long as there is at least one non-daemon thread running the program will not terminate; as none of these threads are marked as a daemon thread the program continues until the last thread has finished printing out the tenth of its letters. Also notice how each of the threads gets a chance to run on the processor before it sleeps again; thus we can see the letters A, B and C [and D] all mixed in together.
#Daemon Thread used for housekeeping tasks such as background data and backups.
def workerfunctiondaemon(sleepnumber, letter):
    for i in range(0, 10):
        print(letter, end="", flush=True)
        sleep(sleepnumber)


print("Start daemon")
daemonthread1A = Thread(daemon=True, target=workerfunctiondaemon, args=[1, "A"])
daemonthread0B = Thread(daemon=True, target=workerfunctiondaemon, args=[0, "B"])
daemonthread1C = Thread(daemon=True, target=workerfunctiondaemon, args=[1, "C"])
daemonthread1A.start()
daemonthread0B.start()
daemonthread1C.start()
print("Done daemon")
'''
Start daemon
ABBBBBBBBBBCDone daemon
'''
#Naming Threads assign a name to a thread
def workerfunctionnaming(sleepnumber, letter):
    for i in range(0, 10):
        print(letter, end="", flush=True)
        sleep(sleepnumber)


print("Start naming")
namingthread1A = Thread(name="1A", target=workerfunctionnaming, args=[1, "A"])
namingthread0B = Thread(name="0B", target=workerfunctionnaming, args=[0, "B"])
namingthread1C = Thread(name="1C", target=workerfunctionnaming, args=[1, "C"])
namingthread1A.start()
namingthread0B.start()
namingthread1C.start()
print("Done naming")
'''
Start naming
ABBBBBBBBBBCDone naming
CAACAACCCAACACCAACCAACCAACCACACAAACC
'''
#Each Thread requires its own copy of the data.  The shared memory or heap is difficiult to use as it's inherently shared between all threads.  Python provides a concept known as Thread-Local data whose values are associated with a thread instead of shared memory.  To create a thread-local data, create an instance of threading.local and store attributes into it.  The instances are thread specific.  One thread doesn't see the values stored by another thread.
from threading import Thread, local, currentThread
from random import randint
def showvaluefunction(data):
    """Access a value in the thread local data object value is present or not present with the try except"""
    try:
        valuevariable = data.value
    except AttributeError:
        print(currentThread().name, "no value yet.")
    else:
        print(currentThread().name, "yes there is a value which is", valuevariable)
def workerfunction(data):
    """Calls showvaluefunction() twice.  Once before it sets a data.value in the local data object and after it sets a data.value in the local data object."""
    showvaluefunction(data)
    data.value = randint(1, 100)
    print(currentThread().name, "at workerfunction random number is", data.value)
    showvaluefunction(data)
print("Start", currentThread().name)
localdata = local() #Create a local data object using local() function
showvaluefunction(localdata) #Call showvaluefunction().  Create two threads to execute the worker function passing the localdata object into the two threads.  Each thread is started.
for i in range(0, 4):
    threadobject = Thread(name="Thread name" + str(i), target=workerfunction, args=[localdata])
    threadobject.start()
showvaluefunction(localdata)
print("Done", currentThread().name)
'''
Start MainThread
MainThread no value yet.
Thread name0 no value yet.
Thread name0 at workerfunction random number is 92
Thread name0 yes there is a value which is 92
Thread name1 no value yet.
Thread name1 at workerfunction random number is 23
Thread name1 yes there is a value which is 23
Thread name2 no value yet.
Thread name2 at workerfunction random number is 58
Thread name2 yes there is a value which is 58
Thread name3 no value yet.
Thread name3 at workerfunction random number is 78
Thread name3 yes there is a value which is 78
MainThread no value yet.
Done MainThread
'''
#The Global Interpreter Lock or GIL protects access to Python objects by preventing multiple threads from executing at the same time.  No need to worry about the GIL when running low level programs.  GIL prevents multithreaded Python programs from taking full advantage of multiprocessor systems.  Python acts like a single CPU machine running one thing at a time.  It's impossible for standard Python threads to take advantage of multiple CPUs.  A solution is to use Python multiprocessing library.