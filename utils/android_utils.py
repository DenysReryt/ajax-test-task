def android_get_desired_capabilities():
    return {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': 'Pixel 7 Pro API 33',
        'platformVersion': '13',
        'newCommandTimeout': 500,
        'udid': 'emulator-5554',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        'appPackage': 'com.ajaxsystems',
        'systemPort': 8301,
        'resetKeyboard': True,
        'noSign': True,
        'autoGrantPermissions': True,
        'takesScreenshot': True
}
