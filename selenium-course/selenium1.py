import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# webdriver setup

def download_file_with_url(url, file_path=None):
    from requests import get
    response = get(url, stream=True)
    if not file_path:
        file_path=os.path.join(os.getcwd(), 'downloaded_file')
    with open(file_path, 'wb+') as f:
        for chunk in response.iter_content(chunk_size=4096):
            if chunk:
                f.write(chunk)

options = Options()
# options.headless = True

chrome_driver_path = os.path.join(os.getcwd(), 'chromedriver')
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# DOWNLOAD AN ECLIPSE IDE SETUP PACKAGE
URL = 'https://www.eclipse.org/downloads/download.php?file=/oomph/epp/2022-06/R/eclipse-inst-jre-mac64.dmg'

driver.get(URL)
driver.implicitly_wait(3) # wait 3 seconds for the slow connections to load the page fully and then proceed; this
# will also wait till the element is found and if found within the time duration, it will proceed with execution;
# also it will use the remaining time to find other elements as well present in the execution flow
download_button = driver.find_element(by=By.XPATH, value="//a[starts-with(@class, 'btn btn-warning')]")
download_url = download_button.get_attribute('href')
download_button.click() # clicks the download button and selenium quits the session before the download is completed

# waiting until the condition is met
WebDriverWait(driver=driver, 30).until(EC.text_to_be_present_in_element(
    # element filtration
    # The expected Text; for example wait till the text of a certain element changes into a desired value
)) # waits for 30 seconds until a condition is met


# download_file_with_url(download_url) # downloads through stream so that program waits to download the
# # # file completely






driver.quit()