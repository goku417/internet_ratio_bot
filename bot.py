__author__ = 'GreyBerry'
from lxml import html
import requests
import re
import os
import tweepy
import time
import random

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
    try:
        page = requests.get(WEBSITE)
        tree = html.fromstring(page.text)

        # Contains
        month =  tree.xpath('//span[@class="txtdata"]/text()')
        available = tree.xpath('//div[@style="padding-top:3px;"]/text()')

        # Get the 6th element of the month element.
        total_month_result = month[5]
        total_available_result = available[3]
        msg = None
        match_month = re.match(r'(\d+\.\d+)\sG',total_month_result)
        total_month = match_month.group(1)
        match_available = re.match(r'\s(\d+\.\d+)\sG',total_available_result)
        total_available = match_available.group(1)

        if float(total_month) < float(140) and float(total_available) > float(10):
            msg = "everything is ok, you're at " + str(float(total_month)/float(150)*100) + \
                  "%. Available: "+ str(total_available) +"G. @goku417"
        elif float(total_month) < float(150) and float(total_available) <= float(10):
            msg = "This is critical, you're at " + str(float(total_month)/float(150)*100) + \
                  "%. You have to buy a block now! @goku417"

        # Update status on bun's bot
        api.update_status(status=msg)
    except:
        msg = None
        string_list = ['Everything seems like yesterday.', 'Yep same like yesterday.', 'Nothing change.',
                       'You\'re not using your Internet :P', 'Same as yesterday.', 'Everything is fine.',
                       'Everything is ok!', 'You can go check but i tell you, everything is fine']
        number = random.randint(0, len(string_list) - 1)
        msg = string_list[number] + ' @goku417'
        api.update_status(status=msg)

    time.sleep(86400)