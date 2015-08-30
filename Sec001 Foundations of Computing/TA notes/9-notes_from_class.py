# The danger of automatically generated stories:

# http://projects.propublica.org/schools/
# http://projects.propublica.org/schools/schools/362058001928
# "and it has two teachers on staff."

########################################################################

# Commas work with `print`, not with `return`!
def dummy0():
	return "A","shallow","strong",",","4.5","earthquake was reported","Tuesday","morning","on ","June 6","."
print "Using commas(,) with `return` gives you a tuple:\n",dummy0()

# Alternatives:
def dummy1():
	return "A %s %s, %s earthquake was reported %s %s on %s." % ( "shallow","strong","4.5","Tuesday","morning","June 6" )
	# %s # string
	# %i # integer
	# %d # float?
	# %r
print dummy1()

def dummy2():
	return "A "+"shallow"+" "+"strong"+", "+"4.5"+" earthquake was reported "+"Tuesday"+" "+"morning"+" on "+"June 6"+"."
print dummy2()

########################################################################

# How to make a list of dictionary from CSVs online
import csv,urllib2
ourlistofdicts = list( csv.DictReader( urllib2.urlopen( "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.csv" ) ) )

########################################################################
