import subprocess
import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.android_utils import android_get_desired_capabilities


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(3)


@pytest.fixture
def driver(run_appium_server):
    capabilities = android_get_desired_capabilities()
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote('http://localhost:4723', options=capabilities_options)
    yield driver
    driver.quit()
    
