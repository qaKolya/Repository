import pytest
import requests
import json
import status

import accesToken
from configFile import baseUrl, headersBasic, data1, headersAuth, formData, params
from accesToken import get_Token

print("Hi")
print(baseUrl + "users/search?user_id=1")
print(headersAuth)


@pytest.fixture(scope='session')
def req():
    s = requests.Session()
    #
    #
    #
    # s.operation
    return s




# def test_click
# class TestMe:
class Testing:

    # def get_Token(self):
    #     response = requests.post(url=baseUrl + "access_token", data=formData, params=params)
    #     req_json = json.loads(response.text)
    #     # print("\n",json.dumps(req_json, indent=4))
    #     # print("\n",req_json)
    #     return req_json["access_token"]

    # url = "http://127.0.0.1:5000/"
    #
    #  def test_own_service(self):
    #      req = requests.get(url=self.url)
    #      req_json = json.loads(req.text)
    #      print(req_json)
    #      if req_json["message"] == "ok":
    #          pass
    #      else:
    #          raise ValueError("Ожидали 'ok', получили {}".format(req_json))
    #
    #  def test_own_service_post(self):
    #      req = requests.get(url=self.url)
    #      req_json = json.loads(req.text)
    #      assert req_json["message"] == "ok"
    #      assert req.status_code == 200
    #      print(req_json)

    def test_receive_single_user(self):
        payload = {
            'status': 200,
            'message': 'OK',
            'data': {'user_id': 1,
                     'customer_id': '5717311193220',
                     'email': 'eraliev.dev@gmail.com',
                     'first_name': 'Kolbai',
                     'last_name': 'Eraliev',
                     'photo_url': 'https://app.growave.io/public/images/nophoto_user_thumb_profile.png',
                     'about': 'Entrepreneur, engineer, inventor, investor',
                     'birthdate': '1971-06-28',
                     'profile_address': 'https://kolbai.myshopify.com/pages/profile/testing',
                     'points': '0',
                     'points_expiration_date': '2022-11-25 16:40:43',
                     'tier': None,
                     'refer_link': 'https://refrr.app/hppuDQpLIh/113308', }}

        response = requests.get(url=baseUrl + "users/search?user_id=1",
                                headers={"Authorization": f"Bearer {get_Token()}"})
        req = json.loads(response.text)
        # print("\n", req["data"]["email"])
        actEmail = req["data"]["email"]
        actCust_id = req["data"]["customer_id"]
        assert response.status_code == status.HTTP_200_OK
        assert actEmail == "eraliev.dev@gmail.com"
        assert actCust_id == "5717311193220"

    def test_add_to_wishlist(self):
        response = requests.post(url=baseUrl + "wishlist?user_id=4&product_id=6976031883396",
                                 headers={"Authorization": "Bearer {}".format(get_Token())},
                                 params=data1)
        print(json.loads(response.text))
        assert response.status_code == status.HTTP_200_OK



