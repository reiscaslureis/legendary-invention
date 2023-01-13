from utils.databases import mysqldb
from flask_jwt_extended import *
from utils.auth.jwt import jwt

class RevokedTokenModel(mysqldb.Model):
    __tablename__ = 'revoked_token'

    id = mysqldb.Column(mysqldb.Integer, primary_key=True)
    jti = mysqldb.Column(mysqldb.String(36), nullable=False, index=True)
    created_at = mysqldb.Column(mysqldb.DateTime, nullable=False)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = mysqldb.session.query(RevokedTokenModel.id).filter_by(jti = jti).scalar()

    return token is not None