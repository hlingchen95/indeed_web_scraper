import numpy as np
import pandas as pd
import math
from datetime import datetime, timedelta
import re

#read in datesets from source file
source_filename = datetime.now().strftime("%m_%d_%Y")
b = pd.read_feather("/Users/huilingchen/Documents/GitHub/indeed_web_scraper/source/10_28_2020")

#Add indicators R, SAS, excel, python, sql
df = pd.DataFrame(b)
df['SAS'] = np.where(b['Description'].str.contains('SAS'), 'True','False')
df['python'] = np.where(b['Description'].str.contains('python', flags=re.IGNORECASE),'True','False')
df['SQL'] = np.where(b['Description'].str.contains('spl', flags=re.IGNORECASE),'True','False')
df['R'] = np.where(b['Description'].str.contains(' R | R,'),'True','False')
df['excel'] = np.where(b['Description'].str.contains('excel', flags=re.IGNORECASE),'True','False')

#output result with indicators to new pickle file
filename = datetime.now().strftime("%m_%d_%Y") + "_with_indicators"
b.to_feather("/Users/huilingchen/Documents/GitHub/indeed_web_scraper/source_with_indicator/10_28_2020_with_indicators")

