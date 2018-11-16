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

from behave import given, when, then
from pageobjects.buying_item import BuyingItemPageObject

@given('site home page is open')
def step_impl(context):
    context.current_page = BuyingItemPageObject()
    assert context.current_page.open()

@when('user logs with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    user = {'username': username, 'password': password}
    context.current_page = context.current_page.login(user)

@when('the user hovers over dresses and select dress choice')
def step_impl(context):
	context.current_page = BuyingItemPageObject()
	assert context.current_page.hover()

@when('the user add item to cart')
def step_impl(context):
	context.current_page = BuyingItemPageObject()
	assert context.current_page.add_item()

@then('the user checkout')
def step_impl(context):
	context.current_page = BuyingItemPageObject()
	assert context.current_page.checkout()
