import binarytree

class CommonRoot:
    def __init__(self, el1, el2):
        self.elements = sorted([el1, el2])
        self.found = [False for i in self.elements]
        self.commonroot = None

class Node(binarytree.Node):

    def insert(self, el):
        if el <= self.data:
            if self.left == None:
                self.left = Node(el)
            else:
                self.left.insert(el)
        if el > self.data:
            if self.right == None:
                self.right = Node(el)
            else:
                self.right.insert(el)

    def checkpresence(self, el):
        if self.data == el:
            return True
        else:
            if el < self.data:
                if self.left:
                    return self.left.checkpresence(el)
                else:
                    return False
            elif self.right:
                return self.right.checkpresence(el)
            else: return False

    def getcommonroot(self, cr):
        #dichotomy found
        if self.data > cr.elements[0] and\
           self.data < cr.elements[1]:
            if self.left.checkpresence(cr.elements[0]) and\
             self.right.checkpresence(cr.elements[1]):
                cr.commonroot = self.data
                return self.data
        #both are on left
        elif all([self.data > i for i in cr.elements]):
            return self.left.getcommonroot(cr)
        #both are on right
        elif all([self.data < i for i in cr.elements]):
            return self.right.getcommonroot(cr)
        #one of the nodes is the commonroot
        else:
            if cr.elements[0] == self.data:
                if self.checkpresence(cr.elements[1]):
                    return self.data
            elif cr.elements[1] == self.data:
                if self.checkpresence(cr.elements[0]):
                    return self.data
