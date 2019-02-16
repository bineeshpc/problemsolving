#! /usr/bin/env python
import sys
import six
import argparse
sys.path.append('../datastructures/linked_list')
from linkedlist import List, Node

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like tail tool')
    parser.add_argument('--lines', 
                        type=int,
                        help='count')
    
    parser.add_argument('--filename',
                        type=str,
                        help='name of the file',
                        default=sys.stdin)
    args = parser.parse_args()
    return args


class Buffer(List):
    def __init__(self, size):
        List.__init__(self)
        self.size = size
        self.content_size = 0
        self.end_of_buffer = self.head
    
    def add(self, data):
        
        if self.content_size < self.size:
            node = Node(data)
            self.end_of_buffer.next = node
            self.end_of_buffer = self.end_of_buffer.next
            self.content_size += 1
        else:
            first_node = self.head.next
            # change the data of first node
            first_node.data = data
            # move the pointer of head by one
            self.head.next = first_node.next
            # and make the first node the last node
            self.end_of_buffer.next = first_node
            first_node.next = None
            # modify the end of buffer pointer to the first node
            self.end_of_buffer = first_node





def tail(filename, count):
    buffer = Buffer(count)
    f = filename if filename is sys.stdin else open(filename)
    for line in f:
        buffer.add(line.strip('\n'))
    if f is not sys.stdin:
        f.close()
    for line in buffer:
        six.print_(line)

def main():
    args = parse_cmdline()
    tail(args.filename, args.lines)


if __name__ == '__main__':
    main()

