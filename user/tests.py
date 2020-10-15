from busking.test.utils import (GraphQLTestCaseWithCookies,
                                generate_fake_token, generate_fake_user)

from .models import CustomUser


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
        mutation createUser($input: CreateUserInput!){
            createUser(data: $input){
                user {
                    id
                    name
                    email
                    artistProfile {
                        id
                        name
                    }
                }
            }
        }
        ''',
            op_name="createUser",
            input_data=user
        )
        data = response.json()['data']['createUser']['user']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], user['name'])
        self.assertEqual(data['email'], user['email'])
        self.assertNotEqual(data['artistProfile']['id'], None)

    def test_create_label_user(self):
        user = generate_fake_user()
        user['labelName'] = "fakeLabel"
        response = self.query(
            '''
        mutation createUser($input: CreateUserInput!){
            createUser(data: $input){
                user {
                    id
                    name
                    email
                    labelProfile {
                        id
                        name
                    }
                }
            }
        }
        ''',
            op_name="createUser",
            input_data=user
        )
        data = response.json()['data']['createUser']['user']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], user['name'])
        self.assertEqual(data['email'], user['email'])
        self.assertNotEqual(data['labelProfile']['id'], None)
