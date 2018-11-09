# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
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


class SearchPageObject(PageObject):

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

        return self
        
       # return SecureAreaPageObject(self.driver_wrapper)

    def search(self):
        self.search_item = self.driver.find_element(By.XPATH, '//*[@id="search_query_top"]').send_keys('t-shirt')
        self.search_btn = self.driver.find_element(By.XPATH, '//*[@id="searchbox"]/button').click()
        time.sleep(3)

        return self

    def add_item(self):
        self.driver.execute_script("window.scrollTo(0, 200, document.body.scrollHeight)")
        self.item = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a')
        self.hover = ActionChains(self.driver).move_to_element(self.item).perform()
        self.add_btn = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/div[2]/a[2]').click()
        self.add_to_cart = self.driver.find_element(By.XPATH, '//*[@id="add_to_cart"]/button').click()
        time.sleep(3)

