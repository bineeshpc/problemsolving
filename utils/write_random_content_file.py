import argparse
import os
#import psutil
import sys
import random


def parse_cmdline():
    parser = argparse.ArgumentParser(description='Create files with random content to protect against personal data recovery')
    parser.add_argument('directoryname', type=str,
                        help='directoryname')
    parser.add_argument('num_megabytes', type=int,
                        help='number of megabytes to write as an integer')
    args = parser.parse_args()
    return args


class DirectoryShouldBeNew(Exception):
    pass


def create_data(args):
    directoryname = args.directoryname
    if os.path.exists(directoryname):
        raise DirectoryShouldBeNew
    else:
        os.mkdir(directoryname)
    os.chdir(directoryname)
    data = [chr(i) for i in range(256)]
    
    with open('filename', 'wb') as f:
        size = 0
        to_write = ''.join([random.choice(data) for i in range(1024 * 1024)])
        if sys.version_info.major == 3:
            to_write = to_write.encode()
        while size < args.num_megabytes:
            if random.random() < .01:
                to_write = ''.join([random.choice(data) for i in range(1024 * 1024)])
                if sys.version_info.major == 3:
                    to_write = to_write.encode()
            f.write(to_write)
            size += 1
    

if __name__ == '__main__':
    args = parse_cmdline()
    create_data(args)
    
