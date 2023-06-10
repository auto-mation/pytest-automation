from selenium import webdriver
from my_project.gui.pages.main_page import MainPage
from selenium.webdriver.common.by import By
import logging
LOGGER = logging.getLogger(__name__)

class HistoryPage (MainPage):
    
    def __init__(self, driver: webdriver):
        super().__init__(driver)
    
    __ELEMENTS_XPATH_LOCATORS={ 
        "gotohome-btn": "//a[contains(@class, ' btn-default')]",
        "booking-details-div" : {
                "container" :  "//div[contains(@class, ' panel-info')]",
                "date": "//div[@class='panel-heading']",
                "facility" : "//p[@id='facility']",
                "readmission" : "//p[@id='hospital_readmission']",
                "program" : "//p[@id='program']",
                "comment" : "//p[@id='comment']",
            }
    }  
    
    def wait_for_page_loading(self):  
            self.wait_for_element_tobe_visiable((By.XPATH, self.__ELEMENTS_XPATH_LOCATORS["gotohome-btn"])) 
            
    def get_appointment(self, date):
        appointments = self.get_driver().find_elements(By.XPATH, self.__ELEMENTS_XPATH_LOCATORS["booking-details-div"]["container"])
        for app in appointments :
            app_date = app.find_element( By.XPATH,self.__ELEMENTS_XPATH_LOCATORS["booking-details-div"]["date"]) 
            if date == app_date.text:
                LOGGER.info("Found appoinment matching giving date : {}".format(app_date.text))
                facility = app.find_element( By.XPATH,self.__ELEMENTS_XPATH_LOCATORS["booking-details-div"]["facility"]) 
                readmission = app.find_element( By.XPATH,self.__ELEMENTS_XPATH_LOCATORS["booking-details-div"]["readmission"]) 
                program = app.find_element( By.XPATH,self.__ELEMENTS_XPATH_LOCATORS["booking-details-div"]["program"]) 
                return {"date" : app_date.text,
                        "facility": facility.text,
                        "readmission": readmission.text,
                        "program": program.text,
                        }
        return None

        