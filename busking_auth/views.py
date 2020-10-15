import datetime
import json

import jwt
from django.contrib.auth import authenticate
from django.http import HttpResponseForbidden, JsonResponse

from busking.settings import SECRET_KEY


def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        user = authenticate(request=request, username=data['email'],
                            password=data['password'])
        if user:
            token = jwt.encode({'user': str(user.id),
                                'exp': datetime.datetime.utcnow() +
                                datetime.timedelta(seconds=5000)},
                               SECRET_KEY,
                               algorithm='HS256')
            response = JsonResponse({"response": "success"})
            response.set_cookie("token", token.decode('utf-8'), httponly=True,
                                samesite="strict", domain="localhost",
                                max_age=3600)
            response.set_cookie("logged_in", "true", httponly=False,
                                samesite="strict", domain="localhost",
                                max_age=3600)
            return response
        response = JsonResponse({"response": "failure",
                                 "error": "Bad email/password"})
        return response
    return HttpResponseForbidden()
