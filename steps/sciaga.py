from assertpy import assert_that

from behave import given, then, when

import page_objects.login_page as login_page

# logowanie na strobnie
'''

####    LOGOWANIE NA STRONIE:

context.page = login_page.LoginPage(context.driver)


####    WYPEŁNIANIE POLA EMAIL Z PRZEKAZANMIEM EMAIL MIEDZY STEPAMI

context.page.email_field.get_when_visible().send_keys(context.page.user_email)


####    WYPEŁANIANIE POLA PASSWORD Z PRZEKAZANMIEM HASLA MIEDZY STEPAMI
context.page.password_field.get_when_visible().send_keys(context.page.user_password)


####    KLIKANIE W BUTTON 'LOGIN'

context.page.login_button.get_when_clickable().click()



####    SPRAWDZENIE CZY UZYTKOWNIK ZOSTAL PRZEKIEROWANY NA WLASCIWA STRONE Z PRZEKAZANMIEM DANYCH MIEDZY STEPAMI

(assert_that(context.page.account_name.get_when_visible().text)
     .described_as("Check if redirected to account page")
     .contains(context.page.user_name))



####    WERYFIKACJA POLA HASLA, WYSWIETLANIE INFORMACJI ZE POLE JEST PUSTE

(assert_that(context.page.empty_password_error.get_when_visible()[1].text)
     .described_as("Checking correctness of information")
     .contains("Pole hasła jest puste. Wypełnij je."))



####    EXECUTE STEPS: DWA KROKI W JEDNYM: WYPELNIENIAE POLA EMAIL I HASLA

    context.execute_steps(
        f"""
        When I fill email field with {user_email} data
        When I fill password field with {user_password} data
        """)



####    WYPEŁNIANIE POLA EMAIL:

context.page.email_field.get_when_visible().send_keys(email)



####    WYPEŁNIANIE POLA HASLA:

context.page.password_field.get_when_visible().send_keys(password)


####    SPRAWDZENIE CZY UZYTKOWNIK ZOSTAL PRZEKIEROWANY NA WLASCIWA STRONE

@then("{username} is visible on account page")
def assert_username(context, username):
context.user_name = username
assert_that(context.page.account_name.get_when_visible().text).described_as("Check if redirected to account page").contains(username)



####    SPRAWDZENIE CZY UZYTKOWNIK ZOSTAL PRZEKIEROWANY NA WLASCIWA STRONE

(assert_that(context.page.account_name.get_when_visible().text).described_as("Check if redirected to account page").contains(context.user_name))


####     WERYFIKACJA POJAWIENIA SIE ERRORA
(assert_that(context.page.error_name.get_when_visible().text).described_as("Check if error is visible").contains(error_text))


'''