import os
import hashlib
import pickle

filename = 'F:/from_gateway/tocopy'
target_dir = 'F:/from_gateway/modified_videos'


filename = 'F:/photos_taken/DCIM'
target_dir = 'F:/from_gateway/bini_modified_videos'

def md5sum(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

class FindDups:
    def __init__(self):
        self.pkl_file = 'data123.pkl'
        try:
            pkl_file = open(self.pkl_file, 'rb')
            self.filename_md5_map, self.md5_filename_map = pickle.load(pkl_file)
            
            pkl_file.close()
        except:
            print('could not open', self.pkl_file, 'initializing')
            self.filename_md5_map = {}
            self.md5_filename_map = {}

    def __del__(self):
        pkl_file = open(self.pkl_file, 'wb')
        pickle.dump((self.filename_md5_map, self.md5_filename_map), pkl_file)
        pkl_file.close()

    def add(self, file):
        if not self.filename_md5_map.get(file):
            self.filename_md5_map[file] = []
        else:
            # Filename already processed
            # need not process again
            print(file, 'already present')
            return
        md5 = md5sum(file)

        self.filename_md5_map[file].append(md5)
        
        if not self.md5_filename_map.get(md5):
            self.md5_filename_map[md5] = []

        self.md5_filename_map[md5].append(file)



    def list_duplicates(self):
        count = 0
        for md5, filenames in self.md5_filename_map.items():
           if len(filenames) > 1:
                print(md5, filenames)
                count += len(filenames) - 1

        print ('Number of duplicates is ', count)

def crawl(filename, patterns=['jpg', 'jpeg']):
    for filename_1 in os.listdir(filename):
        filename_2 = os.path.join(filename, filename_1)
        condition = [pattern in filename_2.lower() for pattern in patterns]
        
        if any(condition):
            yield filename_2
        if os.path.isdir(filename_2):
            yield from crawl(filename_2, patterns)


def find_duplicates():
    fd = FindDups()
    for file in crawl(filename):
        fd.add(file)

    fd.list_duplicates()


def convert_format():
    cmd = r"""C:\Users\uC196302\Downloads\ffmpeg-20180224-28924f4-win64-static\bin\ffmpeg.exe -i {infile} -s 480x360 -b:v 1624k -vcodec mpeg1video -acodec copy {outfile}"""

    for file in crawl(filename, patterns=['mp4']):
        basename = os.path.basename(file)
        dirname = target_dir
        outfile = os.path.join(dirname, basename.replace(".", "_out."))
        cmd1 = cmd.format(infile=file, outfile=outfile)
        print(cmd1)
        os.system(cmd1)



