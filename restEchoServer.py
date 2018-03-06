#!/usr/local/bin/python3
# general
import sys
# flask
from flask import Flask
from flask_restful import Api, Resource, reqparse
# ----- Init -----
app = Flask(__name__)
api = Api(app)


class demoApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message', type=str, location='json')
        super(demoApi, self).__init__()

    # def get(self):
    #     args = self.reqparse.parse_args()
    #     message = args['message']
    #     print('request', message)
    #     message += 'world'
    #     print('response', message)
    #     return {'message': message}

    def post(self):
        args = self.reqparse.parse_args()
        message = args['message']
        print('request', message)
        message += 'world'
        print('response', message)
        return {'message': message}

    # def delete(self):
    #     args = self.reqparse.parse_args()
    #     message = args['message']
    #     print('request', message)
    #     message += 'world'
    #     print('response', message)
    #     return {'message': message}

api.add_resource(demoApi, '/demo', endpoint='demo')

# ----- Main -----
if __name__ == '__main__':
    port = 80
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', debug=True, port=port)
