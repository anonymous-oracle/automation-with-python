from selenium import webdriver  # imports webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime
import os
import sys

# creating the script as an executable
"""
pyinstaller --onefile project2-web-scraping-and-web-automation.py - command for creating the python executable 
"""
application_path = os.path.dirname(sys.executable) # getting the path of the executable that will be created

formatted_timestamp = datetime.now().strftime("%d%m%Y") #DDMMYYYY

# for using safari
# browser = webdriver.Safari()

print("""
===========================IMPORTANT===========================
|   DOWNLOAD CHROMEDRIVER TO THE SAME PATH AS THE EXECUTABLE   |
===============================================================
""")

# setting headless mode
options = Options()
options.headless = True

URL = 'https://www.thesun.co.uk/sport/football/'
CHROME_WEBDRIVER_PATH = "./chromedriver"

# creating the chrome driver
service = Service(CHROME_WEBDRIVER_PATH)
browser = webdriver.Chrome(service=service, options=options)

# running the browser
browser.get(URL)

titles = []
subtitles = []
links = []

# selecting elements using xpath
containers = browser.find_elements(by='xpath', value="""//div[@class="teaser__copy-container"]""")
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text  # to select the element in the current context
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# creating a CSV with pandas
my_dict = {'titles': titles, 'subtitles': subtitles, 'links': links}
CSV_EXPORT_PATH = os.path.join(application_path, f"headlines_{formatted_timestamp}.csv")
pd.DataFrame(my_dict).to_csv(CSV_EXPORT_PATH)



browser.quit()
