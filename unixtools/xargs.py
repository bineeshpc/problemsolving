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

def xargs(filename):
    f = filename if filename == sys.stdin else open(filename)
    data = []
    for line in f:
        data.append(line.strip('\n'))
    if f is not sys.stdin:
        f.close()
    six.print_('\t'.join(data))


if __name__ == '__main__':

    args = parse_cmdline()
    xargs(args.filename)