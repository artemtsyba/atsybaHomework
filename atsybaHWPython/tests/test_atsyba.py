import requests
import json
import pytest

class TestRestApi(object):
## 1. Register a new user:
    def test_create_user(self):
        data = {
            "name":"Atsyba",
            "email":"atsyba8@gmail.com",
            "password":123456
        }
        headers = {
            "Content-type":"Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/registration", headers=headers, data=json.dumps(data))
        assert r.status_code == 200
        print(r.json())
## 1.1. Check that the new user can log in
    def test_login_user(self):
        data = {
        "email":"atsyba8@gmail.com",
        "password":123456
        }
        headers = {
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/login", headers=headers,
                          data=json.dumps(data))
        assert r.status_code == 200
        print(r.json())

## 2. Register a new user with an existing email address:
    def test_create_duplicate_user(self):
        data = {
            "name":"Atsyba",
            "email":"atsyba@gmail.com",
            "password":123456
        }
        headers = {
            "Content-type":"Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/registration", headers=headers, data=json.dumps(data))
        assert r.status_code == 200
        print(r.json())

## 3. Create a new user:
    def test_create_new_user(self):
        data = {
            "name":"artem",
            "email":"atsyba24@gmail.com",
            "password":123456
        }
        headers = {
            "Content-type":"Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/registration", headers=headers, data=json.dumps(data))
        assert r.status_code == 200
        print(r.json())
## 3.1.Log in
    @pytest.fixture()
    def prepare_user(self):
        data = {
        "email":"atsyba24@gmail.com",
        "password":123456
        }
        headers = {
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/login", headers=headers,
                          data=json.dumps(data))
        assert r.status_code == 200
        print(r.json())
        user_token = r.json()['data']['Token']
        yield user_token
## 3.2. Create new user
    def test_create_new_users(self, prepare_user):
        user_token = prepare_user
        data = {
            "name":"transformers",
            "email":"atsybaTraveler21@gmail.com",
            "location":"Kiev"
        }
        headers = {
            "Authorization":"Bearer " + user_token,
            "Content-type":"Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/users", headers=headers, data=json.dumps(data))
        assert r.status_code == 200 or 201
        print(r.json())
## 3.3. Check id
        user_id = r.json()['id']
        r = requests.get(url="http://restapi.adequateshop.com/api/users/%s" % user_id, headers=headers)
        assert r.status_code == 200 or 201
        assert r.json()['name'] == "transformers"
        print(r.json())

## 4. Log in :
    @pytest.fixture
    def prepare_update_user(self):
        data = {
        "email":"atsyba12@gmail.com",
        "password":"123456"
        }
        headers = {
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/authaccount/login", headers=headers,
                          data=json.dumps(data))
        assert r.status_code == 200
        print(r.json())
        user_token = r.json()['data']['Token']
        yield user_token
## 4.1. Create new user
    def test_update_user(self, prepare_update_user):
        user_token = prepare_update_user
        data = {
            "name": "android",
            "email": "atsybaTraveler46@gmail.com",
            "location": "Kiev"
        }
        headers = {
            "Authorization": "Bearer " + user_token,
            "Content-type": "Application/json"
        }
        r = requests.post(url="http://restapi.adequateshop.com/api/users", headers=headers, data=json.dumps(data))
        assert r.status_code == 200 or 201
        print(r.json())
        user_id = r.json()['id']
        r = requests.get(url="http://restapi.adequateshop.com/api/users/%s" % user_id, headers=headers)
        assert r.status_code == 200 or 201
## 4.2. Modify some existing user
        data = {
        "id": user_id,
        "name":"ios",
        "email":"atsybaTraveler46@gmail.com",
        "location":"Kiev"
        }
        headers = {
            "Authorization": "Bearer " + user_token,
            "Content-type":"Application/json"
        }
        r = requests.put(url="http://restapi.adequateshop.com/api/users/%s" % user_id, headers=headers,
                                  data=json.dumps(data))
        assert r.status_code == 200 or 201
        print(r.json())
## 4.2. Check your modifications
        r = requests.get(url="http://restapi.adequateshop.com/api/users/%s" % user_id, headers=headers)
        assert r.status_code == 200 or 201
        assert r.json()['name'] == "ios"
        print(r.json())















