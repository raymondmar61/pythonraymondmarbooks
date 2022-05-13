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

#Extract Text from PDF with Python [0B5N6Xt5K8Q]  #RM:  doesn't work
# from PyPDF2 import PdfFileReader
from PyPDF4 import PdfFileReader

pdffileobject = PdfFileReader("magnummaniamaddogsandenglishmen.pdf")
pdffilepageoneobject = pdffileobject.getPage(0)  #Index starts at zero.  Page one index 0.  Page ten index 9.
print(pdffilepageoneobject) #print {'/Type': '/Page', '/Resources': {'/ProcSet': ['/PDF', '/Text', '/ImageB', '/ImageC', '/ImageI'], '/ExtGState': {'/G3': IndirectObject(3, 0), '/G8': IndirectObject(8, 0)}, '/XObject': {'/X5': IndirectObject(5, 0), '/X6': IndirectObject(6, 0), '/X7': IndirectObject(7, 0), '/X9': IndirectObject(9, 0)}, '/Font': {'/F4': IndirectObject(4, 0), '/F10': IndirectObject(10, 0), '/F11': IndirectObject(11, 0)}}, '/MediaBox': [0, 0, 612, 792], '/Annots': [IndirectObject(12, 0), IndirectObject(13, 0), IndirectObject(14, 0), IndirectObject(15, 0), IndirectObject(16, 0), IndirectObject(17, 0), IndirectObject(18, 0), IndirectObject(19, 0), IndirectObject(20, 0), IndirectObject(21, 0), IndirectObject(22, 0), IndirectObject(23, 0), IndirectObject(24, 0), IndirectObject(25, 0), IndirectObject(26, 0), IndirectObject(27, 0), IndirectObject(28, 0), IndirectObject(29, 0), IndirectObject(30, 0), IndirectObject(31, 0), IndirectObject(32, 0), IndirectObject(33, 0), IndirectObject(34, 0), IndirectObject(35, 0), IndirectObject(36, 0), IndirectObject(37, 0), IndirectObject(38, 0), IndirectObject(39, 0), IndirectObject(40, 0)], '/Contents': IndirectObject(41, 0), '/StructParents': 0, '/Parent': IndirectObject(55, 0)}  RM:  StructParents is the index position of the page which the object is representing.  '/StructParents': 0 is pdf page 1.  '/StructParents': 1 is pdf page 2.
pdffilepageonetext = pdffilepageoneobject.extractText()
print(pdffilepageonetext)


pdffile = open("lynaldenmay2022.pdf", "rb")
pdfread = PdfFileReader(pdffile)
print(pdfread.getNumPages()) #print {'/Type': '/Page', '/Resources': {'/ProcSet': ['/PDF', '/Text', '/ImageB', '/ImageC', '/ImageI'], '/ExtGState': {'/G3': IndirectObject(3, 0), '/G8': IndirectObject(8, 0)}, '/XObject': {'/X5': IndirectObject(5, 0), '/X6': IndirectObject(6, 0), '/X7': IndirectObject(7, 0), '/X9': IndirectObject(9, 0)}, '/Font': {'/F4': IndirectObject(4, 0), '/F10': IndirectObject(10, 0), '/F11': IndirectObject(11, 0)}}, '/MediaBox': [0, 0, 612, 792], '/Annots': [IndirectObject(12, 0), IndirectObject(13, 0), IndirectObject(14, 0), IndirectObject(15, 0), IndirectObject(16, 0), IndirectObject(17, 0), IndirectObject(18, 0), IndirectObject(19, 0), IndirectObject(20, 0), IndirectObject(21, 0), IndirectObject(22, 0), IndirectObject(23, 0), IndirectObject(24, 0), IndirectObject(25, 0), IndirectObject(26, 0), IndirectObject(27, 0), IndirectObject(28, 0), IndirectObject(29, 0), IndirectObject(30, 0), IndirectObject(31, 0), IndirectObject(32, 0), IndirectObject(33, 0), IndirectObject(34, 0), IndirectObject(35, 0), IndirectObject(36, 0), IndirectObject(37, 0), IndirectObject(38, 0), IndirectObject(39, 0), IndirectObject(40, 0)], '/Contents': IndirectObject(41, 0), '/StructParents': 0, '/Parent': IndirectObject(55, 0)}
pageinfo = pdfread.getPage(0)
print(pageinfo.extractText()) #print 39
pageinfopage1 = pageinfo.extractText()
print(pageinfopage1)

#Python File Handling - How to Read & Write Files With 5 Examples [b9rSczloSeA]
fileobjectoldway = open("findtheneedle.txt", "r")
fileobjectoldway.close()
with open("findtheneedle.txt", "r") as fileobjectoneline:
    #print(type(fileobjectoneline.read())) #print <class 'str'>
    print(fileobjectoneline.read())
    '''
    This is the sys module series
    and it is almost done

    we are nearly done
    just a few more videos
    that I need to get done
    '''
with open("findtheneedle.txt", "r") as fileobjectlist:
    print(fileobjectlist.readlines()) #print ['This is the sys module series\n', 'and it is almost done\n', '\n', 'we are nearly done\n', 'just a few more videos\n', 'that I need to get done']
with open("findtheneedle.txt", "r") as fileobjectprintonelineperreadline:
    print(fileobjectprintonelineperreadline.readline()) #print This is the sys module series\n
    print(fileobjectprintonelineperreadline.readline()) #print and it is almost done\n
    print(fileobjectprintonelineperreadline.readline()) #print \n
    print(fileobjectprintonelineperreadline.readline()) #print we are nearly done\n
with open("findtheneedle.txt", "r") as fileobjectnumberoflines:
    print(len(fileobjectnumberoflines.readlines())) #print 6
#Count words in a file
with open("findtheneedle.txt", "r") as fileobjectsplit:
    print(fileobjectsplit.read().split()) #print ['This', 'is', 'the', 'sys', 'module', 'series', 'and', 'it', 'is', 'almost', 'done', 'we', 'are', 'nearly', 'done', 'just', 'a', 'few', 'more', 'videos', 'that', 'I', 'need', 'to', 'get', 'done']
with open("findtheneedle.txt", "r") as fileobjectwordcounter:
    print(len(fileobjectwordcounter.read().split())) #print 26
#Format a file
with open("utopiayoutubedl.txt", "r") as yesblanklines, open("utopiayoutubedlnoblanklines", "w") as noblanklines:
    yesblanklinesvariable = yesblanklines.readlines()
    #print(yesblanklinesvariable) #print ['youtube-dl --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=Eg7yCvc0yGI.  youtube-dl --write-auto-sub https://www.youtube.com/watch?v=VD-fBj4d9Ck.\n', '\n', 'Download all the videos in the YouTube playlist youtube-dl -f best -ciw --playlist-start 1 *playlist URL*.  Select a range of playlist videos youtube-dl  -f best -ciw --playlist-items startnumber-endnumber *playlist URL*\n', '\n', '\n', 'youtube-dl -f best -u inin611@gmail.com -p hitsugayamatsumoto --write-auto-sub --sub-lang en --playlist-start 1 https://www.youtube.com/playlist?list=PL_jIDr2tZiuRHlp-bLwYNgWaFAp6dR7_\n', '\n', 'youtube-dl -f best -u, --username inin611@gmail.com -p, --password hitsugayamatsumoto --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=-8Vu3Hyv_Vk\n', 'youtube-dl -f best --username inin611@gmail.com --password hitsugayamatsumoto --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=-8Vu3Hyv_Vk\n', 'youtube-dl -f best -u inin611@gmail.com -p hitsugayamatsumoto --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=-8Vu3Hyv_Vk\n', "youtube-dl -f best -u 'inin611@gmail.com' -p 'hitsugayamatsumoto' --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=-8Vu3Hyv_Vk\n", 'youtube-dl -f best --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=gTXyTbMa1_w\n', 'youtube-dl -f best --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=IDKUyL4yXrQ\n', 'youtube-dl -f best --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=WyIXO4IVz_c\n', 'youtube-dl -f best --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=8paeqlO98pM\n', 'youtube-dl -f best --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=cKW1F_xMOFc\n', '\n', 'youtube-dl -v --list-subs https://www.youtube.com/watch?v=gTXyTbMa1_w\n', 'youtube-dl --sub-lang en --write-auto-sub --sub-format vtt --skip-download https://www.youtube.com/watch?v=gTXyTbMa1_w\n', 'youtube-dl --write-sub --sub-lang en --skip-download https://www.youtube.com/watch?v=gTXyTbMa1_w  <--WORKED']
    for eachline in yesblanklinesvariable:
        #print(eachline)
        '''
        youtube-dl --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=Eg7yCvc0yGI.  youtube-dl --write-auto-sub https://www.youtube.com/watch?v=VD-fBj4d9Ck.



        Download all the videos in the YouTube playlist youtube-dl -f best -ciw --playlist-start 1 *playlist URL*.  Select a range of playlist videos youtube-dl  -f best -ciw --playlist-items startnumber-endnumber *playlist URL*





        youtube-dl -f best -u inin611@gmail.com -p hitsugayamatsumoto --write-auto-sub --sub-lang en --playlist-start 1 https://www.youtube.com/playlist?list=PL_jIDr2tZiuRHlp-bLwYNgWaFAp6dR7_



        youtube-dl -f best -u, --username inin611@gmail.com -p, --password hitsugayamatsumoto --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=-8Vu3Hyv_Vk
        ...
        '''
        if eachline.strip() != "":
            print(eachline.strip())
            '''
            youtube-dl --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=Eg7yCvc0yGI.  youtube-dl --write-auto-sub https://www.youtube.com/watch?v=VD-fBj4d9Ck.
            Download all the videos in the YouTube playlist youtube-dl -f best -ciw --playlist-start 1 *playlist URL*.  Select a range of playlist videos youtube-dl  -f best -ciw --playlist-items startnumber-endnumber *playlist URL*
            youtube-dl -f best -u inin611@gmail.com -p hitsugayamatsumoto --write-auto-sub --sub-lang en --playlist-start 1 https://www.youtube.com/playlist?list=PL_jIDr2tZiuRHlp-bLwYNgWaFAp6dR7_
            youtube-dl -f best -u, --username inin611@gmail.com -p, --password hitsugayamatsumoto --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=-8Vu3Hyv_Vk
            ...
            '''
            noblanklines.write(eachline.strip())
            noblanklines.write("\n") #add a new line which is not a blank line between two lines with string
#Read all files in a directory and combine them into a single file
#Created four text files day1.txt, day2.txt, day2afternoon.txt, and day3.txt in journal directory
import os
filesindirectory = os.listdir("/home/mar/python/journal")
print(filesindirectory) #print ['day2.txt', 'day2afternoon.txt', 'day3.txt', 'day1.txt']
with open("combinetextfiles.txt", "w") as combinetextfilesinonefile:
    for eachfilesindirectory in filesindirectory:
        #print(eachfilesindirectory)
        '''
        day2.txt
        day2afternoon.txt
        day3.txt
        day1.txt
        '''
        directoryandfilename = "/home/mar/python/journal/" + eachfilesindirectory #python program is executed not in /home/mar/python/journal.  Executed in /home/mar/python/.
        #print(directoryandfilename)
        '''
        /home/mar/python/journal/day2.txt
        /home/mar/python/journal/day2afternoon.txt
        /home/mar/python/journal/day3.txt
        /home/mar/python/journal/day1.txt
        '''
        with open(directoryandfilename, "r") as eachfile:
            #print(eachfile.read())
            '''
            I wrote some Python today.
            I wrote even more Python.
            Today I planned to write some code, but I watched YouTube instead.
            Today I learned how to use the open function in Python.
            '''
            combinetextfilesinonefile.write("File name " + directoryandfilename)
            combinetextfilesinonefile.write("\n")
            combinetextfilesinonefile.write(eachfile.read())
            combinetextfilesinonefile.write("\n")
            combinetextfilesinonefile.write("\n")
            '''
            File name /home/mar/python/journal/day2.txt
            I wrote some Python today.

            File name /home/mar/python/journal/day2afternoon.txt
            I wrote even more Python.

            File name /home/mar/python/journal/day3.txt
            Today I planned to write some code, but I watched YouTube instead.

            File name /home/mar/python/journal/day1.txt
            Today I learned how to use the open function in Python.
            '''
            # savesentenceinvariable = eachfile.read()  #RM:  save the .read() in variable because .read() is used once
            # if "wrote" in savesentenceinvariable:
            #     print("love")
            #     combinetextfilesinonefile.write("File name " + directoryandfilename)
            #     combinetextfilesinonefile.write("\n")
            #     combinetextfilesinonefile.write(savesentenceinvariable)
            #     combinetextfilesinonefile.write("\n")
            #     combinetextfilesinonefile.write("\n")
with open("simple.html", "r") as fileobjectoneline:
    eachlinevariable = fileobjectoneline.readlines()  #RM:  save the .readlines() in eachlinevariable because .readlines() is used once
    for x in eachlinevariable:
        if "article" in x:
            print(x.strip()) #added .strip() to remove tab spaces
            '''
            <div class="article">
            <h2><a href="article_1.html">Article 1 Headline</a></h2>
            <p>This is a summary of article 1</p>
            <div class="article">
            <h2><a href="article_2.html">Article 2 Headline</a></h2>
            <p>This is a summary of article 2</p>
            '''
with open("simple.html", "rb") as fileobjectoneline:
    eachlinevariable = fileobjectoneline.readlines()  #RM:  save the .read() in eachlinevariable because .read() is used once
    print(type(eachlinevariable)) #print <class 'list'>
    print(eachlinevariable)
    '''
    [b'<!doctype html>\n', b'<html class="no-js" lang="">\n', b'    <head>\n', b'        <title>Test - A Sample Website</title>\n', b'        <meta charset="utf-8">\n', b'        <link rel="stylesheet" href="css/normalize.css">\n', b'        <link rel="stylesheet" href="css/main.css">\n', b'    </head>\n', b'    <body>\n', b"        <h1 id='site_title'>Test Website</h1>\n", b'        <hr></hr>\n', b'        <div class="article">\n', b'            <h2><a href="article_1.html">Article 1 Headline</a></h2>\n', b'            <p>This is a summary of article 1</p>\n', b'        </div>\n', b'        <hr></hr>\n', b'        <div class="article">\n', b'            <h2><a href="article_2.html">Article 2 Headline</a></h2>\n', b'            <p>This is a summary of article 2</p>\n', b'        </div>\n', b'        <hr></hr>\n', b"        <div id='footer'>\n", b'            <p>Footer Information</p>\n', b'        </div>\n', b'        <script>\n', b'        var para = document.createElement("p");\n', b'        var node = document.createTextNode("This is text generated by JavaScript.");\n', b'        para.appendChild(node);\n', b'        var element = document.getElementById("footer");\n', b'        element.appendChild(para);\n', b'        </script>\n', b'    </body>\n', b'</html>']
    '''
    for x in eachlinevariable:
        if "article" in str(x):
            print(x.strip())
            '''
            b'<div class="article">'
            b'<h2><a href="article_1.html">Article 1 Headline</a></h2>'
            b'<p>This is a summary of article 1</p>'
            b'<div class="article">'
            b'<h2><a href="article_2.html">Article 2 Headline</a></h2>'
            b'<p>This is a summary of article 2</p>'
            '''
#Read a binary file.  Use a .db file.  Backup the binary file.  Append a timestamp.  Backup file backup file.
from time import time
with open("company.db", "rb") as fileobject, open(f"companybackup.db.backup.{time()}", "wb") as fileobjectbackup:
    chunksizeefficientbackupreadbytes = 4096 #set up a buffer for big memory size files.  Backup by chunk file size
    while True:
        data = fileobject.read(chunksizeefficientbackupreadbytes)
        if not data:
            break
        fileobjectbackup.write(data)
    '''
    b"SQLite format 3\x00\x10\x00\x01\x01\x00@  \x00\x00\x00+\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00+\x00.?\xd9\r\x00\x00\x00\x01\x0fi\x00\x0fi\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
    ...
    '''
    fileobjectbackup.write(data) #Create backup file companybackup.db.backup.1652425537.246177 with the timestamp
