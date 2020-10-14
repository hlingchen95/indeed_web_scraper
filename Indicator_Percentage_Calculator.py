from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import math
from datetime import datetime, timedelta
import pickle
import re

#read in datesets from source file
source_filename = datetime.now().strftime("%m_%d_%Y") + ".pkl"
b = pd.read_pickle(source_filename)

#Add indicators R, SAS, excel, python, sql
df = pd.DataFrame(b)
df['SAS'] = np.where(b['Description'].str.contains('SAS'), 'True','False')
df['python'] = np.where(b['Description'].str.contains('python', flags=re.IGNORECASE),'True','False')
df['SQL'] = np.where(b['Description'].str.contains('spl', flags=re.IGNORECASE),'True','False')
df['R'] = np.where(b['Description'].str.contains(' R '),'True','False')
df['excel'] = np.where(b['Description'].str.contains('excel', flags=re.IGNORECASE),'True','False')

#output result with indicators to new pickle file
filename = datetime.now().strftime("%m_%d_%Y") + "_with_indicators.pkl"
b.to_pickle(filename)

#reads pickle file with indicators
c = pd.read_pickle(filename)

#create appearence freqency percentage chart
df_da = pd.DataFrame()
df_da['sas_percentage'] = c['SAS'].value_counts(normalize=True) * 100 
df_da['python_percentage'] = c['python'].value_counts(normalize=True) * 100 
df_da['excel_percentage'] = c['excel'].value_counts(normalize=True) * 100 
df_da['R_percentage'] = c['R'].value_counts(normalize=True) * 100 
df_da['sql_percentage'] = c['SQL'].value_counts(normalize=True) * 100 

#prints appearence freqency percentage table
print("Percentage of appearence for tools:\n", df_da)