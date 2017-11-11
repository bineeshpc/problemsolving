class BinaryTree:

    def __init__(self, rootnode):
        self.key = rootnode
        self.left = None
        self.right = None

    def getrootval(self):
        return self.key

    def setrootval(self, key):
        self.key = key

    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def insertleft(self, node):
        newnode = BinaryTree(node)
        if self.left is None:
            self.left = newnode
        else:
            tmp = self.left
            newnode.left = tmp
            self.left = newnode

    def insertright(self, node):
        newnode = BinaryTree(node)
        if self.right is None:
            self.right = newnode
        else:
            tmp = self.right
            newnode = BinaryTree(node)
            newnode.right = tmp
            self.right = newnode

    def find_max(self, max1=None):
        if self.key:
            if not max1:
                max1 = self.key
            max1 = max(self.key, max1)
            if self.left:
                leftmax = self.left.find_max(max1)
                max1 = max(leftmax, max1)
            if self.right:
                rightmax = self.right.find_max(max1)
                max1 = max(rightmax, max1)
            return max1


if __name__ == '__main__':
    bt = BinaryTree("/")
    bt.insertleft("sys")
    bt.insertright("tmp")
    print bt.getrootval(), bt.getleft().key
    print bt.getright().getrootval()

    bt1 = BinaryTree(1)
    bt1.insertleft(2)
    bt1.insertright(3)
    bt1.insertright(4)
    
    print bt1.find_max()
