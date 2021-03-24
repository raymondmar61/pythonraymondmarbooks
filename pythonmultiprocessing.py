#Reuven Lerner lerner.co.il Python Threading Multiprocessing.pdf
#Python's Global Interpreter Lock (GIL) ensures only one thread runs at a time.  Sometimes process can be better.  Processes are easier to deal with than threads because processes don't share data, safer, and less likely to corrupt things.  Processes don't worry about deadlocks, mutexes, and semaphores, making writing process-based programs far easier to understand and debut, and are more predictable.
#There are objections to using processes.  Processes are larger than threads consuming more resources and more overhead.  Processes are independent for program stability.  Processes are not good if you want to let different pieces communicate.  For example, someone presses a button on GUI to send a message in the background to update a text box.  With threads, one thread handles the request and display in the background.  The other thread shows the GUI in the background.  With processes, its harder for which the background or calculating process doesn't have access to the GUI.
#Python's subprocess module allows us to work with external processes.  The module is used to launch external programs in separate processes.  Run code in a separate process.  We use the multiprocessing module.  Multiprocessing looks and feels like threads which actually uses processes.  Multiprocessing let you share data in controlled and specified ways.  If your programs are CPU-bound or need parallelism and independence of processes, use multiprocessing.
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
for eachthreadslist in multiprocessinglist:
    multiprocessingvariable.join()
print(mylist) #print [10, 20, 30]