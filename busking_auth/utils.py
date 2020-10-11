from busking.settings import SECRET_KEY
import jwt


def decode_token(cookie):
    return jwt.decode(cookie, SECRET_KEY,
               verify=True)