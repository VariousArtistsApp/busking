## Busking

Schema subject to change as it's yet to be finalized.

# Set up:

```
git clone https://github.com/VA/busking
cd busking

# create & activate your env. Python 3.8 recommended.
pip3 install -r requirements.txt

touch busking/.env
vim busking/.env


# PLEASE NOTE THAT WE DO NOT USE AWS! DIGITAL OCEAN HAS AN OBJECT STORE WITH AN S3 API.
DEBUG=
SECRET_KEY=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_ENDPOINT_URL=
AWS_LOCATION=
AWS_S3_OBJECT_CACHE_CONTROL=
POSTGRES_DB_PASS=
POSTGRES_DB_USERNAME=
POSTGRES_DB_HOST=
PAYPAL_CLIENT_ID=
PAYPAL_CLIENT_SECRET=


./manage.py makemigrations
./manage.py migrate
```
