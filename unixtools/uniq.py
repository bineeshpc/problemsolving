#! /usr/bin/env python
import sys
import six
import argparse

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like head tool')
    parser.add_argument('--filename',
                        type=str,
                        help='name of the file',
                        default=sys.stdin)
    args = parser.parse_args()
    return args

def uniq(filename):
    f = filename if  filename is sys.stdin else open(filename)
    oldline = f.readline().strip('\n')
    six.print_(oldline)
    for line in f:
        line = line.strip('\n')
        if line != oldline:
            six.print_(line)
            oldline = line

    if f is not sys.stdin:
        f.close()

if __name__ == '__main__':

    args = parse_cmdline()
    uniq(args.filename)