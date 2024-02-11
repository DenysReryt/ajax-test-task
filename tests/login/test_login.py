import pytest 
import logging
from appium.webdriver.common.appiumby import AppiumBy


# Setup logging
logging.basicConfig(filename='tests/log/pytest.log', level=logging.INFO, format='%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)')
logger = logging.getLogger(__name__)


@pytest.mark.parametrize('email, password, expected_result', [
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', True),
    ('qa.ajax.app.automation@gmail.com', '', False),
    ('qa.ajax.app.automation@gmail.com', '1', False),
    ('', 'qa_automation_password', False),
    ('qa.ajax.app.gmail.com', 'qa_automation_password', False),
])
def test_login(user_login_fixture, email, password, expected_result):
    login = user_login_fixture
    
    logger.info(f'Starting test for {email} and {password}')
    
    assert login.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/authHelloLogin')
    assert login.login_button()

    assert login.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/authLoginEmail')
    assert login.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/authLoginPassword')
    
    assert login.enter_login_data(email=email, password=password)
    assert login.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/authLogin')
    
    if expected_result:
        assert login.confirm_login()
        logger.info(f'Login successful for {email} and {password}')
    else:
        assert not login.confirm_login()
        logger.warning(f'Login failed for {email} and {password}')
        
    logger.info(f'Test completed for {email} and {password}')
