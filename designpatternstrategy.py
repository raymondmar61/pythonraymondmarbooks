#Python Strategy Design Pattern Iterator Design Pattern.pdf
#The idea is you may want to run several diferent algorithms.  You want to choose from among them at runtime.  You can't know which strategy you need until runtime.  For instance, you receive text from a remote client or office.  We want the text received is the same text they planned to send.  We apply a function to the text we receive.  If the result is the same as the sender's result, then the message arrived intact.  Which function is used?  len function returns the string's length, SHA1 the same algorithm used by Git, or MD5 often used for the purpose.  Which of the three algorithms applied.  We need to choose the appropriate algorithm at runtime.
#How to use the strategy pattern?
#First we can have multiple classes each implementing the same interface.  Then our program chooses from among these options.  This is a weak form of the strategy pattern.  The program below implements a class for each of our strategies and provide a "check" method which takes a string and returns the result of running the appropriate algorithm on it.
import hashlib

class LenChecker:
    def check(self, text):
        return(len(text))

class SHA1Checker:
    def check(self, text):
        h = hashlib.sha1()
        h.update(text.encode())
        return(h.hexdigest())
class MD5Checker:
    def check(self, text):
        h = hashlib.md5()
        h.update(text.encode())
        return h.hexdigest()


lenclass = LenChecker()
sha1class = SHA1Checker()
md5class = MD5Checker()

text = "this is a secret document"
print(lenclass.check(text)) #print 25
print(sha1class.check(text)) #print 5a23d5cddc3da0aabb8a7f2b71cd60ca2bc31272
print(md5class.check(text)) #print 83647c923faa314791bc53417eb59d44

#We want a single class which implements our checking strategy.  We have a single class Checker to communicate.  We don't call any of the three checkers directly.  At runtime, we choose one of the three strategies invoking the check method.
class Checker():
    def __init__(self, whichstrategy):
        self.whichstrategy = whichstrategy
    def check(self, text):
        print("Checker class check method self.strategy " + str(self.whichstrategy))
        return self.whichstrategy.check(text)


text = "this is a secret document which strategy"
selectedlenclass = Checker(LenChecker())
print(selectedlenclass.check(text))
'''
Checker class check method self.strategy <__main__.LenChecker object at 0x7f42c5ceffd0>
40
'''
selectedsha1class = Checker(SHA1Checker())
print(selectedsha1class.check(text))
'''
Checker class check method self.strategy <__main__.SHA1Checker object at 0x7f42c5cf4ee0>
9f0f47e2390ba7b0041907fa2b4875ef3ebb13df
'''
selectedmd5 = Checker(MD5Checker())
print(selectedmd5.check(text))
'''
Checker class check method self.strategy <__main__.MD5Checker object at 0x7faf9ad57b50>
938f1fd8f5b3675a2c64457339282e1f
'''

#Part of the strategy design pattern is we choose or switch at runtime.  The decision is recorded and stored in our strategy-implementing class.  We choose which strategy to use when we invoke the check method.  The CheckerUserChooses class chooses from three algorithms.  We can add additional algorithms over time.
class CheckerUserChooses():
    def check(self, strategyselected, text):
        if strategyselected == "len":
            classused = LenChecker()
        elif strategyselected == "sha1":
            classused = SHA1Checker()
        elif strategyselected == "md5":
            classused = MD5Checker()
        else:
            raise ValueError(f"No strategy {strategyselected} known")
        return classused.check(text)


text = "this is a secret document user selects strategy"
userselectedlenclass = CheckerUserChooses()
print(userselectedlenclass.check("len", text)) #print 47
userselectedsha1class = CheckerUserChooses()
print(userselectedsha1class.check("sha1", text)) #print 1b252993411027ce8e09ec0e7867a747dd52a9fb
userselectedmd5class = CheckerUserChooses()
print(userselectedmd5class.check("md5", text)) #print 37e0fc5dbbe793862a6877160cbcc8fd

#A dispatch table.  Write three functions instead of three classes which have a common interface.  Put the functions in a dictoary.  Retrieve the appropriate function via its key.  We retrieve a value from checksdictionary using the string which identifies the algorithm we want to use.  The value we get back is a function.
def sha1check(s):
    h = hashlib.sha1()
    h.update(text.encode())
    return h.hexdigest()
def md5check(s):
    h = hashlib.md5()
    h.update(text.encode())
    return h.hexdigest()


checksdictionary = {"len": len, "sha1": sha1check, "md5": md5check}
text = "this is a secret message dispatch table dictionary"
print(checksdictionary["len"](text)) #print 50  #RM:  len is a function.  len is a build-in function.
print(checksdictionary["sha1"](text)) #print f6c5c9b114abf523cf751fed5c2c35038c6f8e4e
print(checksdictionary["md5"](text)) #print 1059452daedf155eb82c62158f60445f
