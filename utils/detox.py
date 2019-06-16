
#! /usr/bin/env python

"""
The filenames of books downloaded are not usually unix friendlyself.
Convert those books to unix friendly names
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

pattern_to_remove = re.compile("""
[,']  #patterns to remove
""", re.VERBOSE)

pattern_to_hyphen = re.compile("""
[_\ ]  # space and underscore
""", re.VERBOSE)

def replace_all_dots_except_extension(str1):
    """
    Suppose the filename is
    a.b.c.d.txt
    Replace all dots except the last dot with hyphen
    this function returns
    a-b-c-d.txt
    """
    num_indices_to_replace = -1 # initialize to -1 because I dont want
    # to count the last dot
    for i in range(len(str1)):
        if str1[i] == '.':
            num_indices_to_replace += 1
    new_str_list = []
    
    count = 0
    i = 0
    while i < len(str1):
        if str1[i] == '.' and count < num_indices_to_replace:
            count += 1
            new_str_list.append('-')
        else:
            new_str_list.append(str1[i])
        i += 1
    return ''.join(new_str_list)

    

def visit_all_files(dirname):
    dirnames = os.listdir(dirname)
    for filename in dirnames:
        basename = os.path.basename(filename)
        fullname = os.path.join(
                            dirname, basename)

        if os.path.isdir(fullname):
            visit_all_files(fullname)
            # newname = pattern.sub('', fullname)
        
        newbasename = pattern_to_remove.sub('', basename)
        newbasename = pattern_to_hyphen.sub('-', newbasename)
        newbasename = replace_all_dots_except_extension(newbasename)

        # code to keep hyphen count to 1
        chars = []
        hyphen_count = 0
        for i in newbasename:
            if i == '-':
                hyphen_count += 1
            else:
                if hyphen_count > 0:
                    chars.append('-')
                    hyphen_count = 0
                chars.append(i)
        newbasename = ''.join(chars)
                
        newname = os.path.join(dirname, newbasename)
        if newname != fullname:
            six.print_("replacing ", fullname, "with", newname)
            shutil.move(fullname, newname)

def detox(location):
    dirname = location
    visit_all_files(dirname)

if __name__ == '__main__':
    args = parse_cmdline()
    detox(args.location)
