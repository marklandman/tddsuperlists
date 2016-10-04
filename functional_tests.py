from selenium import webdriver
import time

#newprof = webdriver.FirefoxProfile()
browser = webdriver.Firefox() #newprof)
#time.sleep(5)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
