Feature: Network Service Deployment

  Scenario: List enterprises
    Given I have initialized the vsd service
    When  I query the enterprises
    Then  I get the enterprises

