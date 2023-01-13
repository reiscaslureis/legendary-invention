from flask import request, Response
from flask_restful import Resource

from controllers.measurement import MeasurementController

class MeasurementList(Resource):
    def post(self):
        try: req_json = request.get_json()
        except: req_json = None

        try: return MeasurementController().register(req_json) 
        except Exception as error: return {'error': str(error)}

    def get(self):
        try: return MeasurementController().list() 
        except Exception as error: return {'error': str(error)}