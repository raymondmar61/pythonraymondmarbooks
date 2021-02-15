# import os

# os.system("ls -l")
# #os.system("firefox &")
# stream = os.popen("echo Returned output")
# output = stream.read()
# print(output)

import subprocess
listfiles = subprocess.run(["ls", "-l"])
#openfirefox = subprocess.run(["firefox"])

#https://stackoverflow.com/questions/20810366/executing-shell-script-using-subprocess-popen-in-python
subprocess.call("echo Hello world", shell=True)
subprocess.call("firefox &", shell=True)
