import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from busking.test.utils import generate_fake_user
from label.models import Label
from user.models import CustomUser


class UploadTests(TestCase):
    def test_label_profile_upload(self):
        user = generate_fake_user()
        user['dob'] = "2020-01-01"
        user = CustomUser.objects.create(
            **user
        )
        label = Label.objects.create(name="Fleisch", email=user.email)
        user.label_profile = label
        user.save()
        with open("{0}/upload/2.png".format(os.getcwd()), "rb") as file:  # noqa F841
            response = self.client.post("/upload/profilePicture", {
                "id": label.id,
                "type": "label",
                "profile_picture": SimpleUploadedFile("2.png",
                                                      b"joemama",
                                                      # file.read(),
                                                      content_type="image/png"),  # noqa E501
            })
            response = response.json()
            self.assertEqual(response["response"], "success")
            self.assertNotEqual(response["picture_url"], None)

    def test_label_track_upload(self):
        user = generate_fake_user()
        user['dob'] = "2020-01-01"
        user = CustomUser.objects.create(
            **user
        )
        label = Label.objects.create(name="Fleisch", email=user.email)
        user.label_profile = label
        user.save()
        with open("{0}/upload/2.png".format(os.getcwd()), "rb") as file:  # noqa F841
            response = self.client.post("/upload/tracks", {
                "profile_id": label.id,
                "album_id": "123wdfwsgesrgserg",
                "type": "Label",
                "2.wav": SimpleUploadedFile("2.wav",
                                            b"joemama",
                                            # file.read(),
                                            content_type="image/png"),
            })
            response = response.json()
            self.assertEqual(response["response"], "success")
            self.assertNotEqual(response["track"], None)
