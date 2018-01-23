from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import logging
import sys
from nose.tools import *
import unittest




driver = webdriver.Chrome()

def setup(self):
    print ("TestUM:setup() before each test method")
 
def teardown(self):
    print ("TestUM:teardown() after each test method")
 
@classmethod
def setup_class(cls):
    print ("setup_class() before any methods in this class")

def TestLogin():
    driver.get("http://52.9.78.11:3000/start")
    time.sleep(3)
    driver.find_element_by_id("email").send_keys("manu@celestialsys.com")
    time.sleep(3)
    driver.find_element_by_id("password").send_keys("12345678")
    time.sleep(3)
    driver.find_element_by_id("loginButton").click()
    time.sleep(4)
    driver.find_element_by_id("home")
    time.sleep(4)
    
    driver.close()
