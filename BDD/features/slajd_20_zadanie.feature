@slajd_20
Feature: User Login

  Scenario: Successful login for user testestesttest
        Given I am on log in page
        When I fill email field with testestesttest@cazlq.com data
        And I fill password field with razdwatrzy123 data
        And I click on 'Login' button
        Then testestesttest is visible on account page

  Scenario: Login with wrong username
        Given I am on log in page
        When I fill email field with hhhegl@cazlq.com data
        And I fill password field with Start123#111 data
        And I click on 'Login' button
        Then error: 'A user could not be found with this email address.' is visible on login page

  Scenario: Login with wrong password
        Given I am on log in page
        When I fill email field with testestesttest@cazlq.com data
        And I fill password field with Start123#111 data
        And I click on 'Login' button
        Then error: 'The password you entered for the username testestesttest@cazlq.com is incorrect. Lost your password?' is visible on login page

 Scenario: Login without email
        Given I am on log in page
        When I fill password field with Start123#111 data
        And I click on 'Login' button
        Then error: 'Username is required.' is visible on login page

 Scenario: Login without password
        Given I am on log in page
        When I fill email field with testestesttest@cazlq.com data
        And I click on 'Login' button
        Then error: 'The password field is empty.' is visible on login page

