#! /usr/bin/env python
import sys
import six
import argparse


def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like cat tool')
    parser.add_argument('--filename',
                        help='name of the file',
                        action='append',
            default=None)
    args = parser.parse_args()
    return args

def cat(filenames):
    if filenames is None:
        filenames = [sys.stdin]
    for file_ in filenames:
        if file_ is not sys.stdin:
            f = open(file_)
        else:
            f = file_
        for line in f:
            line = line.rstrip()
            six.print_(line)
        if f is not sys.stdin:
            f.close()

if __name__ == '__main__':

    args = parse_cmdline()
    cat(args.filename)
    