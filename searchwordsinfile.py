#Parsing Text Files in Python [1uA-pLITer0]
def readfile():
    #open file read each line
    file = open("personlog.txt", "r")
    lines = file.readlines()
    file.close()
    #print the file line-by-line
    counterraymond = 0
    counterposey = 0
    for eachlines in lines:
        # eachlines = eachlines.strip() #removes the \n at the end of each line
        eachlines = eachlines.strip().lower() #removes the \n at the end of each line and converts all string to lower case
        print(eachlines) #print each line in file
        if eachlines.find("raymond") != -1:
            counterraymond += 1
        if eachlines.find("posey") != -1:
            counterposey += 1
    print("raymond", counterraymond) #print raymond 30
    print("posey", counterposey) #print posey 8


readfile()

a = "hello there"
print(a.find("there")) #print 6 which is the index number there is found
print(a.find("HELLO")) #print -1 which is didn't find HELLO
print(a.find("the")) #print 6 which is the index number the is found

#Python Find Most Common Words in a Document [Pcyuaj5lCtA]
import collections
import re #regular expression module
words = re.findall(r"\w+", open("personlog.txt").read().lower())
mostcommonwords = collections.Counter(words).most_common(10)
print(mostcommonwords) #print [('name', 57), ('from', 49), ('get', 38), ('returned', 38), ('raymond', 30), ('haku', 30), ('getname', 30), ('method', 30), ('in', 30), ('person', 30)]
print(words) #print ['get', 'name', 'returned', 'raymond', 'set', 'name', 'from', 'raymond', 'to', 'haku', 'get', 'name', 'returned', 'haku', 'get', 'name', 'returned', 'raymond', 'set', 'name', 'from', 'raymond', 'to', 'haku', 'get', 'name', 'returned', 'haku', 'get', 'name', 'returned', 'raymond', 'set', 'name', 'from', 'raymond', 'to', 'haku', 'get', 'name', 'returned', 'haku', 'get', 'name', 'returned', 'raymond', 'set', 'name', 'from', 'raymond', 'to', 'haku', 'get', 'name', 'returned', 'haku', 'get', 'name', 'returned', 'raymond', 'from', 'getname', 'method', 'in', 'person', 'class', 'set', 'name', 'from', 'raymond', 'to', 'haku', 'get', 'name', 'returned', 'haku', 'from', 'getname', 'method', 'in', 'person', 'class', 'get', 'name', 'returned', . . . ]
if "posey" in words:
    print("There is a posey") #print There is a posey
if "doesn't exist" in words:
    print("There is a doesn't exist")

#Python Search Text File Program [icdb5EFzwtc]
filename = "personlog.txt"
openfile = open(filename, "r")
counter = 0
for openfileline in openfile:
    if openfileline.startswith("get"):
        words = openfileline.split()
        print(words[0], words[1], words[2]) #print get name returned
        counter += 1
print("There were", counter, "get lines from " + filename) #print There were 38 get lines from personlog.txt
openfile.close()
filename = "personlog.txt"
openfile = open(filename, "r")
counter = 0
for openfileline in openfile:
    # if openfileline in "get": #doesn't work
    if openfileline.find("get") != -1:
        words = openfileline.split()
        print(words[0], words[1], words[2]) #print get name returned
        counter += 1
print("There were", counter, "get lines from " + filename) #print There were 38 get lines from personlog.txt
openfile.close()

#Read, write, and search text file with functions in Python [MvWfYvd65k4]
def main():
    filename = "temp.txt"
    # writefileexample(filename)
    # readfileexample(filename)
    searchfileexample(filename)
    return
def writefileexample(inputfile):
    name1 = input("Friend 1: ")
    name2 = input("Friend 2: ")
    name3 = input("Friend 3: ")
    openfile = open(inputfile, "w")
    openfile.write(name1 + "\n")
    openfile.write(name2 + "\n")
    openfile.write(name3 + "\n")
    openfile.close()
    return
def readfileexample(inputfile):
    openfile = open(inputfile, "r")
    contents = openfile.read()
    print(contents)
    openfile.close()
    return
def searchfileexample(inputfile):
    foundword = False
    searchword = "blake"
    openfile = open(inputfile, "r")
    readeachline = openfile.readline()
    while readeachline != "":
        readeachline = readeachline.rstrip("\n")
        print(readeachline)
        if readeachline == searchword:
            print("Found it " + readeachline)
            foundword = True
        readeachline = openfile.readline() #read the next line in the while loop
        '''
        jake
        blake
        Found it blake
        cake
        '''
    openfile.close()
    if not foundword:
        print(searchword + " not found")


main()
'''
Friend 1: jake
Friend 2: blake
Friend 3: cake
jake
blake
cake
'''

#How to list file names and file folder path _ Python Tutorial [t4va-o5mcBs]
import os
folderpath = r"/home/mar/python"
def listfilenames(directory):
    filenames = os.listdir(directory)
    for eachfilenames in filenames:
        print("File Name: " + eachfilenames)
        print("Folder Path: " + os.path.abspath(os.path.join(directory, eachfilenames)), sep="\n")


listfilenames(folderpath)
'''
File Name: twitterdownloadtweetsfinalv1.2.py
Folder Path: /home/mar/python/twitterdownloadtweetsfinalv1.2.py
File Name: myphotoalbum.html
Folder Path: /home/mar/python/myphotoalbum.html
File Name: mastermind147.py
Folder Path: /home/mar/python/mastermind147.py
File Name: encrypttextfile.txt
Folder Path: /home/mar/python/encrypttextfile.txt
...
'''
#RM:  also works in Linux
# if __name__ == "__main__":
#     listfilenames(folderpath)

#Search Through Directories to Find Keywords In Files with Python (Recursively) [hkii1p7jPFo]
import os
import uuid #universal unique identifier

listfilescontainsearchword = [] #store the name of the file having the search term
id = uuid.uuid4() #returns a random id number


def directorytosearchword():
    directorypath = "/home/mar/python"
    searchword = "The"
    searchfolder(directorypath, searchword)
def searchfolder(path, keyword):
    global listfilescontainsearchword
    directories = os.listdir(path)
    for eachdirectories in directories: #for eachdirectories listed includes files
        if eachdirectories.endswith(".txt"):
            try:
                file = open(path + "/" + eachdirectories, "r")
                #print(file) #print <_io.TextIOWrapper name='/home/mar/python/encrypttextfile.txt' mode='r' encoding='UTF-8'>
                if keyword in file.read():
                    listfilescontainsearchword.append(eachdirectories)
                    textfilecontainingsearchword = "/home/mar/python/" + keyword + "" + str(id) + ".txt"
                    print(textfilecontainingsearchword) #print /home/mar/python/Thea3c7a3dd-149d-4b9e-8522-45a0dc7e03f1.txt
                    with open(textfilecontainingsearchword, "a") as fileobject:
                        textfilecontainingfilepath = path + "/" + eachdirectories
                        print(path + "/" + eachdirectories) #print /home/mar/python/youtube-dl.txt
                        fileobject.write(str(textfilecontainingfilepath))
                        fileobject.write("\n")

                file.close()
            except:
                pass
        #There is another folder.  The another folder doesn't have a period as the file extension.  A subfolder inside the directorypath variable.  Recursively recursive elif.
        #try and except needed because NotADirectoryError: [Errno 20] Not a directory: '/home/mar/python/twitterdownloadtweetsfinalv1.2.py' error message
        elif "." not in eachdirectories.split(" "):
            try:
                searchfolder(path + "/" + eachdirectories, keyword)
            except:
                pass


directorytosearchword()
print(listfilescontainsearchword) #print ['youtube-dl.txt', 'youtube-dllistextractorswebsites.txt']
