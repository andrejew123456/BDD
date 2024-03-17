#Opis Zadania:
#Stwórz scenariusz BDD testujący funkcję logowania, która odrzuca próby logowania z nieprawidłowymi danymi. Scenariusz powinien zawierać definicje kroków w Gherkin oraz ich implementację w Pythonie przy użyciu frameworka Behave.
#błędny email
#błędne hasło
#brak email
#brak hasła
#
#Krok 1: Plik Feature Gherkin (logowanie.feature)
#Utwórz plik logowanie.feature w folderze features
#
#Krok 2: Implementacja Kroku w Pythonie (logowanie_steps.py)
#W folderze features/steps utwórz plik logowanie_steps.py z implementacjami kroków
#
#Krok 3: Uruchom testy jedna z podanych metod


@slajd_25
Feature: User Login

  Scenario: slajd_25: Successful login for user testestesttest
        Given I am on log in page
        When I fill email field with testestesttest@cazlq.com data
        And I fill password field with razdwatrzy123 data
        And I click on 'Login' button
        Then testestesttest is visible on account page

  Scenario: slajd_25: Login with wrong username
        Given I am on log in page
        When I fill email field with hhhegl@cazlq.com data
        And I fill password field with Start123#111 data
        And I click on 'Login' button
        Then error: 'A user could not be found with this email address.' is visible on login page

  Scenario: slajd_25: Login with wrong password
        Given I am on log in page
        When I fill email field with testestesttest@cazlq.com data
        And I fill password field with Start123#111 data
        And I click on 'Login' button
        Then error: 'The password you entered for the username testestesttest@cazlq.com is incorrect. Lost your password?' is visible on login page

 Scenario: slajd_25: Login without email
        Given I am on log in page
        When I fill password field with Start123#111 data
        And I click on 'Login' button
        Then error: 'Username is required.' is visible on login page

 Scenario: slajd_25: Login without password
        Given I am on log in page
        When I fill email field with testestesttest@cazlq.com data
        And I click on 'Login' button
        Then error: 'The password field is empty.' is visible on login page
