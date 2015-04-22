import re
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv
import os 
import urllib2
from pattern.web import URL
import mechanize
import requests
import urlparse


br = mechanize.Browser()
br._factory.is_html = True


browser = webdriver.Firefox()
# browser.maximize_window()

browser.get("http://trai.gov.in/Content/QosUser/1_QosUser.aspx")
lists= browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gv_Qos"]')
all_options = lists.find_elements_by_css_selector('a')
# print all_options
i = 0
for h in all_options:
	pdf_url =  h.get_attribute('href')
	request2 = br.retrieve(pdf_url, str(i)+'.pdf')[0]
	i += 1


# quarters = ['Jan-Mar','Apr-Jun', 'Jul-Sep','Oct-Dec']
# years = ['2015','2014','2013','2012','2011','2010','2009','2008','2007','2006']



# browser.find_element_by_id('ctl00_ContentPlaceHolder1_btnSubmit').click()
# # lists = browser.find_element_by_class_name('ctl00_ContentPlaceHolder1_gvPerformance_IndReport')
# lists= browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gvPerformance_IndReport"]')
# # lists = []
# # print lists
# all_options = lists.find_elements_by_css_selector('a')
# # print all_options
# for h in all_options:
# 	print h.get_attribute('href')
# for option in all_options:
# 	print option

# print div 
# print div.find_element_by_css_selector('a').get_attribute('href')

# self.driver.find_element_by_css_selector('.eventLink a').get_attribute('href')

# pdf_link = browser.find_element_by_link_text('The Indian Telecom Services Performance Indicator Report April - June 2014')


# pdf_url =  pdf_link.get_attribute('href')
# print pdf_url

# lists = browser.find_element_by_id('dr')
#                 all_options = lists.find_elements_by_tag_name('option')
#                 for option in all_options:
#                     if option.get_attribute('value') == 'Custom':
#                         option.click()