import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL='https://www.browserstack.com/users/sign_in'
options = Options()
# options.headless = True

chrome_driver_path = os.path.join(os.getcwd(), 'chromedriver')
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)

# explicitly wait
driver.implicitly_wait(3)

# demonstrate automated sign-in
username_element = driver.find_element(by=By.XPATH, value="//input[contains(@id, 'user_email_login')]")
password_element = driver.find_element(by=By.XPATH, value="//input[contains(@id, 'user_password')]")
sign_in_btn = driver.find_element(by=By.XPATH, value="//input[contains(@id, 'user_submit') and @type='submit']")
try: # may not always find a cookie reject button
    cookie_reject_button = driver.find_element(By.XPATH, "//button[@id='accept-cookie-notification-cross-icon']")
    cookie_reject_button.click() # always make sure to get the button in view by removing notifications; like
    # rejecting cookies in this case
except:
    pass
username_element.send_keys('deathbolt149@gmail.com') # enter username
password_element.send_keys('test123') # enter password


# the sign_in button may not be in view yet, so we need to scroll into view
# driver.execute_script('arguments[0].scrollIntoView', sign_in_btn)
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)', sign_in_btn)


sign_in_btn.click() # click to sign in

# # now to sign out
# sign_out_button = driver.find_element(By.XPATH, "//a[@title='Sign out' and @class='sign_out_link']")
# # parent_sign_out_button = sign_out_button.find_element(By.XPATH, '..')
# parent_sign_out_button = sign_out_button.parent
# parent_sign_out_button.click()
# sign_out_button.click()



driver.quit()