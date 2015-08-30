########################################################################
# 1: do now

# 1) What's the difference between an API and a normal web page?

# When we want to get data from the outside world, APIs make it easier.
# Basically an API gives you data that's formatted so that it's easy for computers to read (as opposed to a webpage, which is data that's formatted so that it's easy for humans to read in a browser).
# An API is built to transfer nothing but data. No ads, no unnecessary stuff.


# 2) If I have a variable called url, what are the two steps to opening it using urllib2 and reading out the contents?

import urllib2
url = "https://api.forecast.io/forecast/2c680d7472ed0e72a5750bf8ab239057/40.7127,-74.0059"
# Grab the webpage
ourresponse = urllib2.urlopen( url )
# Grab the contents of the webpage
ourcontent = ourresponse.read()


# 3) When an API sends over dictionaries or lists or integers or anything, it's all just text. What's the format this text uses to represent the data inside?

# JSON
import json
ourdata = json.loads( ourcontent )


# We could combine 2) and 3) in a function:
import urllib2
import json
def datafromurl1( url ):
	# Grab the webpage
	ourresponse = urllib2.urlopen( url )
	# Grab the contents of the webpage
	ourcontent = ourresponse.read()
	# Convert the string into a json
	return json.loads( ourcontent )
	
ourdata = datafromurl1( "https://api.forecast.io/forecast/2c680d7472ed0e72a5750bf8ab239057/40.7127,-74.0059" )

# OR,

import requests
def datafromurl2( url ):
	ourresponse = requests.get( url )
	return ourresponse.json()

ourdata = datafromurl2( "https://api.forecast.io/forecast/2c680d7472ed0e72a5750bf8ab239057/40.7127,-74.0059" )


# 4) Here is some strange and unknown code! Using your knowledge of Python and the power of Google, try to figure out what each line might accomplish.

# Download 'haarcascade_default.xml' from Slack
# and put it in the same folder as this .py file

# OpenCV (http://opencv.org/) comes with Anaconda
# In the terminal, run
## conda install opencv

# Move to the same folder as this .py file, and run this:
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

# `cv2.VideoCapture( 0 )` probably opens up your camera
camera_port = 0
camera = cv2.VideoCapture( camera_port )
# FACE DETECTION
# Google `cv2.CascadeClassifier()`, `'haarcascade`
face_cascade = cv2.CascadeClassifier( 'haarcascade_default.xml' )

# `while` is a kind of loop (like `for`)
# It runs the code below it as long as what comes after `while` is true
while(True):
	# `retval` is probably "return value", `img` is probably an image returned from `camera.read()`
	retval,img = camera.read()

	# FACE DETECTION
	# `gray` is probably the image `img` converted to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	# `.detectMultiScale()` probably detects faces
	faces = face_cascade.detectMultiScale( gray,minSize=(20,20) )
	for (x,y,w,h) in faces:
		# This probably draws a rectangle around each face that's found
		cv2.rectangle( img, (x,y),(x+w,y+h), (255,0,0), 2 )

	# `cv2.imshow()` probably shows the image `img`
	cv2.imshow( 'frame',img )

	if cv2.waitKey( 1 ) & 0xFF == ord( 'q' ):
		# break out of the loop
		break