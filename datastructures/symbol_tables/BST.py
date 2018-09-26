import testlib
import sys
sys.path.insert(0, '../queues')
from queue import QueueList


def compare_to(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

class Node:
    def __init__(self, key, value, size):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.size = size

class BST:
    def __init__(self):
        self.root = None

    def isempty(self):
        if self.root == None:
            return True
        return False

    def get(self, key):
        return self.get_helper(self.root, key)

    def get_helper(self, node, key):
        if node is None:
            return None
        cmp = compare_to(key, node.key)
        if cmp < 0:
            return self.get_helper(node.left, key)
        elif cmp > 0:
            return self.get_helper(node.right, key)
        else:
            return node.value

    def put(self, key, value):
        self.root = self.put_helper(self.root, key, value)

    def put_helper(self, node, key, value):
        if node == None:
            return Node(key, value, 1)
        cmp = compare_to(key, node.key)
        if cmp < 0:
            node.left = self.put_helper(node.left, key, value)
        elif cmp > 0:
            node.right = self.put_helper(node.right, key, value)
        else:
            node.value = value
        left_size = node.left.size if node.left else 0
        right_size = node.right.size if node.right else 0
        node.size = left_size + right_size + 1
        return node

    def delete(self, key):
        self.root = self.delete_helper(self.root, key)

    def delete_helper(self, node, key):
        if node == None:
            return None
        cmp = compare_to(key, node.key)
        if cmp < 0:
            node.left = self.delete_helper(node.left, key)
        elif cmp > 0:
            node.right = self.delete_helper(node.right, key)
        else:
            if node.left and node.right:
                # delete the minimum from right subtree
                # replace the present nodes key and value
                # with the minimum from right subtree
                deleted_node = self.delete_min(node.right)
                node.key = deleted_node.key
                node.value = deleted_node.value
                node.size = node.left.size + node.right.size + 1
                return node
            elif node.left:
                return node.left
            elif node.right:
                return node.right


    def delete_min(self, node):
        if node.left == None:
            return None
        node.left = self.delete_min(node.left)
        return node

    def contains(self, key):
        return self.contains_helper(self.root, key)

    def contains_helper(self, node, key):
        if node == None:
            return False
        cmp = compare_to(key, node.key)
        if cmp < 0:
            return self.contains_helper(node.left, key)
        elif cmp > 0:
            return self.contains_helper(node.right, key)
        else:
            return True


    def size(self):
        return self.size_helper(self.root)

    def size_helper(self, node):
        if node == None:
            return 0
        total_size = 1
        if node.left:
            total_size += node.left.size
        if node.right:
            total_size += node.right.size
        return total_size

    def check(self):
        # fix me
        return True

    def in_order(self):
        q = QueueList()
        self.in_order_helper(self.root, q)
        return q

    def in_order_helper(self, node, q):
        if node is not None:
            if node.left:
                self.in_order_helper(node.left, q)
            q.put(node)
            if node.right:
                self.in_order_helper(node.right, q)
            
        


def main():
    st = BST()
    testlib.test_BST(st)

if __name__ == '__main__':
    main()