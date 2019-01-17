
# tweepy module is used to access the twitter via API
import tweepy as tp
import time
import os


# credentials to login to twitter api
consumer_key = 'SugWbSEqzKIFk0DZq8A4CoHK7'
consumer_secret = 'z5wmHWCP7aFZDvO1F5nNsKTdMSY9ihSCplloeE3Ad0ppkj0TCr'
access_token = '1083153464383827968-m3CHBwkLCchZCquYcIbBxANbmX5GNK'
access_secret = 'O0gEHk0B71qxpGf4p7UZiDMlSDQD92zDVgkJgqAK6n6S8'

# login to twiiter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# iterates over pictures in model folder
os.chdir('models')
for model_image in os.listdir('.'):
    api.update_with_media(model_image)
    time.sleep(5)

