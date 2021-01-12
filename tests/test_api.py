import requests
import json

url = 'http://127.0.0.1:5000'  # The root url of the flask app


def test_homepage(app, client):
    del app
    response = client.get('/')  # Assumses that it has a path of "/"
    assert response.status_code == 200  # Assumes that it will return a 200 response
    assert response.get_data(as_text=True) == 'Starships: Welcome to hyperdrive rating'



def test_fetch_external_starships(app, client):
    del app
    response = client.get(url + '/external/starships')
    assert response.status_code == 200  # Assumes that it will return a 200 response
