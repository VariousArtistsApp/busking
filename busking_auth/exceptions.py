# https://github.com/flavors/django-graphql-jwt/blob/28e4f9749bac839d327914cfdda2ea3bb77bd775/graphql_jwt/exceptions.py
# MIT LICENSE
from django.utils.translation import gettext_lazy as _


class JSONWebTokenError(Exception):
    default_message = None

    def __init__(self, message=None):
        if message is None:
            message = self.default_message

        super().__init__(message)


class PermissionDenied(JSONWebTokenError):
    default_message = _('You do not have permission to perform this action')


class JSONWebTokenExpired(JSONWebTokenError):
    default_message = _('Signature has expired')


class JSONWebTokenAbsent(JSONWebTokenError):
    default_message = _('No token was provided!')
