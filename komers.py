import pytest
import json
import requests
import status
from configFile import header1


def test_bank():
    data2 = {
        "grant_type": "password",
        "scope": "private",
        "username": "996705754845",
        "password": "nbjh4412",
        "client_id": "mobile-private",
        "client_secret": "scrt",
        "device_token": "6ebc8523-8e79-4f70-a52e-1a9b66d6cd_"
    }

    response = requests.post(url="https://mbank.cbk.kg/oauth/token",
                             headers=header1, data=data2)
    req = json.loads(response.text)
    print(req)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
