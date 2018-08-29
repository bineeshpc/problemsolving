import sys
import argparse
import re
import six

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like grep tool')
    parser.add_argument('pattern',
                        type=str,
                        help='pattern to search for')
    parser.add_argument('filename', 
                        type=str,
                        help='filename to check search')
    args = parser.parse_args()
    return args

def match(pattern, filename):
    prog = re.compile(pattern)
    with open(filename) as f:
        for line in f:
            if prog.search(line):
                six.print_(line, end='')
    
if __name__ == '__main__':
    
    args = parse_cmdline()
    match(args.pattern, args.filename)

