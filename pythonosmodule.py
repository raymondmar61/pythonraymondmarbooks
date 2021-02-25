import os
from datetime import datetime

#print(dir(os)) #print attributes and functions
print(os.getcwd())  #print /home/mar/python.  prints Current Working Directory
os.chdir("/home/mar") #Change Directory
print(os.getcwd())  #print /home/mar.  prints Current Working Directory
print(os.listdir())  #print files and directories in current working directory as a list
print(os.listdir("/home/mar/python"))  #print files and directories in /home/mar/python directory as a list
os.chdir("/home/mar/python") #Change Directory
print(os.getcwd())  #print /home/mar/python.  prints Current Working Directory
os.mkdir("createnewfolder") #create directory
os.makedirs("usetocreatenewfolder/anditssubdirectorywhichisoptional") #create directories and optional subdirectory
os.makedirs("home1/sub2insidehome1/sub3insidesub2/sub4insidesub3") #create directories and optional subdirectories
os.rmdir("createnewfolder") #delete directory
os.removedirs("usetocreatenewfolder/anditssubdirectorywhichisoptional")  #delete directories and optional subdirectory
os.removedirs("home1/sub2insidehome1/sub3insidesub2/sub4insidesub3") #delete directories and optional subdirectories
#os.rename("originalfilename.txt", "newfilename.txt") #rename file
print(os.stat("pokemon_data.txt")) #print os.stat_result(st_mode=33272, st_ino=1838484, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=999, st_size=40832, st_atime=1602220840, st_mtime=1555637880, st_ctime=1600303417)
print("File size in bytes", os.stat("pokemon_data.txt").st_size) #print File size in bytes 40832
print("Last modification date as time stamp", os.stat("pokemon_data.txt").st_mtime) #print Last modification date as time stamp 1555637880
filemodifiedtime = os.stat("pokemon_data.txt").st_mtime
print(datetime.fromtimestamp(filemodifiedtime)) #print 2019-04-18 18:38:00
#os.walk returns a tuple of string or list, in plain English, directory path, directory names or folders, filenames all three inside given path to start.
print(os.walk("/home/mar/python")) #print <generator object walk at 0x7fe9cd394b48>
for eachdirectorypath, eachdirectoryname, eachfilename in os.walk("/home/mar/python"):
    print("Current Path:", eachdirectorypath)
    print("Directories:", eachdirectoryname)
    print("Files Contained:", eachfilename)
    print("\n")
print(os.environ.get("HOME")) #print /home/mar
print(os.environ.get("home")) #print None
print(os.environ.get("python")) #print None
print(os.environ.get("PYTHON")) #print None
createtempfilenameathomedirectory = os.path.join(os.environ.get("HOME"), "createtextfilefrompythonos.txt")
print(createtempfilenameathomedirectory) #print /home/mar/createtextfilefrompythonos.txt
with open(createtempfilenameathomedirectory, "w") as actuallycreatetempfile:
    actuallycreatetempfile.write("This is a test message")
os.remove(createtempfilenameathomedirectory) #delete file /home/mar/createtextfilefrompythonos.txt
#print(dir(os.path)) #print ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_get_sep', '_joinrealpath', '_varprog', '_varprogb', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
print(os.path.basename("/home/mar/python/marbasicspython.py")) #print marbasicspython.py
print(os.path.dirname("/home/mar/python/marbasicspython.py")) #print /home/mar/python
print(os.path.split("/home/mar/python/marbasicspython.py")) #print ('/home/mar/python', 'marbasicspython.py')
print(os.path.exists("/home/mar/python/marbasicspython.py")) #print True
print(os.path.exists("/home/fakepath")) #print False
print(os.path.isdir("/home/mar/python")) #print True
print(os.path.isdir("/home/mar/python/marbasicspython.py")) #print False
print(os.path.isfile("/home/mar/python")) #print False
print(os.path.isfile("/home/mar/python/marbasicspython.py")) #print True
print(os.path.splitext("/home/mar/python/marbasicspython.py")) #print ('/home/mar/python/marbasicspython', '.py')
print(os.path.splitext("marbasicspython.py")) #print ('marbasicspython', '.py')
createtempdirectory = os.mkdir("directorytoberenamed")
print(os.path.dirname("/home/mar/python/directorytoberenamed")) #print /home/mar/python
print(os.path.isdir("/home/mar/python/directorytoberenamed")) #print True
os.rename("directorytoberenamed", "directoryisrenamed") #rename directory
print(os.path.dirname("/home/mar/python/directoryisrenamed")) #print /home/mar/python
print(os.path.isdir("/home/mar/python/directoryisrenamed")) #print True
os.removedirs("directoryisrenamed")
os.system("jsonfiles/inin61.json") #return sh: 1: jsonfiles/inin61.json: Permission denied
os.system("/home/mar/python/jsonfiles/inin61.json") #return sh: 1: /home/mar/python/jsonfiles/inin61.json: Permission denied
os.system("marbasicspython.py") #return sh: 1: marbasicspython.py: not found
os.system("/home/mar/python/marbasicspython.py") #return /home/mar/python/marbasicspython.py: 9: /home/mar/python/marbasicspython.py: Syntax error: word unexpected (expecting ")")
os.system("subl marbasicspython.py") #opens file marbasicspython.py
os.system("subl /home/mar/python/jsonfiles/inin61.json") #opens file inin61.json
os.system("ls -r") #runs linux command ls list
os.system("pwd") #runs linux command print working directory
#print(help(os)) #print help
