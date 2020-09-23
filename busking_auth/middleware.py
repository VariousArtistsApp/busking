import jwt
from busking.settings import SECRET_KEY
from .exceptions import JSONWebTokenExpired, JSONWebTokenAbsent


class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        context = info.context
        if (info.path != "createUser"):
            if context.COOKIES.get('token'):
                try:
                    jwt.decode(context.COOKIES.get('token'), SECRET_KEY,
                               verify=True)
                except jwt.exceptions.ExpiredSignatureError:
                    raise JSONWebTokenExpired()
            else:
                raise JSONWebTokenAbsent()
        return next(root, info, **args)
