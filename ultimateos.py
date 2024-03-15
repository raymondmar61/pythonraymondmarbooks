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
os.rmdir("/home/mar/createnewfoldername") #delete directory, delete folder permanently
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
print(os.listdir()) #print ['yyextractimages.py', 'pdfextractimagesfunction.py', 'pdfextractimages.py'].  All files in a list in directory function run.  print(os.listdir(os.curdir)) also works specifying current working directory.
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
# also os.unlink("readcreatetextfilefrompythonos.txt") #delete readcreatetextfilefrompythonos.txt permanently
# also os.unlink("/home/mar/readcreatetextfilefrompythonos.txt") #delete readcreatetextfilefrompythonos.txt at /home/mar/ permanently
os.chdir("/home/mar/python")
#print(os.listdir()) #print [..., 'mymath.py', 'quickpythonbook01.py', 'datapipes.txt', 'pandasdataschool2022_01.py', 'page1.jpg', 'iris.csv', 'imagename1.jpeg', 'q', 'pandasdataschool2022_02.py', ...].  Get files list files.
#print(os.listdir("/home/mar")) #print [...'mysql-workbench-community_8.0.29-1ubuntu20.04_amd64.deb', '.mysql_history', 'Music', '.vboxclient-clipboard.pid', 'Pictures', '.sudo_as_admin_successful', 'Documents'].  Get files from another directory.
datelastmodified = os.stat("ultimatepandas1.py").st_mtime
print(datelastmodified) #print 1706153504.5359838
import datetime
print(datetime.datetime.fromtimestamp(datelastmodified)) #print 2024-01-24 19:31:44.535984
filestatistics = os.stat("ultimatepandas1.py")
print(filestatistics) #print os.stat_result(st_mode=33206, st_ino=4214080, st_dev=2053, st_nlink=1, st_uid=1000, st_gid=1000, st_size=176925, st_atime=1706153515, st_mtime=1706153504, st_ctime=1706153504)
filesizeinbytes = os.stat("ultimatepandas1.py").st_size
print(filesizeinbytes) #print 176925
kilobytes = filesizeinbytes / 1000
megabytes = filesizeinbytes / 1000000
gigabytes = filesizeinbytes / 1000000000000 #RM:  twelve zeroes
print(megabytes) #print 0.176925
print(gigabytes) #print 1.76925e-07

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
for forlooplisteachfile in os.listdir("/home/mar/python/"):
    print(forlooplisteachfile)
    '''
    ativityExamplepage3.pdf
    moby01.txt
    endgamecsvexpenses.csv
    endgametabpaymentmethod.txt
    pythoninfiniteloopalistlinks.pdf
    combinedatatitanic.txt
    creditcategoryfilename.xlsx
    pythonforprogrammersbasics02.py
    ...
    '''
for forloopdeletefiles in os.listdir():
    separatefiletype = os.path.splitext(forloopdeletefiles)[1]
    if separatefiletype == ".txt":
        print("pretend delete " + separatefiletype + " by typing os.unlink(forloopdeletefiles) or os.remove(forloopdeletefiles)") #print pretend delete .txt by typing os.unlink(forloopdeletefiles) or os.remove(forloopdeletefiles)
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
print(os.walk("/home/mar/python")) #print <generator object walk at 0x7fd869fc4ac0>
for foldername, subfoldername, filename in os.walk("/home/mar/python"):
    print("FOLDERNAME is Folder in python directory " + foldername)
    for eachsubfoldername in subfoldername:
        print("SubFolderName " + eachsubfoldername + " in " + foldername)
    for eachfilename in filename:
        print("filename " + eachfilename + " in " + foldername)
    '''
    <generator object walk at 0x7fea3d35dac0>
    FOLDERNAME is Folder in python directory /home/mar/python
    SubFolderName ml-100k in /home/mar/python
    SubFolderName node_modules in /home/mar/python
    SubFolderName pdffiles in /home/mar/python
    SubFolderName __pycache__ in /home/mar/python
    filename NativityExamplepage3.pdf in /home/mar/python
    filename moby01.txt in /home/mar/python
    filename endgamecsvexpenses.csv in /home/mar/python
    filename endgametabpaymentmethod.txt in /home/mar/python
    filename pythoninfiniteloopalistlinks.pdf in /home/mar/python
    filename combinedatatitanic.txt in /home/mar/python
    filename creditcategoryfilename.xlsx in /home/mar/python
    filename pythonforprogrammersbasics02.py in /home/mar/python
    ...
    '''
print(os.scandir()) #print <posix.ScandirIterator object at 0x7fbbb50d4ab0>
print(os.scandir(".")) #print <posix.ScandirIterator object at 0x7fbbb50d4ab0>
for extractfilenames in os.scandir():
    print(extractfilenames)
    '''
    <DirEntry 'NativityExamplepage3.pdf'>
    <DirEntry 'moby01.txt'>
    <DirEntry 'endgamecsvexpenses.csv'>
    <DirEntry 'endgametabpaymentmethod.txt'>
    <DirEntry 'pythoninfiniteloopalistlinks.pdf'>
    <DirEntry 'combinedatatitanic.txt'>
    <DirEntry 'creditcategoryfilename.xlsx'>
    <DirEntry 'pythonforprogrammersbasics02.py'>
    ...
    '''
with os.scandir() as checkcurrentdirectoryifafile:
    for eachentry in checkcurrentdirectoryifafile:
        print(eachentry.name, eachentry.is_file())
        print(eachentry.name, os.path.isfile(eachentry))
        '''
        NativityExamplepage3.pdf True
        NativityExamplepage3.pdf True
        moby01.txt True
        moby01.txt True
        endgamecsvexpenses.csv True
        endgamecsvexpenses.csv True
        endgametabpaymentmethod.txt True
        endgametabpaymentmethod.txt True
        pythoninfiniteloopalistlinks.pdf True
        pythoninfiniteloopalistlinks.pdf True
        combinedatatitanic.txt True
        combinedatatitanic.txt True
        creditcategoryfilename.xlsx True
        creditcategoryfilename.xlsx True
        pythonforprogrammersbasics02.py True
        pythonforprogrammersbasics02.py True
        ...
        '''
for extractfilenames in os.scandir():
    print(extractfilenames.name)
    '''
    NativityExamplepage3.pdf
    moby01.txt
    endgamecsvexpenses.csv
    endgametabpaymentmethod.txt
    pythoninfiniteloopalistlinks.pdf
    combinedatatitanic.txt
    creditcategoryfilename.xlsx
    pythonforprogrammersbasics02.py
    ...
    '''

#Operating system
print(os.name) #print posix.  os.name returns the name of the Python module imported to handle the operation system specific details.  Use os.name to determine the operating system user is using.
if os.name == "posix":
    print("User using Linux") #print User using Linux
    rootdirectory = "/"
elif os.name == "nt":
    print("User using Windows")
    rootdirectory = "C:\\"
else:
    print("Don't understand the operating system")
environmentvariables = os.environ
print(environmentvariables) #print environ({'SHELL': '/bin/bash', 'SESSION_MANAGER': 'local/mar-VirtualBox:@/tmp/.ICE-unix/1375,unix/mar-VirtualBox:/tmp/.ICE-unix/1375', 'QT_ACCESSIBILITY': '1', 'COLORTERM': 'truecolor', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/etc/xdg', 'XDG_MENU_PREFIX': 'gnome-', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'GNOME_SHELL_SESSION_MODE': 'ubuntu', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'XMODIFIERS': '@im=ibus', 'DESKTOP_SESSION': 'ubuntu', 'SSH_AGENT_PID': '1282', 'GTK_MODULES': 'gail:atk-bridge', 'PWD': '/home/mar/python', 'LOGNAME': 'mar', 'XDG_SESSION_DESKTOP': 'ubuntu', 'XDG_SESSION_TYPE': 'x11', 'GPG_AGENT_INFO': '/run/user/1000/gnupg/S.gpg-agent:0:1', 'XAUTHORITY': '/run/user/1000/gdm/Xauthority', 'GJS_DEBUG_TOPICS': 'JS ERROR;JS LOG', 'WINDOWPATH': '2', 'HOME': '/home/mar', 'USERNAME': 'mar', 'IM_CONFIG_PHASE': '1', 'LANG': 'en_US.UTF-8', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:', 'XDG_CURRENT_DESKTOP': 'ubuntu:GNOME', 'VTE_VERSION': '6003', 'GNOME_TERMINAL_SCREEN': '/org/gnome/Terminal/screen/fe4e5363_23d8_44ea_af2d_5692ce855abe', 'INVOCATION_ID': 'b9a7785d517847018c7bd71a6114e334', 'MANAGERPID': '1003', 'GJS_DEBUG_OUTPUT': 'stderr', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'XDG_SESSION_CLASS': 'user', 'TERM': 'xterm-256color', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'USER': 'mar', 'GNOME_TERMINAL_SERVICE': ':1.89', 'DISPLAY': ':0', 'SHLVL': '1', 'QT_IM_MODULE': 'ibus', 'XDG_RUNTIME_DIR': '/run/user/1000', 'JOURNAL_STREAM': '8:32202', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/home/mar/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'PATH': '/home/mar/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin', 'GDMSESSION': 'ubuntu', 'DBUS_SESSION_BUS_ADDRESS': 'unix:path=/run/user/1000/bus', 'OLDPWD': '/home/mar', '_': '/usr/bin/python3.8'})
print(environmentvariables["OLDPWD"]) #print /home/mar

#Run Linux commands, execute Linux commands
import subprocess
listfiles = subprocess.run(["ls", "-l"]) #type and execute ls -l in terminal
listfilesneedprintfunction = subprocess.run(["ls", "-l"], capture_output=True)
print(listfilesneedprintfunction) #print CompletedProcess(args=['ls', '-l'], returncode=0, stdout=b'total 215520\n-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf\n-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt\n-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv\n-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json\n-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv\n-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py\n-rw-rw-rw- 1 mar mar . . .
print(listfilesneedprintfunction.stdout) #print b'total 215520\n-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf\n-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt\n-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv\n-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json\n-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv\n-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py\n-rw-rw-rw- 1 mar mar . . .
print(listfilesneedprintfunction.stdout.decode())
'''
total 215520
-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf
-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt
-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv
-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json
-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv
-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py
...
'''
listfilesneedprintfunction = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(listfilesneedprintfunction.stdout)
'''
total 215520
-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf
-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt
-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv
-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json
-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv
-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py
...
'''
listfilesneedprintfunction = subprocess.run(["ls", "-l"], shell=True, capture_output=True, text=True)
print(listfilesneedprintfunction.stdout)
'''
56_power_query_tutorials.pdf
accountscreatetextfile.txt
accountscsvfile.csv
accountsjson.json
Admission_Predict_Ver1.1.csv
advancedguidepythonprogrammingasyncio.py
'''
listfilesneedprintfunction = subprocess.run(["ls", "-l"], shell=True, text=True)
print(listfilesneedprintfunction.stdout) #print None
listfilesneedprintfunctionpipe = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
print(listfilesneedprintfunctionpipe.stdout)
'''
56_power_query_tutorials.pdf                      generatepasswords.py                      pythondataanalyticsvisualization05timeseries.py
 accountscreatetextfile.txt                   Im1.jpg                               pythondataanalyticsvisualization06interactingwithdatabases.py
 accountscsvfile.csv                          Im2.png                               pythondataanalyticsvisualization07dataanalysisapplicationexamples.py
 accountsjson.json                        imagename1.jpeg                           pythonforprogrammersbasics02.py
 Admission_Predict_Ver1.1.csv                     imagename2.png                            pythonforprogrammersbasics.py
 advancedguidepythonprogrammingasyncio.py             imdbratings.csv                           pythonforprogrammersregularexpressions.py
 ...
total 215520
-rwxrwxrw- 1 mar vboxsf    345082 Aug  3  2023 56_power_query_tutorials.pdf
-rw-rw-rw- 1 mar mar          121 Jan 11 14:16 accountscreatetextfile.txt
-rw-rw-rw- 1 mar mar           83 Mar 21  2023 accountscsvfile.csv
-rw-rw-rw- 1 mar mar          119 Mar 21  2023 accountsjson.json
-rwxrwxrw- 1 mar vboxsf     16175 Sep 28  2022 Admission_Predict_Ver1.1.csv
-rw-rw-rw- 1 mar mar         8221 Jun  5  2023 advancedguidepythonprogrammingasyncio.py
...
'''
unsuccessfullinuxcommand = subprocess.run(["ls", "-l", "doesnotexist"], capture_output=True, text=True)
print(unsuccessfullinuxcommand.stdout) #print *nothing*
print(unsuccessfullinuxcommand.returncode) #print 2
print(unsuccessfullinuxcommand.stderr) #print ls: cannot access 'doesnotexist': No such file or directory
unsuccessfullinuxcommand = subprocess.run(["ls", "-l", "doesnotexist"], capture_output=True)
print(unsuccessfullinuxcommand.stdout) #print b''
print(unsuccessfullinuxcommand.returncode) #print 2
print(unsuccessfullinuxcommand.stderr) #print b"ls: cannot access 'doesnotexist': No such file or directory\n"
printworkingdirectory = subprocess.run(["pwd"]) #type and execute pwd in terminal
historytrivia = subprocess.run(["calendar"]) #type and execute calendar in terminal
#openfirefox = subprocess.run(["firefox"]) #type and execute firefox in terminal.  Opens Firefox browser.
readtextfile = subprocess.run(["cat", "moby01.txt"], capture_output=True, text=True)
print(readtextfile.stdout)
'''
Call me Ishmael. Some years ago--never mind how long precisely--
having little or no money in my purse, and nothing particular
to interest me on shore, I thought I would sail about a little
and see the watery part of the world. It is a way I have
of driving off the spleen and regulating the circulation.
...
'''
readtextfilemorecommand = subprocess.run(["more", "moby01.txt"], capture_output=True, text=True)
catviewfile = subprocess.run(["cat"], capture_output=True, text=True, input=readtextfilemorecommand.stdout)
print(catviewfile.stdout)
'''
Call me Ishmael. Some years ago--never mind how long precisely--
having little or no money in my purse, and nothing particular
to interest me on shore, I thought I would sail about a little
and see the watery part of the world. It is a way I have
of driving off the spleen and regulating the circulation.
...
'''

#https://stackoverflow.com/questions/20810366/executing-shell-script-using-subprocess-popen-in-python
subprocess.call("echo Hello world", shell=True) #executes echo to print Hello world
#subprocess.call("firefox &", shell=True) #executes open program Firefox
subprocess.call("calendar", shell=True) #executes calendar Linux command
#typehelloworld = subprocess.run(["echo Hello world"]) #FileNotFoundError: [Errno 2] No such file or directory: 'echo Hello world'
subprocess.call("echo Hello world", shell=True) #executes echo to print Hello world

subprocess.call("ls *.txt", shell=True) #return text files in present directory
listoutput = subprocess.check_output("ls *.txt", shell=True)
print(listoutput) #print b'accountscreatetextfile.txt\nbasicreadwritefile.txt\ncombinedatatitaniclowercasecolumns.txt\ncombinedatatitanic.txt\ncopytemp.txt\nCreate Test File On My Windows.txt\n . . .
print(type(listoutput)) #print <class 'bytes'>
print(listoutput.decode()) #print text files in present directory
print(type(listoutput.decode())) #print <class 'str'>