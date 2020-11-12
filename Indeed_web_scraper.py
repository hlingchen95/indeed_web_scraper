from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import math
from datetime import datetime, timedelta

<<<<<<< HEAD
PATH = "/Users/huilingchen/Desktop/GA/chromedriver"
driver = webdriver.Chrome(PATH)
=======
# PATH = "/Users/huilingchen/Desktop/GA/chromedriver"
# driver = webdriver.Chrome(PATH)

driver = webdriver.Chrome(executable_path=r'C:\Users\li1\Documents\work\indeed_web_scraper\chromedriver.exe')
>>>>>>> 121b74904a8962436cca38f078941f68c9d111d9

driver.get("https://www.indeed.com/")

initial_search_button = driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
initial_search_button.click()

advanced_search = driver.find_element_by_xpath("//a[contains(text(),'Advanced Job Search')]")
advanced_search.click()

#search analyst 
search_job = driver.find_element_by_xpath('//input[@id="as_and"]')
search_job.send_keys(['Analyst'])

#search location 
searchLocation = driver.find_element_by_xpath('//input[@id="where"]')
searchLocation.clear()
searchLocation.send_keys("Columbus,OH")

#set display limit of 20 results per page
display_limit = driver.find_element_by_xpath('//select[@id="limit"]//option[@value="50"]')
display_limit.click()
#sort display with date
display_sort = driver.find_element_by_xpath('//select[@id="sort"]//option[@value="date"]')
display_sort.click()
#limited to 15 days
result_age = driver.find_element_by_xpath('//select[@id="fromage"]//option[@value="15"]')
result_age.click()

driver.implicitly_wait(3) 

<<<<<<< HEAD
search_button = driver.find_element_by_xpath('//*[@id="fj"]')
search_button.click()

=======
# push search button
search_button = driver.find_element_by_xpath('//*[@id="fj"]')
search_button.click()

# close pup up table
>>>>>>> 121b74904a8962436cca38f078941f68c9d111d9
search_button = driver.find_element_by_xpath('//*[@id="popover-x"]')
search_button.click()

driver.implicitly_wait(3) 

search_count = driver.find_element_by_xpath('//div[@id="searchCount"]').text
pages = math.ceil(int(search_count[10:13])/50)

titles=[]
companies=[]
links=[]
salaries = []
locations=[]
descriptions=[]
dates=[]

<<<<<<< HEAD
for i in range(0,pages):
=======
<<<<<<< HEAD:.ipynb_checkpoints/Indeed_web_scraper-checkpoint.py
for i in range(0,1):
=======
for i in range(0,pages):
>>>>>>> 121b74904a8962436cca38f078941f68c9d111d9:Indeed_web_scraper.py
>>>>>>> 121b74904a8962436cca38f078941f68c9d111d9
    
    job_card = driver.find_elements_by_xpath('//div[contains(@class,"clickcard")]')
    
    for job in job_card:
    

        #Title    
        try:
            title  = job.find_element_by_xpath('.//h2[@class="title"]//a').text
        except:
            title = job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="title")
        titles.append(title)   

        #link
        links.append(job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="href"))
        #company
        companies.append(job.find_element_by_xpath('.//span[@class="company"]').text)

        # salary
        try:
            salary = job.find_element_by_xpath('.//span[@class="salaryText"]').text
        except:
            salary = "None"
        
        salaries.append(salary)

        # location    
        try:
            location = job.find_element_by_xpath('.//span[contains(@class,"location")]').text
        except:
            location = "None"

        locations.append(location)

        #date posted
        try:
            date = job.find_element_by_xpath('.//span[@class="date "]').text
            word_list = date.split()

            if word_list[0].isdigit():
                num = int(word_list[0])
                new_date_prior =  datetime.now() - timedelta(days = num)
                date = new_date_prior.strftime("%m/%d/%Y")
            elif word_list[0] == '30+':
                new_date_prior = datetime.now()-timedelta(days=30)
                date = new_date_prior.strftime("%m/%d/%Y")+" prior"
            else:
                date = datetime.now().strftime("%m/%d/%Y")
        except:
            date = "None"

        dates.append(date)

    #Flip to next page
    try:
        next_page = driver.find_element_by_xpath('//a[@aria-label={}]//span[@class="pn"]'.format(i+2))
        next_page.click()
    except:
        next_page = "None"

    print("Page: {}".format(str(i+2)))  

# Despcriptions
for link in links:
    try:
        driver.get(link)
        jd = driver.find_element_by_xpath('//div[@id="jobDescriptionText"]').text
    except:
        jd = "None"

    descriptions.append(jd)


df_da=pd.DataFrame()
df_da['Title']=titles
df_da['Company']=companies
df_da['Location']=locations
df_da['Link']=links
df_da['Salary']=salaries
df_da['Date']=dates
df_da['Description']=descriptions

<<<<<<< HEAD
filename = datetime.now().strftime("%m_%d_%Y") + ".pkl"
df_da.to_pickle(filename)
=======
filename = datetime.now().strftime("%m_%d_%Y")
df_da.to_feather(filename)
>>>>>>> 121b74904a8962436cca38f078941f68c9d111d9
#b = pd.read_pickle("result.pkl")
#print(b)

driver.close()

