from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import math
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )

#driver = webdriver.Chrome(executable_path='chromedriver')

driver.get("https://www.indeed.com/advanced_search")

driver.implicitly_wait(3)

# search analyst
search_job = driver.find_element_by_xpath('//input[@id="as_and"]')
search_job.send_keys(['analytics'])

# search location
searchLocation = driver.find_element_by_xpath('//input[@id="where"]')
searchLocation.clear()
# searchLocation.send_keys("united states")
searchLocation.send_keys("ohio")

# set display limit of 50 results per page
display_limit = driver.find_element_by_xpath(
    '//select[@id="limit"]//option[@value="50"]')
display_limit.click()
driver.implicitly_wait(3)

# sort display with date
display_sort = driver.find_element_by_xpath(
    '//select[@id="sort"]//option[@value="date"]')
display_sort.click()
driver.implicitly_wait(3)

# limited to 1 day
result_age = driver.find_element_by_xpath(
    '//select[@id="fromage"]//option[@value="1"]')
result_age.click()

# location
result_age = driver.find_element_by_xpath(
    '//select[@id="radius"]//option[@value="0"]')
result_age.click()

driver.implicitly_wait(3)

# push search button
search_button = driver.find_element_by_xpath('//*[@id="fj"]')
search_button.click()
driver.implicitly_wait(3)

# Get exact search result amount
search_count = driver.find_element_by_xpath('//div[@id="searchCount"]').text

def sub_str(s, start, end):
    return s[s.find(start)+len(start):s.rfind(end)]
num = sub_str(search_count, "of ", " jobs")
pages = math.ceil(int(num.replace(',', ''))/50)

print(datetime.now().strftime("%m_%d_%Y"))
print("total pages: ", pages)

titles = []
links = []
dates = []

driver.implicitly_wait(3)

try:
    all_page = driver.find_element_by_xpath("//a[contains(., 'repeat your search with the omitted job postings included')]")
    driver.execute_script("arguments[0].click();", all_page)
    print("get all job postings")
except:
    print("no omitted job postings ")


for i in range(0, pages):
    
    job_card = driver.find_elements_by_xpath(
        '//div[contains(@class,"clickcard")]')
    
    print(len(job_card))
    for job in job_card:
        
        date = datetime.now().strftime("%m/%d/%Y")
        dates.append(date)
        try:
            title  = job.find_element_by_xpath('.//h2[@class="title"]//a').text
        except:
            title = job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="title")
        titles.append(title)   

        links.append(job.find_element_by_xpath(
            './/h2[@class="title"]//a').get_attribute(name="href"))
        

    print("Finish the page: {}.".format(str(i+1)))
    driver.implicitly_wait(3)
    if pages > 1:
        next_page = driver.find_elements_by_xpath("//span[@class='pn']")[-1]
        driver.execute_script("arguments[0].click();", next_page)
    
df = pd.DataFrame()
df['date'] = dates
df['title'] = titles
df['link'] = links

filename = datetime.now().strftime("Post_URL_"+"%m_%d_%Y")
df.reset_index().to_feather("./link/"+filename)

driver.quit()
