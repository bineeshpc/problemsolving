#! /usr/bin/env python
import os
import argparse

def delete_empty_directories(directory):
    """
    Recursively removes empty directories
    """
    subdirectories = []
    for dir1 in os.listdir(directory):
        dir1 = os.path.join(directory, dir1)
        if os.path.isdir(dir1):
            subdirectories.append(dir1)
            
    for dir2 in subdirectories:
        delete_empty_directories(dir2)
        
    if os.listdir(directory) == []:
        os.rmdir(directory)
        
parser = argparse.ArgumentParser()
parser.add_argument('directory',
                    help='directory to remove all the empty subdirectories will be removed first')
args = parser.parse_args()
delete_empty_directories(args.directory)
