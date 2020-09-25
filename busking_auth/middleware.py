import jwt
from busking.settings import SECRET_KEY
from .exceptions import JSONWebTokenExpired, JSONWebTokenAbsent


allowed_mutations = ["createUser", "createLabelUser", "createArtistUser",
                     "__schema"]


class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        context = info.context
        # TODO: check for requests only not responses.
        if (info.path[0] not in allowed_mutations):
            if context.COOKIES.get('token'):
                try:
                    jwt.decode(context.COOKIES.get('token'), SECRET_KEY,
                               verify=True)
                except jwt.exceptions.ExpiredSignatureError:
                    raise JSONWebTokenExpired()
            else:
                raise JSONWebTokenAbsent()
        return next(root, info, **args)
