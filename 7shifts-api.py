import flask
from flask import Response
from flask import json
from services import ServiceAPI
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    ''''This method return the location of the services'''

    service = ServiceAPI()
    locations = service.list_location()

    if locations is not None:
        resp = Response(json.dumps(locations), status=200, mimetype='application/json')
    else:
        resp = Response("Error - There is a problem retrieving your data", status=404, mimetype='application/json')
    return resp

@app.route('/users/<locationId>')
def users(locationId):
    '''This method is responsible to retrieve the users on database'''

    consumer = ServiceAPI()
    data = consumer.get_users_data(locationId)
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run()

