import subprocess
listfiles = subprocess.run(["ls", "-l"]) #type and execute ls -l in terminal
printworkingdirectory = subprocess.run(["pwd"]) #type and execute pwd in terminal
historytrivia = subprocess.run(["calendar"]) #type and execute calendar in terminal
#openfirefox = subprocess.run(["firefox"]) #type and execute firefox in terminal.  Opens Firefox browser.

#https://stackoverflow.com/questions/20810366/executing-shell-script-using-subprocess-popen-in-python
subprocess.call("echo Hello world", shell=True) #executes echo to print Hello world
#subprocess.call("firefox &", shell=True) #executes open program Firefox
subprocess.call("calendar", shell=True) #executes calendar Linux command
#typehelloworld = subprocess.run(["echo Hello world"]) #FileNotFoundError: [Errno 2] No such file or directory: 'echo Hello world'
subprocess.call("echo Hello world", shell=True) #executes echo to print Hello world
