#The Quick Python Book by Naomi Ceder Chapter 10 Modules And Scoping Rules
#A module is a file containing code.  A module defines a group of Python functions or other objects.  The name of the module is derived from the name of the file.
import mymath #import mymath is from the file mymath.py in the same directory.
mymathmodulepivariable = mymath.pi
print(mymathmodulepivariable) #print 3.14159
print(mymath.area(2)) #print 12.56636
print(mymath.__doc__) #print my math our example math module
print(mymath.area.__doc__) #print area(r):  returns the area of a circle with radius r.
import importlib
print(importlib.reload(mymath)) #print <module 'mymath' from '/home/mar/python/mymath.py'>
from mymath import area
print(area(2)) #print 12.56636
print(area(20)) #print 1256.636
from mymath import *
print(area(10)) #print 314.159
import sys
print(sys.path) #print ['/home/mar/python', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/mar/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages'] #A list of directories Python searches in the list order to execute an import statement.  Python looks for modules in the directories returned.

#The Quick Python Book by Naomi Ceder Chapter 11 Python Programs
import sys
def main():
    print("This is our first test script file")
    print(sys.argv)


main() #return This is our first test script file\n ['yytest.py']

def mainfilereplace():
    contents = sys.stdin.read()
    sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2])) #replaces first argument with second argument


#mainfilereplace()

#The Quick Python Book by Naomi Ceder Chapter 12 Using The Filesystem
#RM:  Book page 172-174 more filesystem values, filesystem functions, pathlib properties, and pathlib functions
#Forward slash / is used to separate sequential file or directory names in Linux or UNIX.  Backward slash \ is used to separate file or directory names in Windows.  UNIX filesystem has a single root /.  Windows filesystem has a separate root for each drive A:\ B:\ C:\.  UNIX /data/myfile.  Windows C:\data\myfile.  Mac same as UNIX?  It appears yes.
import os
import pathlib
print(os.getcwd()) #print /home/mar/python.  Function get current working directory getcwd is a zero argument function.
print(os.listdir(os.curdir)) #It appears to print all files in current directory
'''
['combinedatatitanic.txt', 'pythonforprogrammersbasics02.py', 'ETH_1h.csv', 'ml-100k', 'survey_results_schema.csv', 'pythondataanalyticsvisualization02numpy.py', 'exporttocsv.csv', 'mymath.py', 'quickpythonbook01.py', 'pandasdataschool2022_01.py', 'iris.csv', 'pandasdataschool2022_02.py', 'advancedguidepythonprogrammingregularexpressions.py', 'kaggletraintitanic.csv', 'usefultools.py', 'node_modules', 'temp.txt', 'combinedatatitaniclowercasecolumns.txt', 'drinks1.csv', 'twitterdownloadtweetsfinalv1.2.py', 'pivot.csv', 'drinksbycountry.csv', 'employees.txt', 'pandasjoejames02.py', 'fullcourseforbeginners.py', 'pandasdataschool2022_03.py', 'ex_06-01.txt', 'gdp.csv', 'timewithproperties.py', 'smallstocks.csv', 'ml-100k.zip', 'package.json', 'advancedguidepythonprogrammingmatplotlib.py', 'pythondataanalyticsvisualization06interactingwithdatabases.py', 'tempexcel.xlsx', 'population_total.csv', 'pythondataanalyticsvisualization04datavisualization.py', 'pythondataanalyticsvisualization03pandas.py', 'csvfilenamefile01.csv', 'irisoriginal.data', 'savedataframe.csv', 'chipotle.csv', 'csvdictionaryheaders.csv', 'pokemon_datamodified.csv', 'Create Test File On My Windows.txt', 'pythonpandasandexcel.py', 'imdbratings.csv', 'pythonforprogrammersregularexpressions.py', '__pycache__', 'package-lock.json', 'pandascoreyschafer.py', 'pandasdataschool2022_04.py', 'accountsjson.json', 'supermarket_sales.xlsx', 'twitterdownloadfavoritesv1.1.py', 'advancedguidepythonprogrammingreadwritefiles.py', 'searchinmyblogs.py', 'pythonforprogrammersbasics.py', 'pandasdataschool2022_05pandatricks.py', 'stocks1.csv', 'ex_06-02.txt', 'namethecsvfile.csv', 'stocks3.csv', 'movieusers.csv', 'StudentsPerformance.csv', 'tempbloghtmlsearchresults.txt', 'survey_results_public.csv', 'accountscsvfile.csv', 'irisoriginal.csv', 'pythondataanalyticsvisualization07dataanalysisapplicationexamples.py', 'quickpythonbook02.py', 'generatepasswords.py', 'pandasjoejames.py', 'pandasdataschool2022_06pycon2019.py', 'introductiontorprogrammingforexceluserstitanic.csv', 'stocks2.csv', 'advancedguidepythonprogrammingcsvexcelfiles.py', 'pandadataframetocsvfile.csv', 'namethejsonfile.txt', 'uforeports.csv', 'documentariesvideos.xlsx', 'csvfilebeatles.csv', 'drinks2.csv', 'pokemon_data.csv', 'Admission_Predict_Ver1.1.csv', 'saveastextcommandelimiter.txt', 'DONT UPLOAD GITHUB PRIVATE TWITTER twitter_credentials.py', 'pythondataanalyticsvisualization05timeseries.py', 'pandaspokemon.py', 'pandasdataschool2022_07webcast.py', 'fremontweather.txt', 'ex_06-03.txt', 'ted.csv', 'small.csv', 'accountscreatetextfile.txt', 'yytest.py']
'''
os.chdir("/media/sf_UbuntuShare2004") #Change directory function
print(os.getcwd()) #print /media/sf_UbuntuShare2004
print(os.listdir(os.curdir))
'''
['advancedguidepythonprogrammingcsvexcelfiles.py', 'advancedguidepythonprogrammingreadwritefiles.py', 'advancedguidepythonprogrammingregularexpressions.py', 'app.js', 'bloghtml', 'completemysqlbeginnertoexpert04.sql', 'deletefolder', 'marinstatslectures02.R', 'marinstatslectures03.R', 'mymath.py', 'quickpythonbook01.py', 'quickpythonbook02.py', 'rstudio COPIED BACK UBUNTU 041423 KEEP TEMPORARILY', 'savedenvironmentmarinstats050923.RData', 'savedenvironmentmarinstats051223.RData', 'Warriors Win Game Seven [qsdaauhtn9Q].m4a', 'What A Weekend! [h4tU-Spc260].m4a']
'''
os.chdir("/home/mar/python") #Change directory function
currentpath = pathlib.Path()
print(currentpath.cwd()) #print /home/mar/python
print(os.path.join("bin", "Utils", "disktools")) #print bin/Utils/disktools.  Create a new pathname inputing directory names or filenames as arguments.  The names or filenames are joined to form a single string as a relative path.  In other words, form file paths from a sequence of directory or filenames.
print(os.path.join("mydir/bin", "utils/disktools/chkdisk")) #print mydir/bin/utils/disktools/chkdisk
path1 = os.path.join("mydir", "bin")
path2 = os.path.join("utils", "disktools", "chkdisk")
print(os.path.join(path1, path2)) #print mydir/bin/utils/disktools/chkdisk.
print(os.path.join("i", "make", "up", "a", "path")) #print i/make/up/a/path
print(os.path.split(os.getcwd())) #print ('/home/mar', 'python').  Separate path names or split path names.
print(os.path.split(os.curdir)) #print ('', '.').  Separate path names or split path names.
print(os.path.basename(os.getcwd())) #print python.  Returns the basename of the path.
print(os.path.basename(os.path.join("media", "sf_UbuntuShare2004", "deletefolder"))) #print deletefolder.  Returns the basename of the path.
print(os.path.dirname(os.getcwd())) #print /home/mar.  Returns the path up to the second to the last name or excludes the last name.
print(os.path.dirname(os.path.join("media", "sf_UbuntuShare2004", "deletefolder"))) #print media/sf_UbuntuShare2004.  Returns the path up to the second to the last name or excludes the last name.
print(os.path.splitext(os.path.join("home", "mar", "python", "yytest.py"))) #print ('home/mar/python/yytest', '.py')
#os.path.commonprefix(path1, path2, path3, . . .) finds the common prefix if any for a set of paths.  Find the lowest level directory which contains every file in a set of files.  RM:  highest level is correct because prefix?  Suffix is the lowest level?
#os.path.expanduser expands username shortcuts in paths.  os.path.expandvars expands environment variables.  Windows 10 os.path.expandvars('$HOME\\temp') returns 'C:\\Users\\administrator\\personal\\temp'
print(os.path.expandvars(os.getcwd())) #print /home/mar/python
print(os.path.expandvars(os.path.join("media", "sf_UbuntuShare2004", "deletefolder"))) #print media/sf_UbuntuShare2004/deletefolder
currentpath = pathlib.Path()
print(currentpath.joinpath("media", "sf_UbuntuShare2004", "deletefolder")) #print media/sf_UbuntuShare2004/deletefolder
print(currentpath.joinpath("i", "make", "up", "a", "path")) #print i/make/up/a/path
print(currentpath.cwd()) #print /home/mar/python
print(currentpath.cwd().parts) #print ('/', 'home', 'mar', 'python').  parts is part of the pathlib module.  parts property returns a tuple of all the components of a path.
print(currentpath.cwd().parent) #print /home/mar.  parent is part of the pathlib module.  parent property returns the path up to the second to the last name or excludes the last name.
print(currentpath.cwd().name) #print python.  name is part of the pathlib module.  name property returns the basename of the path.
print(currentpath.joinpath("home", "mar", "python", "yytest.py")) #print home/mar/python/yytest.py
print(currentpath.joinpath("home", "mar", "python", "yytest.py").suffix) #print .py.  suffix is part of the pathlib module.  suffix returns the dotted extension or file type.
print(os.name) #print posix.  os.name returns the name of the Python module imported to handle the operation system specific details.  Use os.name to determine the operating system user is using.
if os.name == "posix":
    print("User using Linux") #print User using Linux
    rootdirectory = "/"
elif os.name == "nt":
    print("User using Windows")
    rootdirectory = "C:\\"
else:
    print("Don't understand the operating system")
# print(os.environ) #prints environment variables and its values in a dictionary
'''
environ({'SHELL': '/bin/bash', 'SESSION_MANAGER': 'local/mar-VirtualBox:@/tmp/.ICE-unix/1275,unix/mar-VirtualBox:/tmp/.ICE-unix/1275', 'QT_ACCESSIBILITY': '1', 'COLORTERM': 'truecolor', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'XDG_MENU_PREFIX': 'gnome-', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'GNOME_SHELL_SESSION_MODE': 'ubuntu', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'XMODIFIERS': '@im=ibus', 'DESKTOP_SESSION': 'ubuntu', 'SSH_AGENT_PID': '1237', 'GTK_MODULES': 'gail:atk-bridge', 'PWD': '/home/mar/python', 'LOGNAME': 'mar', 'XDG_SESSION_DESKTOP': 'ubuntu', 'XDG_SESSION_TYPE': 'x11', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', 'XAUTHORITY': '/run/user/1000/gdm/Xauthority', 'GJS_DEBUG_TOPICS': 'JS ERROR;JS LOG', 'WINDOWPATH': '2', 'HOME': '/home/mar', 'USERNAME': 'mar', 'IM_CONFIG_PHASE': '1', 'LANG': 'en_US.UTF-8', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'XDG_CURRENT_DESKTOP': 'ubuntu:GNOME', 'VTE_VERSION': '6003', 'GNOME_TERMINAL_SCREEN': '/org/gnome/Terminal/screen/ba8d2f0d_3c26_4cf1_93b8_652e13154df3', 'INVOCATION_ID': '7145af8767e94c6c9ccea1141a33e380', 'MANAGERPID': '953', 'GJS_DEBUG_OUTPUT': 'stderr', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'XDG_SESSION_CLASS': 'user', 'TERM': 'xterm-256color', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'USER': 'mar', 'GNOME_TERMINAL_SERVICE': ':1.79', 'DISPLAY': ':0', 'SHLVL': '1', 'QT_IM_MODULE': 'ibus', 'XDG_RUNTIME_DIR': '/run/user/1000', 'JOURNAL_STREAM': '8:31772', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/home/mar/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'PATH': '/home/mar/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin', 'GDMSESSION': 'ubuntu', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'OLDPWD': '/home/mar', '_': '/usr/bin/python3.8'})
'''
print(type(os.environ)) #prints <class 'os._Environ'>
print(os.path.exists(os.getcwd())) #print True
print(os.path.join(os.getcwd(), "yytest.py")) #print /home/mar/python/yytest.py
print(os.path.exists(os.path.join(os.getcwd(), "yytest.py"))) #print True
print(os.path.isdir(os.getcwd())) #print True
print(os.path.isdir(os.path.join(os.getcwd(), "yytest.py"))) #print False
print(os.path.isfile(os.path.join(os.getcwd(), "yytest.py"))) #print True
print(os.path.isfile(os.getcwd())) #print False
with os.scandir(".") as checkcurrentdirectoryifafile:
    for eachentry in checkcurrentdirectoryifafile:
        print(eachentry.name, eachentry.is_file())
        '''
        combinedatatitanic.txt True
        pythonforprogrammersbasics02.py True
        ETH_1h.csv True
        ml-100k False
        survey_results_schema.csv True
        pythondataanalyticsvisualization02numpy.py True
        exporttocsv.csv True
        mymath.py True
        quickpythonbook01.py True
        pandasdataschool2022_01.py True
        iris.csv True
        pandasdataschool2022_02.py True
        advancedguidepythonprogrammingregularexpressions.py True
        kaggletraintitanic.csv True
        usefultools.py True
        node_modules False
        ...
        '''
#Use the glob module to search for specific filenames
import glob
print(glob.glob("*")) #print ['combinedatatitanic.txt', 'pythonforprogrammersbasics02.py', 'ETH_1h.csv', 'ml-100k', 'survey_results_schema.csv', 'pythondataanalyticsvisualization02numpy.py', 'exporttocsv.csv', 'mymath.py', 'quickpythonbook01.py', 'pandasdataschool2022_01.py', 'iris.csv', 'pandasdataschool2022_02.py', 'advancedguidepythonprogrammingregularexpressions.py', 'kaggletraintitanic.csv', 'usefultools.py', 'node_modules', 'temp.txt', 'combinedatatitaniclowercasecolumns.txt', 'drinks1.csv', 'twitterdownloadtweetsfinalv1.2.py', 'pivot.csv', 'drinksbycountry.csv', . . . ]
print(glob.glob("*.txt")) #print ['combinedatatitanic.txt', 'temp.txt', 'combinedatatitaniclowercasecolumns.txt', 'employees.txt', 'ex_06-01.txt', 'Create Test File On My Windows.txt', 'ex_06-02.txt', 'tempbloghtmlsearchresults.txt', 'namethejsonfile.txt', 'saveastextcommandelimiter.txt', 'fremontweather.txt', 'ex_06-03.txt', 'accountscreatetextfile.txt']
print(glob.glob("*panda*")) #print ['pandasdataschool2022_01.py', 'pandasdataschool2022_02.py', 'pandasjoejames02.py', 'pandasdataschool2022_03.py', 'pythondataanalyticsvisualization03pandas.py', 'pythonpandasandexcel.py', 'pandascoreyschafer.py', 'pandasdataschool2022_04.py', 'pandasdataschool2022_05pandatricks.py', 'pandasjoejames.py', 'pandasdataschool2022_06pycon2019.py', 'pandadataframetocsvfile.csv', 'pandaspokemon.py', 'pandasdataschool2022_07webcast.py']
print(glob.glob("*temp*")) #print ['temp.txt', 'tempexcel.xlsx', 'tempbloghtmlsearchresults.txt']
os.rename("temp.txt", "renametemp.txt") #rename file
print(glob.glob("*temp*")) #print ['tempexcel.xlsx', 'renametemp.txt', 'tempbloghtmlsearchresults.txt']
os.rename("renametemp.txt", "temp.txt")
print(glob.glob("*temp*")) #print ['temp.txt', 'tempexcel.xlsx', 'tempbloghtmlsearchresults.txt']
#os.remove("remove file name") #delete file, remove file.  os.remove can't delete directories delete folders
#os.makedirs("create new directory name")
#os.rmdir("delete directory name") #remove directory
currentpath = pathlib.Path()
print(currentpath.cwd()) #print /home/mar/python
print(list(currentpath.iterdir())) #prints an iterator of paths
'''
[PosixPath('combinedatatitanic.txt'), PosixPath('pythonforprogrammersbasics02.py'), PosixPath('ETH_1h.csv'), PosixPath('ml-100k'), PosixPath('survey_results_schema.csv'), PosixPath('pythondataanalyticsvisualization02numpy.py'), PosixPath('exporttocsv.csv'), PosixPath('mymath.py'), PosixPath('quickpythonbook01.py'), PosixPath('pandasdataschool2022_01.py'), PosixPath('iris.csv'), PosixPath('pandasdataschool2022_02.py'), PosixPath('advancedguidepythonprogrammingregularexpressions.py'), . . . ]
'''
print(list(currentpath.glob("*")))
'''
[PosixPath('combinedatatitanic.txt'), PosixPath('pythonforprogrammersbasics02.py'), PosixPath('ETH_1h.csv'), PosixPath('ml-100k'), PosixPath('survey_results_schema.csv'), PosixPath('pythondataanalyticsvisualization02numpy.py'), PosixPath('exporttocsv.csv'), PosixPath('mymath.py'), PosixPath('quickpythonbook01.py'), PosixPath('pandasdataschool2022_01.py'), PosixPath('iris.csv'), PosixPath('pandasdataschool2022_02.py'), PosixPath('advancedguidepythonprogrammingregularexpressions.py'),
'''
print(list(currentpath.glob("*txt")))
'''
[PosixPath('combinedatatitanic.txt'), PosixPath('temp.txt'), PosixPath('combinedatatitaniclowercasecolumns.txt'), PosixPath('employees.txt'), PosixPath('ex_06-01.txt'), PosixPath('Create Test File On My Windows.txt'), PosixPath('ex_06-02.txt'), PosixPath('tempbloghtmlsearchresults.txt'), PosixPath('namethejsonfile.txt'), PosixPath('saveastextcommandelimiter.txt'), PosixPath('fremontweather.txt'), PosixPath('ex_06-03.txt'), PosixPath('accountscreatetextfile.txt')]
'''
print(list(currentpath.glob("*panda*")))
'''
[PosixPath('pandasdataschool2022_01.py'), PosixPath('pandasdataschool2022_02.py'), PosixPath('pandasjoejames02.py'), PosixPath('pandasdataschool2022_03.py'), PosixPath('pythondataanalyticsvisualization03pandas.py'), PosixPath('pythonpandasandexcel.py'), PosixPath('pandascoreyschafer.py'), PosixPath('pandasdataschool2022_04.py'), PosixPath('pandasdataschool2022_05pandatricks.py'), PosixPath('pandasjoejames.py'), PosixPath('pandasdataschool2022_06pycon2019.py'), PosixPath('pandadataframetocsvfile.csv'), PosixPath('pandaspokemon.py'), PosixPath('pandasdataschool2022_07webcast.py')]
'''
#RM:  can use pathlib to rename files, rename directories, move files, delete files, create new folders or create new directories.  Skipped section
#os.walk traverses recursive directory structures.  Go through an entire directory tree, returning the root or the path, a list of its subdirectories, and a list of files. os.walk(directory, topdown=True, onerror=None, followlinks=False).  directory is the starting directory path.  topdown=True is default the files are processed before its subdirectories resulting ina list which starts at the top and goes down.  topdown=False subdirectories of each directory are processed first giving a bottom-up traversal of the tree.  onerror handles any errors which result from calls to os.listdir which are ignored by default.  os.walk followlinks=False by default doesn't walk down into folders which are symbolic links.
# for root, dirs, files in os.walk(os.getcwd(), topdown=True, onerror=None, followlinks=False):
#     print(files)
