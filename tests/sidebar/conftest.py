import pytest
from framework.login_page import LoginPage


@pytest.fixture(scope='function', autouse=True)
def user_login_fixture(driver):
    login = LoginPage(driver=driver)
    yield login
    