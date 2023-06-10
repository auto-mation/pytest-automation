
from selenium import webdriver
from my_project.gui.pages.main_page import MainPage


class HomePage(MainPage):
    
    URL = 'https://katalon-demo-cura.herokuapp.com/'
    
    def __init__(self, driver: webdriver):
        super().__init__(driver)
    
    def load_home_page(self):
       self.get_driver().get(self.URL)
       