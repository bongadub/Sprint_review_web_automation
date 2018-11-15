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
        self.logger.debug("\nAtempting to open the page")
        self.driver.get('{}/login'.format(self.config.get('Test', 'url')))
        return self

    def wait_until_loaded(self):
        self.username.wait_until_visible()
        return self

    def login(self, user):
        try:
            self.logger.debug("Login with user '%s'", user['username'])
            self.username.text = user['username']
            self.password.text = user['password']
            self.logger.debug("\nAtempting to click login button")
            self.login_button.click()
            time.sleep(3)

            return True
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None
    
    def hover(self):
        try:
            self.hover_dresses = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
            self.hover_over = ActionChains(self.driver).move_to_element(self.hover_dresses).perform()
            time.sleep(3)

            self.select_dress = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/ul/li[3]/a')
            self.hover = ActionChains(self.driver).move_to_element(self.select_dress).click(self.select_dress).perform()
            self.driver.execute_script("window.scrollTo(0,700, document.body.scrollHeight)")
            time.sleep(3)

            return True
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None

    def add_item(self):
        try:
            self.select_item = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img')
            # self.debug("\nAdding new item")
            self.hover = ActionChains(self.driver).move_to_element(self.select_item).perform()
            self.add_to_cart = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]').click()
            time.sleep(3)

            return True
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None

    def checkout(self):
        try:
            self.checkout_btn = self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a').click()
            self.driver.execute_script("window.scrollTo(0,500, document.body.scrollHeight)")

            self.cart_summary = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]').click()
            self.driver.execute_script("window.scrollTo(0,500, document.body.scrollHeight)")

            self.address_btn = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/form/p/button').click()
            self.driver.execute_script("window.scrollTo(0,300, document.body.scrollHeight)")
            self.shipping_btn = self.driver.find_element(By.XPATH, '//*[@id="cgv"]').click()

            self.shipping_btn2 = self.driver.find_element(By.XPATH, '//*[@id="form"]/p/button').click()
            self.driver.execute_script("window.scrollTo(0,300, document.body.scrollHeight)")

            self.pay_method = self.driver.find_element(By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a').click()
            self.confirm_order = self.driver.find_element(By.XPATH, '//*[@id="cart_navigation"]/button').click()
            time.sleep(5)

            return True
        except NoSuchElementException:
            self.auto_log("error", "Element {} does not exist".format(element))
            return None