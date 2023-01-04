import connector
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import connector

app = Flask(__name__)
api = Api(app)

table = "Characters_Players"

class Players(Resource):
    def get(self):
        data = connector.connect_table(table)
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True, type=str, location='values')
        parser.add_argument('origin', required=True, type=str, location='values')
        parser.add_argument('current race', required=True, type=str, location='values')
      
        args = parser.parse_args()

        data = connector.connect_table(table)

        if args['name'] in data['name']:
            return {
                'message': f"{args['name']} already exists"
            }, 409
        else:
            data = data.append({
                'name': args['name'],
                'origin': args['origin'],
                'current race': args['current race']
            }, ignore_index=True)   

        data.to_csv(table, index=False)
        return {'data': data.to_dict()}, 200


api.add_resource(Players, '/players')
if __name__ == "__main__":
    app.run(debug=True)