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

def TestLoginEWA_214():
    driver.get(Get_Config.File_Output('URL'))
    time.sleep(3)
    if (driver.find_element_by_id("password").getAttribute("type") == 'password'):
        assert_equals('password field works good','password field works good')
    else:
         assert_equals('password field','is not defined')
         
    time.sleep(3)
    driver.close()
