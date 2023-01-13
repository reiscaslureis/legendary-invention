from flask import request, Response
from flask_restful import Resource

from controllers.user import UserController

class UserSignUp(Resource):
    def post(self):
        try: return UserController.sign_up(request.get_json())   
        except Exception as error: return {'error': str(error)}
        
class UserSignIn(Resource):
    def post(self):
        try: return UserController.sign_in(request.get_json())
        except Exception as error: return {'error': str(error)}

class UserRefresh(Resource):
    def post(self):
        try: return UserController.refresh()
        except Exception as error: return {'error': str(error)}

class UserSignOut(Resource):
    def delete(self):
        try: return UserController.sign_out()
        except Exception as error: return {'error': str(error)}


    