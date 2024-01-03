#Read files, write files, append files, open files
#To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to look in a specific location on your system.  Here are relative paths.  with open('text_files/filename.txt') as fileobject: on Linux and OS X.  with open('text_files\filename.txt') as fileobject: on Windows.
#"r" read mode, "w" write mode, "a" append mode, "r+" read and write mode, default is read mode.
filewrite = open("basicreadwritefile.txt", "w")
filewrite.write("Write function write to file.\n")
filewrite.write("Second line need \\n.\n")
filewrite.write("Close() function to close file.\n")
filewrite.close()
fileread = open("basicreadwritefile.txt", "r")
printfileread = fileread.read()
print(printfileread)
'''
Write function write to file.
Second line need \\n.
Close() function to close file.

'''
fileread.close()
#Python can only write strings to a text file. If you want to store numerical data in a text file, you'll have to convert the data to string format first using the str() function.
filewrite = open("stringnumerical.txt", "w")
filewrite.write("55\n")
filewrite.write(str(55))
filewrite.close()
fileread = open("stringnumerical.txt", "r")
printfileread = fileread.read()
print(printfileread)
'''
55
55
'''
fileread.close()

#Write files with, read files with, append files with
with open("withreadwritefile.txt", "w") as objectvariablewritefiles:
    objectvariablewritefiles.write("1 With open function write files.")
    objectvariablewritefiles.write("2 No need for close method.")
    writelineslist = ["3 Line one\n", "4 Need the \n", "5 Line three use .write() or .writelines method"]
    objectvariablewritefiles.write(writelineslist[0])
    objectvariablewritefiles.write(writelineslist[1])
    objectvariablewritefiles.write(writelineslist[2])
    objectvariablewritefiles.write("\nwritelines() method below\n")
    objectvariablewritefiles.writelines(writelineslist)
with open("withreadwritefile.txt", "r") as objectvariablereadfiles:
    print(objectvariablereadfiles.readlines()) #print ['1 With open function write files.2 No need for close method.3 Line one\n', '4 Need the \n', '5 Line three use .write() or .writelines method\n', 'writelines() method below\n', '3 Line one\n', '4 Need the \n', '5 Line three use .write() or .writelines method']
    for eachobjectvariablereadfiles in objectvariablereadfiles.readlines():
        print(eachobjectvariablereadfiles)
        '''
        1 With open function write files.2 No need for close method.3 Line one

        4 Need the 

        5 Line three use .write() or .writelines method

        writelines() method below

        3 Line one

        4 Need the 

        5 Line three use .write() or .writelines method
        '''
with open("withreadwritefile.txt", "r") as objectvariablereadfiles:
    for noreadlinesmethod in objectvariablereadfiles:
        print(noreadlinesmethod)
        '''
        1 With open function write files.2 No need for close method.3 Line one

        4 Need the 

        5 Line three use .write() or .writelines method

        writelines() method below

        3 Line one

        4 Need the 

        5 Line three use .write() or .writelines method
        '''
with open("withreadwritefile.txt", "a") as objectvariableappendfiles:
    objectvariableappendfiles.write("6 append the sentence")
with open("withreadwritefile.txt", "r") as objectvariablereadfiles:
    usereadmethod = objectvariablereadfiles.read()
    print(usereadmethod)
    '''
    1 With open function write files.2 No need for close method.3 Line one
    4 Need the 
    5 Line three use .write() or .writelines method
    writelines() method below
    3 Line one
    4 Need the 
    5 Line three use .write() or .writelines method6 append the sentence
    '''

#Open a text file ignore blank lines
#https://codereview.stackexchange.com/questions/145126/open-a-text-file-and-remove-any-blank-lines
filename = "textfilewithblanklines.txt"
readfilelist = []
with open(filename, "r") as openfilenameobjectvariable:
    for eachopenfilenameobjectvariable in openfilenameobjectvariable:
        removeblanklines = eachopenfilenameobjectvariable.strip()
        if removeblanklines:
            readfilelist.append(removeblanklines)
print(readfilelist) #print ['creditcategoryfilename.csv', 'creditcategoryfilename.json', 'creditcategoryfilename.txt', 'creditcategoryfilename.xlsx', 'csvdictionaryheaders.csv', 'csvfilebeatles.csv', 'csvfilenamefile01.csv', 'datapipes.csv', 'datapipesexcel2.xlsx', 'datapipesexcel.xlsx', 'datapipes.txt', 'default.pdf']
for eachreadfilelist in readfilelist:
    print(eachreadfilelist)
    '''
    creditcategoryfilename.csv
    creditcategoryfilename.json
    ...
    datapipes.txt
    default.pdf
    '''
#https://stackoverflow.com/questions/40647881/skipping-blank-lines-in-read-file-python
file = open(filename)
readfilelist = [line for line in file if line.strip()]
file.close()
print(readfilelist)  #print [' creditcategoryfilename.csv\n', ' creditcategoryfilename.json\n', ' creditcategoryfilename.txt\n', ' creditcategoryfilename.xlsx\n', ' csvdictionaryheaders.csv\n', ' csvfilebeatles.csv\n', ' csvfilenamefile01.csv\n', ' datapipes.csv\n', ' datapipesexcel2.xlsx\n', ' datapipesexcel.xlsx\n', ' datapipes.txt\n', ' default.pdf\n']
readfilelist = []
with open(filename, "r") as file:
    for eachline in file:
        if eachline.strip():
            readfilelist.append(eachline)
print(readfilelist)  #print [' creditcategoryfilename.csv\n', ' creditcategoryfilename.json\n', ' creditcategoryfilename.txt\n', ' creditcategoryfilename.xlsx\n', ' csvdictionaryheaders.csv\n', ' csvfilebeatles.csv\n', ' csvfilenamefile01.csv\n', ' datapipes.csv\n', ' datapipesexcel2.xlsx\n', ' datapipesexcel.xlsx\n', ' datapipes.txt\n', ' default.pdf\n']

#Write list to a file
linkslist = ["apple", "bananna", "orange", "bread", "apple", "strawberry", "grape", "apple", "bananna"]
with open("tempdeletelinks.txt", "w") as testwritelinks:
    for eachlinkslist in linkslist:
        testwritelinks.write(eachlinkslist)
        testwritelinks.write("\n")
newlinkslist = []
with open("tempdeletelinks.txt", "r") as extractunique:
    for eachextractunique in extractunique:
        eachline = eachextractunique.strip()
        if eachline not in newlinkslist:
            newlinkslist.append(eachline)
print(newlinkslist) #print ['apple', 'bananna', 'orange', 'bread', 'strawberry', 'grape']
print("\n")
#Append new strings
appendnewlinkslist = ["apple", "chicken", "steak", "bread", "pork"]
for eachappendnewlinkslist in appendnewlinkslist:
    print("*" + eachappendnewlinkslist)
    with open("tempdeletelinks.txt", "r") as objectvariablereadfiles:
        readfilevariable = objectvariablereadfiles.read()
    if eachappendnewlinkslist in readfilevariable:
        print(eachappendnewlinkslist + " is already in the file")
    else:
        with open("tempdeletelinks.txt", "a") as writenew:
            writenew.write(eachappendnewlinkslist)
            writenew.write("\n")
    '''
    *apple
    apple is already in the file
    *chicken
    *steak
    *bread
    bread is already in the file
    *pork
    '''
with open("tempdeletelinks.txt", "r") as objectvariablereadfiles:
    readfilevariable = objectvariablereadfiles.read()
    print(readfilevariable) #print apple bananna\n orange\n bread\n apple\n strawberry\n grape\n apple\n bananna\n chicken\n steak\n pork\n


#try, except write file error write file
tryexceptwritefile = open("errormessagewritefile.txt", "w")
try:
    tryexceptwritefile.write("Errors write errors sentence\n")
    tryexceptwritefile.write("Write() must be closed to read()")
    tryexceptwritefile.close()
except BaseException:
    print("Error writing file")
except Exception as exceptvariableprintexeption:
    print("Problem handling file.  Error is %s" % exceptvariableprintexeption)
finally:
    fileread = open("errormessagewritefile.txt", "r")
    printfileread = fileread.read()
    print(printfileread)
    '''
    Errors write errors sentence
    Write() must be closed to read()
    '''
    tryexceptwritefile.close()

#delete file or remove file
import os
os.remove("basicreadwritefile.txt")
os.remove("stringnumerical.txt")
os.remove("withreadwritefile.txt")
os.remove("textfilewithblanklines.txt")
os.remove("tempdeletelinks.txt")
os.remove("errormessagewritefile.txt")
