from models.user import UserModel
from models.device import DeviceModel
from models.measurement import MeasurementModel

class MeasurementController():
    def register(self, req_json):
        print(req_json)
        MeasurementModel(data = req_json).register()

    def list(self):
        return MeasurementModel().list()