import requests
import pytest

class CreateItemTests():
    def test_createItem(self):
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            "name": "Шортики11333333333333",
            "section": "Платья",
            "description": "Модное платье из новое коллекции!"
        }
        response = requests.post("http://shop.bugred.ru/api/items/create/", headers=headers, json=body)
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json['result']['name'] == 'Шортики11333333333333'
        print(response.text)

    def test_create_error(self):
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            "name": "Шортики3423423423423423423",
            "section": "Платья",
            "description": "Модное платье из новое коллекции!"
        }
        response = requests.post("http://shop.bugred.ru/api/items/create/", headers=headers, data=body)
        resp_json = response.json()
        assert response.status_code == 200
        assert resp_json["status"] == "error"
        assert resp_json["message"] == "Название товара не заполнено!"
        print(response.text)