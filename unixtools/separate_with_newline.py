#! /usr/bin/env python

import argparse

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Given space separated string sepaarte it with new lines')
    
    parser.add_argument('--text',
                        type=str,
                        help='text which are separated by space',
                        )
    args = parser.parse_args()
    return args

def separate_with_newline(args):
    for i in args.text.split():
        print(i)

if __name__ == "__main__":
    args = parse_cmdline()
    separate_with_newline(args)
