########################################################################
# 3: homework 10
# See iPython notebook in Soma's email!

########################################################################
# 4: the New York Times developer API


# Go to http://developer.nytimes.com/

# Register.

# Request a key for everything, because why not.

# You get a page with a key for each API. Take care to use the right key with the right API.
# Check out the calls per second, calls per day. The API limits how many calls you can make so you don't take down their website, but the limits are quite reasonable.


# 0: a list of all APIs:
# http://developer.nytimes.com/docs

# The documentation is way better than forecast.io
# and you also have the API CONSOLE to test/build queries:
# http://developer.nytimes.com/io-docs

	# You can add QUERY PARAMETERS to your API calls:
	# When you have a URL and you want to pass extra information to the website
	# urlurlurl.com/blahblah?key=value&key2=value2&key3=value3
	# e.g.
	# https://search.yahoo.com/search?p=dogs&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-901&fp=1


# 1: the ARTICLE SEARCH API:
# http://developer.nytimes.com/docs/read/article_search_api_v2

# Copy your article search API key.

oururl = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=gay+marriage&api-key=ffaf60d7d82258e112dd4fb2b5e4e2d6:3:72421680"
#OR,
import urllib
oururl = "http://api.nytimes.com/svc/search/v2/articlesearch.json?"+urllib.urlencode( { 
	'q':'gay marriage',
	'api-key':'ffaf60d7d82258e112dd4fb2b5e4e2d6:3:72421680',
} )

import requests
ourresponse = requests.get( oururl ) # <class 'requests.models.Response'>
ourdata = ourresponse.json() # <type 'dict'>
#OR,
import urllib2
ourresponse = urllib2.urlopen( oururl )
ourcontent = ourresponse.read() # You can `.read()` only once.
import json
ourdata = json.loads( ourcontent ) # <type 'dict'>


print ourdata.keys() # [u'status', u'response', u'copyright']

print ourdata['status'] # u'OK'
print ourdata['copyright'] # u'Copyright (c) 2013 The New York Times Company.  All Rights Reserved.'
print ourdata['response'] # <type 'dict'>
print ourdata['response'].keys() # [u'docs', u'meta']

print ourdata['response']['meta'] # {u'hits': 19821, u'offset': 0, u'time': 36}
print ourdata['response']['meta']['hits'] # HOW MANY ARTICLES THERE ARE

print ourdata['response']['docs'] # <type 'list'>
print len( ourdata['response']['docs'] ) # only returns 10 articles at a time

print ourdata['response']['docs'][0] # <type 'dict'>

print ourdata['response']['docs'][0].keys() # [u'type_of_material', u'blog', u'news_desk', u'lead_paragraph', u'headline', u'abstract', u'print_page', u'word_count', u'_id', u'snippet', u'source', u'web_url', u'multimedia', u'subsection_name', u'keywords', u'byline', u'document_type', u'pub_date', u'section_name']

print ourdata['response']['docs'][0]['lead_paragraph'] # u'Justice Kennedy, the onetime altar boy from Sacramento and conservative Republican, has advanced legal equality for gays more than any other American jurist.'


# getting ALL the articles (for a given query, begin_date, end_date)
import urllib
import requests
articlelist = []
p = 0
while True:
	oururl = "http://api.nytimes.com/svc/search/v2/articlesearch.json?"+urllib.urlencode( { 
		'q':'"gay marriage"',
		'page':p, # offsetting by 10*p articles (by p pages)
		'begin_date':19970101,
		'end_date':19971231,
		'api-key':'ffaf60d7d82258e112dd4fb2b5e4e2d6:3:72421680',
	} )
	ourresponse = requests.get( oururl )
	ourdata = ourresponse.json()
	articlelist += ourdata['response']['docs']
	#
	if p == 0:
		numpages = ourdata['response']['meta']['hits']/10.0
	p += 1
	if numpages < p:
		break

print articlelist
print len( articlelist ) # 17
# all the headlines
print [ a['headline']['main']  for a in articlelist ] # [u'Gay Marriage Debate', u'Hawaii Seeks Law to Block Gay Marriage', u'Why Does State Care About Gay Marriage?', u'Worms In the Apple', u"A Mother's Perspective On 'Family Values'", u'God Is My Co-Counsel', u"Messinger's Two Opponents Accuse Her of Superficiality", u'For Sharpton, Debates in Mayor Race Can Be Fun', u'Second Thoughts On Cloning', u'Clinton Is Greeted Warmly as He Speaks to Gay Group', u"States' Rights Lose Some of Their High", u'Consuming Passions', u"Court to Weigh States' Legal Reciprocity", u'NEWS SUMMARY', u"On Adultery Issue, Many Aren't Ready To Cast First Stone", u"A Moderate's Moment", u'The Clinton Principle']


# 2: the BEST-SELLER API:
# http://developer.nytimes.com/docs/books_api/Books_API_Best_Sellers
