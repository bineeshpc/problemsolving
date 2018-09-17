#!/usr/bin/env python
import sys
import six
sys.path.append('../stacks')
from stack_linked_list import Stack
import IterativeBuilder


class IterativePreorder:
    """
    root
    iterative inorder method
    """

    def __init__(self, root):
        self.iterative_preorder(root)

    def iterative_preorder(self, root):
        stack = Stack()
        node = root
        stack.push(node)
        while not stack.isempty():
            node = stack.pop()
            six.print_(node.data)
            # right node is pushed first because we want 
            # the left node to be popped out first
            if node.right is not None:
                stack.push(node.right)            
            if node.left is not None:
                stack.push(node.left)


def main():
    node = IterativeBuilder.build_tree(15)
    IterativePreorder(node)


if __name__ == "__main__":
    main()