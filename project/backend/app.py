from flask import Flask
from flask_restful import Api

from utils.databases import *
from utils.auth.jwt import jwt

from datetime import timedelta

from views.measurement import *
from views.user import *
from views.device import *

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pipoca2007@192.168.0.8/flask_db'
app.config['MONGODB_SETTINGS'] = {"db": "flask_db",}

app.config['SECRET_KEY'] = "super-secret"
app.config["JWT_SECRET_KEY"] = "super-secret"

app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes = 15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days = 1)

mysqldb.init_app(app)
mongodb.init_app(app)

jwt.init_app(app)

api = Api(app)

@app.before_first_request
def create_tables():
    mysqldb.create_all()
    
api.add_resource(UserSignIn, '/auth/signin')
api.add_resource(UserSignUp, '/auth/signup')
api.add_resource(UserRefresh, '/auth/refresh')
api.add_resource(UserSignOut, '/auth/signout')

api.add_resource(DeviceList, '/me/devices')
api.add_resource(DeviceDetail, '/me/devices/<device_id>')

api.add_resource(MeasurementList, '/api')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)