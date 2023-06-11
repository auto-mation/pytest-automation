
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.firefox.service import Service as firefox_Service
from selenium.webdriver.chrome.service import Service as chrome_Service 
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import logging
from selenium import webdriver
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
            service = chrome_Service(executable_path= ChromeDriverManager().install())
            self.__DRIVER = webdriver.Chrome(service=service) 
        elif browser_name == "firefox":  
            service = firefox_Service(executable_path= GeckoDriverManager().install())
            self.__DRIVER = webdriver.Firefox(service=service) 
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
        
       