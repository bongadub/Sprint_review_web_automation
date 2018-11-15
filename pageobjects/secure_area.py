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
import time
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.message import MessagePageObject


class SecureAreaPageObject(PageObject):
    def init_page_elements(self):
        self.message = MessagePageObject()
        self.logout_button = Button(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')

    def logout(self):
        try:
            from pageobjects.login import LoginPageObject
            self.logger.debug("\nAtempting to click logout button")

            self.logout_button.click()
            time.sleep(3)
            return LoginPageObject(self.driver_wrapper).wait_until_loaded()
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None