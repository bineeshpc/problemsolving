import testlib
import sys
sys.path.insert(0, '../queues')
from queue import QueueList
from typing import Any

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
            return Node(key, value, 1) # 1 is size
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
                minimum_node = self.min(node.right)
                right_link = self.delete_min(node.right)
                node.right = right_link
                node.key = minimum_node.key
                node.value = minimum_node.value
                node.size = node.left.size + node.right.size + 1
                return node
            elif node.left:
                return node.left
            elif node.right:
                return node.right


    def delete_min(self, node):
        if node.left == None:
            return node.right
        node.left = self.delete_min(node.left)
        return node

    def min(self, node):
        if node.left == None:
            return node
        else:
            return min(node.left)

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
        return node.size

    def check(self):
        # fix me
        if self.is_BST() == False:
            print("not a bst")
            return False
        if self.is_size_consistent() == False:
            print("size is inconsistent")
            return False
        if self.is_rank_consistent() == False:
            print("rank is insconsistent")
            return False
        return True

    def rank(self, key: Any) -> int:
        """
        Returns the rank of the key in the tree
        rank is number of elements less than key
        """
        return self.rank_helper(self.root, key)

    def rank_helper(self, node: Node, key: Any) -> int:
        if node == None:
            return 0
        cmp = compare_to(key, node.key)
        if cmp < 0:
            return self.rank_helper(node.left, key)
        elif cmp > 0:
            return self.size_helper(node.left) + 1 + self.rank_helper(node.right, key)
        else:
            return self.size_helper(node.left)

    def is_rank_consistent(self) -> bool:
        for rank, node in enumerate(self.in_order()):
            if node.key != self.select(self.rank(node.key)):
                return False
            if rank != self.rank(self.select(rank)):
                return False
        return True

    def select(self, k: int) -> Any:
        """
        Select the k th smallest element
        kth order statistic
        """
        return self.select_helper(self.root, k)

    def select_helper(self, node: Node, k: int) -> Any:
        if node == None:
            return None
        left_size = self.size_helper(node.left)
        cmp = compare_to(k, left_size)
        if cmp < 0:
            # check in left side
            return self.select_helper(node.left, k - 1)
        elif cmp > 0:
            # check in right side
            return self.select_helper(node.right, k - left_size - 1)
        else:
            # select the present element
            return node.key

    def is_BST(self) -> bool:
        return self.is_BST_helper(self.root, None, None)

    def is_BST_helper(self, node: Node, minimum: int, maximum: int) -> bool:
        """
        For each node, its key is the minimum when we consider the right subtree
        For each node, its key is the maximum when we consider the left subtree
        """
        if node == None:
            return True
        if maximum and not self.is_BST_helper(node.left, None, node.key):
            return False
        if minimum and not self.is_BST_helper(node.right, node.key, None):
            return False
        return True


    def is_size_consistent(self) -> bool:
        return self.is_size_consistent_helper(self.root)

    def is_size_consistent_helper(self, node: Node) -> bool:
        if node == None:
            return True
        if (node.size != (self.size_helper(node.left) + self.size_helper(node.right) + 1)):
            return False
        return self.is_size_consistent_helper(node.left) and self.is_size_consistent_helper(node.right)


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


    def height(self) -> int:
        return self.height_helper(self.root)

    def height_helper(self, node: Node) -> int:
        if node == None:
            return 0
        return 1 + max(self.height_helper(node.left), self.height_helper(node.right))

    def floor(self, key: Any) -> Any:
        """
        Floor is the largest key less than or equal to given key
        """
        return self.floor_helper(self.root, key)

    def floor_helper(self, node: Node, key: Any) -> Any:
        if node == None:
            return None

        cmp = compare_to(key, node.key)
        if cmp < 0:
            return self.floor_helper(node.left, key)
        elif cmp > 0:
            return max(node.key, self.floor_helper(node.right, key))
        else:
            return node.key

    def ceiling(self):
        raise NotImplementedError
      
        


def main():
    st = BST()
    testlib.test_BST(st)
    st1 = BST()
    testlib.test_BST_delete(st1)

if __name__ == '__main__':
    main()