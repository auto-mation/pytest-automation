
from pytest_bdd import scenarios, given, when, then
from my_project.api.reqres_api import ReqresAPI 
import logging
LOGGER = logging.getLogger(__name__)
from pytest_bdd import parsers

# Load the scenarios from the feature file
scenarios('reqres_validations.feature')
 
api = ReqresAPI() 

@given(parsers.cfparse('user send login request for username "{user}" and password "{password}"'))
def send_login_user_req(user, password):
    LOGGER.info("user send login request for username {} and password {}".format(user, password)) 
    api.login_reuqest(user, password) 

@given(parsers.cfparse('user send login request for username "" and password "{password}"'))
def send_login_user_req_emptyuser(password):
    send_login_user_req("", password)

@given(parsers.cfparse('user send login request for username "{user}" and password ""'))
def send_login_user_req_emptypass(user):
    send_login_user_req(user, "")
    
@then(parsers.cfparse('user find response code is "{code}"'))
def validate_response_code(code):
    LOGGER.info("user validate response is {}".format(code))   
    assert api.get_reponse().status_code == int(code)
    
@then(parsers.cfparse('user find response data contains "{key}"'))
def validate_response_code(key):
    LOGGER.info("user validate response data contains {}".format(key))   
    json_response = api.get_reponse().json()
    LOGGER.info("Response data {}".format(json_response))
    assert key in json_response 

@then(parsers.cfparse('user find response parameter "{param}" with value "{value}"'))
def validate_response_keyvalue(param, value):
    LOGGER.info("user validate response parameter {} with value {}".format(param, value))   
    json_response = api.get_reponse().json()
    LOGGER.info("Response data {}".format(json_response))
    assert param in json_response 
    assert str(json_response[param]) == value
    
@given(parsers.cfparse('user send list users request'))
def send_list_users_req():
    LOGGER.info("user send list users request") 
    api.list_users() 

@then(parsers.cfparse('user validate return data object from list users'))
def validate_response_keyvalue():
    LOGGER.info("user validate return data object from list users")   
    json_response = api.get_reponse().json()  
    data = json_response['data']
    assert len(data) > 0, "users not list ine data object"
    LOGGER.info("List user data object keys are {}".format(data[0].keys()))
    for key in ['id', 'email', 'first_name', 'last_name', 'avatar']:
        assert key in data[0].keys() 