from werkzeug.exceptions import HTTPException

class InputError(HTTPException):
    code = 400
    message = "No message specified"

class ConnectionError(HTTPException):
    code = 404
    message = "No message specified"