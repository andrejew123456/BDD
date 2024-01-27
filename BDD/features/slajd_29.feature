@slajd_29
Feature: User Login

"""  In order to access my personal account and individual features of the application
  As a registered user
  I want to be able to log into the application
"""

  Scenario: Successful login for user testestesttest
        Given I am on log in page
        When I fill email field with testestesttest@cazlq.com data
        And I fill password field with razdwatrzy123 data
        And I click on 'Login' button
        Then testestesttest is visible on account page

  Scenario: Successful login
        Given I am on log in page
        When I fill email field with hhheglgtvvtmkydmyw@cazlq.com data
        And I fill password field with Start123#111 data
        And I click on 'Login' button
        Then hhheglgtvvtmkydmyw is visible on account page
