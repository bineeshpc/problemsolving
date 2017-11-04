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
        if self.left == None:
            self.left = newnode
        else:
            tmp = self.left
            newnode.left = tmp
            self.left = newnode

    def insertright(self, node):
        newnode = BinaryTree(node)
        if self.right == None:
            self.right = newnode
        else:
            tmp = self.right
            newnode = BinaryTree(node)
            newnode.right = tmp
            self.right = newnode

if __name__ == '__main__':
    bt = BinaryTree("/")
    bt.insertleft("sys")
    bt.insertright("tmp")
    print bt.getrootval(), bt.getleft().key
    print bt.getright().getrootval()
