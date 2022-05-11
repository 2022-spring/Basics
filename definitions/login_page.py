class LoginPage:

    def enter_username(self, username):
        print(f"entering the username : {username}")
        # find element
        # enter the "username" in that element

    def enter_password(self, password):
        print(f"entering the password : {password}")
        # try:
        #     pass
        #     # find element
        #     # enter the "password" in that element
        # except (NoSuchElementFound, TimeoutError) as err:
        #     print("Element was not found by locator provided")

    def click_login(self):
        print("clicking the login")
        # find element
        # click on that element

    def verify_welcome_message(self, username):
        print(f"verifying the welcome message by username '{username}'")
        # find element
        # verify that element is visible
        result = True
        print(f"-- result is '{result}' ----")
        return result

    def verify_error_message(self):
        print(f"verifying the error message by username..")
        # find element
        # verify that element is visible
        result = True
        print(f"-- result is '{result}' ----")
        return result
