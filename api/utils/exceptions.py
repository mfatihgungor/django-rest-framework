from rest_framework.exceptions import APIException


class BadRequestException(APIException):
    status_code = 400
    default_code = 'bad_request'
    default_detail = 'Bad request'
