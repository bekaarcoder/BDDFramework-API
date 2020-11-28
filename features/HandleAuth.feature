# Created by shash at 28-11-2020
Feature: Handle Authentication
  # Enter feature description here

  Scenario: Request github repositories for the user
    Given request url and user credentials are available
    When I send the request to github api
    Then User repos are return successfully and status code is 200