#! /usr/bin/env python
import argparse
import six
import getpass
import os

def parse_cmd_line():
    parser = argparse.ArgumentParser(description='Helper for zulucrypt cli')
    parser.add_argument('--filename',
                        help='path to a zulucrypt file or partition')
    parser.add_argument('--action', choices=['open', 'close'],
                        help='What action to perform open or close')
    args = parser.parse_args()
    return args

def execute(args):
    """ Creates a directory in home directory and give a link to the 
    directory where the directory is actually mounted
    After we unmount we actually delete the directory
    """
    cmds = {"open" : "sudo zuluCrypt-cli -o -d {path} -t vera -m {dirname} -M -p {password}",
            "close": "sudo zuluCrypt-cli -q -d {path}"
            }
    dirname = "zulu"
    cmd = cmds[args.action]
    if args.action == 'open':
        password = getpass.getpass(prompt='Enter the password :')
        cmd = cmd.format(path=args.filename, dirname=dirname, password=password)
        os.system('cd; mkdir -p {dirname}'.format(dirname=dirname))
        os.system(cmd)
        os.system('cd; cd {dirname}; ln -s /run/media/public/{dirname} {dirname}'.format(dirname=dirname))
    
    elif args.action == 'close':
        cmd = cmd.format(path=args.filename)
        os.system(cmd)
        os.system('cd ; unlink {dirname}/{dirname} ; rmdir {dirname}'.format(dirname=dirname))

def main():
    args = parse_cmd_line()
    execute(args)


if __name__ == '__main__':
    main()

