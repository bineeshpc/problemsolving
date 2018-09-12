import sys
import six
import argparse

def parse_cmdline():
    parser = argparse.ArgumentParser(
        description='Unix like sort tool, does not use disk space')
    parser.add_argument('filename',
                        type=str,
                        help='name of the file')
    args = parser.parse_args()
    return args

def sort_(filename):
    with open(filename) as f:
        content = [line.strip() for line in f]
    content.sort()
    for line in content:
        six.print_(line)

if __name__ == '__main__':

    args = parse_cmdline()
    sort_(args.filename)