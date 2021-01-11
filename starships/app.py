from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return 'Starships: Welcome to hyperdrive rating'

class FetchStarships(Resource):
    def get(self):
        return {'starships': 'world' }

api.add_resource(FetchStarships, '/starships')

if __name__ == '__main__':
    app.run(debug=True)