from behave import given, when, then

@given("I create a new user")
def create_new_user(context):
    """
    Step to create a new user
    :param context:
    :return:
    """
    print("I am creating a new user")

@when("I type email")
def create_new_user(context):
    """
    Step to type email address in the email field
    :param context:
    :return:
    """
    print("Typing the email in the email field")

@when("I type password")
def create_new_user(context):
    """
    Step to type email address in the password field
    :param context:
    :return:
    """
    print("Typing the password in the password field")

@when("I click on 'Login'")
def create_new_user(context):
    """
    Step to click login
    :param context:
    :return:
    """
    print("I am clicking login")

@then("I should see the text Welcome")
def create_new_user(context):
    """
    Step to see Welcome text
    :param context:
    :return:
    """
    print("I see Welcome text")