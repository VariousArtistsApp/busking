from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from .models import CustomUser
import json


class UserTests(GraphQLTestCase):
    GRAPHQL_URL = '/graphql'
    
    def test_user_list(self):
        user = CustomUser.objects.create(
            name="aarnav", password="test1234567899999", email="aarnav@test.com",
            location="Berlin, Germany"
        )
        response = self.query(
        '''
        query {
          allUsers {
            id
          }
        }
        ''',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']['allUsers']), 1)

    def test_create_user(self):
        response = self.query(
        '''
        mutation createUser($input: CreateUserInput!){
            createUser(userData: $input){
                user {
                    id
                    name
                    email
                }
            }
        }
        ''',
        op_name="createUser",
        input_data={'name': "Aarnav", "password": "test1234567899999",
                    "email": "asd@example.net", "location": "Berlin, Germany"}
        )
        data = response.json()['data']['createUser']['user']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], "Aarnav")
        self.assertEqual(data['email'], "asd@example.net")
        # self.assertResponseNoErrors(response)