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
from pathlib import PureWindowsPath

logger = logging.getLogger('get_movie_links')
logger.setLevel(logging.INFO)
logfilename = 'get_movie_links.log'
with open(logfilename, 'w') as f:
    pass

fh = logging.FileHandler(logfilename)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


def parse_cmdline():
    parser = argparse.ArgumentParser(
        description='Find the magnetic links of the latest movies available')
    parser.add_argument('language', 
                        type=str,
                        help='give the language to search')
    args = parser.parse_args()
    return args

pattern_to_search = re.compile("""
[,']  #patterns to remove
""", re.VERBOSE)

film_pattern = re.compile('>(.*)</a></td>')

def getProfile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    return profile


def get_old_films():
    filename = 'film_out.pickle'
    with open(filename, 'rb') as f:
        films = pickle.load(f)
    return films


class Page:
    def __init__(self, language, page_number):
        """ Initializes the language and the page number
        """
        self.__language = language
        self.__page_number = page_number
        self.__url = "https://1337x.st/sort-search/{}/time/desc/{}/".format(
            self.__language,
            self.__page_number)
        self.__page_source = None
        self.__films = []

    def get_page(self, driver):
        """ Downloads the page and saves it in a variable
        """
        driver.get(self.__url)
        try:
            element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "autocomplete")))
            logger.debug(self.__url + 'loaded')
        except Exception as e:
            logger.debug(self.__url + 'failed to load')
        try:
            driver.switch_to_alert().dismiss()
        except Exception as e:
            logger.debug(self.__url + 'did not have alert')
            self.__page_source = driver.page_source
            


    def parse_films(self):    
        potential_films = re.findall('.*coll-1 name.*', self.__page_source)
        for potential_film in potential_films:
            try:
                film_name = film_pattern.search(potential_film).group(1).split('>')[-1]
                film = Film(film_name, self.__language, self.__page_number)
                self.__films.append(film)
            except Exception as e:
                logger.debug(self.__url + 'did not have films')
                pass

    def get_films(self):
        return self.__films


    def output_file(self):
        output_file = "output_{}.html".format(language)
        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(driver.page_source)
        


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

class MultiplePages:
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
                self.__pages.append(Page(language, page_number))


    def download_all(self, driver):
        for page in self.__pages:
            page.get_page(driver)
    
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
    def __init__(self):
        start_time = time.time()
        sel_driver = Selenium()
        languages = ["Malayalam", "Tamil", "bollywood"]
        page_number_begin = 1
        page_number_end = 5
        self.output_file = 'film_out.pickle'
        self.multiple_pages = MultiplePages(languages, page_number_begin, page_number_end)
        self.multiple_pages.download_all(sel_driver.driver)
        # self.print_films()
        self.get_new_films()
        self.save_pages()
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
        logger.info('Films read before are: ')
        for film in old_films_list:
            logger.info(film)
        logger.info('Films read now are: ')
        for film in new_films_list:
            logger.info(film)
        unseen_films = set(new_films_list) - set(old_films_list)
        logger.info('Films that came after the last read are:')
        for film in unseen_films:
            print(film)
            logger.info(film)

class Film:
    """ Stores info about film
    """
    def __init__(self, name, language, page_number):
        self.__name = name
        self.__language = language
        self.__page_number = page_number

    def __repr__(self):
        return '({}, {}, {})'.format(self.__name, self.__language, self.__page_number)

    def __eq__(self, other):
        return self.__name == other.__name

    def get_name(self):
        return self.__name

if __name__ == "__main__":
    User()