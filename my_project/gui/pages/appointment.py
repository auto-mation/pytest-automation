
from selenium import webdriver
from my_project.gui.helpers import utils
from my_project.gui.pages.main_page import MainPage
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import Select
LOGGER = logging.getLogger(__name__)

class AppointmentPage (MainPage):
    
    def __init__(self, driver: webdriver):
        super().__init__(driver)
    
    __ELEMENTS_XPATH_LOCATORS={ 
        "facility-select": "//*[@id='combo_facility']",
        "readmission-checkbox" : "//input[@id='chk_hospotal_readmission']",
        "healthcare-program-radio" : "//input[@value='{}']", 
        "visit-date" : "//input[@id='txt_visit_date']", 
        "comment-textarea" : "//textarea[@id='txt_comment']",  
        "book-btn" : "//button[@id='btn-book-appointment']", 
        "confirmation-p" : "//p[@class='lead']"
    }  
    
    def wait_for_page_loading(self):  
            self.wait_for_element_tobe_visiable((By.XPATH, self.__ELEMENTS_XPATH_LOCATORS["book-btn"])) 
    
    def wait_booking_loading(self):  
            self.wait_for_element_tobe_visiable((By.XPATH, self.__ELEMENTS_XPATH_LOCATORS["confirmation-p"])) 
                
    def set_facility_value(self, value): 
        drop_elem = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['facility-select']) 
        select = Select(drop_elem)
        select.select_by_value(value)
        
    def set_readmission(self, value: bool): 
        drop_elem = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['readmission-checkbox']) 
        checkbox = drop_elem.get_attribute('checked')
        if checkbox != value:
            drop_elem.click()
            
    def set_healthcare_program(self, value: str): 
        drop_elem = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['healthcare-program-radio'].format(value)) 
        checkbox = drop_elem.get_attribute('checked')
        if checkbox != value:
            drop_elem.click() 
            
    def set_visit_date(self, desired_date: str): 
        if desired_date == 'CURRENT_DATE': 
            desired_date = utils.get_current_date()
        elem = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['visit-date']) 
        elem.clear()  
        elem.send_keys(desired_date) 
        
    def set_comment(self, comment: str): 
        elem = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['comment-textarea']) 
        elem.clear()  
        elem.send_keys(comment)
        
    def click_book(self): 
        elem = self.get_element_xpath(self.__ELEMENTS_XPATH_LOCATORS['book-btn']) 
        elem.submit()
        elem.click()
        self.wait_booking_loading()