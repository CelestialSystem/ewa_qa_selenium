from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from nose.tools import assert_raises
import time
import logging
import sys
from nose.tools import *
import unittest
from Config import Get_Config




driver = webdriver.Chrome()

def setup(self):
    print ("TestUM:setup() before each test method")
 
def teardown(self):
    print ("TestUM:teardown() after each test method")
 
@classmethod
def setup_class(cls):
    print ("setup_class() before any methods in this class")

def TestLoginEWA_207():
    driver.get(Get_Config.File_Output('URL'))
    time.sleep(3)
    driver.find_element_by_id("email").send_keys('invalid@celestialsys')
    time.sleep(3)
    driver.find_element_by_id("loginButton").click()
    time.sleep(4)
    element = driver.find_element_by_xpath("//div[@class='errorMsgField']//span") 
    assert_equals(element.text,Get_Config.File_Output('206_Incorrect_Email_Format')) 
    time.sleep(3)
    driver.close()
