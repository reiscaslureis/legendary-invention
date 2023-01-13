from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta 
from flask import Response

from utils.exceptions import *
from utils.databases import mysqldb, mongodb

from flask_jwt_extended import *

from flask import jsonify

from uuid import uuid4

class DeviceModel(mysqldb.Model):
    __tablename__ = 'device'
    
    id = mysqldb.Column(mysqldb.Integer, primary_key = True)
    url_id = mysqldb.Column(mysqldb.String(36))
    description = mysqldb.Column(mysqldb.String(32), nullable = True)
    user_id = mysqldb.Column(mysqldb.Integer, nullable = False)

    @jwt_required()
    def create_device(self):
        device = DeviceModel(url_id = uuid4(),user_id = get_jwt_identity())

        mysqldb.session.add(device)
        mysqldb.session.commit()

        access_token = create_access_token(identity = device.id, expires_delta = timedelta(days = 365))

        return {'access_token': access_token, 'description': device.description, 'id': device.url_id}

    @jwt_required() 
    def list(self):
        lst = DeviceModel.query.filter_by(user_id = get_jwt_identity()).all() 

        return {'qtt': len(lst), 'devices': [{'id': item.url_id, 'description': item.description} for item in lst]} 

    @jwt_required() 
    def detail(self):
        device = DeviceModel.query.filter_by(url_id = self.url_id, user_id = get_jwt_identity()).first()

        if device: return {'description': device.description, 'id': device.url_id}
        else: raise DeviceNotFoundError

    @jwt_required() 
    def delete(self):
        device = DeviceModel.query.filter_by(url_id = self.url_id).first()

        if not device: return False

        if get_jwt_identity() == device.user_id:
            mysqldb.session.delete(device)
            mysqldb.session.commit()

            return True

        else: return False

    def validate(self):
        device = DeviceModel.query.filter_by(url_id = self.url_id).first() 

        if not device: return False

        if check_password_hash(device.key, self.key): return True
        else: return False
