from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd

# PATH = "/Users/huilingchen/Desktop/GA/chromedriver"
# driver = webdriver.Chrome(PATH)

driver = webdriver.Chrome(executable_path=r'C:\Users\li1\Documents\work\indeed_web_scraper\chromedriver.exe')

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

#set display limit of 50 results per page
display_limit = driver.find_element_by_xpath('//select[@id="limit"]//option[@value="50"]')
display_limit.click()

# push search button
search_button = driver.find_element_by_xpath('//*[@id="fj"]')
search_button.click()

# close pup up table
search_button = driver.find_element_by_xpath('//*[@id="popover-x"]')
search_button.click()

driver.implicitly_wait(3) 

titles=[]
companies=[]
links=[]
salaries = []
locations=[]
descriptions=[]

for i in range(0,1):
    
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

    #Flip to next page
    try:
        next_page = driver.find_element_by_xpath('//a[@aria-label={}]//span[@class="pn"]'.format(i+2))
        next_page.click()
    except:
        next_page = "None"

    print("Page: {}".format(str(i+2)))  

# Despcriptions
for link in links:
    
    driver.get(link)
    jd = driver.find_element_by_xpath('//div[@id="jobDescriptionText"]').text
    descriptions.append(jd)


df_da=pd.DataFrame()
df_da['Title']=titles
df_da['Company']=companies
df_da['Location']=locations
df_da['Link']=links
df_da['Salary']=salaries
df_da['Description']=descriptions

df_da.to_csv("result.csv")

