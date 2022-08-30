from rest_framework.exceptions import APIException


class BadRequest(APIException):
    status_code = 400
    default_detail = "Server cannot or will not process the request due to something that is perceived to be a client error."
    default_code = "bad_request"


class Unauthorized(APIException):
    status_code = 401
    default_detail = "Client provides no credentials or invalid credentials."
    default_code = "unauthorized"


class Forbidden(APIException):
    status_code = 403
    default_detail = "status code indicates that the server understood the request but refuses to authorize it."
    default_code = "forbidden"


class NotFound(APIException):
    status_code = 404
    default_detail = "Web user that a requested page is not available."
    default_code = "not_found"
