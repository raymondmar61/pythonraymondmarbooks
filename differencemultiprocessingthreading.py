from threading import Thread
import os
import math
def calculatethreading():
    for i in range(0, 4000000):
        math.sqrt(i)
        #print(math.sqrt(i))


threads = []
for i in range(os.cpu_count()):
    print("Registering thread %d" % i)
    threads.append(Thread(target=calculatethreading))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

from multiprocessing import Process
import os
import math

def calculatemultiprocessing():
    for i in range(0, 4000000):
        math.sqrt(i)
        #print(math.sqrt(i))


processes = []
for i in range(os.cpu_count()):
    print("Registering thread %d" % i)
    processes.append(Process(target=calculatemultiprocessing))
for process in processes:
    process.start()
for process in processes:
    process.join()
