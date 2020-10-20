import datetime
import uuid

import jwt
from graphene_django.utils.testing import GraphQLTestCase

from busking.settings import SECRET_KEY
from busking.test.graphql import graphql_query


def generate_fake_token():
    return jwt.encode({'user': "test",
                       'exp': datetime.datetime.utcnow() +
                       datetime.timedelta(seconds=5000)},
                      SECRET_KEY,
                      algorithm='HS256')


def generate_fake_email():
    return "{}@va.app".format(uuid.uuid4().hex)


def generate_fake_user():
    return {'name': uuid.uuid4().hex, "password": "test1234567899999",
            "email": generate_fake_email(), "location": "Berlin, Germany",
            "dob": "01.01.2020"}


class GraphQLTestCaseWithCookies(GraphQLTestCase):
    def query(self, query, op_name=None, input_data=None, variables=None,
              headers=None, login_token=None):
        return graphql_query(
            query,
            op_name=op_name,
            input_data=input_data,
            variables=variables,
            headers=headers,
            client=self._client,
            graphql_url=self.GRAPHQL_URL,
            login_token=login_token
        )
