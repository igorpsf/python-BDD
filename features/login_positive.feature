Feature: Logging with valid credentials

    @login
    Scenario: User login succesfully

        Given I create a new user
        When I type email
        When I type password
        When I click on 'Login'
        Then I should see the text Welcome