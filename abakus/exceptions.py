# -*- coding: utf-8 -*-


class AbakusAuthException(Exception):

    def __init__(self, resp):
        super().__init__(resp)
        self.response = resp
        self.code = resp.status_code


class ResponseError(AbakusAuthException):
    pass


class TransportError(AbakusAuthException):

    msg_format = 'An error occurred while making a request to LEGO: {0}'

    def __init__(self, exception):
        Exception.__init__(self, exception)
        self.exception = exception
        self.msg = self.msg_format.format(str(exception))

    def __str__(self):
        return '{0}: {1}'.format(type(self.exception), self.msg)


class ConnectionError(TransportError):
    msg_format = 'A connection-level exception occurred: {0}'


class UnprocessableResponseBody(ResponseError):
    def __init__(self, message, body):
        Exception.__init__(self, message)
        self.body = body
        self.msg = message


class BadRequest(ResponseError):
    pass


class AuthenticationFailed(ResponseError):
    pass


class ForbiddenError(ResponseError):
    pass


class NotFoundError(ResponseError):
    pass


class MethodNotAllowed(ResponseError):
    pass


class NotAcceptable(ResponseError):
    pass


class ClientError(ResponseError):
    pass


class ServerError(ResponseError):
    pass


error_classes = {
    400: BadRequest,
    401: AuthenticationFailed,
    403: ForbiddenError,
    404: NotFoundError,
    405: MethodNotAllowed,
    406: NotAcceptable,
}


def error_for(response):
    klass = error_classes.get(response.status_code)
    if klass is None:
        if 400 <= response.status_code < 500:
            klass = ClientError
        if 500 <= response.status_code < 600:
            klass = ServerError
    return klass(response)
