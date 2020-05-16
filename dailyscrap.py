# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
import json
from ds_functions import *
from ds_personal_functions import *

# Creater Driver based on Google Chrome
chromedriver = "Google Drive/Python/DailyScraping/chromedriver"
chromeOptions = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chromeOptions)

# Read searches.json. This file contains user informed functions and parameters to call
with open('searches.json') as f:
    data = json.load(f)

# Run web scrap!
for key in list(data): # Iterates over searches.json keys
    try:
        inputs = data[key]
        locals()[key](inputs, driver) # activates and runs a function with the same name as the key and uses the values as input
    except:
        print("Feature '{}' not implemented") # in case something goes wrong...
        
# Closes the Driver
driver.close()