import urllib2
import dateutil.parser
import csv
# import parser from dateutil

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

# Measurements from
# http://earthquake.usgs.gov/learn/topics/seismology/determining_depth.php
# 0-70 is shallow
# 70-300 intermediate
# 300+ deep
def eq_depth(input_depth):
  depth = float(input_depth)
  if depth < 70:
    return "shallow"
  elif depth < 300:
    return "intermediate"
  else:
    return "deep"

def eq_description(magnitude):
  mag = float(magnitude)
  if mag >= 5:
    return "strong"
  else:
    return "weak"

def eq_day(happened_at):
  parsed = dateutil.parser.parse(happened_at)
  return parsed.strftime("%A")

# 4am-12pm is morning
# 12pm-6pm is afternoon
# 6pm-9pm evening
# 9pm-4am 

def eq_time_of_day(happened_at):
  parsed = dateutil.parser.parse(happened_at)
  hour = parsed.hour
  if hour >= 4 and hour < 12:
    return "morning"
  elif hour >= 12 and hour < 18:
    return "afternoon"
  elif hour >= 18 and hour < 21:
    return "evening"
  else:
    return "night"

def eq_date(happened_at):
  parsed = dateutil.parser.parse(happened_at)
  return parsed.strftime("%B %d")

def eq_to_sentence(quake):
  depth = eq_depth(quake['depth'])
  description = eq_description(quake['mag'])
  mag = quake['mag']
  dayofweek = eq_day(quake['time'])
  date = eq_date(quake['time'])
  timeofday = eq_time_of_day(quake['time'])

  return "A %s %s, %s earthquake was reported %s %s on %s." % (depth, description, mag, dayofweek, date, timeofday)

# Data source: http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv
urllib2.urlopen("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.csv")
file = open("1.0_month.csv")
quakes = list(csv.DictReader(file))

for quake in quakes:
  print eq_to_sentence(quake)

