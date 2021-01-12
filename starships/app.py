import os
from flask import Flask
from flask_restful import Resource, Api

from .manage import db, Starship

import json
import urllib
import requests



app = Flask(__name__)
api = Api(app)
app.config.from_object(os.environ.get("APP_SETTINGS"))


@app.route('/')
def home():
    return 'Starships: Welcome to hyperdrive rating'

class FetchStarships(Resource):
    def get(self):
        user = Starship.query.all()
        return {}

class SWAPIFetchStarships(Resource):
    def get(self):
        where = urllib.parse.quote_plus("""
        {
            "name": {
                "$exists": true
            }
        }
        """)

        url = 'https://parseapi.back4app.com/classes/SWAPI_Starship?count=1&order=-hyperdriveRating&where=%s' % where
        headers = {
            'X-Parse-Application-Id': os.environ.get("Application_Id"), # This is your app's application id
            'X-Parse-REST-API-Key': os.environ.get("REST_API_Key") # This is your app's REST API key
        }
        data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
        return data

api.add_resource(FetchStarships, '/starships')
api.add_resource(SWAPIFetchStarships, '/external/starships')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)