#! /usr/bin/env python

"""
crawl the webself.
A simple case is going to be implemented first
Download all files of a given type from a url

Given a url download every hrefs matching a particular pattern

I intend to extend this to a more generic crawler

Right now the functionality is limited.

python .\crawl.py "https://ece.uwaterloo.ca/~dwharder/aads/Lecture_materials/" --pattern '[0-9A-Za-
z_\.]*\.pptx|[a-z0-9A-Z_\.]\.pdf'

tasklist | findstr "python"

taskkill /IM python.exe /F
"""


import re
import argparse
import urllib.request
import queue # required later to extend using bfs
import os
import shutil
import requests

from concurrent import futures

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Unix like wget tool')
    parser.add_argument('url', 
                        type=str,
                        help='A regex pattern to download the files')
    parser.add_argument('--pattern',
    type=str,
    help='pattern of urls to download',
    default='.*')
    args = parser.parse_args()
    return args


def get_all_urls(url, pattern):
    """
    Given a url return an iterable of all urls in the page
    """
    req = urllib.request.Request(url)
    the_page = None
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    if the_page:
        # fix me if this is called multiple times
        # this will not be efficient
        # but for the time being this is good enough
        pattern = '{}'.format(pattern)
        regex = re.compile(pattern)
        values = regex.findall(str(the_page))
        return values


def download(url, dirname):
    """
    Given a url download it.
    """
    print(url)
    output_file = url.split('/')[-1]
    output_file = os.path.join(dirname, output_file)
    try:
        if not os.path.exists(output_file):
            print("downloading {} to {}".format(url, output_file))
            req = requests.get(url)
            with open(output_file, 'wb') as output:
                output.write(req.content)
        else:
            print('{} already exists'.format(output_file))
    except Exception as e:
        print(e)
    
def crawl(url, pattern):
    dirname = 'crawlout'
    try:
        os.mkdir(dirname)
    except FileExistsError:
        pass
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        all_urls = get_all_urls(url, pattern)
        future_to_url = dict((executor.submit(download, url + internal_filename, dirname), url + internal_filename) 
        for internal_filename in all_urls)

        for future in futures.as_completed(future_to_url):
            url = future_to_url[future]
            if future.exception() is not None:
                print('%r generated an exception: %s' % (url,
                                                        future.exception()))
            else:
                print('%r page did not produce any exceptions, result is %s' % (url, future.result()))
       
            

def main():
    args = parse_cmdline()
    crawl(args.url, args.pattern)


if __name__ == "__main__":
    main()