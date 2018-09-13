import sys
import six
import argparse

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like head tool')
    parser.add_argument('--lines', 
                        type=int,
                        help='count')
    
    parser.add_argument('--filename',
                        type=str,
                        help='name of the file',
                        default=sys.stdin)
    args = parser.parse_args()
    return args

def head(filename, count):
    cnt = 0
    if filename is sys.stdin:
        f = filename
    else:
        f = open(filename)
    for line in f:
        cnt += 1
        six.print_(line, end='')
        if cnt == count:
            break
    if f is not sys.stdin:
        f.close()

if __name__ == '__main__':

    args = parse_cmdline()
    head(args.filename, args.lines)