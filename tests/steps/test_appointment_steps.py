
from pytest_bdd import scenarios, given, when, then
from my_project.gui.helpers import utils
from my_project.gui.pages.home import HomePage
from my_project.gui.pages.login import LoginPage
from my_project.gui.pages.appointment import AppointmentPage
from my_project.gui.pages.history import HistoryPage
import logging
LOGGER = logging.getLogger(__name__)
from pytest_bdd import parsers

# Load the scenarios from the feature file
scenarios('appointment.feature')

@given('user navigate to home page')
def load_home_page(browser):
    LOGGER.info("user navigate to home page")
    page = HomePage(browser)
    page.load_home_page() 
    
@then(parsers.cfparse('user login with username "{user}" and password "{password}"'))
def authenticate_login_page(browser, user, password): 
    LOGGER.info("user login with username '{}' and password '{}'".format(user, password))
    login_page = LoginPage(browser) 
    login_page.navigate_to_login_page()  
    login_page.wait_for_page_loading() 
    login_page.set_username_value(user)
    login_page.set_password_value(password)
    login_page.click_login_btn()

@when('user navigate to appointments page')
def navigate_appointments_page(browser):
    LOGGER.info("user navigate to appointments page")
    page = AppointmentPage(browser)
    page.wait_for_page_loading()

@then(parsers.cfparse('user set Facility "{value}"'))
def set_facility(browser, value):
    LOGGER.info("user set facility {}".format(value))
    page = AppointmentPage(browser)
    page.wait_for_page_loading()
    page.set_facility_value(value) 
  
@then(parsers.cfparse('user set hospital readmission "{value}"'))
def set_hospital_readmission(browser, value):
    LOGGER.info("user set hospital readmission {}".format(value))
    page = AppointmentPage(browser)
    page.wait_for_page_loading() 
    page.set_readmission(value)
        
@then(parsers.cfparse('user set Healthcare Program "{value}"'))
def set_healthcare_programs(browser, value):
    LOGGER.info("user set healthcare program {}".format(value))
    page = AppointmentPage(browser)
    page.wait_for_page_loading()
    page.set_healthcare_program(value)
    
@then(parsers.cfparse('user set Visit date "{value}"'))
def set_visit_date(browser, value):
    LOGGER.info("user set date {}".format(value))
    page = AppointmentPage(browser)
    page.wait_for_page_loading()
    page.set_visit_date(value)
    
@then(parsers.cfparse('user set Comment "{value}"'))
def set_comment(browser, value):
    LOGGER.info("user set Comment {}".format(value))
    page = AppointmentPage(browser)
    page.wait_for_page_loading()
    page.set_comment(value)

@then(parsers.cfparse('user set Comment ""'))
def set_empty_comment(browser):
    set_comment(browser, "")
                
@when('user click Book Appointment')
def click_book_appointment(browser): 
    LOGGER.info("user click Book Appointment")
    page = AppointmentPage(browser)
    page.wait_for_page_loading()
    page.click_book() 
     
@then('user navigate to history page')
def navigate_history_page(browser):  
    LOGGER.info("user navigate to history page")
    page = HistoryPage(browser) 
    page.navigate_to_history_page()
    page.wait_for_page_loading()  
    
@then(parsers.cfparse('user find appointment with date "{value_date}" and Facility "{value_facility}" and Program "{value_program}"'))
def validate_appointment(browser, value_date, value_facility, value_program):  
    LOGGER.info("user validate appointment details")
    page = HistoryPage(browser) 
    page.wait_for_page_loading()
    if value_date == 'CURRENT_DATE': 
        value_date = utils.get_current_date()
    details = page.get_appointment(value_date)
    LOGGER.info("Found appointment with details : ".format(details))
    assert details and 'date' in details.keys(), "Couldn't fetch date!" 
    assert value_date == details['date'], "Existing date is not matched with the given value!"
    assert value_facility == details['facility'], "Existing facility is not matched with the given value!"
    assert value_program == details['program'], "Existing program is not matched with the given value!"
 
@then('user logout')
def logout(browser): 
    LOGGER.info("user logout")
    page = HomePage(browser)
    page.logout()
    
    
    
    
    