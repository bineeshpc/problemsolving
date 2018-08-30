import sys
import six
sys.path.insert(0, '../queues')
import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorder(self):
        six.print_(self.data, end='')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        six.print_(self.data, end='')
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        six.print_(self.data, end='')
        
    def findmax(self):
        left = self.left.findmax() if self.left else None
        right = self.right.findmax() if self.right else None
        
        return max(self.data, left, right)
    
    def findmaxlevelorder(self):
        q = queue.Queue()
        q.enqueue(self)
        max1 = self.data
        while not q.isempty():
            node = q.dequeue()
            
            if node.data > max1:
                max1 = node.data
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            
        return max1
    
    def size(self):
        left = self.left.size() if self.left else 0
        right = self.right.size() if self.right else 0
        return left + 1 + right
    
    def height(self):
        left = self.left.height() if self.left else 0
        right = self.right.height() if self.right else 0
        return max(left, right) + 1
    
    def tomirror(self):
        if self.left:
            self.left.tomirror()
        if self.right:
            self.right.tomirror()
        temp = self.left
        self.left = self.right
        self.right = temp
        
    def leastcommonancestor(self, a, b):
        if self.data == a or self.data == b:
            return self.data
        left = self.left.leastcommonancestor(a, b) if self.left else None
        right = self.right.leastcommonancestor(a, b) if self.right else None
        if left and right:
            return self.data
        elif left:
            return left
        else:
            return right
        
    def verticalsum(self, column, hashtable):
        """
           1
         /   \
         2   3
          \
           4
        Vertical nodes are the nodes that come in the same vertical column
        
        assuming that root node is at column 0
        root's left will be on -1 and root's right will be on 1
        This can be called with a column number of 0 for root and 
        and empty hashtable or dictionary
        """
        if hashtable.get(column):
            hashtable[column] += self.data
        else:
            hashtable[column] = self.data
        six.print_(column)
        if self.left:
            self.left.verticalsum(column - 1, hashtable)
        if self.right:
            self.right.verticalsum(column + 1, hashtable)
