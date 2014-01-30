Feature: Confirming that the Potluck Planning App functions correctly

    Scenario: check that users can get to the main page
        When I go to the party app
        Then I should see the homepage

    Scenario: check that users can create an event
        When I go to the party app
        And I input an event name
        And I select an event date
        And I click on create event
        Then I should see a blank event page with a unique url
