#Python Binary Search Tree - BST [YlgPi75hIBc]

class Node: #helper class.  Invisible to the user.  Recursive functions.
    def __init__(self, val):
        self.value = val #data value
        self.leftChild = None
        self.rightChild = None
    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()
    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree: #main interface for the user to use a binary tree
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder(self):
        print("PreOrder")
        self.root.preorder()
    def postorder(self):
        print("PostOrder")
        self.root.postorder()
    def inorder(self):
        print("InOrder")
        self.root.inorder()


bstbinarysearchtree = Tree()
bstbinarysearchtree.insert(10)
print("print statement", bstbinarysearchtree.insert(15))
bstbinarysearchtree.preorder()
bstbinarysearchtree.postorder()
bstbinarysearchtree.inorder()
'''
print statement True
PreOrder
10
15
PostOrder
15
10
InOrder
10
15
'''

#69 Python Tutorial for Beginners ｜ Binary Search Using Python [DE-ye0t0oxE]
position = -1
def searchbinary(listnumbers, n):
    # i = 0
    # while i < len(listnumbers):
    #     if listnumbers[i] == n:
    #         globals()["position"] = i
    #         return True
    #     i += 1
    # return False
    lowerbound = 0
    upperbound = len(listnumbers) - 1
    while lowerbound <= upperbound:
        midbound = (lowerbound + upperbound) // 2
        if listnumbers[midbound] == n:
            globals()["position"] = midbound
            return True
        else:
            if listnumbers[midbound] < n:
                lowerbound = midbound + 1
            else:
                upperbound = midbound - 1
    return False


listnumbers = [4, 7, 8, 12, 45, 99]
listnumbers = [4, 7, 8, 12, 45, 99, 102, 702, 10987, 56666]
nfindnumber = 10
if searchbinary(listnumbers, nfindnumber):
    print("Found at position number", position + 1)
else:
    print("Not found")

#Binary Search - Leetcode 704 - Python [s4DPM8ct1pI]
#A list of integers sorted ascending.  Integer target.  Write a function search target in the list.  Return the index number.  Otherwise return -1.  Run the program efficiently with 0(log n) runtime.  Use binary search.
class Solution:
    def search(self, numslist: list[int], targetnumber: int) -> int:
        lleft, rright = 0, len(numslist) - 1
        print("lleft", lleft)
        print("rright", rright)
        while lleft <= rright:
            mmiddle = (lleft + rright) // 2
            if numslist[mmiddle] > targetnumber:
                rright = mmiddle - 1
            elif numslist[mmiddle] < targetnumber:
                lleft = mmiddle + 1
            else:
                return mmiddle
        return -1


integerslist = [-1, 0, 3, 5, 9, 12]
target = 9
firstexample = Solution()
print(firstexample.search(integerslist, target))
'''
lleft 0
rright 5
4
'''
integerslist = [-1, 0, 3, 5, 9, 12]
target = 2
secondexample = Solution()
print(secondexample.search(integerslist, target)) #print -1
'''
lleft 0
rright 5
-1
'''

#Binary Search Algorithm Explained (Full Code Included) - Python Algorithms Series for Beginners [DnvWAd-RGhk]
def binarysearch(sequence, itemsearched):
    sequence.sort()
    beginningindex = 0
    endingindex = len(sequence) - 1
    while beginningindex <= endingindex:
        midpoint = beginningindex + ((endingindex - beginningindex) // 2)
        midpointvalue = sequence[midpoint]
        if midpointvalue == itemsearched:
            return midpoint
        elif itemsearched < midpointvalue:
            endingindex = midpoint - 1
        else:
            beginningindex = midpoint + 1
    return None


sequencea = [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
itemsearcheda = 12
print(binarysearch(sequencea, itemsearcheda)) #print 8
sequenceb = [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
itemsearchedb = 3
print(binarysearch(sequenceb, itemsearchedb)) #print None

#recursivebinarysearch is wrong
def recursivebinarysearch(sequencelist, searchfor):
    sequencelist.sort()
    beginningindex = 0
    endingindex = len(sequencelist) - 1
    midpoint = beginningindex + ((endingindex - beginningindex) // 2)
    print(sequencelist)
    print("inside recursive beginning index, ending index, midpoint", beginningindex, endingindex, midpoint)
    midpointnumbervalue = sequencelist[midpoint]
    print("inside recursive midpointvalue", midpointnumbervalue)
    if midpointnumbervalue == searchfor:
        return searchfor
    elif sequencelist[midpoint] == searchfor:
        return searchfor
    elif searchfor < midpointnumbervalue:
        condenselist = sequencelist[0:midpoint]
        print(condenselist)
        recursivebinarysearch(condenselist, searchfor)
    elif searchfor > midpointnumbervalue:
        condenselist = sequencelist[midpoint + 1:]
        print(condenselist)
        recursivebinarysearch(condenselist, searchfor)
    else:
        return "Error"
    return None


sequencelista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
searchfora = 5
print(recursivebinarysearch(sequencelista, searchfora))
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9]
inside recursive beginning index, ending index, midpoint 0 8 4
inside recursive midpointvalue 5
5
'''
print(recursivebinarysearch(sequencelista, 6))
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9]
inside recursive beginning index, ending index, midpoint 0 8 4
inside recursive midpointvalue 5
[6, 7, 8, 9]
[6, 7, 8, 9]
inside recursive beginning index, ending index, midpoint 0 3 1
inside recursive midpointvalue 7
[6]
[6]
inside recursive beginning index, ending index, midpoint 0 0 0
inside recursive midpointvalue 6
None
'''

singlenumbersequence = list(range(1, 10))
print(singlenumbersequence) #print [1, 2, 3, 4, 5, 6, 7, 8, 9]
searchfor = 7
beginningindex = 0
endingindex = len(singlenumbersequence) - 1
midpoint = beginningindex + ((endingindex - beginningindex) // 2)
print("beginning index, ending index, midpoint", beginningindex, endingindex, midpoint)
midpointnumbervalue = singlenumbersequence[midpoint]
print("midpointvalue", midpointnumbervalue)
if midpointnumbervalue == searchfor:
    print("found number", searchfor)
elif searchfor < midpointnumbervalue:
    condenselist = singlenumbersequence[0:midpoint]
elif searchfor > midpointnumbervalue:
    condenselist = singlenumbersequence[midpoint:]
print(condenselist)
endingindex = len(condenselist) - 1
midpoint = beginningindex + ((endingindex - beginningindex) // 2)
print("beginning index, ending index, midpoint", beginningindex, endingindex, midpoint)
midpointnumbervalue = condenselist[midpoint]
print("midpointvalue", midpointnumbervalue)
if midpointnumbervalue == searchfor:
    print("found number", searchfor)
elif searchfor < midpointnumbervalue:
    condenselist = singlenumbersequence[0:midpoint]
elif searchfor > midpointnumbervalue:
    condenselist = singlenumbersequence[midpoint:]
'''
[1, 2, 3, 4, 5, 6, 7, 8, 9]
beginning index, ending index, midpoint 0 8 4
midpointvalue 5
[5, 6, 7, 8, 9]
beginning index, ending index, midpoint 0 4 2
midpointvalue 7
found number 7
'''