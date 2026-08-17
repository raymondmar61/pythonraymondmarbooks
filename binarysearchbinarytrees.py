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
