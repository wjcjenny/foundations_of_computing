########################################################################
# APIs

# API: application programming interface
# When we want to get data from the outside world, APIs make it easier.
# Basically an API gives you data that's formatted so that it's easy for computers to read (as opposed to a webpage, which is data that's formatted so that it's easy for humans to read in a browser).

# Scraping is what we do for websites without an API; scraping is generally harder and takes longer.


# Examples of APIs:
# http://developer.nytimes.com/docs
	# http://data-gov.tw.rpi.edu/wiki/How_to_use_New_York_Times_Article_Search_API
	# Courtesy of Mr. Tian Chuan, with the message "That article this outdated! Ouch!"
# https://sunlightfoundation.com/api/
# http://www.census.gov/data/developers/data-sets.html


########################################################################
# Let's try getting data from http://forecast.io/

import urllib2
ourresponse = urllib2.urlopen( "http://forecast.io/" ) # <addinfourl at 4342369456 whose fp = <socket._fileobject object at 0x1004ec0d0>> # This describes what language the webpage is in, how big it is, what file format, blah blah blah, the stuff your browser cares about.
ourcontent = ourresponse.read() # the HTML (It's actually the raw HTML before any JavaScript is executed)
# Neither forms are really useful to us.


# Instead, we use its API:

# Google `forcast.io API`
# https://developer.forecast.io/

# Register

# Ignore what it says about entering your billing information
# Click on https://api.forecast.io/forecast/apikeyapikeyapikeyapikeyapikey/37.8267,-122.423
# It looks a lot like a dictionary! Actually it's JSON.

	# JSON: JavaScript Object Notation
	# JSON is a data-interchange format looks a lot like a Python dictionary.
	# http://json.org/


# So what does it mean?
# On https://developer.forecast.io/
# click Documentation: https://developer.forecast.io/docs/v2

# The following API call returns the current forecast (for the next week):
# https://api.forecast.io/forecast/apikeyapikeyapikeyapikeyapikey/37.8267,-122.423
	# apikeyapikeyapikeyapikeyapikey is the API key; a way of attaching you to what you do with the API (different for every user)
	# 37.8267,-122.423 is latitude and longitude

# The following API call returns a forecast from a specific time, past or future:
# https://api.forecast.io/forecast/apikeyapikeyapikeyapikeyapikey/37.8267,-122.423,1435604340
	# 1435604340 is unix time
		# UNIX TIME / EPOCH TIME: seconds since Jan 1, 1970 (UTC)
		# http://www.unixtimestamp.com/index.php


import urllib2
ourresponse = urllib2.urlopen( "https://api.forecast.io/forecast/apikeyapikeyapikeyapikeyapikey/37.8267,-122.423" )
ourcontent = ourresponse.read()

# `ourcontent` is just a string that looks like a dictionary, so we want to turn it into a dictionary.
# In iPython notebook, type `json.` and hit the tab key
# Or Google `how to parse json with the json module in python`
import json
ourdata = json.loads( ourcontent ) # <type 'dict'>


# Let's look what's in `ourdata`. You can keep chaining this stuff forever:

print type( ourdata ) # <type 'dict'>


print ourdata.keys() # [u'hourly', u'alerts', u'currently', u'longitude', u'flags', u'daily', u'offset', u'latitude', u'timezone', u'minutely']
	# CHARACTER ENCODING:
	# `u'blah blah blah'` means it's a UNICODE string
	# Includes all possible characters: http://unicode-table.com/
	# Python 2 is horrible with unicode. Guesses if string is unicode or ascii or whatever.
	# Most of the time, you can just ignore the difference:
print 'hourly' == u'hourly' # True

print ourdata["flags"] # <type 'dict'>

print ourdata["minutely"] # <type 'dict'>


print ourdata["minutely"].keys() # [u'icon', u'data', u'summary']

print ourdata["minutely"]["summary"] # <type 'str'>
# which is the same as
minutely = ourdata["minutely"]
print minutely["summary"]

print ourdata["minutely"]["data"] # <type 'list'>
# which is the same as
minutely = ourdata["minutely"]
print minutely["data"]


print ourdata["minutely"]["data"][2] # <type 'dict'>
# which is the same as
minutely = ourdata["minutely"]
data = minutely["data"]
print data[2]


print ourdata["minutely"]["data"][2]["time"] # <type 'int'>
# which is the same as
minutely = ourdata["minutely"]
data = minutely["data"]
thirddata = data[2]
print thirddata["time"]


########################################################################
# Let's use the Twitter API.
# This is an API where you can send stuff, not just receive stuff.
# OAuth can drive you crazy.



# Instructions with pictures are here:
# https://github.com/ledeprogram/courses/blob/master/algorithms/twitter.md



# 1: If you don't already have a Twitter account, create one. This is your REAL account.

# Also add your phone number to your account. This is necessary for our bot to write to Twitter.
# Go to https://twitter.com/settings/devices
# Click Mobile on the left
# Add your number



# 2: You "make an app" from that REAL Twitter account, meaning that you fill out a form (Don't ask).

# Logged into your REAL account, go to
# https://apps.twitter.com/
# Click the Create New App button

# "Don't stress too much about your application details, you're going to be the only one seeing them. They're mostly important if you're getting other people to sign up for your application."
	# Name can be anything
	# Description can be anything, just make it more than 10 characters
	# Website can be anything: example.com
	# Callback URL (The URL we return to after successfully authenticating) can be blank; we're doing this all by hand so we don't need it.

# Click on the Permissions tab
# For Access, select Read and Write
	# Read and Write might not be availble if you didn't add a phone number. You get
	# Error: You must add your mobile phone to your Twitter profile before creating an application. Please read https://support.twitter.com/articles/110250-adding-your-mobile-number-to-your-account-via-web for more information.
	# Go to https://twitter.com/settings/devices
	# Click Mobile on the left
	# Add your number

# Click on the Keys and Access Tokens tab
# Copy your API keys
	# Don't accidently put your api key on GitHub! There are bots out there that scrape secret api keys from new GitHub pushes.

# In your code, 
# create variables called `consumer_token` and `consumer_secret` ("because all code ever made ever in history ever ever calls them `consumer_token` and `consumer_secret`") and paste your API keys as values
consumer_token = 'consumertokenconsumertoken'
consumer_secret = 'consumersecretconsumersecretconsumersecret'



# 3: You make a new, DUMMY Twitter acount (your robot)

# "Your Twitter bot needs to use a different account than your real, live primary account. You'll need to sign out of your main Twitter account and create a new account."
# Go to https://twitter.com/signup
	# For the email, you can use PLUS ADDRESSING.
	# After your real email username add +blahblahblah, like jonathan.soma+weatherbotgarbage@gmail.com
	# This way you can sign up for multiple Twitter accounts with just one email account. Twitter thinks it's a separate email account, but you'll get Twitter's emails in one email account.
# Ignore it when it asks you for a phone number, and just go to twitter.com

	# OR for this exercise you can use username: kasdkjn332449d password: lkm398iojLKSA



# 4: Authenticate with Twitter using Tweepy from your DUMMY Twitter account

# In the terminal, run
# `pip install tweepy`
	# If it complains about permissions, run
	# `sudo pip install tweepy`
	# and enter your password if it asks
# We are installing Tweepy (http://www.tweepy.org/)
# We installed Anaconda never to install anything again, but Anaconda is for scientific/mathematic stuff and apparently Twitter stuff is NOT. So we have to install Tweepy with `pip` and NOT `conda`.


# In your code, using the `consumer_token` and `consumer_secret` from before,
import tweepy
consumer_token = 'consumertokenconsumertoken'
consumer_secret = 'consumersecretconsumersecretconsumersecret'
ourauth = tweepy.OAuthHandler( consumer_token,consumer_secret )
	# If Tweepy is giving you an authorization error (http://stackoverflow.com/questions/29803645/403-error-with-tweepy), type
	# ourauth = tweepy.OAuthHandler( consumer_token,consumer_secret,secure=True )
# get the authorization URL
print ourauth.get_authorization_url()

# Run the code,
# copy the URL you get.


# In your browser,
# logged into your DUMMY account
# go to the URL you got from above
	# If you get an error, run the above again; you might have timed out
# Click on the Authorize App button
# Copy the pin


# In your code,
# paste the pin from before as value to a variable `ourpin`
# and add
ourpin = '1111111111'
print ourauth.get_access_token( verifier=ourpin )

# Run the code,
# and you will get a tuple of 2 strings, like (u'accesstokenaccesstokenaccesstokenaccesstoken', u'accesssecretaccesssecretaccesssecret')
# Copy the strings you get.

	# You also could have done
	## ourtoken = ourauth.get_access_token( verifier=ourpin )
	## access_token = ourtoken[0] # ourtoken.key for older version of Tweepy
	## access_secret = ourtoken[1] # ourtoken.secret for older version of Tweepy
	# But you don't want to authenticate more than once, so the above is preferred.



# 5: Authorize your app to use that DUMMY Twitter account, and do stuff!

# In your code,
# create variables called `access_token` and `access_secret` and paste the strings from before as values paste the strings from before,
# and type
import tweepy
consumer_token = 'consumertokenconsumertoken'
consumer_secret = 'consumersecretconsumersecretconsumersecret'
access_token = 'accesstokenaccesstokenaccesstokenaccesstoken'
access_secret = 'accesssecretaccesssecretaccesssecret'
ourauth = tweepy.OAuthHandler( consumer_token,consumer_secret )
ourauth.secure = True
ourauth.set_access_token( access_token,access_secret )
ourapi = tweepy.API( ourauth )


# Now you can do stuff with it!

# If you want to tweet from your DUMMY account:
ourapi.update_status( status="hello world" )
	# You might get
	# tweepy.error.TweepError: Read-only application cannot POST.
	# There's an an issues page on GitHub, and this page too https://twittercommunity.com/t/read-only-application-cannot-post-error/511/21

# If you want to search for tweets:
tweets = ourapi.search( q="supreme court") # q for query
print tweets
print len( tweets ) # only 15
print tweets[0]
print type( tweets[0] ) # tweepy.models.Status
print tweets[0].text # the text of the tweet
	# what's the ranking of the tweets? By time?

# http://tweepy.readthedocs.org/en/v2.3.0/api.html#tweepy-api-twitter-api-wrapper
