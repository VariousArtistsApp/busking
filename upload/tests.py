from django.test import TestCase
from user.models import CustomUser
from label.models import Label
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
import os


def generate_fake_email():
    return "{}@va.app".format(uuid.uuid4().hex)


def generate_fake_user():
    return {'name': uuid.uuid4().hex, "password": "test1234567899999",
            "email": generate_fake_email(), "location": "Berlin, Germany",
            "dob": "01.01.2020"}
                

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
        with open("{0}/upload/2.png".format(os.getcwd()), "rb") as file:
            response = self.client.post("/upload/profilePicture", {
                "id": label.id,
                "type": "label",
                "profile_picture": SimpleUploadedFile("2.png",
                                        b"joemama",
                                        #file.read(),
                                          content_type="image/png"),
            })
            response = response.json()
            self.assertEqual(response["response"], "success")
            self.assertNotEqual(response["picture_url"], None)