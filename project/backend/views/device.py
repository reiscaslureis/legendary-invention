from flask import request, Response
from flask_restful import Resource

from controllers.device import DeviceController

class DeviceList(Resource):
    def post(self):
        try: return DeviceController.register()   
        except Exception as error: return {'error': str(error)}

    def get(self):
        try: return DeviceController.list()   
        except Exception as error: return {'error': str(error)}

class DeviceDetail(Resource):
    def get(self, device_id):
        try: return DeviceController.detail(device_id)   
        except Exception as error: return {'error': str(error)}

    def delete(self, device_id):
        try: return DeviceController.delete(device_id)   
        except Exception as error: return {'error': str(error)}
    