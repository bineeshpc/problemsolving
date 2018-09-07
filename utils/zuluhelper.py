#! /usr/bin/env python
import argparse
import six
import getpass
import os

def parse_cmd_line():
    parser = argparse.ArgumentParser(description='Helper for zulucrypt cli')
    parser.add_argument('--filename',
                        help='path to a zulucrypt file or partition',
                        action='append')
    parser.add_argument('--action', choices=['open', 'close'],
                        help='What action to perform open or close')
    args = parser.parse_args()
    return args

def execute(args):
    """ Creates a directory in home directory and give a link to the 
    directory where the directory is actually mounted
    After we unmount we actually delete the directory
    """
    cmds = {"open" : "sudo zuluCrypt-cli -o -d {path} -t vera -m {basename} -M -p {password}",
            "close": "sudo zuluCrypt-cli -q -d {path}"
            }
    dirname = "zulu"
    password = None
    for filename in args.filename:
        cmd = cmds[args.action]
        basename = os.path.basename(filename)
        if args.action == 'open':
            if not password:
                password = getpass.getpass(prompt='Enter the password :')
            cmd = cmd.format(path=filename, basename=basename, password=password)
            os.system('cd; mkdir -p {dirname}'.format(dirname=dirname))
            os.system(cmd)
            os.system('cd; cd {dirname}; ln -s /run/media/public/{basename} {basename}'.format(basename=basename, dirname=dirname))

        elif args.action == 'close':
            cmd = cmd.format(path=filename)
            os.system(cmd)
            os.system('cd ; unlink {dirname}/{basename} ; sleep 1; rmdir {dirname}'.format(dirname=dirname, basename=basename))

def main():
    args = parse_cmd_line()
    execute(args)


if __name__ == '__main__':
    main()

