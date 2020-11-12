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


b = pd.read_pickle("09_29_2020_with_indicators.pkl")
print(b)






