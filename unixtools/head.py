#! /usr/bin/env python

import sys
import six
import argparse


def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like xargs tool')
    parser.add_argument('--lines', 
                        type=int,
                        help='count')
    
    parser.add_argument('--start', 
                        type=int,
                        help='start from this line instead of line 1',
                        default=0)
    
    parser.add_argument('--filename',
                        type=str,
                        help='name of the file',
                        default=sys.stdin)
    args = parser.parse_args()
    return args


def head(args):
    start = args.start
    count = args.lines
    filename = args.filename
    cnt = 0
    if filename is sys.stdin:
        f = filename
    else:
        f = open(filename)
    for line in f:
        cnt += 1
        if start != 0:
            if cnt < start:
                continue
            else:
                cnt = 1
                start = 0
        six.print_(line, end='')
        if cnt == count:
            break
    if f is not sys.stdin:
        f.close()


if __name__ == '__main__':

    args = parse_cmdline()
    head(args)
