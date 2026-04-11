@slajd_26+6
Feature: User Login

  @login666
  Scenario Outline: slajd_26: Successful login for user: <user_name>
      Given I am on log in page
      And I accept cookies consent
      When I login with email "<user_email>" and password "<user_password>"
      And I click on 'Login' button
      Then "<user_name>" is visible on account page

  Examples:
    |user_email                     |user_password |user_name           |
    |hhheglgtvvtmkydmyw@cazlq.com   |Start123#111  |hhheglgtvvtmkydmyw  |
    |testestesttest@cazlq.com       |razdwatrzy123 |testestesttest      |



  @incorrect
  Scenario Outline:  Login with wrong password
        Given I am on log in page
        And I accept cookies consent
        When I fill email fild with '<user_email>' and pasword '<user_password>'
        And I click on 'Login' button
        Then login error "Your email or password is incorrect!" is visible
   Examples:
    |user_email                        |user_password |
    |hhheglgtvvtmkydmywqqq@cazlq.com   |Start123#111  |
    |testestesttestqqq@com.pl          |razdwatrzy123 |


