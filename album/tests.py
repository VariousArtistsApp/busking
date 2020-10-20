from album.models import Album
from artist.models import Artist
from busking.test.utils import (GraphQLTestCaseWithCookies,
                                generate_fake_token, generate_fake_user)
from label.models import Label
from track.models import Track
from user.models import CustomUser


class ReleaseTests(GraphQLTestCaseWithCookies):
    GRAPHQL_URL = '/graphql'

    def test_create_release(self):
        user = generate_fake_user()
        user['dob'] = "2020-01-01"
        CustomUser.objects.create(
            **user
        )
        Label.objects.create(name='Fleisch', email='fleisch@va.app')
        release = Album.objects.create()
        track_one = Track.objects.create(name="Temptress")
        track_two = Track.objects.create(name="My Tourist Dystopia")
        artist = Artist.objects.create(name="asdf123")
        response = self.query(
            '''
        mutation updateRelease($input: UpdateReleaseInput!) {
          updateRelease(data: $input) {
            release {
                id
                name
                tracks {
                    id
                    name
                    price
                }
            }
          }
        }
        ''',
            login_token=generate_fake_token().decode('utf-8'),
            op_name="updateRelease",
            input_data={
                "id": str(release.id),
                "name": "Temptress",
                "date": "06.08.2020",
                "credits": "Mixed by Aarnav, Mastered by Aarnav. W+P Aarnav",
                "tracks": [{
                    "name": "Temptress",
                    "price": 0.99,
                    "id": str(track_one.id),
                    "artists": [str(artist.id)]
                }, {
                    "name": "My Tourist Dystopia",
                    "price": 0.99,
                    "id": str(track_two.id),
                    "artists": [str(artist.id)]
                }]

            })
        response = response.json()['data']['updateRelease']['release']
        self.assertEqual(response['id'], str(release.id))
        self.assertEqual(response['tracks'][0]['id'], str(track_one.id))
        self.assertEqual(response['tracks'][1]['id'], str(track_two.id))
