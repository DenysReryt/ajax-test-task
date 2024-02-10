from setuptools import setup, find_packages

setup(
    name='ajax-test',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest==8.0.0',
        'appium-python-client==3.1.1'
    ],
)
