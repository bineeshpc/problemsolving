import pickle
import sys


class File(object):

    def __init__(self, file1):
        self.file = file1

    def filenavigator(self, numbering=False):
        with open(self.file) as op:
            if numbering:
                fun = enumerate
            else:
                fun = lambda x: x

            for line in fun(op):
                yield line

    def write_itr(self, inp_itr, append='a'):
        with open(self.file, append) as of:
            for line in inp_itr:
                self.write_except(of, line)

    def write(self, inp, append='a'):
        with open(self.file, append) as of:
            self.write_except(of, inp)

    def writeline(self, inp, append='a'):
        self.write(inp + '\n', append=append)

    def write_except(self, of, line):
        try:
            of.write(line)
        except:
            print('write failed', of, line)

    def fprint(self):
        for line in self.filenavigator():
            print(line)

    def numlines(self):
        for num, line in self.filenavigator(True):
            pass
        return num + 1

    def read(self):
        with open(self.file) as op:
            return op.read()


class Filebinary(object):

    def __init__(self, file1, data):
        self.file = file1
        self.data = data

    def dump(self):
        with open(self.file, 'wb') as output:
            # Pickle dictionary using protocol 0.
            print 'Dumping to {}'.format(self.file)
            pickle.dump(self.data, output)

    def load(self):
        with open(self.file, 'rb') as pkl_file:
            self.data = pickle.load(pkl_file)
            print 'Loading {0}'.format(self.file)
        return self.data

if __name__ == '__main__':
    filepath = '/tmp'
    inputtestfile = 'itf.txt'
    outputtestfile = 'otf.txt'
#     File(inputtestfile).write_itr((i + '\n'
#                               for i in ['mathai', 'kura', 'dhileesh']), 'w')
#     itf = File(inputtestfile)
#     itf.fprint()
#     File(outputtestfile).write_itr(b for a, b in itf.filenavigator(True))
#     otf = File(outputtestfile)
#     otf.fprint()
#     print(otf.numlines())
    print File(inputtestfile).read()
