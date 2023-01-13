from models.user import UserModel
from models.device import DeviceModel
from models.measurement import MeasurementModel

class DeviceController():
    def detail(device_id):
        info = DeviceModel(url_id = device_id).detail()
        qtt, measurements = MeasurementModel(device_id = device_id).list()

        info['qtt'] = qtt
        info['data'] = measurements

        return info

    def register():
        return DeviceModel().create_device()

    def delete(device_id):
        if DeviceModel(url_id = device_id).delete() == True:
            MeasurementModel(device_id = device_id).delete_all_from_device()

    def list():
        return DeviceModel().list()