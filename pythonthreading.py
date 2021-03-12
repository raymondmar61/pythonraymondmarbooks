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
