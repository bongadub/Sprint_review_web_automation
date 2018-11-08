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
        """ Open login url in browser

        :returns: this page object instance
        """
        self.logger.debug("\nAtempting to open the page")
        self.driver.get('{}/login'.format(self.config.get('Test', 'url')))

        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.username.wait_until_visible()
        return self

    def create_account(self):
        self.email = self.driver.find_element(By.XPATH, '//*[@id="email_create"]').send_keys('abc1141wwwe1335345@gmail.com')
        self.submit = Button(By.ID, 'SubmitCreate').click()

       
        time.sleep(3)
        return self

    def personal_info(self):
        self.radio = self.driver.find_element(By.XPATH, '//*[@id="id_gender1"]').click()
        self.first_name = self.driver.find_element(By.XPATH, '//*[@id="customer_firstname"]').send_keys('Sam')
        self.last_name = self.driver.find_element(By.XPATH, '//*[@id="customer_lastname"]').send_keys('Nyubatya')
        self.password = self.driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys('password')
        
        time.sleep(3)
        return self