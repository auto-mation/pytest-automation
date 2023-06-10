import requests
import logging
LOGGER = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        LOGGER.info("Send GET request url: {} params {} ".format(url, params))
        response = requests.get(url, params=params)
        return response

    def post(self, endpoint, params=None, data=None):
        url = f"{self.base_url}{endpoint}" 
        LOGGER.info("Send POST request url: {} params {} data {}".format(url, params, data))
        response = requests.post(url=url, params=params, data=data)
        return response