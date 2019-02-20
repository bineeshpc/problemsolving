#! /usr/bin/env python
import argparse
import six

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like seq tool')
    parser.add_argument('begin', 
                        type=int,
                        help='Print a sequence from the value of begin')
    parser.add_argument('end', 
                        type=int,
                        help='Print a sequence till the value of end')
    args = parser.parse_args()
    return args

def seq(begin, end):
    for i in range(begin, end+1):
        six.print_('{}'.format(i))

def main():
    args = parse_cmdline()
    seq(args.begin, args.end)

if __name__ == '__main__':  
    main()