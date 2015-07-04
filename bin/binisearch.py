#! /usr/bin/env python2 
import webbrowser
import time
import pickle
import filehelper
import collections

def enclose(data, s='"'):
    return '{s}{data}{s}'.format(s=s, data=data)

def apply_join(lst, s):
    return s.join(lst)

class Research(object):
    def __init__(self):
        self.searchstring1, self.searchstring2 = 'epistemology', 'knowledge'
        self.toremove = ''
        self.site = ''
        self.domains = ['.edu', '.org', '.com', '.in']
        self.filetypes = ['pdf', 'ppt', 'doc']
        self.sites = ['en.wikipedia.org']#, 'webopedia.com']

        self.removedphrases = [] #['badg', 'fccochin', enclose('real madrid', '"')]
        self.orr = [] #['kevin', 'mitnik', 'sachin']
        self.supportstrings = ['glossary', 'faq', 'introduction', 'books', 'amazon best sellers', 'torrent']
        self.searchstrings = []
        self.browseropened = False
        self.get_ready()
    
    def get_ready(self):
        lst = [
               "define:" + enclose(self.searchstring1),
               enclose(self.searchstring1),
               "intext:" + enclose(self.searchstring1),
               apply_join(self.orr, " OR "),
               enclose(self.searchstring1) + ' -' + apply_join(self.removedphrases, " -"),
               'inurl:' + enclose(self.searchstring1),
               '{a} * {b}'.format(a=enclose(self.searchstring1), b=self.searchstring2),
               '{a} AROUND(10) {b}'.format(a=enclose(self.searchstring1), b=self.searchstring2),
               ]
        domains = ['site:{x} {d}'.format(x=x, d=enclose(self.searchstring1)) for x in self.domains + self.sites]
        filetypes = ['filetype:{x} {d}'.format(x=x, d=enclose(self.searchstring1)) for x in self.filetypes]
        supportstrings = ['{} {}'.format(enclose(self.searchstring1), s) for s in self.supportstrings]
        
        lst1 = [lst, domains, filetypes, supportstrings]
        self.supportstrings = sum(lst1, [])
        
        self.openbrowser(self.supportstrings)
            
            
    
    def openbrowser(self, lst):
        for str_data in lst:
            print str_data
            str_data = "https://www.google.co.in/#q={}".format(str_data)
            if not self.browseropened:
                webbrowser.open(str_data)
                self.browseropened = True
                time.sleep(7)
            else:
                webbrowser.open_new_tab(str_data)
        
        

r = Research()

od = collections.OrderedDict()


