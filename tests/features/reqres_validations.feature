Feature: Reqres api validations
 
    @api @api_login
    Scenario Outline: create a user request
        Given user send login request for username "<user>" and password "<password>"
        Then user find response code is "<code>"
        Then user find response data contains "<response_param_1>" 
    Examples:
        | user | password | code | response_param_1 |   
        | eve.holt@reqres.in | cityslicka | 200 | token | 
        | eve.holt@reqres.in |  | 400 | error | 
        |  | cityslicka | 400 | error | 
        

    @api @api_list_users
    Scenario: list users
        Given user send list users request
        Then user find response code is "200" 
        Then user find response data contains "data"
        Then user find response data contains "support" 
        Then user find response data contains "total_pages"
        Then user find response parameter "per_page" with value "6"
        Then user find response parameter "total" with value "12"
        Then user validate return data object from list users



     