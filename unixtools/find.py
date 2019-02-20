#! /usr/bin/env python
import sys
import argparse
import re
import six
import os

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like grep tool')
    parser.add_argument('--pattern',
                        type=str,
                        default = '.*',
                        help='pattern to search for')
    parser.add_argument('location', 
                        type=str,
                        help='path to search for pattern in filename')
    args = parser.parse_args()
    return args

def find(pattern, location):
    pattern_re = re.compile(pattern)
    def find_helper(location):
        if pattern_re.search(location):
            six.print_(location)
        if os.path.isdir(location):
            files = os.listdir(location)
            for file in files:
                full_filename = os.path.join(location, file)
                find_helper(full_filename)

    return find_helper(location)

def main():
    args = parse_cmdline()
    find(args.pattern, args.location)

if __name__ == '__main__':  
    main()