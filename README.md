# Autotests for Ajax Systems 
### First of all, make sure you have made the correct settings for Appium:
Quickstart Appium - https://appium.io/docs/en/2.0/quickstart/
### Also in my case i used Android Studio to emulate Android device:
Android Studio - https://developer.android.com/studio/run/emulator
> **_Note:_** After installing Android Studio and setting up the device, you need to install [Ajax Systems App](https://play.google.com/store/apps/details?id=com.ajaxsystems) on your Android device
### To inspect element on the testing app i used Appium Inspector:
Appium Inspector - https://github.com/appium/appium-inspector/releases

## Preparing
### 1. Make env for your project 
```
python -m venv <name_env>
```
or
```
python3 -m venv <name_env>
```
### Then activate venv
```
.\<name_env>\Scripts\activate
```
### 2. Clone repo from github
```
git clone https://github.com/DenysReryt/ajax-test-task.git
```
### 3. Make setup 
```
pip install -e .
```
### 4. Prepare capabilities for Appium session 
#### In utils\android_utils.py change parameters that you will use for your device and app

## Starting
### In one terminal run appium
> **_Note:_** If you run only ```pytest```, you dont need to run appium (look in tests\conftest)
```
appium
```
### In other terminal run tests with pytest
```
pytest
```
