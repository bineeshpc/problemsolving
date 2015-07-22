import argparse
import unittest
from sel import *

parser = argparse.ArgumentParser(description='download profiles in /tmp directory.')
parser.add_argument('filename', default='profiles.org',
                    help='add filename to read from')
args = parser.parse_args()
print(args.filename)

unittest.main()
