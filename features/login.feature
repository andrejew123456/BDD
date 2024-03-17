@login
Feature: User Login

#"""  In order to access my personal account and individual features of the application
#  As a registered user
#  I want to be able to log into the application
#"""
#  Background: User is on the Login Page
#    Given The user is on the login page

#  @login
  Scenario: login: Successful login
        Given I am on log in page
        When I fill email field with correct data
        And I fill password field with correct data
        And I click on 'Login' button
        Then I am redirected to my account page

#    Scenario: Unuccessful login
#        Given I am on log in page
#        When I fill email field with correct data
#        And I fill password field with correct data
##        And I click on 'Login' button
#        Then I am redirected to my account page
#
#  Scenario: Unsuccessful login due to incorrect credentials
#    When The user enters an incorrect username or password
#    Then The user receives an error message about login failure
#
#  Scenario: Attempt to login without entering credentials
#    When The user does not enter any username or password
#    And The user clicks the login button
#    Then The user receives a message requiring them to enter login credentials
