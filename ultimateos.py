import os
#Help
#print(dir(os)) #print os attributes and os functions.  [... 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', ...]

#Directories directory
print(os.getcwd())  #print /home/mar/python.  Get current working directory.
os.chdir("/home/mar") #Change working directory.
print(os.getcwd())  #print /home/mar.  Get current working directory.
os.mkdir("createnewfoldername") #Create new directory.
os.chdir("/home/mar/createnewfoldername")
print(os.getcwd()) #print /home/mar/createnewfoldername
os.rmdir("/home/mar/createnewfoldername") #delete directory, delete folder
os.makedirs("/home/mar/anditssubdirectorywhichisoptional") #create directories and optional subdirectory
os.makedirs("/home/mar/sub2insidehome1/sub3insidesub2/sub4insidesub3")
os.removedirs("/home/mar/anditssubdirectorywhichisoptional")  #delete directories and optional subdirectory
os.removedirs("/home/mar/sub2insidehome1/sub3insidesub2/sub4insidesub3")
os.chdir("/home/mar")
gethomedirectory = os.environ.get("HOME") #os.environ.get("home") returns None
print(gethomedirectory) #print /home/mar

#os path directory
#print(dir(os.path)) #print ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_get_sep', '_joinrealpath', '_varprog', '_varprogb', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
#print(help(os)) #print help
joinseparatedirectories = os.path.join("/", "home", "mar", "python")
print(joinseparatedirectories) #print /home/mar/python
os.chdir(joinseparatedirectories)
print(os.getcwd()) #print /home/mar/python
previousdirectories = os.path.dirname(joinseparatedirectories)
print(previousdirectories) #print /home/mar
presentdirectory = os.path.basename(joinseparatedirectories)
print(presentdirectory) #print python
filepathseparator = os.path.sep
print(filepathseparator) #print /
splitfilepathbycommalist = joinseparatedirectories.split(filepathseparator)
print(splitfilepathbycommalist) #print ['', 'home', 'mar', 'python']
filenameforospath = "/home/mar/python/ultimatestringsbooleansvariables.py"
filenameonly = os.path.basename(filenameforospath)
print(filenameonly) #print ultimatestringsbooleansvariables.py
directorynameonly = os.path.dirname(filenameforospath)
print(directorynameonly) #print /home/mar/python
separatedirectoryfilename = os.path.split(filenameforospath)
print(separatedirectoryfilename) #print ('/home/mar/python', 'ultimatestringsbooleansvariables.py')
checkfilenameexists = os.path.exists(filenameforospath)
print(checkfilenameexists) #print True
confirmdirectory = os.path.isdir(directorynameonly)
print(confirmdirectory) #print True
confirmfile = os.path.isfile(filenameonly)
print(confirmfile) #print True
separatefiletype = os.path.splitext(filenameforospath)
print(separatefiletype) #print ('/home/mar/python/ultimatestringsbooleansvariables', '.py')
absolutepath = os.path.abspath(".")
print(absolutepath) #print /home/mar/python
absolutepathwithsubolder = ("./pdffiles")
print(absolutepathwithsubolder) #print ./pdffiles
os.chdir(absolutepathwithsubolder)
print(os.getcwd()) #print /home/mar/python/pdffiles
print(os.listdir()) #print ['yyextractimages.py', 'pdfextractimagesfunction.py', 'pdfextractimages.py']
confirmabsolutepath = os.path.isabs(".")  #returns True if absolute path and False if relative path
print(confirmabsolutepath) #print False
confirmabsolutepath = os.path.isabs(absolutepath)  #returns True if absolute path and False if relative path
print(confirmabsolutepath) #print True
confirmrelativepath = os.path.relpath("/home/python", "~") #returns a string of a relative path from the start path to path.  If start path is not provided, the current working directory is used as the start path.
print(confirmrelativepath) #print ../../../python
confirmrelativepath = os.path.relpath("/home/", "~")
print(confirmrelativepath) #print ../../..
confirmrelativepath = os.path.relpath("/home", "~")
print(confirmrelativepath) #print ../../..
confirmrelativepath = os.path.relpath("/", "~")
print(confirmrelativepath) #print ../../../..
confirmrelativepath = os.path.relpath("/home/python", "/home/")
print(confirmrelativepath) #print python
confirmrelativepath = os.path.relpath("/home/python", "/home")
os.chdir(joinseparatedirectories)
print(confirmrelativepath) #print python
filesizeinbyptes = os.path.getsize(filenameforospath)
print(filesizeinbyptes) #print 31382
print(os.system(filenameforospath)) #print sh: 1: /home/mar/python/ultimatestringsbooleansvariables.py: Permission denied\n 32256
print(os.system(filenameonly)) #print sh: 1: ultimatestringsbooleansvariables.py: not found\n 32512
print(os.system(directorynameonly)) #print sh: 1: /home/mar/python: Permission denied\n 32256
print(os.system("/home/mar/python/moby01.txt")) #print sh: 1: /home/mar/python/moby01.txt: Permission denied\n 32256
os.system("subl moby01.txt") #ppen moby01.txt file with Sublime Text
os.system("ls *.jpg") #executes the ls command list all .jpg files in Linux terminal
os.system("pwd") #executes the pwd Print Working Directory in Linux terminal

#Files
#Create file, write file, read file, remove file
os.chdir("/home/mar/")
createtempfilenameathomedirectory = os.path.join(os.environ.get("HOME"), "createtextfilefrompythonos.txt")
print(createtempfilenameathomedirectory) #print /home/mar/createtextfilefrompythonos.txt
with open(createtempfilenameathomedirectory, "w") as actuallycreatetempfile:
    actuallycreatetempfile.write("This is a test message\n")
    actuallycreatetempfile.write("Write in the file")
os.rename("createtextfilefrompythonos.txt", "readcreatetextfilefrompythonos.txt") #rename file
with open("readcreatetextfilefrompythonos.txt", "r") as readactuallycreatetempfile:
    for eachreadactuallycreatetempfile in readactuallycreatetempfile.readlines():
        print(eachreadactuallycreatetempfile)
        '''
        This is a test message

        Write in the file
        '''
os.remove("readcreatetextfilefrompythonos.txt") #delete file
os.chdir("/home/mar/python")
#print(os.listdir()) #print [..., 'mymath.py', 'quickpythonbook01.py', 'datapipes.txt', 'pandasdataschool2022_01.py', 'page1.jpg', 'iris.csv', 'imagename1.jpeg', 'q', 'pandasdataschool2022_02.py', ...].  Get files list files.
#print(os.listdir("/home/mar")) #print [...'mysql-workbench-community_8.0.29-1ubuntu20.04_amd64.deb', '.mysql_history', 'Music', '.vboxclient-clipboard.pid', 'Pictures', '.sudo_as_admin_successful', 'Documents'].  Get files from another directory.
datelastmodified = os.stat("ultimatepandas1.py").st_mtime
print(datelastmodified) #print 1706153504.5359838
import datetime
print(datetime.datetime.fromtimestamp(datelastmodified)) #print 2024-01-24 19:31:44.535984
#Loop file names
selectedpythonfilenames = ["fullcourseforbeginners.py", "quickpythonbook01.py", "ultimatepandas1.py", "yytext.py"]
for combinedirectoryfilename in selectedpythonfilenames:
    print(os.path.join(os.getcwd(), combinedirectoryfilename))
    '''
    /home/mar/python/fullcourseforbeginners.py
    /home/mar/python/quickpythonbook01.py
    /home/mar/python/ultimatepandas1.py
    /home/mar/python/yytext.py
    '''
filenamesanditsdirectories = os.walk("/home/mar/python") #os.walk returns a tuple of string or list, in plain English, directory path, directory names or folders, filenames all three inside given path to start.
print(filenamesanditsdirectories) #print <generator object walk at 0x7f71908b8f90>
for eachdirectorypath, eachdirectoryname, eachfilename in filenamesanditsdirectories:
    print("Current Path:", eachdirectorypath)
    print("Directories:", eachdirectoryname)
    print("Files Contained:", eachfilename)
    print("\n")
    '''
    Current Path: /home/mar/python
    Directories: ['ml-100k', 'node_modules', 'pdffiles', '__pycache__']
    Files Contained: ['NativityExamplepage3.pdf', 'moby01.txt', 'endgamecsvexpenses.csv', 'endgametabpaymentmethod.txt', 'pythoninfiniteloopalistlinks.pdf', 'combinedatatitanic.txt', 'creditcategoryfilename.xlsx', 'pythonforprogrammersbasics02.py', 'ETH_1h.csv', 'survey_results_schema.csv', 'pythondataanalyticsvisualization02numpy.py', 'exporttocsv.csv', ..., 'yytest.py']

    Current Path: /home/mar/python/ml-100k
    Directories: []
    Files Contained: ['ub.base', 'u4.base', 'u4.test', 'u.data', 'u.item', 'u.occupation', 'u5.test', 'u.user', 'u.genre', 'u2.base', 'u3.base', 'u1.base', 'u5.base', 'u1.test', 'ub.test', 'u2.test', 'allbut.pl', 'mku.sh', 'ua.base', 'ua.test', 'u.info', 'u3.test', 'README']

    Current Path: /home/mar/python/node_modules
    Directories: ['@faker-js', 'loose-envify', 'js-tokens', '.bin', 'faker', 'react']
    Files Contained: []
    ...
    '''
filestatistics = os.stat("ultimatepandas1.py")
print(filestatistics) #print os.stat_result(st_mode=33206, st_ino=4214080, st_dev=2053, st_nlink=1, st_uid=1000, st_gid=1000, st_size=176925, st_atime=1706153515, st_mtime=1706153504, st_ctime=1706153504)
filesizeinbytes = os.stat("ultimatepandas1.py").st_size
print(filesizeinbytes) #print 176925
kilobytes = filesizeinbytes / 1000
megabytes = filesizeinbytes / 1000000
gigabytes = filesizeinbytes / 1000000000000 #RM:  twelve zeroes
print(megabytes) #print 0.176925
print(gigabytes) #print 1.76925e-07
