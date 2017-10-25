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


def replace_all_strings(s, str1):
    """
    given a string s replace all strings in the list of tuples
    replace alls strings with their curresponding strings in the tuple
    Args:
    s(str): is a string where some somestrings should be replaced
    str1(list): list of tuples [(s1, s1_replacement), (s2, s2_replacement) ..]
    """
    for str2, str2_replacement in str1:
        s = s.replace(str2, str2_replacement)
    return s


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
                               'common mistakes', 'examples',
                               'introduction', 'books', 'cheatsheet',
                               'notes', 'summary',
                               'amazon best sellers', 'torrent',
                               'lecture notes', 'hashtag on twitter',
                               'lectures', 'top 10', 'alternatives',
                               'practical', 'companies', 'government',
                               'mind the book', 'quora', 'yahoo answers',
                               'super user', 'stack overflow', 'arch',
                               'debian', 'open source'
        ]
        self.searchstrings = []
        self.toreplace = [(' ', '%20'),
                          ('"', ''),
                          ('(', '%40'),
                          (')', '%41')
        ]
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
            '{} {}'.format(
                enclose(self.searchstring1), s) for s in self.supportstrings]

        lst1 = [lst, domains, filetypes, supportstrings]
        self.supportstrings = sum(lst1, [])
        self.urls = self.build_urls(self.supportstrings)
        self.annotation = [ ('define', 0), 
                            ('Base Search', 0),
                            ('intext', 10),
                            ('blank', 10),
                            ('dont know', 10),
                            ('inurl', 10),
                            ('Education sites', 7),
                            ('org sites', 7), 
                            ('com sites', 7),
                            ('india sites', 6),
                            ('wikipedia', 1),
                            ('pdf format', 5),
                            ('ppt format', 5),
                            ('doc format', 6),
                            ('Slides', 0),
                            ('Glossary', 5),
                            ('Frequently asked questions', 3),
                            ('Common Mistakes', 4),
                            ('Examples', 5),
                            ('Introduction', 4),
                            ('Books about it',3),
                            ('Cheatsheet', 3),
                            ('Notes', 6),
                            ('Summary', 4),
                            ('Best Sellers', 5),
                            ('Torrent', 8),
                            ('Lecture Notes', 4),
                            ('Twitter hashtag search', 5),
                            ('Lectures about it', 4),
                            ('Top 10', 7),
                            ('Alternatives for it', 8),
                            ('Practical ideas', 6),
                            ('Companies doing it', 8),
                            ('Governments doing it', 8),
                            ('Mind the book', 9),
                            ('Quora questions', 5),
                            ('Yahoo answers', 8),
                            ('Super User', 8),
                            ('Stack Overflow', 5),
                            ('Arch linux world', 6),
                            ('Debian linux world', 7),
                            ('Open Source world', 8),
                            ('Scholar', 9),
                            ('Video', 1),
                            ('Blog search', 5),
                            ('Image search', 1),
                            ('Books', 6)
        ]

        self.prioritizer = Prioritizer(self.urls, self.annotation)

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
        url_list = [replace_all_strings(url1,
                    self.toreplace) for url1 in url_list]
        return url_list

    def emacs(self):
        
        for url1, ann in self.prioritizer.prioritized():
            print "[[{}][{}]]".format(url1, ann)
            # print url1, ann
        
    def openbrowser(self, lst=None):
        """
        Create an html output and open it in browser
        """
        search_output = "/tmp/searches.html"
        html_string = """
            <html>
            <title>
            Convenient searches
            </title>
            <body>
            {}
            </body>
            </html>
            """
        search_line_template = '''<a href="{}" target="_blank">{}</a>'''
        with open(search_output, 'w') as search_output_file:
            search_lines = []
            for url1, ann in self.prioritizer.prioritized():
                search_line = search_line_template.format(url1, ann)
                search_lines.append(search_line)
            all_search_lines_string = '<br>'.join(search_lines)
            html_string_to_write = html_string.format(all_search_lines_string)
            search_output_file.write(html_string_to_write)
        
        if self.browseropened:
            webbrowser.open_new_tab(search_output)
        else:
            self.browseropened = True
            webbrowser.open(search_output)
        """
        Earlier code for opening browser tabs for every url generated
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
        """

class Prioritizer(object):
    def __init__(self, urls, annotations):
        self.urls = urls
        self.annotations = annotations
        self.url_annotation_mapping = self.u_a_mapping()

    def u_a_mapping(self):
        mapping = []
        for url, annotation in zip(self.urls, self.annotations):
            mapping.append((url, annotation[0], annotation[1]))
        return mapping


    def prioritized(self):
        ordered = sorted(self.url_annotation_mapping, key=lambda(x): x[2])
        for x in ordered:
            yield x[0], x[1]

        
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
    else:
        r.emacs()


if __name__ == '__main__':
    main()
