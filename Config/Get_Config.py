from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import logging
import sys

def File_Output(i_param):
    file = open("F:/config.txt","r")
    with open("F:/config.txt","r") as f:
        config_list = f.readlines()

    element = i_param


    for text in config_list:
        if element in text:
            test = text.split("-")[1]
            return test.rstrip()