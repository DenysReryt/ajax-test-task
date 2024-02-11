import pytest 
import logging
from appium.webdriver.common.appiumby import AppiumBy
from framework.login_page import LoginPage


# Setup logging
logging.basicConfig(filename='tests/log/pytest.log', level=logging.INFO, format='%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)')
logger = logging.getLogger(__name__)


@pytest.mark.parametrize('by, value, expected_element_by, expected_element_value, expected_result', [
    (AppiumBy.ID, 'com.ajaxsystems:id/settings', AppiumBy.ID, 'com.ajaxsystems:id/toolbarTitle', True),
    (AppiumBy.ID, 'com.ajaxsystems:id/settings', AppiumBy.ID, '', False),
    (AppiumBy.ID, 'com.ajaxsystems:id/help', AppiumBy.ID, 'com.ajaxsystems:id/toolbarTitle', True),
    (AppiumBy.ID, 'com.ajaxsystems:id/logs', AppiumBy.ID, 'com.ajaxsystems:id/sendButton', True),
    (AppiumBy.XPATH, '//android.widget.Button', AppiumBy.ID, 'com.ajaxsystems:id/list', True),  
    (AppiumBy.ID, 'com.ajaxsystems:id/documentation_text', AppiumBy.ID, 'com.ajaxsystems:id/toolbarTitle', True),
    (AppiumBy.ID, 'com.ajaxsystems:id/build', AppiumBy.ID, 'com.ajaxsystems:id/snackbar', True)
])
def test_sidebar(user_login_fixture, by, value, expected_element_by, expected_element_value, expected_result):
    login = user_login_fixture
    
    logger.info(f'Starting test for {by}: {value}')
    
    # First try to login with email and password
    login_page = LoginPage(driver=login)
    login_page.login_button()
    login_page.enter_login_data(email='qa.ajax.app.automation@gmail.com', password='qa_automation_password')
    
    # Check if we can see and click on sidebar button
    assert login_page.confirm_login()
    
    ## Start to check elements of SideBar
    assert login.find_element(by=by, value=value)
    assert login.click_element(by=by, value=value)
    
    if expected_result:
        assert login.find_element(by=expected_element_by, value=expected_element_value)
        logger.info(f'Pass for {by}: {value}')
    else:
        logger.info(f'Failed - cant find element {by}: {value}')

