#!/usr/bin/env python
from concurrent.futures import ThreadPoolExecutor
import re
import subprocess
import os
import datetime
import argparse


def parse_cmdline():

    parser = argparse.ArgumentParser(description="""Download youtube playlists easily \n
                                     Playlist filename is remaining.txt\n
                                     The playlist filename with titles is playlistnames.txt
                                     
                                     format of remaining.txt 
                                     $ head -2 remaining.txt
https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8
https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi

                                     $ head -2 playlistnames.txt
    MIT 18.06 Linear Algebra Spring 2005,https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8
    MIT 6.034 Artificial Intelligence Fall 2010,https://www.youtube.com/playlist?list=PLUl4u3cNGP63gFHB6xb-kVBiQHYe_4hSi


    """,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--create_playlist_file',
                        action='store_true',
                       help='create a playlist file with after reading the titles from the playlistfile')
    parser.add_argument('--download', action='store_true',
                        help='download the already existing playlist file with titles')
    args = parser.parse_args()
    return args



def get_valid_filename(s):
    badchars = re.compile(r"""[^A-Za-z0-9_. ]+  # Anything other than these are bad chars 
                            ,
                            """,
                            re.VERBOSE)
    badnames = re.compile(r"""(aux
|
com[1-9]
|
con
|
lpt[1-9]
|
prn
)
(
\.|$
)""",
                          re.VERBOSE)
    name = badchars.sub('_', s)
    if badnames.match(name):
        name = '_' + name
    return name


def get_playlistname(playlist):
    simulator = "youtube-dl -si '{}'".format(playlist)
    status, output = subprocess.getstatusoutput(simulator)
    #assert status == 0
    playlistnameregex = re.compile("\[download\].*Downloading playlist: (?P<playlistname>.*)", re.MULTILINE)
    playlistname = playlistnameregex.search(
        output).groupdict().get('playlistname')
    return playlistname

def create_playlistnamefile():
    cnt = 0
    playlistnamefile = open('playlistnames.txt','w')
    for line in open('remaining.txt'):
        print(line)
        cnt += 1
        #if cnt < 8: continue
        playlistname = get_playlistname(line)
        print(playlistname)
        playlistnamefileline = "{},{}".format(playlistname, line)
        print(playlistnamefileline)
        playlistnamefile.write(playlistnamefileline)
    playlistnamefile.close()

def downloadplaylist(playlistname, playlist):
    """
    Download an individual playlist
    """
    dirname = get_valid_filename(playlistname)
    cwd = os.getcwd()
    try:
        os.mkdir(dirname)
    except OSError:
        pass
    #os.chdir(dirname)
    #print(os.getcwd())
    print("Downloading", playlistname, datetime.datetime.now())
    
    cmd1 = 'youtube-dl --continue --ignore-errors'
    cmd2 = ' --format 18 --output'
    cmd3 = ' "{}/{}/%(title)s.%(ext)s" "{}" --restrict-filenames'
    download_cmd_string = '{}{}{}'.format(cmd1, cmd2, cmd3)
    os.system(download_cmd_string.format(cwd, dirname, playlist))
    #os.system("echo youtubedl he he he;echo '{}';date;sleep 60;date".format(playlist))
    #os.chdir(cwd)
    #print(cwd)

def download():
    playlists = []
    with open('playlistnames.txt') as playlistnamefile:
        for line in playlistnamefile:
            playlistname, playlist = line.strip('\n').split(',')
            playlists.append((playlistname, playlist))
            
    pool = ThreadPoolExecutor(max_workers=1)
    for playlistname, playlist in playlists:
        pool.submit(downloadplaylist, playlistname, playlist)


def main():
    args = parse_cmdline()
    if args.create_playlist_file:
        create_playlistnamefile()
    if args.download:
        download()

if __name__ == '__main__':
    main()
