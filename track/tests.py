from django.test import TestCase
from busking.utils import GraphQLTestCaseWithCookies
from user.models import CustomUser
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


class TrackTest(GraphQLTestCaseWithCookies):
    GRAPHQL_URL = '/graphql'

    def test_track_create(self):
        user = generate_fake_user()
        user['dob'] = "2020-01-01"
        CustomUser.objects.create(
            **user
        )
        fake_track = {
            "name": "Temptress (Original Mix)",
            "artistName": "Permanent Daylight",
            "cost": 199,
            "file": "http://va.app/static/something"
        }
        response = self.query(
        '''
        mutation createTrack($input: CreateTrackInput!){
            createTrack(data: $input){
                track {
                    name
                    id
                }
            }
        }
        ''',
        op_name="createTrack",
        input_data=fake_track,
        login_token=generate_fake_token().decode('utf-8')
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['data']['createTrack']['track']['name'], "Temptress (Original Mix)")
