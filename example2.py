'''
Created on Aug 4, 2018

@author: Rajesh Rathod
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, datetime
from test.test_pickle import getattribute

class Z1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.weightwatchers.com/us/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_z1(self):
        dayOfToday = datetime.datetime.today().weekday()
        print(dayOfToday)
        driver = self.driver
        driver.get(self.base_url + "/")
        titleOfFirstPage = driver.title
        print(titleOfFirstPage)
        if(titleOfFirstPage == "Weight Loss Program, Recipes & Help | Weight Watchers"):
            print("Test 1 Passed")
        else:
            print("Test 1 FAILED")
        driver.find_element_by_id("ela-menu-visitor-desktop-supplementa_find-a-meeting").click()
        titleOfPage = driver.title
        print(titleOfPage)
        if(titleOfPage == "Get Schedules & Times Near You"):
            print("Test 2 Passed")
        else:
            print("Test 2 FAILED")
        driver.find_element_by_id("meetingSearch").click()
        driver.find_element_by_id("meetingSearch").clear()
        driver.find_element_by_id("meetingSearch").send_keys("10011")
        driver.find_element_by_id("ela-mfsr:mf-find-btn").click()
        #driver.find_element_by_name("mfsearch").submit()
        result1 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Please enter a valid city and state or zip code'])[1]/following::span[1]").text
        print("First Result is", result1)
        result2 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Please enter a valid city and state or zip code'])[1]/following::span[1]/following::div[1]").text
        print("Distance of First result is", result2)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Please enter a valid city and state or zip code'])[1]/following::span[1]").click()
        result3 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Report a map error'])[1]/following::span[1]").text
        print(result3)
        if(result1 == result3):
            print("Test 3 Passed")
        else:
            print("Test 3 FAILED")
        k2 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Hours of Operation'])[1]/following::div[4]").text
        print(k2)
        l2 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Hours of Operation'])[1]/following::div[4]/following::div[2]").text
        #l2 = driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sunday'])[1]/following::div[2]").text
        print(l2)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
