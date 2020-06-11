from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Greeting(Resource):
    def get(self):
        return {'greeting': {'phrase': 'Hellow', 'language': 'en'}}  # Fetches first column that is Employee ID




api.add_resource(Greeting, '/greeting')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')

# http://127.0.0.1:5002/greeting