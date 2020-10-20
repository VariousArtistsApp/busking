from busking.test.utils import (GraphQLTestCaseWithCookies,
                                generate_fake_token, generate_fake_user)
from user.models import CustomUser


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
            "price": 199,
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
        self.assertEqual(data['data']['createTrack']['track']['name'], "Temptress (Original Mix)")  # noqa E501
