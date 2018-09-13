import sys
import argparse

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like tail tool')
    parser.add_argument('--lines', 
                        type=int,
                        help='count')
    
    parser.add_argument('--filename',
                        type=str,
                        help='name of the file',
                        default=sys.stdin
                        )
    args = parser.parse_args()
    return args

def wc(filename):
    cnt = 0
    f = filename if filename == sys.stdin else open(filename)
    for line in f:
        cnt += 1
    print(cnt)
    if f is not sys.stdin:
        f.close()

if __name__ == '__main__':
    args = parse_cmdline()
    wc(args.filename)
