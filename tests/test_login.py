from definitions.login_page import LoginPage
from utilities import *

print("---------- Test Automation Scenario Sample ------------------------")
data = load_yaml_file(f"../data/config.yml")
uname = data['username']
passwrd = data['password']
inv_passwrd = data['inv_passwrd']
url = data['url']

print("# scenario1: login to the website")

login_page = LoginPage()

login_page.enter_username(uname)
login_page.enter_password(passwrd)
login_page.click_login()

assert login_page.verify_welcome_message(uname), print("Assert Failed!!! :( ")
print("---- scenario 1 is completed -----")

print("----------------------------------")
print("# scenario2: Invalid password")
login_page.enter_username(uname)
login_page.enter_password(inv_passwrd)
login_page.click_login()

assert login_page.verify_error_message(), print(" error message Assert Failed!!! :( ")
print("---- scenario 2 is completed -----")
