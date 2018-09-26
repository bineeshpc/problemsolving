import importlib
import argparse
import sys
import glob

class FrequencyCounter:
    def __init__(self, st, filename):
        if isinstance(st, str):
            modulename, classname = st.split('.')
            lib = importlib.import_module(modulename)
            self.st = getattr(lib, classname)()
        else:
            self.st = st
        self.filename = filename

    def count_frequency(self):
        if self.filename is not sys.stdin:
            file = open(self.filename)
        num_words = 0
        num_words_distinct = 0
        max_word = ""
        self.st.put(max_word, 0)
        for line in file:
            words = line.strip().split()
            for word in words:
                num_words += 1
                if self.st.contains(word):
                    self.st.put(word, self.st.get(word) + 1)
                else:
                    self.st.put(word, 1)
                    num_words_distinct += 1
                if self.st.get(word) > self.st.get(max_word):
                    max_word = word
                
        print("Number of words = {}".format(num_words))
        print("Number of distinct words = {}".format(num_words_distinct))
        print("The word with maximum frequency is {} and its frequency is {}".format(max_word, self.st.get(max_word)))
        if self.filename is not sys.stdin:
            file.close()

def parse_cmdline():
    parser = argparse.ArgumentParser(description='A frequency counter for text files')
    parser.add_argument('--filename',
                        help='name of the file',
            default=__file__)
    parser.add_argument('--symboltable',
    help='symbol table to use',
    default='SequentialSearchST.SequentialSearchST',
    choices=['{0}.{0}'.format(filename.split('.')[0]) for filename in glob.glob('*ST.py')]
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_cmdline()
    ft = FrequencyCounter(args.symboltable, args.filename)
    ft.count_frequency()

if __name__ == '__main__':
    main()