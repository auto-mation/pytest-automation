
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
LOGGER = logging.getLogger(__name__)

class BaseDriver():
    
    __DRIVER = None
    __MAX_WAIT_FOR_ELEMENT = 20 
    
    def __init__(self, driver: webdriver = None):
        if driver:
            self.__DRIVER = driver
     
    def initiate_browser(self, browser_name : str):  
        LOGGER.info(f"Starting browser with anme : {browser_name}")
        if browser_name == "chrome":
            self.__DRIVER = webdriver.Chrome()
        elif browser_name == "firefox":
            self.__DRIVER = webdriver.Firefox()
        elif browser_name == "edge":
            self.__DRIVER = webdriver.Edge()    
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        return self.__DRIVER
        
    def get_driver(self):
        if self.__DRIVER is None:
            raise ValueError("Web Driver was not initialized")
        else:
            return self.__DRIVER
        
    def get_element_xpath(self, xpath_value):
        LOGGER.info(f"Getting element with xpath : {xpath_value}")
        return self.get_driver().find_element(By.XPATH, xpath_value)
        
    def wait_for_element_tobe_visiable(self, by: By):
        wait = WebDriverWait(self.get_driver(), self.__MAX_WAIT_FOR_ELEMENT)
        wait.until(EC.presence_of_element_located(by))
        wait.until(EC.visibility_of_element_located(by))
        