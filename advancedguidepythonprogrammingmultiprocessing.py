#Advanced Guide To Python 3 Programming by John Hunt Chapter 31 Multiprocessing
#The multiprocessing library supports separate processes to execute behaviors such as functions or methods using an API.  Multiprocessing avoids the limitation from the Global Interpreter Lock or GIL by using separate operating system processes instead of lightweight threads which runs within a single process.  Multiprocessing allows developers to exploit the multiple processor environment allowing multiple operations to run in parallel.
#The Process class is the multiprocessing library equivalent to the Thread class in the threading library.  Create a new instance of the Process class and call the start() method.  When a new Process is created, it runs within a separate process on the underlying operating systems.  In contrast, a Thread runs within the same process as the original program.  The process is managed and executed on one processor.  The downside using Process is Process takes more work to set up than the lighter weight Threads.
'''
The constructor for the Process class is the same set of arguments as the Thread class: class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)
1 group should always be None; it exists solely for compatibility with the Threading API.
2 target is the callable object to be invoked by the run() method. It defaults to None, meaning nothing is called.
3 name is the process name.
4 args is the argument tuple for the target invocation.
5 kwargs is a dictionary of keyword arguments for the target invocation.
6 daemon argument sets the process daemon flag to True or False.  If None (the default), this flag will be inherited from the creating process.
As with the Thread class, the Process constructor should always be called using keyword arguments.
The Process class also provides a similar set of methods to the Thread class
1 start() Start the process’s activity. This must be called at most once per process object. It arranges for the object’s run() method to be invoked in a separate process.
2 join([timeout]) If the optional argument timeout is None (the default), the method blocks until the joined process terminates. If timeout is a positive number, it blocks at most timeout seconds. Note that the method returns None if its process terminates or if the method times out.
3 is_alive() Return whether the process is alive. Roughly, a process object is alive from the moment the start() method returns until the child process terminates.
The process class also has several attributes:
1 name The process’s name. The name is a string used for identification purposes only. It has no semantics. Multiple processes may be given the same name. It can be useful for debugging purposes.
2 daemon The process’s daemon flag, a boolean value. This must be set before start() is called. The default value is inherited from the creating process. When a process exits, it attempts to terminate all of its daemonic child processes. Note that a daemonic process is not allowed to create child processes.
3 pid Return the process ID. Before the process is spawned, this will be None.
4 exitcode The process exit code. This will be None if the process has not yet terminated. A negative value -N indicates that the child was terminated by signal N.
In addition to these methods and attributes, the Process class also defines additional process related methods including:
1 terminate() Terminate the process.
2 kill() Same as terminate() except that on Unix the SIGKILL signal is used instead of the SIGTERM signal.
3 close() Close the Process object, releasing all resources associated with it. ValueError is raised if the underlying process is still running. Once close() returns successfully, most of the other methods and attributes of the Process object will raise a ValueError.
'''
#The following simple program creates three Process objects; each runs the function worker(), with the string arguments A, B and C respectively. These three process objects are then started using the start() method.
from multiprocessing import Process
from time import sleep

# def workerfunction(messageletter, sleepnumber):
#     for i in range(0, 10):
#         print(messageletter, end="", flush=True)
#         sleep(sleepnumber)


# print("Start workerfunction")
# lettera1 = Process(target=workerfunction, args=["A", 1])
# letterb0 = Process(target=workerfunction, args=["B", 0])
# letterc0 = Process(target=workerfunction("C", 0))
# lettera1.start()
# letterb0.start()
# letterc0.start()
# print("Done workerfunction")
'''
Start workerfunction
CCCCCCCCCCADone workerfunction
BBBBBBBBBBAAAAAAAAA
'''
#The main difference between the Thread and Process versions is that the Process version runs the worker function in separate processes whereas in the Thread version all the Threads share the same process.
from multiprocessing import Process, Pipe
from time import sleep
def workerfunction(connectionvariable):
    print("Worker started new sleeping for 1 second")
    sleep(1)
    print("Worker sending data via Pipe")
    connectionvariable.send("Hello")
    print("Worker closing worker end of connection")
    connectionvariable.close()
def main():
    print("Main function starting to create the pipe")
    mainconnection, workerconnection = Pipe()
    print("Main function setting up the process.  Go to workerfunction with workerconnection Pipe() created")
    processinstance = Process(target=workerfunction, args=[workerconnection])
    print("Main function start the process")
    processinstance.start()
    print("Main function waiting for a response from the child processor")
    print(mainconnection.recv())
    print("Main function closing parent process end connection")
    mainconnection.close()
    print("Main done")


main()
'''
Main function starting to create the pipe
Main function setting up the process.  Go to workerfunction with workerconnection Pipe() created
Main function start the process
Main function waiting for a response from the child processor
Worker started new sleeping for 1 second
Worker sending data via Pipe
Worker closing worker end of connection
Hello
Main function closing parent process end connection
Main done
'''
#In general, avoid sharing state between separate processes.  If it's unavoidable, then the multiprocessing library provides two wasy in which the state (data) can be shared.  These are Shared Memory and Server Process.