@slajd_34
Feature: User Login

  @login @critical
  Scenario Outline: slajd_34: Successful login for user <user_name>
        Given I am on log in page
        When I fill email field with <user_email> data
        And I fill password field with <user_password> data
        And I click on 'Login' button
        Then <user_name> is visible on account page

  Examples:
    |user_email                     |user_password |user_name           |
    |hhheglgtvvtmkydmyw@cazlq.com   |Start123#111  |hhheglgtvvtmkydmyw  |
    |testestesttest@cazlq.com       |razdwatrzy123 |testestesttest      |