'''
https://github.com/graphql-python/graphene-django/blob/master/graphene_django/utils/testing.py
MIT LICENSE
'''
import json
from django.test import TestCase, Client
from http.cookies import SimpleCookie
from graphene_django.utils.testing import GraphQLTestCase


DEFAULT_GRAPHQL_URL = "/graphql/"


def graphql_query(
    query,
    op_name=None,
    input_data=None,
    variables=None,
    headers=None,
    client=None,
    graphql_url=None,
    login_token=None,
):
    """
    Args:
        query (string)              - GraphQL query to run
        op_name (string)            - If the query is a mutation or named query, you must
                                      supply the op_name.  For annon queries ("{ ... }"),
                                      should be None (default).
        input_data (dict)           - If provided, the $input variable in GraphQL will be set
                                      to this value. If both ``input_data`` and ``variables``,
                                      are provided, the ``input`` field in the ``variables``
                                      dict will be overwritten with this value.
        variables (dict)            - If provided, the "variables" field in GraphQL will be
                                      set to this value.
        headers (dict)              - If provided, the headers in POST request to GRAPHQL_URL
                                      will be set to this value.
        client (django.test.Client) - Test client. Defaults to django.test.Client.
        graphql_url (string)        - URL to graphql endpoint. Defaults to "/graphql".
        login_token (string)        - Sets a token cookie for auth.
    Returns:
        Response object from client
    """
    if client is None:
        client = Client()
    if not graphql_url:
        graphql_url = DEFAULT_GRAPHQL_URL

    body = {"query": query}
    if op_name:
        body["operationName"] = op_name
    if variables:
        body["variables"] = variables
    if input_data:
        if variables in body:
            body["variables"]["input"] = input_data
        else:
            body["variables"] = {"input": input_data}
    
    # Pretty much the only difference in the function to add a token cookie
    if login_token:
        client.cookies = SimpleCookie({"token": login_token})
    else:
        # Since the token persists, send an empty one if the query doesn't
        # explicitly provide login_token.
        client.cookies = SimpleCookie({"token": ""})

    if headers:
        resp = client.post(
            graphql_url, json.dumps(body), content_type="application/json", **headers
        )
    else:
        resp = client.post(
            graphql_url, json.dumps(body), content_type="application/json"
        )
    return resp


class GraphQLTestCaseWithCookies(GraphQLTestCase):
    def query(self, query, op_name=None, input_data=None, variables=None, headers=None, login_token=None):
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