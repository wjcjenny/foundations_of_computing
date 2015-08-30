# HOMEWORK 8

### First, tips:

Be careful that you're doing all of your math with ints or floats instead of strings that look like ints or floats.

When you write your functions, you can pass either the entire dictionary to the function OR just the part you're curious about (e.g., when you're getting the day you could send the whole earthquake dictionary or just what's in the 'time' key.)

Writing empty functions that always return the same thing are a great way to start off. You can start saying every earthquake is shallow and then fill in the actual code later.

### PART ONE: Write the eq_to_sentence function

Given an earthquake defined like this...

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
  
I want to be able to run

    print eq_to_sentence(earthquake)

and get the following:

> A DEPTH DESCRIPTION, MAGNITUDE earthquake was reported DAY TIME_OF_DAY on DATE.

So, for example, "A deep, huge 4.5 magnitude earthquake was reported Monday morning on June 22".

DEPTH, DESCRIPTION, MAGNITUDE, DAY, and TIME_OF_DAY should all come from separate functions. So you'll probably have an eq_description and an eq_time_of_day, etc

DEPTH can be determined from the USGS website - http://earthquake.usgs.gov/learn/topics/seismology/determining_depth.php - it should be either 'shallow', 'intermediate' or 'deep'

DESCRIPTION can be something like 'easily ignored' or 'huge' or 'very destructive' (feel free to pick your own) - look on Google Image Search for "richter scale" to see some possible descriptors.

MAGNITUDE should be the actual numerical magnitude.

DAY should be the day of the week.

TIME_OF_DAY should be morning, afternoon, evening or night.

DATE should be "Monthname day", e.g. "June 22".


### PART TWO: Doing it in bulk

Read in the csv of the past 30 days of 1.0+ earthquke activity from http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv

Loop through each earthquake, printing sentence descriptions for the ones that are above or equal to 4.0 on the Richter scale.


### PART THREE: The other bits

If the earthquake is anything other than an earthquake (e.g. explosion or quarry blast), print

    There was also a magnitude MAGNITUDE TYPE_OF_EVENT on DATE LOCATION.
 
For example,

> There was also a magnitude 1.29 quarry blast on June 19 12km SE of Tehachapi, California.

with TYPE_OF_EVENT being explosion, quarry blast, etc and LOCATION being 'place' - e.g. '0km N of The Geysers, California'.

### TURNING IT IN

Same as always! Turn in as much as you can by 10am Wednesday morning.
