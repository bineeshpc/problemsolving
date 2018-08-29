import sys
import six
import argparse

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like tail tool')
    parser.add_argument('--lines', 
                        type=int,
                        help='count')
    
    parser.add_argument('filename',
                        type=str,
                        help='name of the file')
    args = parser.parse_args()
    return args


def tail(filename, count):
    
    cnt = 0
    with open(filename) as f:
        for line in f:
            cnt += 1
            if cnt == count:
                f1 = open(filename)
            if cnt > count:
                line1 = f1.readline()
    
    for line1 in f1:
        six.print_(line1, end='')
    f1.close()

args = parse_cmdline()
tail(args.filename, args.lines)

