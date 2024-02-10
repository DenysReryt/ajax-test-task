import pytest 
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.parametrize('email, password, expected_result', [
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', True),
    ('qa.ajax.app.automation@gmail.com', '', False),
    ('qa.ajax.app.automation@gmail.com', '1', False),
    ('', 'qa_automation_password', False),
    ('qa.ajax.app.gmail.com', 'qa_automation_password', False),
])
def test_login(user_login_fixture, email, password, expected_result):
    login = user_login_fixture
    
    assert login.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/authHelloLogin')
    assert login.login_button()

    assert login.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/authLoginEmail')
    assert login.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/authLoginPassword')
    
    assert login.enter_login_data(email=email, password=password)
    assert login.find_element(by=AppiumBy.ID, value='com.ajaxsystems:id/authLogin')
    
    if expected_result:
        assert login.confirm_login()
    else:
        assert not login.confirm_login()
