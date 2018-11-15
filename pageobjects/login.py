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

from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.message import MessagePageObject
from pageobjects.secure_area import SecureAreaPageObject
import time

class LoginPageObject(PageObject):

    def init_page_elements(self):
        self.username = InputText(By.ID, 'email')
        self.password = InputText(By.ID, 'passwd')
        self.login_button = Button(By.ID, 'SubmitLogin')
        self.message = MessagePageObject()

    def open(self):
        try:
            self.logger.debug("\nAtempting to open the page")
            self.driver.get('{}/login'.format(self.config.get('Test', 'url')))

            return True
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None

    def wait_until_loaded(self):
        try:
            self.username.wait_until_visible()

            return True
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None

    def login(self, user):
        try:
            self.logger.debug("Login with user '%s'", user['username'])
            self.username.text = user['username']
            self.password.text = user['password']
            self.logger.debug("\nAtempting to click login button")
            self.login_button.click()
            time.sleep(3)

            return SecureAreaPageObject(self.driver_wrapper)
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None