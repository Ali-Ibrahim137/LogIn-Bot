# LogIn Bot
One day I was wondering how much users are careful in choosing their Passwords, A lot of sites allow you to put a weak password, so I wrote this script of code to parse users from some site and try to login using the most common passwords, I have chosen [Codeforces](https://codeforces.com/) to parse, using BeautifulSoup I parsed different pages to get the handles of different users, and then used selenium to try to login, I parsed 1000 handles, and I manged to login 2 times !!! I didn't mean any harm so I sent the users a message to warn them, and both of them changed their passwords.

# Selenium
Selenium is a web automation framework that can be used to automate website testing. Because Selenium starts a web-browser, it can do any task you would normally do on the web, you can use Selenium to make a simple bot and use it to open any web page, Register/Login in different sites, send E-mails ...
To start a web browser, the Selenium module needs a web driver, there are a lot of supported browsers.

### Selenium Installation
To start using selenium you need to install the selenium package using pip command:
> pip install selenium

Next you need to download the driver, you can check all the supported browsers [here](https://docs.seleniumhq.org/download/) chose the driver you want to work with,  I will be using geckodriver driver used with Firefox browser.
**Make sure it’s in your PATH.**

# BeautifulSoup
BeautifulSoup is a library that makes it easy to scrape information from web pages, Web scraping automatically extracts data from different web pages and presents this data in a format you can easily make sense of.
### BeautifulSoup Installation
To start using BeautifulSoup you need to install the BeautifulSoup Library using pip command:

> pip install BeautifulSoup4

