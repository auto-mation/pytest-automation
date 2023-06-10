
from selenium import webdriver
from my_project.gui.pages.main_page import MainPage
from selenium.webdriver.common.by import By
import logging
LOGGER = logging.getLogger(__name__)

class LoginPage (MainPage):
    
    def __init__(self, driver: webdriver):
        super().__init__(driver)
    
    __ELEMENTS_XPATH_LOCATORS={ 
        "login-btn": "//*[@id='btn-login']",
        "username-input" : "//*[@id='txt-username']",
        "password-input" : "//*[@id='txt-password']", 
        "error-msg" : "//p[@class='lead text-danger']", 
    }  
    
    def wait_for_page_loading(self):  
            self.wait_for_element_tobe_visiable((By.XPATH, self.__ELEMENTS_XPATH_LOCATORS["login-btn"])) 
        
    def set_username_value(self, value):
        element = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['username-input'])
        element.send_keys(value)
        
    def set_password_value(self, value):
        element = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['password-input'])
        element.send_keys(value)
        
    def click_login_btn(self):
        element = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['login-btn'])
        element.click()
        
    def get_error_message(self):
        self.wait_for_element_tobe_visiable((By.XPATH, self.__ELEMENTS_XPATH_LOCATORS["error-msg"])) 
        element = self.get_element_xpath(self._ELEMENTS_XPATH_LOCATORS['error-msg'])
        LOGGER.info(element.text)
        return element.text