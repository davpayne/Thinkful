Feature: Confirming that the potluck app works

    Scenario: check that the homepage displays
        When I go to the potluck app
        Then I should see the potluck app

    Scenario: check that the form submits successfully
        When I go to the potluck app
        And I submit the form with a valid event name
        Then I should see the event page

    Scenario: check that the add item function works properly
        When I go to the event page
        And I submit the form with a valid event name
	And I submit a valid name and item name
        Then I should see the item displayed
	
    Scenario: check that items can be deleted
	When I got to the event page
	And I submit the form with a valid event name
	And I submit a valid name and item name
	And I click delete
	Then I should no longer see the item displayed