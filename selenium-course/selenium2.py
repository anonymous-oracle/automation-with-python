import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


options = Options()
# options.headless = True

chrome_driver_path = os.path.join(os.getcwd(), 'chromedriver')
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# DOWNLOAD AN ECLIPSE IDE SETUP PACKAGE
URL = 'https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2022-06/R/eclipse-inst-jre-mac64.dmg'

driver.get(URL)
driver.implicitly_wait(3)
download_button = driver.find_element(by=By.XPATH, value="//a[starts-with(@class, 'btn btn-warning')]")
download_url = download_button.get_attribute('href')
download_button.click() # clicks the download button and selenium quits the session before the download is completed






driver.quit()
