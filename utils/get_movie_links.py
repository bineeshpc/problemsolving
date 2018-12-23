#! /usr/bin/env python

"""

Get the magnetic links of movies to download later

"""

import os
import re
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.options import Options

import time
import re
import datetime
import os
import pickle
import logging
import tempfile

from pathlib import PureWindowsPath
from bs4 import BeautifulSoup

logger = logging.getLogger('get_movie_links')
logger.setLevel(logging.INFO)

formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')

logfilename = 'get_movie_links.log'
with open(logfilename, 'w') as f:
    pass

fh = logging.FileHandler(logfilename,
                        encoding='utf8')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


def parse_cmdline():
    parser = argparse.ArgumentParser(
        description='Find the magnetic links of the latest movies available')
    parser.add_argument('language', 
                        type=str,
                        help='give the language to search',
                        default='',
                        nargs='?')
    parser.add_argument('query', 
                        type=str,
                        help='give a substring to search',
                        default='',
                        nargs='?')
    args = parser.parse_args()
    return args

pattern_to_search = re.compile("""
[,']  #patterns to remove
""", re.VERBOSE)

#film_pattern = re.compile('>(.*)</a></td>')
film_pattern = re.compile('<a href="(?P<link>/torrent/.*)">(?P<movie>.*)</a></td>')

def getProfile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    return profile


def get_old_films():
    filename = 'film_out.pickle'
    try:
        with open(filename, 'rb') as f:
            films = pickle.load(f)
    except Exception as e:
        print(e)
        return []
    return films

class BasePage:
    """ Abstract Base page with definition of get_page function
    """

    def __init__(self, url):
        self._url = url
        self._page_source = None

    def get_page(self, driver):
        """ Downloads the page and saves it in a variable
        """
        driver.get(self._url)
        try:
            element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "autocomplete")))
            logger.debug(self._url + 'loaded')
        except Exception as e:
            logger.debug(self._url + 'failed to load')
        try:
            driver.switch_to_alert().dismiss()
        except Exception as e:
            logger.debug(self._url + 'did not have alert')
            self._page_source = driver.page_source
            


class LanguagePage(BasePage):
    def __init__(self, language, page_number):
        """ Initializes the language and the page number
        """
        url = "https://1337x.st/sort-search/{}/time/desc/{}/".format(
            language,
            page_number)
        super().__init__(url)
        self.__language = language
        self.__page_number = page_number
        self.__films = []
        

    def parse_films(self):
        
        def get_headers(soup):
            name0 = soup.find('tr')
            return [i.get_text() for i in name0.find_all('th')]

        def get_data(soup):
            headers = get_headers(soup)
            for name1 in soup.find_all('tr'):
                table_data = name1.find_all('td')
                if table_data:
                    link = table_data[0].find_all('a')[-1]['href']
                    link = 'https://1337x.st{}'.format(link)
                    values = [data.get_text() for data in table_data]
                    yield dict(zip(headers, values)), link
        
        soup = BeautifulSoup(self._page_source, 'html.parser')
        for film_dict, film_link in get_data(soup):
            film = Film(film_dict, film_link, self.__language, self.__page_number)
            self.__films.append(film)
                


    def parse_films_old(self):    
        potential_films = re.findall('.*coll-1 name.*', self._page_source)
        for potential_film in potential_films:
            try:
                out_dict = film_pattern.search(potential_film).groupdict()
                film_name = out_dict['movie']
                link = 'https://1337x.st{}'.format(out_dict['link'])
                film = Film(film_name, link, self.__language, self.__page_number)
                
                self.__films.append(film)
            except Exception as e:
                logger.debug(self._url + 'did not have films')
                pass

    def get_films(self):
        return self.__films


    def save_output_file(self):
        tempdir = tempfile.gettempdir()
        output_file = "{}/{}_{}.html".format(tempdir,
            self.__language, self.__page_number)
        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(self._page_source)
        
class FilmPage(BasePage):
    def __init__(self, url):
        super().__init__(url)
        

    def get_magnet(self):
        pattern = r'.*magnet.*'
        #link_pattern = r'.*href="(?P<magnet>magnet:\?xt=urn:btih:[a-zA-Z0-9]*).*'
        #link_pattern = r'.*(?P<magnet>magnet.*)&.*'
        line = re.search(pattern, self._page_source).group()
        return line.split('href="')[1].split('&')[0]



class Selenium:

    def __init__(self):
        self.setUp()

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(
            firefox_options=options,
            firefox_profile=getProfile()
         )
        self.verificationErrors = []
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            print(e)
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            print(e)
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)

    def __del__(self):
        self.tearDown()

class MultipleLanguagePages:
    """
    This class is an agrregation of all Pages to download.
    User class typically uses this class
    """
    def __init__(self, languages, begin, end):
        """ Languages of the movies to download
        Begin page number
        End page number
        Both inclusive
        """
        self.__languages = languages
        self.__begin = begin
        self.__end = end
        self.__pages = []
        for page_number in range(self.__begin, self.__end + 1):
            for language in self.__languages:
                self.__pages.append(LanguagePage(language, page_number))


    def download_all(self, driver):
        for page in self.__pages:
            page.get_page(driver)
            page.save_output_file()
    
    def get_films(self):
        films = []
        for page in self.__pages:
            page.parse_films()
            films.extend(page.get_films())
        return films

class User:
    """ This is the user class
    User want to download some movies
    User knows which urls to look for
    And download
    """
    def __init__(self, language, query):
        start_time = time.time()
        sel_driver = Selenium()
        self.sel_driver = sel_driver
        if language == '':
            languages = ["Malayalam", "Tamil", "bollywood"]
        else:
            languages = [language]
        page_number_begin = 1
        page_number_end = 5
        self.output_file = 'film_out.pickle'
        self.multiple_pages = MultipleLanguagePages(languages, page_number_begin, page_number_end)
        self.multiple_pages.download_all(sel_driver.driver)
        # self.print_films()
        
        if language == '' and query == '': # do not call for small queries
            self.get_new_films()
            self.save_pages()
        else:
            self.get_films_match(query)

        end_time = time.time()
        print('excuted in {} seconds'.format(end_time - start_time))

    def print_films(self):
        for film in self.multiple_pages.get_films():
            print(film)

    def save_pages(self):
        with open(self.output_file, 'wb') as f:
            pickle.dump(self.multiple_pages.get_films(), f, pickle.HIGHEST_PROTOCOL)

    def get_new_films(self):
        old_films_list = [film.get_name() for film in get_old_films()]
        new_films_list = [film.get_name() for film in self.multiple_pages.get_films()]
        
        logger.info('Films read in the previous run are: ')
        for film in old_films_list:        
            logger.info(film)

        logger.info('\n\n\n\nFilms read in the current run are: ')
        for film in new_films_list:
            logger.info(film)

        logger.info('\n\n\n\nFilms newly found are:')
        unseen_films = set(new_films_list) - set(old_films_list)
        film_mapping = dict([(fo.get_name(), fo) for fo in self.multiple_pages.get_films()])
        for film in unseen_films:
            # film_obj = [fo for fo in self.multiple_pages.get_films() if fo.get_name() == film][0]
            film_obj = film_mapping[film]
            print(film_obj.get_name())
            print(film_obj.get_link())
            logger.info(film)
            logger.info(film_obj)
            filmpage = FilmPage(film_obj.get_link())
            filmpage.get_page(self.sel_driver.driver)
            print(filmpage.get_magnet())
            logger.info(filmpage.get_magnet())


    def get_films_match(self, query):
        """ Do a case insensitive search and give the result
        """
        logger.info('\n\n\n\nTrying to match {}'.format(query))
        for film_obj in self.multiple_pages.get_films():
            if film_obj.get_name().lower().find(query.lower()) != -1:
                print(film_obj.get_name())
                logger.info(film_obj.get_name())
                logger.info(repr(film_obj))
                filmpage = FilmPage(film_obj.get_link())
                filmpage.get_page(self.sel_driver.driver)
                print(filmpage.get_magnet())
                logger.info(filmpage.get_magnet())


class Film:
    """ Stores info about film
    """
    def __init__(self, film_dict, link, language, page_number):
        self.__name = film_dict['name']
        self.__language = language
        self.__page_number = page_number
        self.__link = link
        self.__leachers = film_dict['le']
        self.__seeders = film_dict['se']
        self.__time = film_dict['time']
        self.__size = film_dict['size info']
        self.__uploader = film_dict['uploader']


    def __repr__(self):
        v = []
        v.append('(\nname={}')
        v.append('link={}')
        v.append('language={}')
        v.append('pagenumber={}')
        v.append('leachers={}')
        v.append('seaders={}')
        v.append('size={}')
        v.append('time={}')
        v.append('uploader={}\n)')

        return '\n'.join(v).format(self.__name,
         self.__link,
          self.__language,
           self.__page_number,
           self.__leachers,
           self.__seeders,
           self.__size,
           self.__time,
           self.__uploader)

    def __eq__(self, other):
        return self.__name == other.__name

    def get_name(self):
        return self.__name

    def get_link(self):
        return self.__link

if __name__ == "__main__":
    args = parse_cmdline()
    User(args.language, args.query)