# HOMEWORK 8

### First, tips:


#Be careful that you're doing all of your math with ints or floats instead of strings that look like ints or floats.
#When you write your functions, you can pass either the entire dictionary to the function 
#OR just the part you're curious about (e.g., when you're getting the day you could send the whole earthquake dictionary or just what's in the 'time' key.)
#Writing empty functions that always return the same thing are a great way to start off. 
#You can start saying every earthquake is shallow and then fill in the actual code later.

### PART ONE: Write the eq_to_sentence function
#Given an earthquake defined like this...

earthquake = {
      'rms': '1.85', 
      'updated': '2014-06-11T05:22:21.596Z', 
      'type': 'earthquake', 
      'magType': 'mwp', 
      'longitude': '-136.6561', 
      'gap': '48', 
      'depth': '10', 
      'dmin': '0.811', 
      'mag': '5.7', 
      'time': '2014-06-04T11:58:58.200Z', 
      'latitude': '59.0001', 
      'place': '73km WSW of Haines, Alaska', 
      'net': 'us', 
      'nst': '', 
      'id': 'usc000rauc'}


#I want to be able to run
#    print eq_to_sentence(earthquake)

#and get the following:

#> A DEPTH DESCRIPTION, MAGNITUDE earthquake was reported DAY TIME_OF_DAY on DATE.

#So, for example, "A deep, huge 4.5 magnitude earthquake was reported Monday morning on June 22".

#DEPTH, DESCRIPTION, MAGNITUDE, DAY, and TIME_OF_DAY should all come from separate functions. 
#So you will probably have an eq_description and an eq_time_of_day, etc

#DEPTH can be determined from the USGS website - http://earthquake.usgs.gov/learn/topics/seismology/determining_depth.php 
#- it should be either 'shallow', 'intermediate' or 'deep'
def eq_depth(depth):
  if 70 > depth > 0:
    return "Shallow"
  elif 300 > depth:
    return "Intermediate"
  else:
    return "Deep"
depth = earthquake["depth"]
#print eq_depth(10)

#DESCRIPTION can be something like 'easily ignored' or 'huge' or 'very destructive' (feel free to pick your own) - 
#look on Google Image Search for "richter scale" to see some possible descriptors.
def eq_description(depth):
  if 70 > depth > 0:
    return "easily ignored"
  elif 300 > depth:
    return "huge"
  else:
    return "very destructive"
depth = earthquake["depth"]
#print eq_description(10)

#MAGNITUDE should be the actual numerical magnitude.
eq_magnitude = earthquake["mag"]
#print eq_magnitude

#DAY should be the day of the week.
import dateutil.parser
happend_at = '2014-06-04T11:58:58.200Z'
date = dateutil.parser.parse(happend_at)
#print date
#2014-06-04 11:58:58.200000+00:00
eq_day = date.strftime("%A")
#print eq_day
#Wednesday

#TIME_OF_DAY should be morning, afternoon, evening or night.
def eq_time_of_day(time_of_day):
  if 12 > time_of_day > 0:
    return "Morning"
  elif 18 > time_of_day:
    return "Afternoon"
  elif 22 > time_of_day:
    return "Evening"
  elif 24 > time_of_day:
    return "Night"
time_of_day = date.strftime("%H")
#print eq_time_of_day(time_of_day)

#DATE should be "Monthname day", e.g. "June 22".
eq_date = date.strftime("%B %d")
#print eq_date


def eq_to_sentence(qwerty):
  date = dateutil.parser.parse(qwerty['time'])
  return "A "+eq_depth(float(qwerty["depth"]))+" "+qwerty["mag"]+" earthquake was reported "+date.strftime("%A")+" "+eq_time_of_day(int(date.strftime("%H")))+" on "+date.strftime("%B %d")+"."
print eq_to_sentence(earthquake)


### PART TWO: Doing it in bulk
# Read in the csv of the past 30 days of 1.0+ earthquke activity from http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv
# Loop through each earthquake, printing sentence descriptions for the ones that are above or equal to 4.0 on the Richter scale.
import csv
ourfile = open( "1.0_month.csv" )
earthqukedicts = list( csv.DictReader( ourfile ) ) # list of dictionaries
print type( earthqukedicts )
#list

#so first need to write for loop to grab every dictionaries in this list
for earthquake in earthqukedicts:
	if float(earthquake['mag']) >= 4.0:
		print eq_to_sentence(earthquake)


### PART THREE: The other bits

# If the earthquake is anything other than an earthquake (e.g. explosion or quarry blast), print

#     There was also a magnitude MAGNITUDE TYPE_OF_EVENT on DATE LOCATION.
 
# For example,

# > There was also a magnitude 1.29 quarry blast on June 19 12km SE of Tehachapi, California.

# with TYPE_OF_EVENT being explosion, quarry blast, etc and LOCATION being 'place' - e.g. '0km N of The Geysers, California'.
'''
EG = {
  'rms': '0.09', 
  'updated': '2015-05-27T22:13:25.153Z',
  'type': 'quarry blast', 
  'magType': 'ml', 
  'longitude': '-118.356',
  'gap': '78', 
  'depth': '0.01',
  'dmin': '0.06256', 
  'mag': '1.46',
  'time': '2015-05-27T18:09:32.980Z',
  'latitude': '35.0521667',
  'place': '12km SE of Tehachapi, California',
  'net': 'ci',
  'nst': '13',
  'id': 'ci37388360'}
'''

def sentence(qwerty):
	date = dateutil.parser.parse(qwerty['time'])
#  return "A "+eq_depth(float(qwerty["depth"]))+" "+qwerty["mag"]+" earthquake was reported "+date.strftime("%A")+" "+eq_time_of_day(int(date.strftime("%H")))+" on "+date.strftime("%B %d")+"."
	return "There was also a magnitude"+qwerty["mag"]+" "+earthquake['type']+"on"+date.strftime("%B %d")+earthquake['place']+"."

for earthquake in earthqukedicts:
	if earthquake['type'] != 'earthquake':
		print sentence(earthquake)
















