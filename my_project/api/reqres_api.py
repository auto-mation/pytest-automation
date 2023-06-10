
from my_project.api.api_client import APIClient


class ReqresAPI(APIClient):
    
    __URL = "https://reqres.in/"
    __users_endpoint = "api/users" 
    __login_endpoint = "api/login" 
    __response = None
    
    def __init__(self):
        super().__init__(self.__URL)
    
    def login_reuqest(self, user, password):
        end_point = self.__login_endpoint
        data = {
                    "email": user,
                    "password": password
                }
        self.__response = self.post(end_point, data=data)    

    def create_user(self, name, job):
        end_point = self.__users_endpoint
        data = {
                    "name": name,
                    "job": job
                }
        self.__response = self.post(end_point, data=data)
    
    def list_users(self, params=None):
        end_point = self.__users_endpoint
        self. __response = self.get(end_point, params=params)
    
    def get_reponse(self):
        return self.__response