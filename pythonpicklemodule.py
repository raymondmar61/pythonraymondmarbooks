import pickle

#Using Pickle to write to and read from a file in Python -Part 3-
grades = {"andy": ["A", "A", "B"], "laura": ["B", "B", "A"], "sam": ["A", "B", "C"]}
print(grades) #print {'andy': ['A', 'A', 'B'], 'laura': ['B', 'B', 'A'], 'sam': ['A', 'B', 'C']}
print(grades["andy"]) #print ['A', 'A', 'B']
print(grades["andy"][2]) #print B
filename = "grades.txt"
createfile = open(filename, "wb")  #wb write binary
pickle.dump(grades, createfile) #create text file grades.txt with the grades dictionary
'''
grades.txt
8003 7d71 0028 5804 0000 0061 6e64 7971
015d 7102 2858 0100 0000 4171 0368 0358
0100 0000 4271 0465 5805 0000 006c 6175
7261 7105 5d71 0628 6804 6804 6803 6558
0300 0000 7361 6d71 075d 7108 2868 0368
0458 0100 0000 4371 0965 752e
'''
createfile.close()
readfile = open(filename, "rb") #rb read binary
loadfiletoread = pickle.load(readfile)
print(loadfiletoread) #print {'andy': ['A', 'A', 'B'], 'laura': ['B', 'B', 'A'], 'sam': ['A', 'B', 'C']}
print("Andy's grades: ", loadfiletoread["andy"]) #print Andy's grades:  ['A', 'A', 'B']
print("Andy's grades: ", loadfiletoread["andy"][2]) #print Andy's grades:  B
readfile.close()
editfile = open(filename, "wb")
grades["andy"][1] = "A*"
pickle.dump(grades, editfile)
editfile.close()
readfile = open(filename, "rb")
loadfiletoread = pickle.load(readfile)
print(loadfiletoread) #print {'andy': ['A', 'A*', 'B'], 'laura': ['B', 'B', 'A'], 'sam': ['A', 'B', 'C']}
print(loadfiletoread["andy"]) #print ['A', 'A*', 'B']

#Python Pickle Module for saving objects -serialization-
exampledictionary = {1: "6", 2: "2", 3: "f"}
pickleout = open("filenamedict.pickle", "wb")
pickle.dump(exampledictionary, pickleout)
'''
filenamedict.pickle
8003 7d71 0028 4b01 5801 0000 0036 7101
4b02 5801 0000 0032 7102 4b03 5801 0000
0066 7103 752e
'''
pickleout.close()
picklein = open("filenamedict.pickle", "rb")
readexampledictionary = pickle.load(picklein)
print(readexampledictionary) #{1: '6', 2: '2', 3: 'f'}

#Pickling Data With Python-
import numpy as np
datadictionary = {"volts": np.random.random(10), "current": np.random.random(10)}
print(datadictionary) #print {'volts': array([0.6240698 , 0.8339828 , 0.61809062, 0.1597007 , 0.76666477, 0.2401808 , 0.41191396, 0.9056749 , 0.21747809, 0.51328096]), 'current': array([0.06169582, 0.27808511, 0.44090432, 0.95971034, 0.04403591, 0.57499199, 0.29685635, 0.18778733, 0.53790769, 0.45414134])}
filename = "datadictionarypickle.pkl"
with open(filename, "wb") as objectnamepicklefile:
    pickle.dump(datadictionary, objectnamepicklefile)
    '''
    8003 7d71 0028 5805 0000 0076 6f6c 7473
    7101 636e 756d 7079 2e63 6f72 652e 6d75
    6c74 6961 7272 6179 0a5f 7265 636f 6e73
    6c74 6961 7272 6179 0a5f 7265 636f 6e73
    7472 7563 740a 7102 636e 756d 7079 0a6e
    6461 7272 6179 0a71 034b 0085 7104 4301
    6271 0587 7106 5271 0728 4b01 4b0a 8571
    0863 6e75 6d70 790a 6474 7970 650a 7109
    5802 0000 0066 3871 0a4b 004b 0187 710b
    5271 0c28 4b03 5801 0000 003c 710d 4e4e
    4e4a ffff ffff 4aff ffff ff4b 0074 710e
    6289 4350 28e6 4c3a 61f8 e33f 1d58 bfb4
    fcaf ea3f 6f07 5ef9 65c7 e33f 2c25 b89a
    1271 c43f 936d aa8b 8488 e83f c436 0397
    3ebe ce3f 3472 2d62 cc5c da3f 93f6 aaec
    49fb ec3f cccc ae6e 52d6 cb3f a9cb ec2e
    cc6c e03f 710f 7471 1062 5807 0000 0063
    7572 7265 6e74 7111 6802 6803 4b00 8571
    1268 0587 7113 5271 1428 4b01 4b0a 8571
    1568 0c89 4350 c0b3 6512 9896 af3f dc2e
    a878 25cc d13f d666 95bd c637 dc3f dd95
    da73 f2b5 ee3f f027 bbf8 df8b a63f a3fb
    da9a 5566 e23f a4be f3c4 b1ff d23f fcc8
    1c42 6a09 c83f 6e6f d72f 8a36 e13f 70cd
    a2d5 a610 dd3f 7116 7471 1762 752e 
    '''
with open(filename, "rb") as objectnamereadpicklefile:
    readpicklefile = pickle.load(objectnamereadpicklefile)
print(readpicklefile) #print {'volts': array([0.6240698 , 0.8339828 , 0.61809062, 0.1597007 , 0.76666477, 0.2401808 , 0.41191396, 0.9056749 , 0.21747809, 0.51328096]), 'current': array([0.06169582, 0.27808511, 0.44090432, 0.95971034, 0.04403591, 0.57499199, 0.29685635, 0.18778733, 0.53790769, 0.45414134])}

#Storing and retrieving Python objects with pickle
import pickle
dictionarynumber = {"a": 1, "b": 2, "c": 3}
serializationstring = pickle.dumps(dictionarynumber)
print(serializationstring) #print b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02X\x01\x00\x00\x00cq\x03K\x03u.'
deserializationstring = pickle.loads(serializationstring)
print(deserializationstring) #print {'a': 1, 'b': 2, 'c': 3}
print(deserializationstring == dictionarynumber) #print True; same values
print(deserializationstring is dictionarynumber) #print False; different dictionary.  Not same object in memory.
outfile = open("dictionarynumberfile.pkl", "wb")  #wb is write bytes being a byte string
pickle.dump(dictionarynumber, outfile)
'''
dictionarynumberfile.pkl
8003 7d71 0028 5801 0000 0061 7101 4b01
5801 0000 0062 7102 4b02 5801 0000 0063
7103 4b03 752e 
'''
outfile.close()
infile = open("dictionarynumberfile.pkl", "rb") #rb is read bytes being a byte string
openinfile = pickle.load(infile)
print(openinfile) #print {'a': 1, 'b': 2, 'c': 3}
print(openinfile == dictionarynumber) #print True; same values
print(openinfile is dictionarynumber) ##print False; different dictionary.  Not same object in memory.
class Fool():
    def __init__(self, x, y):
        self.x = x
        self.y = y


callclassfool = Fool(10, [100, 200, 300])
print(callclassfool) #print <__main__.Fool object at 0x7fcefa4ccb00>
print(vars(callclassfool)) #print {'x': 10, 'y': [100, 200, 300]}
classfooloutfile = open("classfoolpickle.pkl", "wb")
pickle.dump(callclassfool, classfooloutfile)
classfooloutfile.close()
classfoolinfile = open("classfoolpickle.pkl", "rb")
openclassfoolinfile = pickle.load(classfoolinfile)
print(type(openclassfoolinfile)) #print <class '__main__.Fool'>
print(vars(openclassfoolinfile)) #print {'x': 10, 'y': [100, 200, 300]}