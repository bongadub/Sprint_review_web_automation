import selenium.webdriver.support.expected_conditions as WAITCON
import random
import string
import time
import inspect

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from toolium.pageelements import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from toolium.pageelements import InputText, Button
from toolium.pageobjects.page_object import PageObject

class RegistrationPageObject(PageObject):

    
    def open(self):
        self.logger.debug("\nAtempting to open the page")
        self.driver.get('{}/login'.format(self.config.get('Test', 'url')))

        return self

    def create_account(self):
        try:
            self.email = self.driver.find_element(By.XPATH, '//*[@id="email_create"]').send_keys('1b@gmail.com')
            self.submit = Button(By.ID, 'SubmitCreate').click()
            time.sleep(3)

            return True
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None

    def personal_info(self):
        try:
            self.radio = self.driver.find_element(By.XPATH, '//*[@id="id_gender1"]').click()
            self.first_name = self.driver.find_element(By.XPATH, '//*[@id="customer_firstname"]').send_keys('Sam')
            self.last_name = self.driver.find_element(By.XPATH, '//*[@id="customer_lastname"]').send_keys('Nyubatya')
            self.password = self.driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys('password')
            self.date = self.driver.find_element(By.XPATH, '//*[@id="days"]/option[@value=5]').click()
            self.month = self.driver.find_element(By.XPATH, '//*[@id="months"]/option[@value=5]').click()
            self.years = self.driver.find_element(By.XPATH, '//*[@id="years"]/option[@value=1995]').click()
            self.company = self.driver.find_element(By.XPATH, '//*[@id="company"]').send_keys('Company PTY (LTD')
            self.address = self.driver.find_element(By.XPATH, '//*[@id="address1"]').send_keys(' 1 street')
            self.city = self.driver.find_element(By.XPATH, '//*[@id="city"]').send_keys('City')
            self.state = self.driver.find_element(By.XPATH, '//*[@id="id_state"]/option[@value=11]').click()
            self.zip_code = self.driver.find_element(By.XPATH, '//*[@id="postcode"]').send_keys('90002')
            self.add_info = self.driver.find_element(By.XPATH, '//*[@id="other"]').send_keys('027 0010 0489')
            self.mobile_num = self.driver.find_element(By.XPATH, '//*[@id="phone_mobile"]').send_keys('073 4534 764')
            #self.register = self.driver.find_element(By.XPATH, '//*[@id="submitAccount"]').click()
            time.sleep(3)

            return True
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None