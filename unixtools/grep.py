#! /usr/bin/env python
import sys
import argparse
import re
import six


def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like grep tool')
    parser.add_argument('pattern',
                        type=str,
                        help='pattern to search for')
    parser.add_argument('--filename', 
                        type=str,
                        help='filename to check search',
                        default=sys.stdin)
    args = parser.parse_args()
    return args

def match(pattern, filename):
    prog = re.compile(pattern)
    if filename is sys.stdin:
        f = filename
    else:
        f = open(filename, encoding='utf-8')

    for line in f:
        if prog.search(line):
            six.print_(line, end='')

    if filename is not sys.stdin:
        f.close()

if __name__ == '__main__':
    
    args = parse_cmdline()
    match(args.pattern, args.filename)

