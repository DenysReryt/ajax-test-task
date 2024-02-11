import subprocess

def get_udid():
    '''
    By default using first device from list.
    '''
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
        devices = result.stdout.strip().split('\n')[1]
        if devices:
            udid = devices.split('\t')[0]
            return udid
        else:
            print("No devices found.")
            return None
    except subprocess.CalledProcessError as ex:
        print(f"Error executing 'adb devices': {ex}")
        return None
    

def android_get_desired_capabilities():
    return {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': 'Pixel 7 Pro API 33',
        'platformVersion': '13',
        'newCommandTimeout': 500,
        'udid': get_udid(),
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        'appPackage': 'com.ajaxsystems',
        'systemPort': 8301,
        'resetKeyboard': True,
        'noSign': True,
        'autoGrantPermissions': True,
        'takesScreenshot': True
}
