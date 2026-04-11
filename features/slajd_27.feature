@slajd_27
@run1234
Feature: User Login

  Scenario: slajd_27: Successful login for user testestesttest
        Given I am on log in page
        And I accept cookies consent
        When I fill email field with "testestesttest@cazlq.com" data
        And I fill password field with "razdwatrzy123" data
        And I click on 'Login' button
        Then "testestesttest" is visible on account page

  Scenario: slajd_27: Login with wrong username
        Given I am on log in page
        And I accept cookies consent
        When I fill email field with "hhhegl@cazlq.com" data
        And I fill password field with "Start123#111" data
        And I click on 'Login' button
        Then login error "Your email or password is incorrect!" is visible

  Scenario: slajd_27: Login with wrong password
        Given I am on log in page
        And I accept cookies consent
        When I fill email field with "testestesttest@cazlq.com" data
        And I fill password field with "Start123#111" data
        And I click on 'Login' button
        Then login error "Your email or password is incorrect!" is visible

 Scenario: slajd_27: Login without email
        Given I am on log in page
        And I accept cookies consent
        When I fill password field with "Start123#111" data
        And I click on 'Login' button
        Then error: 'Username is required.' is visible on login page

 Scenario: slajd_27: Login without password
        Given I am on log in page
        And I accept cookies consent
        When I fill email field with "testestesttest@cazlq.com" data
        And I click on 'Login' button
        Then error: 'The password field is empty.' is visible on login page

