
from selenium import webdriver
from my_project.gui.webdriver.setup import BaseDriver


class MainPage(BaseDriver):
    
    def __init__(self, driver: webdriver):
        super().__init__(driver)
    
    __ELEMENTS_XPATH_LOCATORS={
        "side-menu": "//a[@id='menu-toggle']",
        "login-link": "//a[@href='profile.php#login']",
        "logout-link": "//a[@href='authenticate.php?logout']",
        "history-link": "//a[@href='history.php#history']"
    }
    
    def navigate_to_side_menu(self):
        menu = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['side-menu'])
        menu.click()
        
    def navigate_to_login_page(self):
        self.navigate_to_side_menu()
        menu = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['login-link'])
        menu.click()
        
    def navigate_to_history_page(self):
        self.navigate_to_side_menu()
        menu = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['history-link'])
        menu.click()  
    
    def logout(self):
        self.navigate_to_side_menu()
        menu = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['logout-link'])
        menu.click() 