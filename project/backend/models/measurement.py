from utils.databases import mongodb, mysqldb
from werkzeug.security import check_password_hash
from flask_jwt_extended import *

class MeasurementModel(mongodb.Document):
    meta = {'collection': 'measurement'}

    device_id = mongodb.IntField()
    data = mongodb.DictField()

    @jwt_required()
    def register(self):
        bttf = MeasurementModel(device_id = get_jwt_identity(),
                                data = self.data)

        bttf.save()

    @jwt_required()
    def list(self):        
        bttf = MeasurementModel.objects(device_id = get_jwt_identity()).all()
        qtt = len(bttf)
        
        return [{'data': item.data} for item in bttf]

    def delete_all_from_device(self):
        bttf = MeasurementModel.objects(device_id = self.device_id).delete()