@slajd_26+6
Feature: User Login

  @login
  Scenario Outline: slajd_26: Successful login for user: <user_name>
        Given I am on log in page
        When I fill email field with: '<user_email>' and password field with: '<user_password>'
        And I click on 'Login' button
        Then <user_name> is visible on account page

  Examples:
    |user_email                     |user_password |user_name           |
    |hhheglgtvvtmkydmyw@cazlq.com   |Start123#111  |hhheglgtvvtmkydmyw  |
    |testestesttest@cazlq.com       |razdwatrzy123 |testestesttest      |