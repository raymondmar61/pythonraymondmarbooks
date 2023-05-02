#Advanced Guide To Python 3 Programming by John Hunt Chapter 18 Reading And Writing Files
#Read file
fileobjectvariable = open("temp.txt", "r")
print("file name: " + fileobjectvariable.name) #print file name: temp.txt
print("file mode file is opened: " + fileobjectvariable.mode) #print file mode file is opened: r
fileobjectvariable.close()
print("file closed method returns a boolean:", fileobjectvariable.closed) #print True
print("file mode file is closed: " + fileobjectvariable.mode) #print file mode file is closed: r
fileobjectvariable = open("temp.txt", "r")
fileallinesprinted = fileobjectvariable.read()
print(fileallinesprinted) #print *all the file contents*
fileobjectvariable.close()
#Note that once you have read some text from a file using read(), readline(), or readlines(), then that line is not read again.
fileobjectvariable = open("temp.txt", "r")
eachlineinfile = fileobjectvariable.readlines()
for x in eachlineinfile:
    print(x, end="") #print *all the file contents*

fileobjectvariable.close()
fileobjectvariable = open("temp.txt", "r")
for noreadlinesmethod in fileobjectvariable:
    print(noreadlinesmethod, end="") #print *all the file contents*
fileobjectvariable.close()
fileobjectvariable = open("temp.txt", "r")
listcomprehension = [noreadlinesmethod.upper() for noreadlinesmethod in fileobjectvariable]
fileobjectvariable.close()
print(listcomprehension) #print ['\n', '200601BLOG.HTML\n', '167 <P>I WENT TO THE INTERVIEW AND WAS HIRED ON THE SPOT. I WAS GIVEN A CONTRACT AND MY PRIMARY RESPONSIBILITY WAS TO SOLVE PROBLEMS—OR AT LEAST, GET THEIR WORKERS TO SOLVE PROBLEMS.</P>\n', '\n', '200906BLOG.HTML\n', . . . ]
with open("temp.txt", "r") as fileobjectvariable:
    eachline = fileobjectvariable.readlines()
    for x in eachline:
        print(x, end="") #print *all the file contents*
#Write file
newfileobjectvariable = open("mynewfile.txt", "w")
newfileobjectvariable.write("Line 1 Hello from Python\n")
newfileobjectvariable.write("Line 2 Working with files is easy\n")
newfileobjectvariable.write("Line 3 It is cool no need for \\n because it's the last line")
newfileobjectvariable.close()
import fileinput
# with fileinput.input(files=("temp.txt", "mynewfile.txt")) as fileobjectvariable:
#     for x in fileobjectvariable:
#         process(x) #return NameError: name 'process' is not defined
with fileinput.input(files=("temp.txt", "mynewfile.txt")) as fileobjectvariable:
    eachline = fileobjectvariable.readline()
    print("filename: " + fileobjectvariable.filename()) #print filename: temp.txt
    print("The first line:", fileobjectvariable.isfirstline()) #print The first line: True
    print("The first line number:", fileobjectvariable.lineno()) #print The first line number: 1
    print("The first file line number:", fileobjectvariable.filelineno()) #print The first file line number: 1
    for x in fileobjectvariable:
        print(x, end="")
        '''
        *file contexts from temp.txt and mynewfile.txt*
        ...
        Line 1 Hello from Python
        Line 2 Working with files is easy
        Line 3 It is cool no need for \n because it's the last line
        '''
#rename files
import os
os.rename("mynewfile.txt", "new name for mynewfile.txt")
#delete files
import os
os.remove("new name for mynewfile.txt")
