import requests
import json

url = 'http://127.0.0.1:5000'  # The root url of the flask app


def test_homepage():
    response = requests.get(url + '/')  # Assumses that it has a path of "/"
    assert response.status_code == 200  # Assumes that it will return a 200 response
    assert response.content == b'Starships: Welcome to hyperdrive rating'


def test_fetch_starships():
    response = requests.get(url + '/starships')
    data = json.loads(response.content.decode('utf-8'))
    assert response.status_code == 200  # Assumes that it will return a 200 response
    assert data[0]['id'] == 1


def test_fetch_external_starships():
    response = requests.get(url + '/external/starships')
    data = json.loads(response.content.decode('utf-8'))
    assert response.status_code == 200  # Assumes that it will return a 200 response
    assert 'count' in data
    assert 'results' in data
