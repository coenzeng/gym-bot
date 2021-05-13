#run command:
#python gym-booking-bot.py email password

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datetime
import os
import sys

options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

#print(os.environ.get("CHROMEDRIVER_PATH"))
#driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)

#function that scrolls to elements in the web page
def scrollTo(driver, element):
    driver.execute_script("""arguments[0].scrollIntoView({
            block: 'center',
            inline: 'center'
        });""", element)
    driver.execute_script("arguments[0].scrollIntoView();", element);
    return element

class Person():
    def __init__(self, email, password):
        self.email = email
        self.password = password

user = Person(sys.argv[1], sys.argv[2])

#path to chrome driver
PATH = "C:\Program Files (x86)\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://myfit4less.gymmanager.com/portal/login.asp")

email = scrollTo(driver, driver.find_element_by_id('emailaddress'))

#ENTER EMAIL
email.send_keys(user.email)
pw = scrollTo(driver, driver.find_element_by_id('password'))

#ENTER PASSWORD 
pw.send_keys(user.password)
login=scrollTo(driver, driver.find_element_by_id('loginButton'))     
login.click()

#change location (for testing purposes)
#scrollTo(driver, driver.find_element_by_id('btn_club_select')).click()
#scrollTo(driver, driver.find_element_by_id('club_0E64CA8C-388B-4CD8-B1D7-385369A15E7B')).click()   
#   

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
dayaftertomorrow = (today + datetime.timedelta(days=2)).strftime("%Y-%m-%d")
three_days_later = (today + datetime.timedelta(days=3)).strftime("%Y-%m-%d")

try:
    select_day=scrollTo(driver, driver.find_element_by_id('btn_date_select'))   
    select_day.click()
except NoSuchElementException:
    print("Gyms are closed!")  
    sys.exit()



try:
    driver.find_element_by_id("date_" + three_days_later).click()
except NoSuchElementException:
    driver.find_element_by_id("date_" + dayaftertomorrow).click()

booking = driver.find_element(By.XPATH, '//div[@data-slottime="at 7:00 PM"]')

clock = scrollTo(driver, booking)

clock.click()

driver.find_element_by_id("dialog_book_yes").click()
