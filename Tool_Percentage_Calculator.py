import numpy as np
import pandas as pd
import math
from datetime import datetime, timedelta


#reads pickle file with indicators
c = pd.read_feather("/Users/huilingchen/Documents/GitHub/indeed_web_scraper/source_with_indicator/10_28_2020_with_indicators")

#create appearence freqency percentage chart
df_da = pd.DataFrame()
df_da['sas_percentage'] = c['SAS'].value_counts(normalize=True) * 100 
df_da['python_percentage'] = c['python'].value_counts(normalize=True) * 100 
df_da['excel_percentage'] = c['excel'].value_counts(normalize=True) * 100 
df_da['R_percentage'] = c['R'].value_counts(normalize=True) * 100 
df_da['sql_percentage'] = c['SQL'].value_counts(normalize=True) * 100 

#prints appearence freqency percentage table
print("Percentage of appearence for tools:\n", df_da)
