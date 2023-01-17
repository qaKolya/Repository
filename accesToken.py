import pytest
import json
import requests
from configFile import baseUrl, formData, params
import status



def get_Token():
    response = requests.post(url=baseUrl + "access_token", data=formData, params=params)
    req_json = json.loads(response.text)
    print(req_json["access_token"])
    return req_json["access_token"]


