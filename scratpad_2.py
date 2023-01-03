#import psycopg2
#from config import config
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

players_path = 'csv_vault/Characters_Players.csv'
class Players(Resource):
    def get(self):
        data = pd.read_csv(players_path)  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code


api.add_resource(Players, '/players')
if __name__ == "__main__":
    app.run(debug=True)