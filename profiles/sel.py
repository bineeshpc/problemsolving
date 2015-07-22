# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class Sel(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.keralamatrimony.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sel(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("ID").clear()
        driver.find_element_by_id("ID").send_keys("9446429976")
        try:
            driver.find_element_by_id("TEMPPASSWD1").clear()
            driver.find_element_by_id("TEMPPASSWD1").send_keys("Password")
        except:
            pass
        driver.find_element_by_id("PASSWORD").clear()
        driver.find_element_by_id("PASSWORD").send_keys("ajanta")
        driver.find_element_by_xpath("//input[@value='Log In']").click()
        self.downloadprofiles()

    def downloadprofile(self, profileid):
        time.sleep(2)
        url = "http://profile.keralamatrimony.com/profiledetail/viewprofile.php?id={}&gaact=SID&gasrc=SRCH".format(
            profileid)
        self.driver.get(url)
        open(
            '/tmp/{}.html'.format(profileid), 'w').write(self.driver.page_source.encode('utf8'))

    def downloadprofiles(self):
        for url in open('filtered.txt'):
            url_str = url.strip('\n')
            profileid = self.getprofile_id_from_url(url_str)
            if not profileid:
                profileid = re.match('E[0-9]{7}', url_str).group()
            if profileid:
                self.downloadprofile(profileid.capitalize())

    def getprofile_id_from_url(self, url):
        b = re.search(r'id=(?P<id>[Ee][0-9]{7})', url)
        try:
            return b.groupdict()['id']
        except:
            return None

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
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
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
