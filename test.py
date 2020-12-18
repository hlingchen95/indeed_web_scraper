from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = '/usr/bin/google-chrome'
driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
driver.get('http://www.google.com/')
