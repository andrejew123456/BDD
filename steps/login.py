from assertpy import assert_that

from behave import given, then, when

import page_objects.login_page as login_page


@given("I am on log in page")
def login(context):
    context.page = login_page.LoginPage(context.driver)


@when("I fill email field with correct data")
def step_impl(context):
    context.page.email_field.get_when_visible().send_keys(context.page.user_email)


@when("I fill password field with correct data")
def step_impl(context):
    context.page.password_field.get_when_visible().send_keys(context.page.user_password)


@when("I click on 'Login' button")
def step_impl(context):
    context.page.login_button.get_when_clickable().click()


@then("I am redirected to my account page")
def step_impl(context):
    (assert_that(context.page.account_name.get_when_visible().text)
     .described_as("Check if redirected to account page")
     .contains(context.page.user_name))


@then("I see information that password field is empty")
def step_impl(context):
    (assert_that(context.page.empty_password_error.get_when_visible()[1].text)
     .described_as("Checking correctness of information")
     .contains("Pole hasła jest puste. Wypełnij je."))

@when("I fill email field with: '{user_email}' and password field with: '{user_password}'")
def fill_email_password(context, user_email,  user_password):
    context.execute_steps(
        f"""
        When I fill email field with {user_email} data
        When I fill password field with {user_password} data
        """)

@when("I fill email field with {email} data")
def fill_email(context, email):
    context.page.email_field.get_when_visible().send_keys(email)


@when("I fill password field with {password} data")
def fill_password(context, password):
    context.page.password_field.get_when_visible().send_keys(password)

@then("{username} is visible on account page")
def assert_username(context, username):
    context.user_name = username
    (assert_that(context.page.account_name.get_when_visible().text)
     .described_as("Check if redirected to account page")
     .contains(username))


@then("context.user_name is shared between steps")
def sharing_data(context):
    (assert_that(context.page.account_name.get_when_visible().text)
     .described_as("Check if redirected to account page")
     .contains(context.user_name))


@then("error: '{error_text}' is visible on login page")
def step_impl(context, error_text):
    (assert_that(context.page.error_name.get_when_visible().text)
     .described_as("Check if error is visible")
     .contains(error_text))