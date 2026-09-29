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

#Algorithms in Python： Binary Search [zeULw-a7Mw8]
datalist = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
targetnumber = 28
#Linear search or brute force
def linearsearch(datalist, targetnumber):
    datalist.sort()
    for eachdatalist in range(len(datalist)):
        if datalist[eachdatalist] == targetnumber:
            return True
    return False


print(linearsearch(datalist, targetnumber)) #print True
print(linearsearch(datalist, 50)) #print False
#Iterative binary search
def binarysearchiterative(datalist, targetnumber):
    datalist.sort()
    low = 0 #initial low first element index number
    high = len(datalist) - 1 #initial high last element index number
    while low <= high: #main binary search
        mid = low + ((high - low) // 2) #acquire the middle element index number
        midelementvalue = datalist[mid] #the middle element number or value.  midelementvalue is short for middleelement.
        if targetnumber == midelementvalue:
            return True
        elif targetnumber < midelementvalue: #move the search area to the left of the list.  Eliminate all index numbers on the right side of the mid variable.  No need to search the right side of the mid variable.  The high variable is the mid variable minus 1.
            high = mid - 1
        elif targetnumber > midelementvalue: #move the search area to the right of the list.  Eliminate all index numbers on the left side of the mid variable.  No need to search the left side of the mid variable.  The low variable is the mid variable minus 1.
            low = mid + 1
        else:
            print("Error")
            return False
    return False


print(binarysearchiterative(datalist, targetnumber)) #print True
print(binarysearchiterative(datalist, 50)) #print False
#Recursive binary search
def binarysearchrecursive(datalist, targetnumber, low, high):
    if low > high: #Base case
        return False
    else:
        mid = low + ((high - low) // 2) #acquire the middle element index number
        midelementvalue = datalist[mid] #the middle element number or value.  midelementvalue is short for middleelement.
        if targetnumber == midelementvalue:
            return True
        elif targetnumber < midelementvalue:
            return binarysearchrecursive(datalist, targetnumber, low, mid - 1) #change high variable calculating new high variable high = mid - 1
        elif targetnumber > midelementvalue: ##change low variable calculating new low variable low = mid + 1
            return binarysearchrecursive(datalist, targetnumber, mid + 1, high)
        else:
            print("Error")
            return False
    return False


print(binarysearchrecursive(datalist, targetnumber, 0, len(datalist) - 1)) #print True
print(binarysearchrecursive(datalist, 50, 0, len(datalist) - 1)) #print False

#Binary Search in Python [4Q36e9EOxLU]
'''
import random
numberslist = []
for x in range(100):
    numberslist.append(random.randint(0, 500))
print(numberslist) #print [487, 353, 211, 75, 207, 353, 253, 315, 295, 131, 447, 269, 149, 273, 249, 416, 164, 333, 441, 351, 48, 314, 485, 327, 158, 395, 21, 455, 418, 471, 123, 438, 70, 101, 139, 247, 256, 363, 52, 150, 432, 338, 185, 216, 185, 166, 331, 12, 208, 378, 306, 304, 446, 240, 333, 443, 245, 486, 494, 80, 127, 1, 360, 370, 222, 193, 220, 217, 172, 349, 408, 440, 377, 220, 66, 129, 475, 85, 431, 421, 368, 360, 352, 262, 285, 486, 179, 12, 197, 209, 93, 311, 52, 430, 379, 127, 341, 407, 185, 336]
'''
numberslist = [487, 353, 211, 75, 207, 353, 253, 315, 295, 131, 447, 269, 149, 273, 249, 416, 164, 333, 441, 351, 48, 314, 485, 327, 158, 395, 21, 455, 418, 471, 123, 438, 70, 101, 139, 247, 256, 363, 52, 150, 432, 338, 185, 216, 185, 166, 331, 12, 208, 378, 306, 304, 446, 240, 333, 443, 245, 486, 494, 80, 127, 1, 360, 370, 222, 193, 220, 217, 172, 349, 408, 440, 377, 220, 66, 129, 475, 85, 431, 421, 368, 360, 352, 262, 285, 486, 179, 12, 197, 209, 93, 311, 52, 430, 379, 127, 341, 407, 185, 336]
def binarysearchrecursive(numberslist, numbersearch, leftboundary, rightboundary):
    numberslist.sort()
    if leftboundary > rightboundary: #Bad numberslist or numbersearch not in numberslist
        return -1
    middleboundary = (leftboundary + rightboundary) // 2
    if numbersearch == numberslist[middleboundary]:
        return "The number", numbersearch, "is found at sorted numberslist index number", middleboundary
    elif numbersearch < numberslist[middleboundary]:
        return binarysearchrecursive(numberslist, numbersearch, leftboundary, middleboundary - 1) #change rightboundary to the middleboundary-1.  Move search area to the left of the middleboundary.
    else:
        return binarysearchrecursive(numberslist, numbersearch, middleboundary + 1, rightboundary) #change leftboundary to the middleboundary+1.  Move search area to the right of the middleboundary.


numberslist.sort()
print(numberslist) #print [1, 12, 12, 21, 48, 52, 52, 66, 70, 75, 80, 85, 93, 101, 123, 127, 127, 129, 131, 139, 149, 150, 158, 164, 166, 172, 179, 185, 185, 185, 193, 197, 207, 208, 209, 211, 216, 217, 220, 220, 222, 240, 245, 247, 249, 253, 256, 262, 269, 273, 285, 295, 304, 306, 311, 314, 315, 327, 331, 333, 333, 336, 338, 341, 349, 351, 352, 353, 353, 360, 360, 363, 368, 370, 377, 378, 379, 395, 407, 408, 416, 418, 421, 430, 431, 432, 438, 440, 441, 443, 446, 447, 455, 471, 475, 485, 486, 486, 487, 494]
print(binarysearchrecursive(numberslist, 93, 0, len(numberslist) - 1)) #print ('The number', 93, 'is found at sorted numberslist index number', 12)

#Binary Search Tree in Python [DlWxqU3LLpY]
class TreeNode:
    def __init__(self, value):
        self.leftnode = None
        self.rightnode = None
        self.value = value
    def insertnewnode(self, value):
        if value < self.value:
            if self.leftnode is None: #there is no value on the left node
                self.leftnode = TreeNode(value)
            else:
                self.leftnode.insertnewnode(value)
        else:
            if self.rightnode is None: #there is no value on the right node
                self.rightnode = TreeNode(value)
            else:
                self.rightnode.insertnewnode(value)
    def inordertraversal(self):
        if self.leftnode:
            self.leftnode.inordertraversal()
        print(self.value)
        if self.rightnode:
            self.rightnode.inordertraversal()
    def preordertraversal(self):
        print(self.value)
        if self.leftnode:
            self.leftnode.preordertraversal()
        if self.rightnode:
            self.rightnode.preordertraversal()
    def postordertraversal(self):
        if self.leftnode:
            self.leftnode.postordertraversal()
        if self.rightnode:
            self.rightnode.postordertraversal()
        print(self.value)
    def findnode(self, value):
        if value < self.value:
            if self.leftnode is None:
                return False
            else:
                return self.leftnode.findnode(value)
        elif value > self.value:
            if self.rightnode is None:
                return False
            else:
                return self.rightnode.findnode(value)
        else:
            return True


tree1 = TreeNode(10)
tree1.insertnewnode(5)
tree1.insertnewnode(4)
tree1.insertnewnode(2)
tree1.insertnewnode(1)
tree1.insertnewnode(3)
tree1.insertnewnode(22)
tree1.insertnewnode(11)
tree1.insertnewnode(12)
print(tree1.leftnode.leftnode.leftnode.rightnode.value) #print 3
tree2 = TreeNode(6)
tree2.insertnewnode(5)
tree2.insertnewnode(2)
tree2.insertnewnode(4)
tree2.insertnewnode(1)
tree2.insertnewnode(2)
tree2.insertnewnode(4)
tree2.insertnewnode(19)
tree2.insertnewnode(29)
tree2.insertnewnode(11)
tree2.insertnewnode(4)
tree2.insertnewnode(2)
tree2.inordertraversal()
'''
1
2
2
2
4
4
4
5
6
11
19
29
'''
print("\n")
tree3 = TreeNode(6)
tree3.insertnewnode(5)
tree3.insertnewnode(2)
tree3.insertnewnode(4)
tree3.insertnewnode(1)
tree3.insertnewnode(2)
tree3.insertnewnode(4)
tree3.insertnewnode(19)
tree3.insertnewnode(29)
tree3.insertnewnode(11)
tree3.insertnewnode(4)
tree3.insertnewnode(2)
tree3.preordertraversal()
'''
6
5
2
1
4
2
2
4
4
19
11
29
'''
print("\n")
tree4 = TreeNode(6)
tree4.insertnewnode(5)
tree4.insertnewnode(2)
tree4.insertnewnode(4)
tree4.insertnewnode(1)
tree4.insertnewnode(2)
tree4.insertnewnode(4)
tree4.insertnewnode(19)
tree4.insertnewnode(29)
tree4.insertnewnode(11)
tree4.insertnewnode(4)
tree4.insertnewnode(2)
tree4.postordertraversal()
'''
1
2
2
4
4
4
2
5
11
29
19
6
'''
print(tree4.findnode(7)) #print False
print(tree4.findnode(29)) #print True

'''
#Binary Search Tree Simulation
#Pseudocode from https://see-algorithms.com/data-structures/BST
function insert(node, key):
    if key < node.value
        if node.left is null:
            node.left = new Node(key)
        else:
            insert(node.left, key)
    else if key > node.value:
        if node.right is null:
            node.right = new Node(key)
        else:
            insert(node.right, key)
'''

#Binary Search Trees in Python： Introduction - Insertion and Search [yC83Kp2xig8]

#Node class for the binary search tree.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.leftchildsouthwest = None
        self.rightchildsoutheast = None

class BinarySearchTree:
    def __init__(self):
        self.root = None #root node is empty when start creating binary search tree.
    def insert(self, data): #insert method.  Provide the data which contains the nodes to be inserted to the binary search tree.
        if self.root is None: #If nothing in the tree, then root is set to None.  Set the root equal to the node constructed.
            self.root = Node(data) #Construct the node from the data provided.  Is this the parent or root node or initial insert node?
        else:
            self._insertallothernodes(data, self.root) #One or more nodes.  Helper method with the underscore in a recursive manner.  Insert the new node for which there is a parent.
    def _insertallothernodes(self, data, currentnode):
        if data < currentnode.data:
            if currentnode.leftchildsouthwest is None: #If there is no left child, then insert the node as the left child
                currentnode.leftchildsouthwest = Node(data)
            else: #There is a left child.  Move to the left or move southwest(?).  Recursively call the _insertallothernodes() function.
                self._insertallothernodes(data, currentnode.leftchildsouthwest)
        elif data > currentnode.data:
            if currentnode.rightchildsoutheast is None: #If there is no right child, then insert the node as the right child
                currentnode.rightchildsoutheast = Node(data)
            else: #There is a right child.  Move to the right or move southeast(?).  Recursively call the _insertallothernodes() function.
                self._insertallothernodes(data, currentnode.rightchildsoutheast)
        else: #data is equal to an element or node already in the tree.  No duplicates.
            print("Value is already present in tree.")
    def findandsearch(self, data):
        if self.root:
            isfound = self._find(data, self.root) #Find the node in the binary tree
            if isfound:
                return True
            return False
        else:
            return None
    def _find(self, data, currentnode):
        if data > currentnode.data and currentnode.rightchildsoutheast: #Finding the node is on the right side
            return self._find(data, currentnode.rightchildsoutheast)
        elif data < currentnode.data and currentnode.leftchildsouthwest: #Finding the node is on the left side
            return self._find(data, currentnode.leftchildsouthwest)
        if data == currentnode.data: #Found the node after self._find recursively
            return True


bst1 = BinarySearchTree()
bst1.insert(4)
bst1.insert(2)
bst1.insert(8)
bst1.insert(5)
bst1.insert(10)
print(bst1.findandsearch(4)) #print True
print(bst1.findandsearch(5)) #print True
print(bst1.findandsearch(10)) #print True
print(bst1.findandsearch(11)) #print False