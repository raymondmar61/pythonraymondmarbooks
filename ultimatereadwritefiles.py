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
print("file name: " + fileread.name) #print file name: basicreadwritefile.txt
print("file name mode file status opened: " + fileread.mode) #print file name mode file status opened: r
print("file name closed? boolean datatype:", fileread.closed) #print file name closed? boolean datatype: False
printfileread = fileread.read()
print(printfileread)
'''
Write function write to file.
Second line need \\n.
Close() function to close file.

'''
#Note that once you have read some text from a file using read(), readline(), or readlines(), then that line is not read again.
fileread.close()
openfileobject = open("keylog.txt", "r")
readfiletoview = openfileobject.readlines()
print(readfiletoview) #print ['319\n', '680\n', '180\n', '690\n', '129\n', '620\n', '762\n', '689\n', '762\n', '318\n', '368\n', '710\n', . . .
openfileobject.close() #Close the open file when you're done.  The reason is if another program needs to use the file, the other program might not be able to access the file.
openfileobject = open("keylog.txt", "r")
readfiletoviewline1 = openfileobject.readline()
readfiletoviewline2 = openfileobject.readline()
readfiletoviewline3 = openfileobject.readline()
print(readfiletoviewline1) #print 319
print(readfiletoviewline2) #print 680
print(readfiletoviewline3) #print 180
#Use the seek() method to start at the beginning when read each line one at a time with readline().  Set seek() to zero.
openfileobject.seek(0)
readfiletoviewline1again = openfileobject.readline()
readfiletoviewline2again = openfileobject.readline()
readfiletoviewline3again = openfileobject.readline()
print(readfiletoviewline1again) #print 319
print(readfiletoviewline2again) #print 680
print(readfiletoviewline3again) #print 180
openfileobject.close()
writefileusingprint = open("printtotextfile.txt", "w")
print("Use print() to write to a file.  Include file=*object name* at the end.", file=writefileusingprint)
writefileusingprint.close()
readfileusingprint = open("printtotextfile.txt", "r")
readfiletoviewline = readfileusingprint.readline()
print(readfiletoviewline) #print Use print() to write to a file.  Include file=*object name* at the end.
readfileusingprint.close()
#Binary files don't have text.  Binary files are music, pictures, or data not text formatted.  Binary files don't have lines.  readline() and readlines() can't be used in binary files.  Open binary files add the letter b to the file mode.  binarymusicfile = open("openmusicfile.mp3","rb").
openmusicfileobject = open("bartsimpsonsbankrun.mp4", "rb")
readmusicfileobject = openmusicfileobject.readlines()
openmusicfileobject.close()
print(readmusicfileobject) #print . . . \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x007\xa3\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00{']
fileread = open("basicreadwritefile.txt", "r")
readlinesobjectvariable = fileread.readlines()
for eachreadlinesobjectvariable in readlinesobjectvariable:
    print(eachreadlinesobjectvariable, end="")
    '''
    Write function write to file.
    Second line need \\n.
    Close() function to close file.
    '''
fileread.close()
fileread = open("basicreadwritefile.txt", "r")
for forlooponly in fileread:
    print(forlooponly, end="") #RM:  The \n at the end is still valid for new lines.
    '''
    Write function write to file.
    Second line need \\n.
    Close() function to close file.
    '''
fileread.close()
print("file name mode file status opened: " + fileread.mode) #print file name mode file status opened: r
print("file name closed? boolean datatype:", fileread.closed) #print file name closed? boolean datatype: True
#Python can only write strings to a text file. If you want to store numerical data in a text file, you'll have to convert the data to string format first using the str() function.
filewrite = open("stringnumerical.txt", "w")
print(filewrite.readable()) #print False.  Check can read file.
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
import fileinput
with fileinput.input(files=("basicreadwritefile.txt", "stringnumerical.txt")) as filesobjectvariable:
    eachline = filesobjectvariable.readline()
    print("file name method: " + filesobjectvariable.filename()) #print file name method: basicreadwritefile.txt
    print("The first line method boolean answer:", filesobjectvariable.isfirstline()) #print The first line method boolean answer: True
    print("The first line number method integer answer:", filesobjectvariable.lineno()) #print The first line number method integer answer: 1
    print("The first file line number method integer answer:", filesobjectvariable.filelineno()) #print The first file line number method integer answer: 1
    for x in filesobjectvariable:
        print(x)
        '''
        Second line need \n.

        Close() function to close file.

        55

        55
        '''
#Note that once you have read some text from a file using read(), readline(), or readlines(), then that line is not read again.
with fileinput.input(files=("basicreadwritefile.txt", "stringnumerical.txt")) as filesobjectvariable:
    for eachfilesobjectvariable in filesobjectvariable:
        print(filesobjectvariable.filename()) #RM:  notice the variable for the methods and the variable for the for loop.  I can't solve how to print the file name once or no repeats.
        print(filesobjectvariable.lineno()) #RM:  notice the variable for the methods and the variable for the for loop
        print(filesobjectvariable.filelineno()) #RM:  notice the variable for the methods and the variable for the for loop
        print(eachfilesobjectvariable)
        '''
        1
        1
        basicreadwritefile.txt
        Write function write to file.

        2
        2
        basicreadwritefile.txt
        Second line need \n.

        3
        3
        basicreadwritefile.txt
        Close() function to close file.

        4
        1
        stringnumerical.txt
        55

        5
        2
        stringnumerical.txt
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
    readoneline = objectvariablereadfiles.readline()
    print(readoneline) #print 1 With open function write files.2 No need for close method.3 Line one
with open("withreadwritefile.txt", "r") as objectvariablereadfiles:
    readoneline = objectvariablereadfiles.readline()
    print(readoneline) #print 1 With open function write files.2 No need for close method.3 Line one
    print(readoneline) #print 1 With open function write files.2 No need for close method.3 Line one
    print(readoneline) #print 1 With open function write files.2 No need for close method.3 Line one
with open("withreadwritefile.txt", "r") as objectvariablereadfiles:
    readalllines = objectvariablereadfiles.readlines()
    print(readalllines) #print ['1 With open function write files.2 No need for close method.3 Line one\n', '4 Need the \n', '5 Line three use .write() or .writelines method\n', 'writelines() method below\n', '3 Line one\n', '4 Need the \n', '5 Line three use .write() or .writelines method']
with open("withreadwritefile.txt", "r") as objectvariablereadfiles:
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

#Copy file
sourcefile = open("temp.txt", "r", newline="\n")
preparecopyfile = sourcefile.readlines()
sourcefile.close()
copyfile = open("copytemp.txt", "w")
copyfile.writelines(preparecopyfile)
copyfile.close()

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
with open("csvdictionaryheaders.csv", "w", newline="") as csvwritedictionaryvariable:
    #RM:  how to I insert commas?
    columnheaders = ["Title", "Author", "Year"]
    writer = csv.DictWriter(csvwritedictionaryvariable, fieldnames=columnheaders)
    writer.writeheader()
    writer.writerow({"Title": "The Glass Castle", "Author": "Jeanette Walls", "Year": 2005})
    writer.writerow({"Title": "Steve Jobs", "Author": "Walter Issacson", "Year": 2011})
    writer.writerow({"Title": "A Brief History Of Time", "Author": "Stephen Hawking", "Year": 1988})
    writer.writerow({"Title": "To Kill A Mockingbird", "Author": "Harper Lee", "Year": 1960})
    writer.writerow({"Title": "Harry Potter", "Author": "J.K. Rowling", "Year": 1992})
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
with open("csvwriter.csv", "r", newline="") as csvreadobjectvariable:
    reader = csv.reader(csvreadobjectvariable)
    for eachreader in reader:
        print(*eachreader, sep=", ")
        '''
        1, Catan, 54.54
        22, Puerto Rico, 69.99
        333, Pandemic, 39.59
        4444, Fluxx, 9.15
        55555, Dixit, 11.4
        '''
with open("csvwriter.csv", "r", newline="") as csvreadobjectvariable:
    reader = csv.reader(csvreadobjectvariable)
    for eachreader in reader:
        print(eachreader, sep=", ")
        '''
        ['1', 'Catan', '54.54']
        ['22', 'Puerto Rico', '69.99']
        ['333', 'Pandemic', '39.59']
        ['4444', 'Fluxx', '9.15']
        ['55555', 'Dixit', '11.4']
        '''
with open("csvdictionaryheaders.csv", "r", newline="") as csvreaddictionaryvariable:
    reader = csv.DictReader(csvreaddictionaryvariable)
    for headingfieldnames in reader.fieldnames:
        print(headingfieldnames, end=",")
    print("\b")
    for eachreader in reader:
        print(eachreader["Title"], eachreader["Author"], eachreader["Year"], sep=",")
        '''
        Title,Author,Year,
        The Glass Castle,Jeanette Walls,2005
        Steve Jobs,Walter Issacson,2011
        A Brief History Of Time,Stephen Hawking,1988
        To Kill A Mockingbird,Harper Lee,1960
        Harry Potter,J.K. Rowling,1992
        '''
for eachline in csv.reader(open("csvdictionaryheaders.csv", newline=""), delimiter=","):
    print(eachline)
    '''
    ['Title', 'Author', 'Year']
    ['The Glass Castle', 'Jeanette Walls', '2005']
    ['Steve Jobs', 'Walter Issacson', '2011']
    ['A Brief History Of Time', 'Stephen Hawking', '1988']
    ['To Kill A Mockingbird', 'Harper Lee', '1960']
    ['Harry Potter', 'J.K. Rowling', '1992']
    '''

#Write Excel file, write xlsx file, write.xlsx file, write .xlsx file
from openpyxl import Workbook
workbookobject1 = Workbook()
worksheetobject1 = workbookobject1.active
worksheetobject1.title = "Change Sheet1 name"
fruitlisteachownseparateline = [["apple"], ["bananna"], ["orange"], ["bread"], ["apple"], ["strawberry"], ["grape"], ["apple"], ["bananna"]]
for eachfruitlisteachownseparateline in fruitlisteachownseparateline:
    worksheetobject1.append(eachfruitlisteachownseparateline)
workbookobject1.save("fruitlisteachownseparatelinefruitsexcel.xlsx") #RM:  Good Excel file.  Worksheet name changed to Change Sheet1 name.  One column.  Each fruit or bread in its own separate row and cell.
workbookobject2 = Workbook()
worksheetobject2 = workbookobject2.active
worksheetobject2.title = "worksheet name instead of Sheet1"
for writetoexcel in csv.reader(open("csvdictionaryheaders.csv", newline=""), delimiter=","):
    worksheetobject2.append(writetoexcel)
workbookobject2.save("csvfilesavedExcel2.xlsx") #RM:  Good Excel file.  Worksheet name mostly changed because 30 character limit.  Three columns Title, Author, Year.  Each row its own book.

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

#Use the glob module to search for specific filenames
import glob
printallfilesaslist = glob.glob("*")
print(printallfilesaslist) #print ['NativityExamplepage3.pdf', 'moby01.txt', . . ., 'advancedguidepythonprogrammingthreading.py', 'advancedguidepythonprogrammingasyncio.py', 'advancedguidepythonprogrammingsynchronization.py', 'ted.csv', 'small.csv', 'accountscreatetextfile.txt', 'yytest.py']
printtextfilesaslist = glob.glob("*.txt")
print(printtextfilesaslist) #print ['moby01.txt', 'endgametabpaymentmethod.txt', 'combinedatatitanic.txt', . . ., 'ex_06-03.txt', 'accountscreatetextfile.txt']
printfilesnametemp = glob.glob("*temp*")
print(printfilesnametemp) #print ['tempcopied.txt', 'temp.txt', 'temp.html', 'tempexpensesrearrangedcolumns.csv', 'tempexcel.xlsx', 'tempexpensesrearrangedcolumns.xlsx', 'tempbloghtmlsearchresults.txt', 'tempexpensesrearrangedcolumns.txt', 'renamefiletempdeletelinks.txt']

#delete file or remove file.  Rename file.  Remove directory.
import os
os.remove("basicreadwritefile.txt")
os.remove("stringnumerical.txt")
os.remove("withreadwritefile.txt")
os.remove("textfilewithblanklines.txt")
os.remove("tempdeletelinks.txt")
os.remove("errormessagewritefile.txt")
os.rename("tempdeletelinks.txt", "renamefiletempdeletelinks.txt")
os.rmdir("delete directory name")

#File paths, file directory, file pathways
import os
#/home/mar/python
filepath = os.path.join("home", "mar", "python")
print(filepath) #print home/mar/python
printallfilesaslist = os.listdir(os.curdir)
print(printallfilesaslist) #print ['NativityExamplepage3.pdf', 'moby01.txt', . . ., 'advancedguidepythonprogrammingthreading.py', 'advancedguidepythonprogrammingasyncio.py', 'advancedguidepythonprogrammingsynchronization.py', 'ted.csv', 'small.csv', 'accountscreatetextfile.txt', 'yytest.py']
os.chdir("/media/sf_UbuntuShare2004") #Change directory function
print(os.getcwd()) #print /media/sf_UbuntuShare2004
filepath1 = os.path.join("/home", "mar")
filepath2 = os.path.join("python")
print(os.path.join(filepath1, filepath2)) #print /home/mar/python
os.chdir(os.path.join(filepath1, filepath2))
print(os.path.basename(os.getcwd())) #print python
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
os.makedirs("create new directory name")

import sys
#Use sys for user input or screen input
print("Type the following:  Camping pamping dramping.  Press Enter when done.")
screeninputfromuser = sys.stdin.readline()
print(screeninputfromuser) #print Camping pamping dramping.
sys.stdout = sys.__stdout__
print("\n")
#Use sys to write file
quickcreatefile = open("tempuserinputonterminal.txt", "w")
quickcreatefile.close()
createfileforinputfromuser = open("tempuserinputonterminal.txt", "a")
sys.stdout = createfileforinputfromuser
sys.stdout.writelines(["A list of writelines number one sentence in its line.\n", "A list of writelines number two sentence in its own line.\n"])
print("A line from the print function.  The line is inclded in the tempuserinputonterminal.txt file.")
print("Print function for A list of writelines number one.", "A list of writelines number one.\n", file=createfileforinputfromuser)
sys.stdout = sys.__stdout__
readthecreatefileforinputfromuser = sys.stdin.readline()
print(readthecreatefileforinputfromuser, file=createfileforinputfromuser)
sys.stdout = sys.__stdout__
createfileforinputfromuser.close()
'''
RM:  tempuserinputonterminal.txt contains.  I needed to press Ctrl+C to stop terminal from running.  I don't know the Python code to stop running.  It appears I can press Enter to stop running.
A list of writelines number one sentence in its line.
A list of writelines number two sentence in its own line.
A line from the print function.  The line is inclded in the tempuserinputonterminal.txt file.
Print function for A list of writelines number one. A list of writelines number one.




'''
