from behave import given, when, then, step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login_page import LoginPage


@step("pdb")
def step_impl(context):  # noqa: PLW613
    import pdb  # noqa: PLC415
    import sys  # noqa: PLC415

    pdb.Pdb(stdout=sys.__stdout__).set_trace()

@given("I am on log in page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.driver.get(context.login_page.page_url)


@given("I accept cookies consent")
def step_accept_cookies(context):
    try:
        wait = WebDriverWait(context.driver, 10)
        button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='Zgadzam się' or @aria-label='Agree']")
            )
        )
        context.driver.execute_script("arguments[0].click();", button)
    except Exception:
        pass


@when("I fill email field with correct data")
def step_fill_email(context):
    ##########
    # using POM
    context.login_page.email_field.get_when_visible().send_keys(context.login_page.user_email)

    #############
    #
    # wait = WebDriverWait(context.driver, 10)
    # email = wait.until(
    #     EC.visibility_of_element_located(
    #         (By.CSS_SELECTOR, "input[data-qa='login-email']")
    #     )
    # )
    # email.clear()
    # email.send_keys(context.login_page.user_email)


@when("I fill password field with correct data")
def step_fill_password(context):
    wait = WebDriverWait(context.driver, 10)
    password = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-qa='login-password']")
        )
    )
    password.clear()
    password.send_keys(context.login_page.user_password)


@when("I click on 'Login' button")
def step_click_login(context):
    wait = WebDriverWait(context.driver, 10)
    button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-qa='login-button']")
        )
    )
    context.driver.execute_script("arguments[0].click();", button)


@then("I am redirected to my account page")
def step_verify_logged_in(context):
    wait = WebDriverWait(context.driver, 10)

    logged_in = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(., 'Logged in as')]")
        )
    )

    actual_text = logged_in.text.strip()
    print(f"Logged in label text: {repr(actual_text)}")

    assert logged_in.is_displayed(), "Logged in label is not displayed"
    assert "Logged in as" in actual_text, f"Unexpected label text: {actual_text}"

@then('login error "{expected_error}" is visible')
def step_verify_login_error(context, expected_error):
    wait = WebDriverWait(context.driver, 10)
    error = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//form[contains(., 'Login')]//p")
        )
    )

    actual_error = error.text.strip()
    print(f"Actual login error: {repr(actual_error)}")

    assert expected_error == actual_error, (
        f"Expected error '{expected_error}', but got '{actual_error}'"
    )


@then("email field validation message is visible")
def step_verify_email_required_validation(context):
    email_input = context.driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")
    validation_message = context.driver.execute_script(
        "return arguments[0].validationMessage;", email_input
    )

    print(f"Email validation message: {repr(validation_message)}")
    assert validation_message.strip() != "", "Expected validation message for empty email field"


@then("password field validation message is visible")
def step_verify_password_required_validation(context):
    password_input = context.driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")
    validation_message = context.driver.execute_script(
        "return arguments[0].validationMessage;", password_input
    )

    print(f"Password validation message: {repr(validation_message)}")
    assert validation_message.strip() != "", "Expected validation message for empty password field"

@when('I fill email field with "{email}" data')
def step_fill_email(context, email):
    wait = WebDriverWait(context.driver, 10)
    email_input = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-qa='login-email']")
        )
    )
    email_input.clear()
    email_input.send_keys(email)


@when('I fill password field with "{password}" data')
def step_fill_password(context, password):
    wait = WebDriverWait(context.driver, 10)
    password_input = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-qa='login-password']")
        )
    )
    password_input.clear()
    password_input.send_keys(password)

@when('I login with email "{email}" and password "{password}"')
def step_login(context, email, password):
    wait = WebDriverWait(context.driver, 10)

    email_input = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-qa='login-email']")
        )
    )
    password_input = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[data-qa='login-password']")
        )
    )

    email_input.clear()
    email_input.send_keys(email)

    password_input.clear()
    password_input.send_keys(password)

@then('"{user_name}" is visible on account page')
def step_verify_user(context, user_name):
    wait = WebDriverWait(context.driver, 10)

    logged_in = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//a[contains(., 'Logged in as')]")
        )
    )

    actual_text = logged_in.text.strip()
    print(f"Logged in label: {repr(actual_text)}")

    assert "Logged in as" in actual_text, f"Unexpected label: {actual_text}"
    assert user_name.lower() in actual_text.lower(), (
        f"Expected '{user_name}' in '{actual_text}'"
    )


@step("I am on login page")
def login(context):
    context.login_page = LoginPage(context.driver)
    context.driver.get(context.login_page.page_url)


@step("I fill email fild with '{user_email}' and pasword '{user_password}'")
def step_fill_user(context, user_email, user_password):
    context.execute_steps(
        f"""
        When I fill email field with "{user_email}" data
        When I fill password field with "{user_password}" data
        """
    )