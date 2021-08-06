# Created by shash at 8/6/2021
Feature: Create User Account
  Create a new user account

  Scenario: Verify a new user account is created
    Given User data is available
    When Post request is send to api url for account creation
    Then User account is created
    Then Verify the account username


  Scenario: Verify account is not created with already existing username
    Given User data is available
    When Post request is send to api url for account creation
    Then Verify User account is not created