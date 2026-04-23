#Thread Pool Pattern in Python [tcQxnt_tB8Q]
import threading
from time import sleep
import timeit
from concurrent.futures import ThreadPoolExecutor

#Sleep thread for one second
def dojobfunction():
    sleep(1)

#Thread pool code one worker and one job or one task
def executefunction():
    executor = ThreadPoolExecutor(max_workers=1)
    runthreadtrackthreadexecuted = executor.submit(dojobfunction)
    runthreadtrackthreadexecuted.result()
#Thread pool code one worker and two jobs or two tasks one at a time
def executefunctionfirstthensecond():
    executor = ThreadPoolExecutor(max_workers=1)
    runthreadtrackthreadexecuted = executor.submit(dojobfunction)
    runthreadtrackthreadexecuted.result()
    runthreadtrackthreadexecuted = executor.submit(dojobfunction)
    runthreadtrackthreadexecuted.result()
#Thread pool code one worker and two jobs or two tasks submit both at the same time; second must wait for the first
def executefunctionsecondwaitsforfirst():
    executor = ThreadPoolExecutor(max_workers=1)
    runthreadtrackthreadexecuted1 = executor.submit(dojobfunction)
    runthreadtrackthreadexecuted2 = executor.submit(dojobfunction)
    runthreadtrackthreadexecuted1.result()
    runthreadtrackthreadexecuted2.result()
#Thread pool code two workers and two jobs or two tasks submit both at the same time; first and second work at the same time
def executefunctiontwoworkersfirstsecondcompletedsametime():
    executor = ThreadPoolExecutor(max_workers=2)
    runthreadtrackthreadexecuted1 = executor.submit(dojobfunction)
    runthreadtrackthreadexecuted2 = executor.submit(dojobfunction)
    runthreadtrackthreadexecuted1.result()
    runthreadtrackthreadexecuted2.result()

test = timeit.timeit(executefunction, number=1) #number=1 means execute the executefunction one time
print("Test result executefunction: " + str(test) + "s") #print Test result executefunction: 1.0021687119997296s
test = timeit.timeit(executefunctionfirstthensecond, number=1)
print("Test result executefunctionfirstthensecond: " + str(test) + "s") #print Test result executefunctionfirstthensecond: 2.006740119999904s
test = timeit.timeit(executefunctionsecondwaitsforfirst, number=1)
print("Test result executefunctionsecondwaitsforfirst: " + str(test) + "s") #print Test result executefunctionsecondwaitsforfirst: 2.0025115779999396s
test = timeit.timeit(executefunctiontwoworkersfirstsecondcompletedsametime, number=1)
print("Test result executefunctiontwoworkersfirstsecondcompletedsametime: " + str(test) + "s") #print Test result executefunctiontwoworkersfirstsecondcompletedsametime: 1.0030087970003478s

#Thread Pools in Python - Asynchronous Programming [2Koubj0fF9U]
import time
from concurrent.futures import ThreadPoolExecutor

def workerfunction(number):
    print(f"Calculating the result for number {number}")
    time.sleep(2)
    return number ** 2


createthreadpool2workers = ThreadPoolExecutor(2) #The number 2 is the number of individual threads or number of maximum workers
worker1 = createthreadpool2workers.submit(workerfunction, 7) #Submit the number 7.  First worker submits the number 7 to workerfunction.
worker2 = createthreadpool2workers.submit(workerfunction, 9) #Submit the number 9.  Second worker submits the number 9 to workerfunction.
worker3 = createthreadpool2workers.submit(workerfunction, 5) #Submit the number 5.  Third worker submits the number 5 to workerfunction.
worker4 = createthreadpool2workers.submit(workerfunction, 5) #Submit the number 5.  Fourth worker submits the number 5 to workerfunction.
worker5 = createthreadpool2workers.submit(workerfunction, 8) #Submit the number 8.  Fifth worker submits the number 8 to workerfunction.
print(worker3.done()) #print False.  Check if worker3 worker completed the assigned task.
print(worker3.result()) #print 25.  Result method to get the completed task.  Result is printed when available after worker3 is completed the task.
print(worker3.done()) #print True.  Check if worker3 worker completed the assigned task.
print("Hello World.  Printed immediately.  Anything after the createthreadpool2workers submissions is executed in the main thread afterwards.  createthreadpool2workers submissions are being completed in their own threads.")
createthreadpool2workers.shutdown() #abort all threads for createthreadpool2workers
print("\n")
createthreadpool5workers = ThreadPoolExecutor(5) #The number 5 is the number of individual threads or number of maximum workers
worker1 = createthreadpool5workers.submit(workerfunction, 7) #Submit the number 7.  First worker submits the number 7 to workerfunction.
worker2 = createthreadpool5workers.submit(workerfunction, 9) #Submit the number 9.  Second worker submits the number 9 to workerfunction.
worker3 = createthreadpool5workers.submit(workerfunction, 5) #Submit the number 5.  Third worker submits the number 5 to workerfunction.
worker4 = createthreadpool5workers.submit(workerfunction, 5) #Submit the number 5.  Fourth worker submits the number 5 to workerfunction.
worker5 = createthreadpool5workers.submit(workerfunction, 8) #Submit the number 8.  Fifth worker submits the number 8 to workerfunction.

#Python Concurrent Futures - ThreadPoolExecutor & ProcessPoolExecutor [nRVT4olRbMA]
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

#Function to compute the sum of squares
def sumofsquares(n):
    return sum(i * i for i in range(n))


#No Process Pool Executor
numbers = [10000000, 20000000, 30000000, 40000000]
start = time.time()
results = [sumofsquares(n) for n in numbers]
end = time.time()
print("results: ", results) #print results:  [333333283333335000000, 2666666466666670000000, 8999999550000005000000, 21333332533333340000000]
print(f"Time {end-start:.2f} seconds") #print Time 6.87 seconds

#Yes Processor Pool Executor
numbers = [10000000, 20000000, 30000000, 40000000]
start = time.time()
with ProcessPoolExecutor() as executorvariable:
    results = list(executorvariable.map(sumofsquares, numbers))
end = time.time()
print("results: ", results) #print results:  [333333283333335000000, 2666666466666670000000, 8999999550000005000000, 21333332533333340000000]
print(f"Time {end-start:.2f} seconds") #print Time 2.82 seconds

#Yes Thread Pool Executor
numbers = [10000000, 20000000, 30000000, 40000000]
start = time.time()
with ThreadPoolExecutor() as executorvariable:
    results = list(executorvariable.map(sumofsquares, numbers))
end = time.time()
print("results: ", results) #print results:  [333333283333335000000, 2666666466666670000000, 8999999550000005000000, 21333332533333340000000]
print(f"Time {end-start:.2f} seconds") #print Time 6.96 seconds

#Python 3 - Episode 45 - Thread Pools [BagTTT7l1pU]
import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

def testfunctionrunonathread(item):
    s = random.randrange(1, 5)
    logging.info(f"Thread {item}: id = {threading.get_ident()}")
    logging.info(f"Thread {item}: name = {threading.current_thread().name}")
    logging.info(f"Thread {item}: sleep for {s}")
    time.sleep(s)
    logging.info(f"Thread {item}: finished")

def mainfunction():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt="%H:%M:%S", level=logging.DEBUG)
    logging.info("Start")
    #Threaded Python code
    numberofworkerthreads = 5
    numberofitems = 15
    with ThreadPoolExecutor(max_workers=numberofworkerthreads) as executorvariable:
        executorvariable.map(testfunctionrunonathread, range(numberofitems))
    logging.info("Finished")


if __name__ == "__main__":
    mainfunction()
'''
INFO - 17:43:47: Start
INFO - 17:43:47: Thread 0: id = 139010461660736
INFO - 17:43:47: Thread 0: name = ThreadPoolExecutor-0_0 #Thread 0 or worker number 1 said I'm available for work
INFO - 17:43:47: Thread 0: sleep for 3
INFO - 17:43:47: Thread 1: id = 139010453268032
INFO - 17:43:47: Thread 1: name = ThreadPoolExecutor-0_1
INFO - 17:43:47: Thread 1: sleep for 3
INFO - 17:43:47: Thread 2: id = 139010374628928
INFO - 17:43:47: Thread 2: name = ThreadPoolExecutor-0_2 #Thread 2 or worker number 3 said I'm available for work
INFO - 17:43:47: Thread 2: sleep for 1
INFO - 17:43:47: Thread 4: id = 139010357843520
INFO - 17:43:47: Thread 4: name = ThreadPoolExecutor-0_4
INFO - 17:43:47: Thread 3: id = 139010366236224
INFO - 17:43:47: Thread 3: name = ThreadPoolExecutor-0_3
INFO - 17:43:47: Thread 4: sleep for 3
INFO - 17:43:47: Thread 3: sleep for 2
INFO - 17:43:48: Thread 2: finished #Thread 2 or worker number 3 said work completed
INFO - 17:43:48: Thread 5: id = 139010374628928
INFO - 17:43:48: Thread 5: name = ThreadPoolExecutor-0_2
INFO - 17:43:48: Thread 5: sleep for 2
INFO - 17:43:49: Thread 3: finished
INFO - 17:43:49: Thread 6: id = 139010366236224
INFO - 17:43:49: Thread 6: name = ThreadPoolExecutor-0_3
INFO - 17:43:49: Thread 6: sleep for 2
INFO - 17:43:50: Thread 1: finished
INFO - 17:43:50: Thread 7: id = 139010453268032
INFO - 17:43:50: Thread 7: name = ThreadPoolExecutor-0_1
INFO - 17:43:50: Thread 7: sleep for 4
INFO - 17:43:50: Thread 4: finished
INFO - 17:43:50: Thread 8: id = 139010357843520
INFO - 17:43:50: Thread 8: name = ThreadPoolExecutor-0_4
INFO - 17:43:50: Thread 8: sleep for 1
INFO - 17:43:50: Thread 0: finished #Thread 0 or worker number 1 said work completed
INFO - 17:43:50: Thread 9: id = 139010461660736
INFO - 17:43:50: Thread 9: name = ThreadPoolExecutor-0_0
INFO - 17:43:50: Thread 9: sleep for 1
INFO - 17:43:50: Thread 5: finished
INFO - 17:43:50: Thread 10: id = 139010374628928
INFO - 17:43:50: Thread 10: name = ThreadPoolExecutor-0_2
INFO - 17:43:50: Thread 10: sleep for 4
INFO - 17:43:51: Thread 9: finished
INFO - 17:43:51: Thread 11: id = 139010461660736
INFO - 17:43:51: Thread 11: name = ThreadPoolExecutor-0_0
INFO - 17:43:51: Thread 11: sleep for 2
INFO - 17:43:51: Thread 8: finished
INFO - 17:43:51: Thread 12: id = 139010357843520
INFO - 17:43:51: Thread 12: name = ThreadPoolExecutor-0_4
INFO - 17:43:51: Thread 12: sleep for 1
INFO - 17:43:51: Thread 6: finished
INFO - 17:43:51: Thread 13: id = 139010366236224
INFO - 17:43:51: Thread 13: name = ThreadPoolExecutor-0_3
INFO - 17:43:51: Thread 13: sleep for 4
INFO - 17:43:52: Thread 12: finished
INFO - 17:43:52: Thread 14: id = 139010357843520
INFO - 17:43:52: Thread 14: name = ThreadPoolExecutor-0_4
INFO - 17:43:52: Thread 14: sleep for 4
INFO - 17:43:53: Thread 11: finished
INFO - 17:43:54: Thread 10: finished
INFO - 17:43:54: Thread 7: finished
INFO - 17:43:55: Thread 13: finished
INFO - 17:43:56: Thread 14: finished
INFO - 17:43:56: Finished
'''