@slajd_21
Feature: User Login

  Scenario: Successful login for user testestesttest
        Given I am on log in page
        When I fill email field with testestesttest@cazlq.com data
        And I fill password field with razdwatrzy123 data
        And I click on 'Login' button
        Then testestesttest is visible on account page
        And context.user_name is shared between steps
