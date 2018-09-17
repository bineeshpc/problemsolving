#!/usr/bin/env python
import sys
import six
sys.path.append('../stacks')
from stack_linked_list import Stack
import IterativeBuilder


class IterativePostorder:
    """
    root
    iterative inorder method
    """

    def __init__(self, root):
        self.iterative_postorder(root)

    def iterative_postorder(self, root):
        # stack1 is for simulating
        # post order of a tree is the 
        # reverse pre order traversal of 
        # the mirror image of the tree
        # stack_2 is for getting the reverse 
        # pre order of the mirror image of tree
        stack_1 = Stack()
        stack_2 = Stack()
        node = root
        stack_1.push(node)

        while not stack_1.isempty():
            node = stack_1.pop()
            stack_2.push(node.data)
            if node.left:
                stack_1.push(node.left)
            if node.right:
                stack_1.push(node.right)
        
        while not stack_2.isempty():
           data = stack_2.pop()
           six.print_(data)


def main():
    node = IterativeBuilder.build_tree(15)
    IterativePostorder(node)


if __name__ == "__main__":
    main()