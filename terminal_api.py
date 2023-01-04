import connector
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import connector

app = Flask(__name__)
api = Api(app)

class Players(Resource):
    def __init__(self, table, columns=None):
        self.table=table
        self.columns=columns

    def get(self):
        if self.columns != None:
            return connector.connect_columns(self.table, self.columns).to_dict()
        else:
            return connector.connect_table(self.table).to_dict()

api.add_resource(Players, '/players')


#if __name__ == "__main__":
    #app.run(debug=True)