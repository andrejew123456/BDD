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

    @testowy1
    Scenario: slajd_25: Successful login
        Given I am on log in page
        And I accept cookies consent
        When I fill email field with correct data
        And I fill password field with correct data
        And I click on 'Login' button
        Then I am redirected to my account page

    Scenario: slajd_25: Login with wrong email
        Given I am on log in page
        And I accept cookies consent
        When I fill email field with "wrong@email.com" data
        And I fill password field with "Start123" data
        And I click on 'Login' button
        Then login error "Your email or password is incorrect!" is visible

    Scenario: slajd_25: Login without email
        Given I am on log in page
        And I accept cookies consent
        When I fill password field with "Start123" data
        And I click on 'Login' button
        Then email field validation message is visible

    Scenario: slajd_25: Login without password
        Given I am on log in page
        And I accept cookies consent
        When I fill email field with "iwona123@wp.pl" data
        And I click on 'Login' button
        Then password field validation message is visible
