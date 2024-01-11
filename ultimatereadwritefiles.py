#Read files, write files, append files, open files
#To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to look in a specific location on your system.  Here are relative paths.  with open('text_files/filename.txt') as fileobject: on Linux and OS X.  with open('text_files\filename.txt') as fileobject: on Windows.
#"r" read mode, "w" write mode, "a" append mode, "r+" read and write mode, default is read mode.
filewrite = open("basicreadwritefile.txt", "w")
filewrite.write("Write function write to file.\n")
filewrite.write("Second line need \\n.\n")
filewrite.write("Close() function to close file.\n")
filewrite.close()
fileread = open("basicreadwritefile.txt", "r")
print(fileread.readline()) #print Write function write to file.
print(fileread.readline()) #print Second line need \n.
print(fileread.readline()) #print Close() function to close file.
fileread.close()
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
print(fileread.readable()) #print True.  Check can read file.
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
#Open multiple files
openfile1 = open("basicreadwritefile.txt", "r")
openfile2 = open("stringnumerical.txt", "r")
with openfile1, openfile2:
    for eachopenfile1 in openfile1:
        print(eachopenfile1)
        '''
        Write function write to file.

        Second line need \\n.

        Close() function to close file.
        '''
    for eachopenfile2 in openfile2:
        print(eachopenfile2)
        '''
        55

        55
        '''
openfile1 = open("basicreadwritefile.txt", "r")
openfile2 = open("stringnumerical.txt", "r")
with openfile1, openfile2 as twofilesobject:
    print(twofilesobject) #print <_io.TextIOWrapper name='stringnumerical.txt' mode='r' encoding='UTF-8'>
    for eachtwofilesobject in twofilesobject:
        print(eachtwofilesobject)
        '''
        55

        55
        '''

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
with open("accountscreatetextfile.txt", mode="w") as accountsvariableobject:
    accountsvariableobject.write("100 Jones 24.98\n")
    accountsvariableobject.write("200 Doe  345.67\n")
    accountsvariableobject.write("300 White 0.00\n")
    accountsvariableobject.write("400 Stone -42.16\n")
    accountsvariableobject.write("500 Rich 224.62\n")
    print("600 printstatementwritetotextfile 123.45", file=accountsvariableobject)
with open("accountscreatetextfile.txt", mode="r") as accountsvariableobject:
    print(f'{"Account":<10}{"Name":<40}{"Balance":<10}') #header for the three columns and its lengths
    for eachaccountsvariableobject in accountsvariableobject:
        account, name, balance = eachaccountsvariableobject.split() #The split method returns tokens in the line as a list unpacked to variables.  The default is split discards the newline character \n.
        print(f"{account:<10}{name:<40}{balance:<10}") #displays the variables in columns using field widths
        '''
        Account   Name                                    Balance   
        100       Jones                                   24.98     
        200       Doe                                     345.67    
        300       White                                   0.00      
        400       Stone                                   -42.16    
        500       Rich                                    224.62    
        600       printstatementwritetotextfile           123.45
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

#Read csv file, write csv file, read.csv file, write .csv file
import csv
writecsvfile = open("writecsvfile.csv", "w")
headers = "Name,Number,One Sentence Two Words\n"
writecsvfile.write(str(headers))
namevariable = "Harry"
numbervariable = 1
onesentencetwowordsvariable = "Chosen One"
writecsvfile.write(namevariable + "," + str(numbervariable) + "," + onesentencetwowordsvariable + "\n")
writecsvfile.close()
readcsvfile = open("writecsvfile.csv", "r")
for eachreadcsvfile in readcsvfile:
    print(eachreadcsvfile)
    '''
    Name,Number,One Sentence Two Words

    Harry,1,Chosen One
    '''
writecsvfile.close()
appendcsvfile = open("writecsvfile.csv", "a")
appendcsvfile.write("Ron" + "," + str(22) + "," + "The Burrow" + "\n")
appendcsvfile.write("Hermione" + "," + str(333) + "," + "Bookworm smart" + "\n")
appendcsvfile.write("Luna" + "," + str(4444) + "," + "Weird smart" + "\n")
appendcsvfile.write("Neville" + "," + str(55555) + "," + "Loyal trustworthy" + "\n")
appendcsvfile.write("Ginny" + "," + str(666666) + "," + "Strong self-esteem" + "\n")
appendcsvfile.close()
with open("writecsvfile.csv", "r") as readobject:
    usereadmethod = readobject.read()
    print(type(usereadmethod)) #print <class 'str'>
    print(usereadmethod)
    '''
    Name,Number,One Sentence Two Words
    Harry,1,Chosen One
    Ron,22,The Burrow
    Hermione,333,Bookworm smart
    Luna,4444,Weird smart
    Neville,55555,Loyal trustworthy
    Ginny,666666,Strong self-esteem
    '''
with open("writecsvfile.csv", "r") as csvfileobject:
    lineisalist = csvfileobject.readlines()
    print(type(lineisalist)) #print <class 'list'>
    print(lineisalist) #print ['Name,Number,One Sentence Two Words\n', 'Harry,1,Chosen One\n', 'Ron,22,The Burrow\n', 'Hermione,333,Bookworm smart\n', 'Luna,4444,Weird smart\n', 'Neville,55555,Loyal trustworthy\n', 'Ginny,666666,Strong self-esteem\n']
    for eachlineisalist in lineisalist:
        print(eachlineisalist)
        '''
        Name,Number,One Sentence Two Words

        Harry,1,Chosen One

        Ron,22,The Burrow

        Hermione,333,Bookworm smart

        Luna,4444,Weird smart

        Neville,55555,Loyal trustworthy
        '''
character = "Harry"
with open("writecsvfile.csv", "r") as searchcharacter:
    usereadlinesmethod = searchcharacter.readlines()
    for eachusereadlinesmethod in usereadlinesmethod:
        if character in eachusereadlinesmethod:
            print(f"I found {character} from the {eachusereadlinesmethod}") #print I found Harry from the Harry,1,Chosen One
with open("csvwriter.csv", mode="w", newline="") as csvwriterobjectvariable:
    writer = csv.writer(csvwriterobjectvariable)
    writer.writerow([1, "Catan", 54.54])
    writer.writerow([22, "Puerto Rico", 69.99])
    writer.writerow([333, "Pandemic", 39.59])
    writer.writerow([4444, "Fluxx", 9.15])
    writer.writerow([55555, "Dixit", 11.40])
with open("csvwriter.csv", "r", newline="") as csvreadobjectvariable:
    print(f'{"HeaderRow25leftalign":<25}{"Board Game":<15}{"Float20rightalign":>20}') #RM:  single quotes for the f.  Furthest right column must be right algin.  Disregard Excel left align for text and right align for numbers
    reader = csv.reader(csvreadobjectvariable)
    for eachreader in reader:
        firstcolumn, secondcolumn, thirdcolumn = eachreader
        print(f'{firstcolumn:<25}{secondcolumn:<15}{thirdcolumn:>20}')
        '''
        HeaderRow25rightalign    Board Game        Float20rightalign
        1                        Catan                         54.54
        22                       Puerto Rico                   69.99
        333                      Pandemic                      39.59
        4444                     Fluxx                          9.15
        55555                    Dixit                          11.4
        '''

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

#delete file or remove file.  Rename file
import os
os.remove("basicreadwritefile.txt")
os.remove("stringnumerical.txt")
os.remove("withreadwritefile.txt")
os.remove("textfilewithblanklines.txt")
os.remove("tempdeletelinks.txt")
os.remove("errormessagewritefile.txt")
os.rename("tempdeletelinks.txt", "renamefiletempdeletelinks.txt")

#File paths, file directory, file pathways
import os
#/home/mar/python
filepath = os.path.join("home", "mar", "python")
print(filepath) #print home/mar/python
pythonfileslist = ["ultimatereadwritefiles.py", "ultimatefunctionstryexceptlambda.py", "ultimateifelseforwhile.py", "ultimateliststuplesdictionariessets.py"]
for eachpythonfileslist in pythonfileslist:
    print(os.path.join(filepath, eachpythonfileslist))
    '''
    home/mar/python/ultimatereadwritefiles.py
    home/mar/python/ultimatefunctionstryexceptlambda.py
    home/mar/python/ultimateifelseforwhile.py
    home/mar/python/ultimateliststuplesdictionariessets.py
    '''
currentfilepath = os.getcwd() #current working directory
print(currentfilepath) #print /home/mar/python
print(currentfilepath.split(os.path.sep)) #print ['', 'home', 'mar', 'python']
for eachpythonfileslist in pythonfileslist:
    print(os.path.join(currentfilepath, eachpythonfileslist))
    print(os.path.split(os.path.join(currentfilepath, eachpythonfileslist)))
    '''
    /home/mar/python/ultimatereadwritefiles.py
    ('/home/mar/python', 'ultimatereadwritefiles.py')
    /home/mar/python/ultimatefunctionstryexceptlambda.py
    ('/home/mar/python', 'ultimatefunctionstryexceptlambda.py')
    /home/mar/python/ultimateifelseforwhile.py
    ('/home/mar/python', 'ultimateifelseforwhile.py')
    /home/mar/python/ultimateliststuplesdictionariessets.py
    ('/home/mar/python', 'ultimateliststuplesdictionariessets.py')
    '''
filesindirectorylist = os.listdir(currentfilepath)
print(filesindirectorylist) #print ['NativityExamplepage3.pdf', 'moby01.txt', 'endgamecsvexpenses.csv', 'endgametabpaymentmethod.txt', 'pythoninfiniteloopalistlinks.pdf', 'combinedatatitanic.txt', . . . ]
filename = "basicreadwritefile.txt"
with open(currentfilepath + "/" + filename, "r") as fileobject:
    print(fileobject) #print <_io.TextIOWrapper name='/home/mar/python/basicreadwritefile.txt' mode='r' encoding='UTF-8'>
    readandprint = fileobject.read()
    print(readandprint)
    '''
    Write function write to file.
    Second line need \\n.
    Close() function to close file.
    '''
