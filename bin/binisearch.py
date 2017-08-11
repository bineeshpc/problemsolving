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
        self.supportstrings = ['slide', 'glossary', 'faq',
                               'introduction', 'books',
                               'amazon best sellers', 'torrent',
                               "lecture notes",
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
        self.urls = self.build_urls(self.supportstrings)
        # self.openbrowser(self.urls)

    def build_urls(self, lst):
        url_list = []
        for str_data in lst:
            str_data = "https://www.google.co.in/#q={}".format(str_data)
            url_list.append(str_data)
        lst2 = ["https://scholar.google.co.in/scholar?q={}",
                "https://www.google.co.in/search?tbm=vid&q={}",
                "https://www.google.co.in/search?site=blogsearch&q={}",
                "https://www.google.co.in/search?q={}&hs=cX5&source=lnms&tbm=isch&sa=X", "https://www.google.co.in/search?q={}&btnG=Search+Books&tbm=bks&tbo=1"
                ]
        sstring = lst[0]
        for url1 in lst2:
            url_list.append(url1.format(sstring))

        url_list = [url1.replace(' ', '%20').replace('"', '') for url1 in url_list]
        for url1 in url_list:
            print url1
        return url_list
        
    def openbrowser(self, lst=None):
        if not lst:
            lst = self.urls
        for url1 in lst:
            if not self.browseropened:
                self.browseropened = True
                webbrowser.open(url1)
                browsertabs_count = 1
            else:
                if browsertabs_count <= 7:
                    webbrowser.open_new_tab(url1)
                    browsertabs_count += 1
                else:
                    webbrowser.open(url1)
                    browsertabs_count = 1



def main():
    # od = collections.OrderedDict()
    parser = argparse.ArgumentParser()
    parser.add_argument("searchstring1", help="first search string")
    parser.add_argument("searchstring2",
                        help="second search string", nargs="?")

    parser.add_argument('-o', dest='open_browser', action='store_true',
                    default=False,
                    help='Open browser if this is passed')
    args = parser.parse_args()
    # print args.searchstring1
    # print args.searchstring2
    r = Research(args.searchstring1, args.searchstring2)
    if args.open_browser:
        r.openbrowser()


if __name__ == '__main__':
    main()
