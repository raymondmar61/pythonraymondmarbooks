import subprocess

subprocess.call("ls", shell=True) #return list files in present directory
listoutput = subprocess.check_output("ls", shell=True)
print(listoutput)
'''
b'arraytextfilename.txt\narraytextfile.txt\ncreatetempfilenameathomedirectory\ncsvalltutorials.py\ncsvfiles\ndeveloper_survey_2019\ndifferencemultiprocessingthreading.py\ndivclassitemcontainersample.html\ndownloadimages.py\nespnfavoritetweets.csv\nespntweets.csv\nETH_1h.csv\nexistingmodules.py\nfavoritetweets.csv\nfavoritetweetstext.txt\nfilename\nfilename.png\nfoo.csv\nfremontweather.txt\nfunctionsfile.py\ngrasspoisonhp70plusexporttocsvfile\nidtweets.csv\ninin61tweets.csv\nininbloghtmlnodate.py\njsonfiles\njsonpython.py\nmarbasicspythonclasses.py\nmarbasicspython.py\nmarcommonmodulespython.py\nmardatestimes.py\nmatplotlib\nmatplotliballtutorials.py\nmytweetsroughdraft.csv\nnihilist_arbystweets.csv\nnumpyalltutorials.py\nnumpyw3resource01.py\nnumpyw3resource02.py\noneminutedeletetemp.txt\noverwritefile.py\npandasalltutorials2.py\npandasalltutorials.py\npandasdataschool.py\npokemon_data.csv\npokemon_data.txt\npokemon_data.xlsx\npopularpackages.py\n__pycache__\npythonmultiprocessing.py\npythonosmodule.py\npythonpicklemodule.py\npythonthreading.py\nRaymond Mar.jpeg\nsampleinin61tweets.txt\nsavednumpyfilename.npz\nsavetextarray.out\nsavetextarray.txt\nsavetextarray.txt.npz\ntempdelete.txt\ntempnumpyarray.txt.npy\ntemptwitterjson.json\ntemptwitter.txt\ntestdelete.py\ntroubleshoottweets.csv\ntroubleshoottweets.py\ntweepybasics.py\ntweepyfavorites.py\ntwitter-2020-03-27-4d697e69ff1b8b36c5d7caaa564e8a0a1b5a8ce59b08bf00b389ed1e456b965f\ntwitterapiallvideos.py\ntwitter_credentials.py\ntwitterdownloadfavoritesv1.py\ntwitterdownloadtweetsfinalv1.py\ntwitterwritecsv.py\ntxtfiles\nwebscraping.py\nwork3.7\nyywork.py\nZulu Dawn 1979 Full Movie-r1tMgptVe7I.mp4.part\nzzpandas.py\n'
'''
# for eachlistoutput in listoutput:
#     print(eachlistoutput) #printed random numbers I don't understand
subprocess.call("python3.6 overwritefile.py", shell=True) #return result from overwritefile.py which is love
subprocess.call("python3.6 overwritefile.py" "the quick brown fox jumped over the lazy dog", shell=True) #return python3.6: can't open file 'overwritefile.pythe': [Errno 2] No such file or directory
subprocess.call("'''checkthisout'''", shell=True) #return /bin/sh: 1: checkthisout: not found
subprocess.check_output("python3.6 overwritefile.py", shell=True)

#Coding in Python 20 - Subprocess-EOb37Oug_cw
#install modules
#subprocess.call("sudo apt-get install python-tweepy", shell=True)

# svc = "sshd"
# servicecheck = subprocess.call(["ps", "-c", svc])
# if servicecheck == 0:
# 	print("The service is running.")
# else:
# 	print("The service is not running.")
'''
error: unsupported option (BSD syntax)

Usage:
 ps [options]

 Try 'ps --help <simple|list|output|threads|misc|all>'
  or 'ps --help <s|l|o|t|m|a>'
 for additional help text.

For more details see ps(1).
The service is not running.
'''

#Python Tutorial - Calling External Commands Using the Subprocess Module-2Fp1N6dof0Y
import subprocess
subprocess.call("ls", shell=True) #return list files in present directory
listoutput = subprocess.check_output("ls", shell=True)
print(listoutput)
'''
RM:  printed as bytes
b'arraytextfilename.txt\narraytextfile.txt\ncreatetempfilenameathomedirectory\ncsvalltutorials.py\ncsvfiles\ndeveloper_survey_2019\ndifferencemultiprocessingthreading.py\ndivclassitemcontainersample.html\ndownloadimages.py\nespnfavoritetweets.csv\nespntweets.csv\nETH_1h.csv\nexistingmodules.py\nfavoritetweets.csv\nfavoritetweetstext.txt\nfilename\nfilename.png\nfoo.csv\nfremontweather.txt\nfunctionsfile.py\ngrasspoisonhp70plusexporttocsvfile\nidtweets.csv\ninin61tweets.csv\nininbloghtmlnodate.py\njsonfiles\njsonpython.py\nmarbasicspythonclasses.py\nmarbasicspython.py\nmarcommonmodulespython.py\nmardatestimes.py\nmatplotlib\nmatplotliballtutorials.py\nmytweetsroughdraft.csv\nnihilist_arbystweets.csv\nnumpyalltutorials.py\nnumpyw3resource01.py\nnumpyw3resource02.py\noneminutedeletetemp.txt\noverwritefile.py\npandasalltutorials2.py\npandasalltutorials.py\npandasdataschool.py\npokemon_data.csv\npokemon_data.txt\npokemon_data.xlsx\npopularpackages.py\n__pycache__\npythonmultiprocessing.py\npythonosmodule.py\npythonpicklemodule.py\npythonthreading.py\nRaymond Mar.jpeg\nsampleinin61tweets.txt\nsavednumpyfilename.npz\nsavetextarray.out\nsavetextarray.txt\nsavetextarray.txt.npz\ntempdelete.txt\ntempnumpyarray.txt.npy\ntemptwitterjson.json\ntemptwitter.txt\ntestdelete.py\ntroubleshoottweets.csv\ntroubleshoottweets.py\ntweepybasics.py\ntweepyfavorites.py\ntwitter-2020-03-27-4d697e69ff1b8b36c5d7caaa564e8a0a1b5a8ce59b08bf00b389ed1e456b965f\ntwitterapiallvideos.py\ntwitter_credentials.py\ntwitterdownloadfavoritesv1.py\ntwitterdownloadtweetsfinalv1.py\ntwitterwritecsv.py\ntxtfiles\nwebscraping.py\nwork3.7\nyywork.py\nZulu Dawn 1979 Full Movie-r1tMgptVe7I.mp4.part\nzzpandas.py\n'
'''
print(listoutput.decode()) #print list files in present directory as one line
print(type(listoutput.decode())) #print <class 'str'>
# for eachfilename in listoutput.decode():
#     print("eachfilename " + eachfilename)
#     '''
#     eachfilename a
#     eachfilename r
#     eachfilename r
#     eachfilename a
#     eachfilename y
#     eachfilename t
#     eachfilename e
#     eachfilename x
# 	...
# 	'''
subprocess.run("ls") #return list files in present directory
subprocess.run("ls", shell=True) #return list files in present directory
subprocess.run("ls -la", shell=True) #return list files with option -la in present directory
# subprocess.run("ls -la") #return FileNotFoundError: [Errno 2] No such file or directory: 'ls -la': 'ls -la'
subprocess.run(["ls", "-la"]) #return list files with option -la in present directory
capturevariable = subprocess.run(["ls", "-la"]) #return list files with option -la in present directory as capturevariable itself
print(capturevariable) #print CompletedProcess(args=['ls', '-la'], returncode=0)
print(capturevariable.args) #print ['ls', '-la']
print(capturevariable.returncode) #print 0 which means run successful or zero errors
print(capturevariable.stdout) #print None

#code run on Python3.8
capturevariableforprinting = subprocess.run(["ls", "-la"], capture_output=True)
print(capturevariableforprinting) #print CompletedProcess(args=['ls', '-la'], returncode=0, stdout=b'total 4204\ndrwxrwxr-x  4 mar mar     593920 May  1 13:03 .\ndrwxr-xr-x 20 mar mar       4096 May  3 14:53 ..\n-rw-rw-r--  1 mar mar     137172 May  1 13:33 beautifulsouppics.py\n-rw-rw-r--  1 mar mar      85875 Jan 31 14:36 beautifulsouptutorial.py\n-rw-rw-r--  1 mar mar . . .
print(capturevariableforprinting.stdout) #print b'total 4204\ndrwxrwxr-x  4 mar mar     593920 May  1 13:03 .\ndrwxr-xr-x 20 mar mar       4096 May  3 14:53 ..\n-rw-rw-r--  1 mar mar     137172 May  1 13:33 beautifulsouppics.py\n-rw-rw-r--  1 mar mar      85875 Jan 31 14:36 beautifulsouptutorial.py\n-rw-rw-r--  1 mar mar . . .
print(capturevariableforprinting.stdout.decode())
'''
total 4204
drwxrwxr-x  4 mar mar     593920 May  1 13:03 .
drwxr-xr-x 20 mar mar       4096 May  3 14:53 ..
-rw-rw-r--  1 mar mar     137172 May  1 13:33 beautifulsouppics.py
-rw-rw-r--  1 mar mar      85875 Jan 31 14:36 beautifulsouptutorial.py
'''
capturevariableforprintingtext = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(capturevariableforprintingtext.stdout)
'''
total 4204
drwxrwxr-x  4 mar mar     593920 May  1 13:03 .
drwxr-xr-x 20 mar mar       4096 May  3 14:53 ..
-rw-rw-r--  1 mar mar     137172 May  1 13:33 beautifulsouppics.py
-rw-rw-r--  1 mar mar      85875 Jan 31 14:36 beautifulsouptutorial.py
'''
capturevariableforprintingtext = subprocess.run(["ls", "-la"], shell=True, capture_output=True, text=True)
print(capturevariableforprintingtext.stdout) #print beautifulsouppics.py\n beautifulsouptutorial.py . . .
capturevariableforprintingtext = subprocess.run(["ls", "-la"], shell=True, text=True) #return list files with option -la in present directory
print(capturevariableforprintingtext.stdout) #print None
capturevariableforprintingtextpipe = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE, text=True)
print(capturevariableforprintingtextpipe) #print CompletedProcess(args=['ls', '-la'], returncode=0, stdout=b'total 4204\ndrwxrwxr-x  4 mar mar     593920 May  1 13:03 .\ndrwxr-xr-x 20 mar mar       4096 May  3 14:53 ..\n-rw-rw-r--  1 mar mar     137172 May  1 13:33
with open("temptext.txt", "w") as fileobject:
    filesintextfile = subprocess.run(["ls", "-la"], stdout=fileobject, text=True) #return temptext.txt text file written ls -la output
unsuccessfulcommand = subprocess.run(["ls", "-la", "doesnotexist"], capture_output=True, text=True)
print(unsuccessfulcommand) #print CompletedProcess(args=['ls', '-la', 'doesnotexist'], returncode=2, stdout='', stderr="ls: cannot access 'doesnotexist': No such file or directory\n")
print(unsuccessfulcommand.returncode) #print 2
print(unsuccessfulcommand.stderr) #print ls: cannot access 'doesnotexist': No such file or directory
unsuccessfulcommandchecked = subprocess.run(["ls", "-la", "doesnotexist"], capture_output=True, check=True)
print(unsuccessfulcommandchecked.stderr) #print subprocess.CalledProcessError: Command '['ls', '-la', 'doesnotexist']' returned non-zero exit status 2.
unsuccessfulcommanddevnull = subprocess.run(["ls", "-la", "doesnotexist"], stderr=subprocess.DEVNULL)
print(unsuccessfulcommanddevnull.stderr) #print None
readtextfilereturnbytes = subprocess.run(["cat", "temptext.txt"], capture_output=True)
print(readtextfilereturnbytes.stdout)
'''
b'total 4204\ndrwxrwxr-x  4 mar mar     593920 May  3 15:05 .\ndrwxr-xr-x 20 mar mar       4096 May  3 14:53 ..\n-rw-rw-r--  1 mar mar     137172 May  1 13:33 beautifulsouppics.py\n-rw-rw-r--  1 mar mar      85875 Jan 31 14:36 beautifulsouptutorial.py\n-rw-rw-r--  1 mar mar . . .
'''
readtextfile = subprocess.run(["cat", "temptext.txt"], capture_output=True, text=True)
print(readtextfile.stdout)
'''
total 4204
drwxrwxr-x  4 mar mar     593920 May  3 15:05 .
drwxr-xr-x 20 mar mar       4096 May  3 14:53 ..
-rw-rw-r--  1 mar mar     137172 May  1 13:33 beautifulsouppics.py
-rw-rw-r--  1 mar mar      85875 Jan 31 14:36 beautifulsouptutorial.py
-rw-rw-r--  1 mar mar 
...
'''
grepsearchtesttextfile = subprocess.run(["grep", "-n", "test"], capture_output=True, text=True, input=readtextfile.stdout)
print(grepsearchtesttextfile.stdout)
'''
32:-rw-rw-r--  1 mar mar    1137114 May  1 12:43 test.html
33:-rw-rw-r--  1 mar mar          0 Feb 14 18:09 testlinks.txt
34:-rw-rw-r--  1 mar mar        672 Jun  9  2020 testmoduleoriginal.py
35:-rw-rw-r--  1 mar mar        831 Jun  9  2020 testmodule.py
36:-rwxrwx---  1 mar mar         36 May 12  2020 testpython2.py
37:-rwxrwx---  1 mar mar         68 May 12  2020 testpython.py
46:-rw-rw-r--  1 mar mar       6662 May  1 13:32 yytest.py
47:-rw-rw-r--  1 mar mar       2706 May  3 15:08 zztest.py
'''
combinegrepreadtextfile = subprocess.run("cat temptext.txt | grep -n test", capture_output=True, text=True, shell=True)
