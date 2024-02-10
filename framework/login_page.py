from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from utils.android_utils import android_get_desired_capabilities
from page import Page


LOGIN_BUTTON = 'com.ajaxsystems:id/authHelloLogin'
EMAIL_BUTTON = 'com.ajaxsystems:id/authLoginEmail'
PASSWORD_BUTTON = 'com.ajaxsystems:id/authLoginPassword'
CONFIRM_BUTTON = 'com.ajaxsystems:id/authLogin'
CHECK_SIDEBAR = 'com.ajaxsystems:id/menuDrawer'

class LoginPage(Page):

    def login_button(self):
        try:
            self.click_element(by=AppiumBy.ID, value=LOGIN_BUTTON)
            return True
        except Exception as ex:
             print(f"Error clicking login button: {ex}")
             return False
        
    def enter_login_data(self, email, password):
        try:
            self.send_element(by=AppiumBy.ID, value=EMAIL_BUTTON, key=email)
            self.send_element(by=AppiumBy.ID, value=PASSWORD_BUTTON, key=password)
            return True
        except Exception as ex:
            print(f"Error with: {ex}")
            return False
    
    
    def confirm_login(self):
        try:
            self.click_element(by=AppiumBy.ID, value=CONFIRM_BUTTON)
            self.click_element(by=AppiumBy.ID, value=CHECK_SIDEBAR)
            return True
        except Exception as ex:
            print(f"Error with: {ex}")
            return False
        

if __name__ == '__main__':
    capabilities = android_get_desired_capabilities()

    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    login_page = LoginPage(driver=driver)
    login_page.login_button()
    login_page.enter_login_data(email='qa.ajax.app.automation@gmail.com', password='qa_automation_password')
    
    driver.quit()
