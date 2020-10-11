import jwt
from busking.settings import SECRET_KEY
from .exceptions import JSONWebTokenExpired, JSONWebTokenAbsent
from busking_auth.utils import decode_token

allowed_mutations = ["createUser", "createLabelUser", "createArtistUser",
                     "__schema"]


class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        context = info.context
        # TODO: check for requests only not responses.
        if (info.path[0] not in allowed_mutations):
            if context.COOKIES.get('token'):
                try:
                    decode_token(context.COOKIES.get('token'))
                except jwt.exceptions.ExpiredSignatureError:
                    raise JSONWebTokenExpired()
            else:
                raise JSONWebTokenAbsent()
        return next(root, info, **args)
