import sys

sys.stderr.write("pronounced s-t-err\n") #return pronounced s-t-err
sys.stderr.flush()
sys.stdout.write("pronounced s-t-out\n") #return pronounced s-t-out
print(sys.argv)  #print ['yytest.py', 'Sentence typed on terminal.']  Returns file name and more; typed python yytest.py "Sentence typed on terminal."  Pronounced arg-v.
print(type(sys.argv)) #print <class 'list'>
print(len(sys.argv)) #print 2
if len(sys.argv) > 1:
    print(sys.argv[1]) #print Sentence typed on terminal.
    sys.argv[1] = 5.67 #change Sentence typed on terminal. to number 5 for math problem (float(sys.argv[1]) + 5)
    print(float(sys.argv[1]) + 5) #print 10.67
def returnarv(argument):
    print(argument) #print 5.67 RM:  I changed sys.argv[1] from Sentence typed on terminal. to 5.67.


returnarv(sys.argv[1])
