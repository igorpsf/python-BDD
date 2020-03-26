# Example

Feature:

    Scenario:

        Given I have a new "DVD" in my cart
        And I have a new "BOOK" in my cart
        When I click on "Next"
        And I click on "Finish"
        Then I should see "success"

    Scenario:  Add 10 participants in the call

        Given I start a call with "10" participants