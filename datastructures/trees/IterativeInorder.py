#!/usr/bin/env python
import sys
import six
sys.path.append('../stacks')
from stack_linked_list import Stack
import IterativeBuilder

class IterativeInorder:
    def __init__(self, root):
        self.iterative_inorder(root)

    def iterative_inorder(self, root):
        node = root
        stack = Stack()
        while True:
            if node is not None:
                stack.push(node)
                node = node.left
            else:
                # node is none
                if stack.isempty():
                    break
                node = stack.pop()
                six.print_(node.data)
                node = node.right



def main():
    root = IterativeBuilder.build_tree(15)
    IterativeInorder(root)

if __name__ == '__main__':
    main()