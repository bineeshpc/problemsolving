#! /usr/bin/env python
import os
import argparse
import re
import shutil
import logging
import sys

logger = logging.getLogger('root')

def copy_directory_matching_pattern(directory, destination, pattern):
    logger.debug('creating directory {}'.format(destination))
    os.mkdir(destination)
    files_or_directories = os.listdir(directory)
    logger.debug('all files and directories %s', files_or_directories)
    for file_or_directory in files_or_directories:
        full_name = os.path.join(directory, file_or_directory)
        if os.path.isdir(full_name):
            new_destination = os.path.join(destination, file_or_directory)
            logger.debug('new destination directory %s', new_destination)
            copy_directory_matching_pattern(full_name, new_destination, pattern)
        elif os.path.isfile(full_name):
            new_filename = os.path.join(directory, full_name)
            if re.match(pattern, file_or_directory):
                new_destination_filename = os.path.join(destination, file_or_directory)
                logger.debug('copying {} {}'.format(new_filename, new_destination_filename))
                shutil.copyfile(new_filename, new_destination_filename)
            else:
                logger.debug('ignoring {}'.format(new_filename))

if __name__ == '__main__':                                        
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory',
                        help='directory to copy')
    parser.add_argument('--pattern', help='pattern to match')
    parser.add_argument('--destination', help = 'destination directory')
    parser.add_argument('--debug', action='store_true', help = 'debug flag')
    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.StreamHandler(sys.stdout))
    copy_directory_matching_pattern(args.directory, args.destination, args.pattern)
