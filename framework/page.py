from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver


    def find_element(self, by, value):
        '''
        Find an element based on the provided 'by' and 'value'.
        '''
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            return False


    def click_element(self, by, value):
        '''
        Click on an element based on the provided 'by' and 'value'.
        '''
        element = self.find_element(by=by, value=value)
        if element:
            element.click()
        else:
            raise NoSuchElementException()
        
        
    def send_element(self, by, value, key):
        '''
        Send keys to an element based on the provided 'by' and 'value'.
        '''
        element = self.find_element(by=by, value=value)
        if element:
            element.send_keys(key)
        else:
            raise NoSuchElementException()
                
    
    def get_text_from_element(self, by, value):
        '''
        Get the text of an element based on the provided 'by' and 'value'.
        '''
        element = self.find_element(by=by, value=value)
        if element:
            return element.text
        else:
            raise NoSuchElementException()
        
    
    def clear_element_from_text(self, by, value):
        '''
        Get the element based on the provided 'by' and 'value' and then clear it from text.
        '''
        element = self.find_element(by=by, value=value)
        if element:
            return element.clear()
        else:
            raise NoSuchElementException()
        
