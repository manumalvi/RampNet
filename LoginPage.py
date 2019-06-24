import time

class LoginPage():
    '''
    This class consist the login Page functions, which are for user login.
    They are being called by the main class.
    '''

    def __init__(self,driver):
        self.driver = driver

        self.login_username_xpath = "/html/body/app-root/app-login/div/div/form/div[1]/div[1]/div[2]/input"
        self.login_password_xpath = "/html/body/app-root/app-login/div/div/form/div[1]/div[2]/div[2]/input"
        self.login_button         = "/html/body/app-root/app-login/div/div/form/div[2]/button"
        self.profile_logo_xpath = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/div[2]/img"
        self.logout_xpath = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/div[2]/div"


    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.login_username_xpath).clear()
        self.driver.find_element_by_xpath(self.login_username_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.login_password_xpath).clear()
        self.driver.find_element_by_xpath(self.login_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def profile_button(self):
        try:
            print("Clicking on Profile Button...")
            self.driver.find_element_by_xpath(self.profile_logo_xpath).click()
            print("Profile_button : Test PASS")
        except:
            print("profile_button : Test FAIL")

    def logout_button(self):
        try:
            print("Clicking on Logout Button...")
            self.driver.find_element_by_xpath(self.logout_xpath).click()
            print("logout_button : Test PASS")
        except:
            print("logout_button : Test FAIL")

    def invalid_username(self):
        driver = self.driver
        try:
            print("Entering invalid username and password....")
            time.sleep(2)
            self.enter_username("abc")
            time.sleep(2)
            self.enter_password("xyz")
            time.sleep(2)
            self.click_login_button()
            time.sleep(2)
            driver.switch_to.alert.accept()
            time.sleep(2)
            print("invalid_login : PASS")
        except:
            print("invalid_login : FAIL")
            raise
