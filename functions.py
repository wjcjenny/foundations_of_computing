#functions.py

print len("Hello")

print abs(-3.4)
#absolute value

print round(5.9)
#rounded up

#functions : https://docs.python.org/2/library/functions.html

#the function is to double the number
#name of the function is double()
def double(number):
	bigger = number * 2
	return bigger
#You can ONLY RETURN ONCE
print double(3)

#Don't overwrite your functions

#double = 40
#print double(double)
number = 40
print double (number)

def exclaim(sentence):
	return sentence + "!!"
print exclaim("Happy Birthday")

#print exclaim("Hello","Goodbye")
#TypeError: exclaim() takes exactly 1 argument (2 given)

#Sometimes you need more than one??????????????????????????????
#Sometimes some are optional
print round(3.49578648,4)
#the second number is the number of decimals



#D.E.Y Don't Repeat Yourself
'''
if boat_count > car_count:
	print "Larger"
else:
	print "Smaller"

if motorcycle_count > car_count:
	print "Larger"
else:
	print "Smaller"
'''

def size_comparison(countA,countB):
	if countA > countB:
		return "Larger"
	else:
		return "Smaller"

print size_comparison(5,6)

result = size_comparison(78,2)
print result


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

happend_at = '2014-06-04T11:58:58.200Z'
# figure out how to parse a string and turn it into a date(or a time or a datetime)

#UTC
#ISO
#https://en.wikipedia.org/wiki/ISO_8601












