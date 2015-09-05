__author__ = 'GreyBerry'
from lxml import html
import requests
import re
import os
import tweepy
import time

# Set Environment Variables into variable
WEBSITE = os.environ.get('WEBSITE')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

# Set Authentification with twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while 1:
    page = requests.get(WEBSITE)
    tree = html.fromstring(page.text)

    # Contains
    month =  tree.xpath('//span[@class="txtdata"]/text()')

    # Get the 6th element of the month element.
    total_month_result = month[5]
    msg = None
    match = re.match(r'(\d+\.\d+)\sG',total_month_result)
    total_month = match.group(1)

    if float(total_month) < (150*0.10):
        msg = "everything is ok, below 10%"
    elif float(total_month) < (150*0.20):
        msg = "everything is ok, below 20%"
    elif float(total_month) < (150*0.30):
        msg = "everything is ok, below 30%"
    elif float(total_month) < (150*0.40):
        msg = "everything is ok, below 10%"
    elif float(total_month) < (150*0.50):
        msg = "everything is still ok, below 50%"
    elif float(total_month) < (150*0.60):
        msg = "everything is still ok but you have to watch, below 60%"
    elif float(total_month) < (150*0.70):
        msg = "everything is still ok but check your internet limit, below 70%"
    elif float(total_month) < (150*0.80):
        msg = "You better see if you need a block, below 80%"
    elif float(total_month) < (150*0.90):
        msg = "YOU HAVE TO BUY A BLOCK, below 90% !!"
    msg += " @goku417"

    # Update status on bun's bot
    api.update_status(status=msg)
    time.sleep(86400)
