#!/usr/bin/python
from concurrent.futures import ThreadPoolExecutor
import re
import subprocess
import os
import datetime

def get_valid_filename(s):
    badchars = re.compile(r'[^A-Za-z0-9_. ]+|^\.|\.$|^ | $|^$')
    badnames = re.compile(r'(aux|com[1-9]|con|lpt[1-9]|prn)(\.|$)')
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
    dirname = get_valid_filename(playlistname)
    cwd = os.getcwd()
    try:
        os.mkdir(dirname)
    except OSError:
        pass
    #os.chdir(dirname)
    #print(os.getcwd())
    print("Downloading", playlistname, datetime.datetime.now())
    os.system('youtube-dl -ci -o "{}/{}/%(title)s.%(ext)s" "{}" --restrict-filenames'.format(cwd, dirname, playlist))
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


#create_playlistnamefile()
download()
