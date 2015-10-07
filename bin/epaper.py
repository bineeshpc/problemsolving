# !/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import datetime
import commands
import glob
import os

class Epaper(unittest.TestCase):
    def setUp(self):
        self.temp_dir = commands.getoutput('mktemp -d /tmp/epaper.XXXXXXX')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir",'/tmp')
        #fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")
        fp.set_preference("browser.download.manager.alertOnEXEOpen", False)
        mimetypes1 = "application/msword,application/csv,application/ris,text/csv,image/png,"
        mimetypes2 = "application/pdf,text/html,text/plain,application/zip,application/x-zip,"
        mimetypes3 = "application/x-zip-compressed,application/download,application/octet-stream"
        mimetypes = mimetypes1 + mimetypes2 + mimetypes3
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mimetypes)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.manager.focusWhenStarting", False)  
        fp.set_preference("browser.download.useDownloadDir", True)
        fp.set_preference("browser.helperApps.alwaysAsk.force", False)
        fp.set_preference("browser.download.manager.alertOnEXEOpen", False)
        fp.set_preference("browser.download.manager.closeWhenDone", True)
        fp.set_preference("browser.download.manager.showAlertOnComplete", False)
        fp.set_preference("browser.download.manager.useWindow", False)
        fp.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
        fp.set_preference("pdfjs.disabled", True)
        #print dir(fp)
        #print fp.default_preferences
        self.driver = webdriver.Firefox(firefox_profile=fp)
        self.driver.implicitly_wait(30)
        self.base_url = "https://epaper.thehindu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_epaper(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php?rt=login/loginAction")
        '''driver.find_element_by_id("loginbtn").click()
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("bineeshpc@gmail.com")
        driver.find_element_by_id("Passwrd").clear()
        driver.find_element_by_id("Passwrd").send_keys("CID@aj123")'''
        driver.find_element_by_id("txtemail").clear()
        driver.find_element_by_id("txtemail").send_keys("bineeshpc@gmail.com")
        driver.find_element_by_id("txtpwd").clear()
        driver.find_element_by_id("txtpwd").send_keys("CID@aj123")
        driver.find_element_by_id("loginbtn").click()
        
        try:
            driver.find_element_by_id("readofflinpage").click()
            driver.find_element_by_xpath("//div[@id='main']/div/span/a/span[2]").click()
            while True:
                print "waiting for download to complete"
                time.sleep(15)
                downloaded_filename = datetime.datetime.today().strftime(self.temp_dir + '/%Y%m%d*.zip.part')
                if glob.glob(downloaded_filename) == []:
                    os.system("""cd {tempdir}
                              unzip *.zip
                              ls *.pdf
                              cp *.pdf ~/Documents
                              rmdir {tempdir}
                          """.format(tempdir=self.temp_dir))
                    break
                
        except Exception, e:
            driver.find_element_by_id("logoutbtn").click()
            raise e
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
