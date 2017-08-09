#! /usr/bin/env python2
import webbrowser
import time
import pickle
import filehelper
import collections
import argparse


def enclose(data, s='"'):
    return '{s}{data}{s}'.format(s=s, data=data)


def apply_join(lst, s):
    return s.join(lst)


class Research(object):

    def __init__(self, searchstring1, searchstring2):
        self.searchstring1 = searchstring1
        self.searchstring2 = "" if not searchstring2 else searchstring2
        self.toremove = ''
        self.site = ''
        self.domains = ['.edu', '.org', '.com', '.in']
        self.filetypes = ['pdf', 'ppt', 'doc']
        self.sites = ['en.wikipedia.org']  # , 'webopedia.com']

        # ['badg', 'fccochin', enclose('real madrid', '"')]
        self.removedphrases = []
        self.orr = []  # ['kevin', 'mitnik', 'sachin']
        self.supportstrings = ['slide', 'glossary', 'faq', 'introduction', 'books',
                               'amazon best sellers', 'torrent', "lecture notes",
                               'lectures']
        self.searchstrings = []
        self.browseropened = False
        self.get_ready()

    def get_ready(self):
        lst = [
            "define:" + enclose(self.searchstring1),
            enclose(self.searchstring1),
            "intext:" + enclose(self.searchstring1),
            apply_join(self.orr, " OR "),
            enclose(self.searchstring1) + ' -' +
            apply_join(self.removedphrases, " -"),
            'inurl:' + enclose(self.searchstring1)
        ]
        if self.searchstring2:
            lst.extend([
                '{a} * {b}'.format(a=enclose(self.searchstring1),
                                   b=self.searchstring2),
                '{a} AROUND(10) {b}'.format(
                    a=enclose(self.searchstring1), b=self.searchstring2),
            ])
        domains = ['site:{x} {d}'.format(
            x=x, d=enclose(self.searchstring1)) for x in self.domains + self.sites]
        filetypes = ['filetype:{x} {d}'.format(
            x=x, d=enclose(self.searchstring1)) for x in self.filetypes]
        supportstrings = [
            '{} {}'.format(enclose(self.searchstring1), s) for s in self.supportstrings]

        lst1 = [lst, domains, filetypes, supportstrings]
        self.supportstrings = sum(lst1, [])

        self.openbrowser(self.supportstrings)

    def openbrowser(self, lst):
        for str_data in lst:
            print str_data
            str_data = "https://www.google.co.in/#q={}".format(str_data)
            print str_data
            if not self.browseropened:
                self.browseropened = True
                webbrowser.open(str_data)
                time.sleep(15)
            else:
                pass
                webbrowser.open_new_tab(str_data)
        lst2 = ["https://scholar.google.co.in/scholar?q={}",
                "https://www.google.co.in/search?tbm=vid&q={}",
                "https://www.google.co.in/search?site=blogsearch&q={}",
                "https://www.google.co.in/search?q={}&btnG=Search+Books&tbm=bks&tbo=1"
                ]
        sstring = lst[0]
        for url in lst2:
            webbrowser.open_new_tab(url.format(sstring))


od = collections.OrderedDict()


parser = argparse.ArgumentParser()
parser.add_argument("searchstring1", help="first search string")
parser.add_argument("searchstring2", help="second search string", nargs="?")
args = parser.parse_args()
print args.searchstring1
print args.searchstring2
r = Research(args.searchstring1, args.searchstring2)
