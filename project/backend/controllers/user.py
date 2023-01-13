from models.user import UserModel
from models.device import DeviceModel
from models.measurement import MeasurementModel

from utils.exceptions import *

class UserController():
    def sign_up(req_json):
        if 'username' not in req_json or 'password' not in req_json: raise RequiredFieldsError
        if len(req_json['username']) < 8 or len(req_json['username']) > 16: raise UsernameLengthError
        if len(req_json['password']) < 8 or len(req_json['password']) > 16: raise PasswordLengthError

        if not UserModel(username = req_json['username']).check_if_user_exists():
            return UserModel(username = req_json['username'], password = req_json['password']).create_user()

        else: raise UsernameInUseError

    def sign_in(req_json):
        user = UserModel(username = req_json['username']).check_if_user_exists()
        if not user: raise UsernamePasswordMatchError

        token = UserModel(username = req_json['username'], password = req_json['password']).validate_password(user)
        if not token: raise UsernamePasswordMatchError
        else: return token

    def refresh():
        return UserModel().new_access_token()

    def sign_out():
        return UserModel().add_token_to_blocklist()