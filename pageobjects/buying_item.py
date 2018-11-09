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

class BuyingItemPageObject(PageObject):

    
    def init_page_elements(self):
        self.username = InputText(By.ID, 'email')
        self.password = InputText(By.ID, 'passwd')
        self.login_button = Button(By.ID, 'SubmitLogin')

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

    def login(self, user):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        self.logger.debug("Login with user '%s'", user['username'])
        self.username.text = user['username']
        self.password.text = user['password']
        self.logger.debug("\nAtempting to click login button")
        self.login_button.click()
        time.sleep(3)
    
    def hover(self):
        self.hover_dresses = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
        self.hover_over = ActionChains(self.driver).move_to_element(self.hover_dresses).perform()
        time.sleep(3)
        self.select_dress = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/ul/li[3]/a')
        self.hover = ActionChains(self.driver).move_to_element(self.select_dress).click(self.select_dress).perform()
        self.driver.execute_script("window.scrollTo(0,700, document.body.scrollHeight)")
        time.sleep(3)

    def add_item(self):
        self.select_item = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img')
        self.hover = ActionChains(self.driver).move_to_element(self.select_item).perform()
        self.add_to_cart = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]').click()
        time.sleep(3)