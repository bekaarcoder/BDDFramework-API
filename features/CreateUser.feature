# Created by shash at 27-11-2020
Feature: User Creation
  # Enter feature description here

  @smoke @library
  Scenario: Verify if User is created
    Given User details is available which needs to be added
    When Add User Post API method is executed
    Then New user is successfully created

  @regression @library
  Scenario Outline: Verify if Users are created
    Given User <name> and <job> is available
    When Add User Post API method is executed
    Then New user is successfully created
    Examples:
      | name     | job       |
      | John Doe | Developer |
      | Jane Doe | Tester    |