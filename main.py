import time
import math
import random
import schedule
from twilio.rest import Client

account_sid = 'AC394a8d90ef1b41c65531a1cf2e879b85'
auth_token = '0562e0319dd5fdc63f9d13023d4b2a5d'
client = Client(account_sid, auth_token)

# insert great quotes here
messages = ['What\'s next?', 'What\'s the worst that could happen']

def send_death_msg():
	print("Sending message...")
	message = client.messages \
        .create(
             body="Remember, you're going to die. Don't forget! " + messages[int(math.floor(random.random() * len(messages)))],
             from_='+12165022834',
             to='+12165448688'
         )

# schedule.every().minutes.do(send_death_msg)
times = ["08:30", "14:00", "20:00", "23:00", "16:21"]
for t in times:
    print("scheduling message to send at time: " + str(t))
    schedule.every().day.at(t).do(send_death_msg)

while True:
	schedule.run_pending()
	time.sleep(1)
