Feature:Order Transaction
  Tests related to oder Transactions

  Scenario Outline: Verify Order success message is shown in details page
    Given place the item order with <username> and <password>
    And user is on landing page
    When I login to portal with <username> and <password>
    And Navigate to order page
    And Select the OrderId
    Then Order message is successfully displayed
    Examples:
      | username              | password    |
      | rahulshetty@gmail.com | Iamking@000 |
      | anshika@gmail.com     | Iamking@000 |