from django.test import TestCase
from busking.utils import GraphQLTestCaseWithCookies
from .models import CustomUser
import json
import uuid
from busking.settings import SECRET_KEY
import jwt
import datetime
from http.cookies import SimpleCookie


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
                "email": generate_fake_email(), "location": "Berlin, Germany", "dob": "01.01.2020"}


class UserTests(GraphQLTestCaseWithCookies):
    GRAPHQL_URL = '/graphql'
    
    def test_user_list(self):
        user = generate_fake_user()
        user['dob'] = "2020-01-01"
        CustomUser.objects.create(
            **user
        )
        response = self.query(
        '''
        query {
          allUsers {
            id
          }
        }
        ''',
        login_token=generate_fake_token().decode('utf-8')
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']['allUsers']), 1)

    def test_create_user(self):
        user = generate_fake_user()
        response = self.query(
        '''
        mutation createUser($input: CreateUserInput!){
            createUser(data: $input){
                user {
                    id
                    name
                    email
                }
            }
        }
        ''',
        op_name="createUser",
        input_data=user
        )
        data = response.json()['data']['createUser']['user']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], user["name"])
        self.assertEqual(data['email'], user["email"])

    def test_create_artist_user(self):
        user = generate_fake_user()
        user['artistName'] = "fakeArtist"
        response = self.query(
        '''
        mutation createArtistUser($input: CreateArtistUserInput!){
            createArtistUser(data: $input){
                user {
                    id
                    name
                    email
                    artistProfile {
                        id
                    }
                }
            }
        }
        ''',
        op_name="createArtistUser",
        input_data=user
        )
        data = response.json()['data']['createArtistUser']['user']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], user['name'])
        self.assertEqual(data['email'], user['email'])
        self.assertNotEqual(data['artistProfile']['id'], None)

    def test_create_label_user(self):
        user = generate_fake_user()
        user['labelName'] = "fakeLabel"
        response = self.query(
        '''
        mutation createLabelUser($input: CreateLabelUserInput!){
            createLabelUser(data: $input){
                user {
                    id
                    name
                    email
                    labelProfile {
                        id
                    }
                }
            }
        }
        ''',
        op_name="createLabelUser",
        input_data=user
        )
        data = response.json()['data']['createLabelUser']['user']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], user['name'])
        self.assertEqual(data['email'], user['email'])
        self.assertNotEqual(data['labelProfile']['id'], None)