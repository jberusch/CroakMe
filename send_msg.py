# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC394a8d90ef1b41c65531a1cf2e879b85'
auth_token = '0562e0319dd5fdc63f9d13023d4b2a5d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Remember, you're going to die. Don't forget!",
                     from_='+12165022834',
                     to='+12165448688'
                 )