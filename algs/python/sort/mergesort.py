"""
let t be the total size of the memory.
let m be the maximum size we can hold in memory
split the file int t/m files
read each file and sort all of them.
merge each files together to a single file.
delete intermediate files
"""
import tempfile
import os
import glob

filename = '/mnt/testing/mergesort_input.txt'
fileoutput = '/mnt/testing/mergesort_output.txt'
tempdir = '/tmp/mergefiles'

memory = 10**6

def split(filename):
    os.mkdir(tempdir)
    filenumber = 1
    with open(filename) as f:
        lines = []
        cnt = 0
        for line in f:
            cnt += 1
            lines.append(int(line))
            if cnt == memory:
                lines.sort()
                with open(tempdir + '/file{}'.format(filenumber), 'w') as f1:
                    for a in lines:
                        f1.write('{}\n'.format(a))
                filenumber += 1
                lines = []
                cnt = 0
    
def kwaymerge():
    filenames = glob.glob(tempdir + '/*')
    fds = [open(file1) for file1 in filenames]
    xs = []
    for ind in range(0, len(fds)):
        value = int(fds[ind].readline())
        xs.append((len(xs) , value))
        
        

#split(filename)
kwaymerge()    