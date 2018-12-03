#! /usr/bin/env python

"""
The filenames of movies downloaded from internet are filled
with advertisements of the people who uploaded it.
Cleanup the filenames and keep only relevant information
"""

import os
import re
import shutil
import six
import argparse

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like grep tool')
    parser.add_argument('location', 
                        type=str,
                        help='path to search for pattern in filename')
    args = parser.parse_args()
    return args


pattern = re.compile("""
[wW]{3}\.[a-zA-Z0-9]*\.[a-zA-Z0-9]*-# website names
|MovCr.com\- # movcr
|ZippyMovieZ\.(Date|DE|CH)\- # zippymovies
|[a-zA-Z]*\.(in|com|cc|org|net|site)\- # generic for .com .in .cc etc
""", re.VERBOSE)

def visit_all_files(dirname):
    dirnames = os.listdir(dirname)
    for filename in dirnames:
        basename = os.path.basename(filename)
        fullname = os.path.join(
                            dirname, basename)

        if os.path.isdir(fullname):
            visit_all_files(fullname)
            # newname = pattern.sub('', fullname)
        
        newbasename = pattern.sub('', basename)
        newname = os.path.join(dirname, newbasename)
        if newname != fullname:
            six.print_("replacing ", fullname, "with", newname)
            shutil.move(fullname, newname)


def detox(location):
    dirname = location
    os.system('detox -r {}'.format(dirname))
    visit_all_files(dirname)

if __name__ == '__main__':
    args = parse_cmdline()
    detox(args.location)
