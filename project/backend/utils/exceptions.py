class RequiredFieldsError(Exception):
    def __str__(self):
        return 'some fields are required'
    
class UsernameInUseError(Exception):
    def __str__(self):
        return 'username already in use'
    
class UsernameLengthError(Exception):
    def __str__(self):
        return 'username must contain between 8 and 16 characters'

class PasswordLengthError(Exception):
    def __str__(self):
        return 'password must contain between 8 and 16 characters'
    
class UsernamePasswordMatchError(Exception):
    def __str__(self):
        return "name and password don't match"
    
class UserNotLoggedInError(Exception):
    def __str__(self):
        return 'user not logged in'
    
class HeaderTokenRequiredError(Exception):
    def __str__(self):
        return 'header token is required' 
    
class InvalidTokenError(Exception):
    def __str__(self):
        return 'invalid token' 
    
class DeviceNotFoundError(Exception):
    def __str__(self):
        return 'device not found'    