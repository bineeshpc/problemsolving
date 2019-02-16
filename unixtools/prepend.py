#! /usr/bin/env python

import argparse
import os
import random

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Prepend a text to a file')
    
    parser.add_argument('--text', 
                        type=str,
                        help='Prepend this text to file',
                        )
    
    parser.add_argument('--filename',
                        type=str,
                        help='name of the file',
                        )
    args = parser.parse_args()
    return args

def prepend(args):
    temp_file_name = ''.join([str(random.randint(1, 25)) for i in range(10)])
    with open(args.filename) as source_f, open(temp_file_name, 'w') as target_f:
        target_f.write('{}\n'.format(args.text))
        for line in source_f:
            target_f.write(line)
    os.rename(temp_file_name, args.filename)

if __name__ == "__main__":
    args = parse_cmdline()
    prepend(args)
