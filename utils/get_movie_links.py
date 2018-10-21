#! /usr/bin/env python

"""

Get the magnetic links of movies to download later

"""

import os
import re
import argparse
import requests
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

from pathlib import PureWindowsPath



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


def get_magnetic_link(language):
    url = "https://1337x.st/sort-search/{}/time/desc/1/".format(language)
    req = requests.get(url, allow_redirects=True)
    print(req.text)

def getProfile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.privatebrowsing.autostart", True)
    return profile

class Downloader:

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
        self.base_url = "https://1337x.st/sort-search/{}/time/desc/1/"
        self.output_file = 'film_out.pickle'

    def save_data(self, driver, language):
        url = self.base_url.format(language)
        driver.get(url)

        try:
            element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "autocomplete"))
            
        )
            print(element)
        except Exception as e:
            print(e)
        try:
            driver.switch_to_alert().dismiss()
        except Exception as e:
            print(e)
        output_file = "output_{}.html".format(language)
        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(driver.page_source)

    def update_films(self, pattern, language, film_dict):
        
        output_file = "output_{}.html".format(language)
        with open(output_file, encoding="utf-8") as f:
            content = f.read()
            potential_films = re.findall('.*coll-1 name.*', content)
            for potential_film in potential_films:
                try:
                    film = pattern.search(potential_film).group(1).split('>')[-1]
                    film_dict[language].append(film)
                except Exception as e:
                    print(e)
                    pass
        
    def print_new_films(self, film_dict):
        print("new films are:")    
        with open(self.output_file, 'rb') as f:
            film_dict_old = pickle.load(f)
            for language in film_dict:
                new_films = set(film_dict[language])
                old_films = set(film_dict_old[language])
                for film in (new_films - old_films):
                    print(film)

    def remove_files(self, languages):
        for language in languages:
            output_file = 'output_{}.html'.format(language)
            os.remove(output_file)


    def write_film_info_to_disk(self, film_dict):
        text_output_file = 'film_output.txt'
        old_text_output_file = 'film_output_1.txt'
        os.remove(old_text_output_file)
        os.rename(text_output_file, old_text_output_file)
        with open(text_output_file, 'w') as f:
            for language in film_dict:
                f.write(language + '\n')
                for film in film_dict[language]:
                    f.write(film + '\n')

        with open(self.output_file, 'wb') as f:
            pickle.dump(film_dict, f, pickle.HIGHEST_PROTOCOL)
    
    def download(self):
        driver = self.driver
        languages = ["Malayalam", "Tamil", "bollywood"]
        pattern = re.compile('>(.*)</a></td>')
        film_dict = dict([(language, []) for language in languages])

        for language in languages:
            self.save_data(driver, language)
            self.update_films(pattern, language, film_dict)
        self.print_new_films(film_dict)
        self.remove_files(languages)
        self.write_film_info_to_disk(film_dict)
        
    
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

if __name__ == "__main__":
    downloader = Downloader()
    downloader.download()
