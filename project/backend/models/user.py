from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta , timezone
from flask import Response

from utils.exceptions import *
from utils.databases import mysqldb 

from flask_jwt_extended import *

from flask import jsonify

from utils.auth.revoked_token import RevokedTokenModel

class UserModel(mysqldb.Model):
    __tablename__ = 'user'
    
    id = mysqldb.Column(mysqldb.Integer, primary_key = True, autoincrement = True)
    username = mysqldb.Column(mysqldb.String(32), nullable = False, unique = True)
    password = mysqldb.Column(mysqldb.String(128), nullable = False)

    def check_if_user_exists(self):
        user = UserModel.query.filter_by(username = self.username).first()

        if not user: return False
        else: return user

    def validate_password(self, user):
        if check_password_hash(user.password, self.password):
            access_token = create_access_token(identity = user.id)
            refresh_token = create_refresh_token(identity = user.id)

            return {'refresh_token': refresh_token, 'access_token': access_token}
        
        else: return False

    def create_user(self):
        self.password = generate_password_hash(self.password)     
        mysqldb.session.add(self)
        mysqldb.session.commit()

        return {'username': self.username}

    @jwt_required(refresh = True)
    def new_access_token(self):
        access_token = create_access_token(identity = get_jwt_identity())
        refresh_token = create_refresh_token(identity = get_jwt_identity())

        self.add_token_to_blocklist()

        return {'refresh_token': refresh_token, 'access_token': access_token}

    @jwt_required(verify_type = False)
    def add_token_to_blocklist(self):
        mysqldb.session.add(RevokedTokenModel(jti = get_jwt()["jti"], created_at = datetime.now()))
        mysqldb.session.commit()

        return jsonify(msg = "JWT revoked")
