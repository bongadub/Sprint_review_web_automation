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

from pageobjects.registration import RegistrationPageObject


@given('home page is opened')
def step_impl(context):
    context.current_page = RegistrationPageObject()
    assert context.current_page.open()

@when('user enters email address and clicks the create account button')
def step_impl(context):
	context.current_page = RegistrationPageObject()
	assert context.current_page.create_account()


@when('fills in user registration form')
def step_impl(context):
	context.current_page = RegistrationPageObject()
	assert context.current_page.personal_info()
    