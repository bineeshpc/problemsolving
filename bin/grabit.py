#!/usr/bin/env python
"""
Used to download files from websites.
Input is a file containing urls
"""
import os
import re
import argparse
import subprocess
import time
import shutil
import sys
import multiprocessing
import logging
import tempfile
import random
import io
import glob
from urllib.parse import urlparse


def get_duration(duration_string):
    try:
        h, m, s = duration_string.split(':')
    except:
        try:
            m, s = duration_string.split(':')
            h = '0'
        except:
            h = m = '0'
            s = duration_string
    logging.debug('%s hours %s minutes %s seconds', h, m, s)
    try:    
        h, m, s = int(h), int(m), int(s)
    except ValueError:
        return 0
    return h * 60 * 60 + m * 60 + s


def find_suitable_format(line, timeout=54):
    """Finds a suitable format for youtube"""
    isyoutube = (urlparse(line).netloc.find('youtube') != -1)
    duration_string = subprocess.getoutput(
        'youtube-dl -s --get-duration {} 2>/dev/null'.format(line))
    if re.search('ERROR', duration_string):
        logging.error('%s %s', duration_string, "cannot be downloaded")
        fmt = 1
        return fmt
    else:
        duration = get_duration(duration_string)
    tempdir = tempfile.TemporaryDirectory()
    formats = [''] + ['{}'.format(fm) for fm in [18, 5, 36, 17]]

    for fmt in formats:
        retry = 5
        retryonerror = 5
        while retry > 0:
            if fmt == '':
                cmd = """cd {} && timeout {} ~/temp/youtube-dl/bin/youtube-dl {} {}""".format(
                    tempdir.name, timeout, fmt, line)
            else:
                cmd = """cd {} && timeout {} ~/temp/youtube-dl/bin/youtube-dl -f {} {}""".format(
                    tempdir.name, timeout, fmt, line)
            logging.debug(cmd)
            logging.debug(time.ctime())
            textoutput = subprocess.getoutput(cmd)
            logging.debug(textoutput)
            if re.search('ERROR', textoutput):
                if retryonerror == 0:
                    return 1
                else:
                    retryonerror -= 1
                    continue
            try:
                extracted = re.search("\d*\.\d*(MiB|GiB)", textoutput).group()
                break
            except AttributeError:
                retry -= 1
                timeout += 10
                logging.error(
                    "Network seems to be slow retrying {} more times".format(retry))
        unit = re.search("\d*\.\d*(MiB|GiB)", textoutput).groups()[0]
        size = float(re.split('MiB|GiB', extracted)[0])
        if unit == 'GiB':
            size = size * 1024
            logging.debug('duration %s, size %s, duration/size %s',
                          duration, size, duration / size)
        if duration / size < 14:
            if isyoutube:
                logging.error("Trying another size in youtube")
                continue
            else:
                logging.error("Not youtube, cannot get lower file sizes")
                return fmt
        else:
            logging.info("File size is ok")
            return fmt

def isalready_downloaded(line):
    if urlparse(line).netloc.find('youtube') != -1:
        _, videoid = line.split('=')
        already_existing_files_list = glob.glob(args.outputdir + '/*')
        if any([(filename.find(videoid) != -1) for filename in already_existing_files_list]):
            return True
        else:
            return False
    

def download(line):
    """Downloads the given link"""
    logging.info("download: trying to download %s", line)
    path = '~/temp/youtube-dl'
    sys.path.insert(0, path)
    import youtube_dl
    words_for_skipping = '100%|Unsupported URL|has already been downloaded and merged'
    if not args.format:
        if isalready_downloaded(line):
            print('{} already downloaded.'.format(line))
            return
        format = find_suitable_format(line, args.timeout)
    else:
        format = args.format

    outputfile = args.outputdir + '/%(title)s-%(id)s.%(ext)s'
    os.system('mkdir -p {}'.format(args.outputdir))
    if urlparse(line).netloc.find('youtube') != -1:  # youtube specific options
        if format:
            sys.argv = [
                path + '/bin/youtube-dl', '-u', 'itsmayashekhar',
                '-p', 'koudilya', '-f', format, '-o', outputfile, line]
        else:
            sys.argv = [
                path + '/bin/youtube-dl', '-u', 'itsmayashekhar',
                '-p', 'koudilya', '-o', outputfile, line]
    else:  # for other websites
        sys.argv = [path + '/bin/youtube-dl', '-o', outputfile, line]
    logging.debug(sys.argv)
    retry = args.retries
    while retry > 0:
        try:
            logging.debug("retries remaining is %s", retry)
            p = multiprocessing.Process(target=youtube_dl.main)
            p.start()
            p.join()
            if p.exitcode == 0:
                retry = 0
            else:
                retry -= 1
        except Exception as e:
            logging.error(e)
    if p.exitcode != 0:
        logging.error("Giving up %s after %s retries", line, retry)
        return 1
    logging.debug("Successfully downloaded %s", line)
    return 0


class FileState(object):

    def __init__(self, filename):
        self.filename = filename
        self.filelines = set()
        self.donefilelines = set()
        shutil.copyfile(self.filename,
                        self.filename + str(random.randint(10000, 20000)) + '.txt')
        with open(self.filename) as f:
            for line in f:
                line = line.strip('\n')
                self.filelines.add(line)
        logging.debug("set filelines %s", self.filelines)

    def download(self):
        for line in self.filelines:
            download(line)
            self.donefilelines.add(line)

    def __del__(self):
        """        
        diff = self.filelines - self.donefilelines
        if len(diff) == 0:
            os.unlink(self.filename)
            return
        with open(self.filename, 'w') as f:
            for line in diff:
                f.write(line + '\n')
        """
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin,
                        help="get input filename stdin can also be used as input")
    parser.add_argument(
        "-f", "--format", help="pass specific youtube format to download")
    parser.add_argument("-r", "--retries", type=int,
                        default=1000, help="number of retries")
    parser.add_argument("-t", "--timeout", type=int,
                        default=30, help="timeout to use while determining appropriate format")
    parser.add_argument("-o", "--outputdir",
                        default=".",
                        help="pass output directory to download files to"
                        "output directory will be created if it does not exist")
    parser.add_argument("-l", "--logfile",
                        default=sys.stdout,
                        help="pass the log file, default is sys.stdout")
    args = parser.parse_args()

    if args.infile.name == '<stdin>':
        f = tempfile.NamedTemporaryFile(delete=False)
        for line in args.infile:
            f.write(line.encode('utf-8'))
        f.close()
        args.infile = f.name
    else:
        infile = args.infile.name
        args.infile.close()
        args.infile = infile

    logging.basicConfig(stream=args.logfile, level=logging.DEBUG)
    logging.debug('infile %s, args.format %s', args.infile, args.format)

    FileState(args.infile).download()
