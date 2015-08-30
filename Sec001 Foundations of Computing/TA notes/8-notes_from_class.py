########################################################################
# Save this in your Lede folder as functions.py

# In the terminal,
# move to your Lede folder.
## python functions.py


# Let's look at the functions in
# https://docs.python.org/2/library/functions.html

print len( "Hello" ) # prints 5
print abs( -3.4 ) # prints 3.4
print round( 5.9 ) # prints 6.0


# DEFINING YOUR OWN FUNCTIONS

# `double` is the function name
# `number` is a PARAMETER name
def double( number ):
	bigger = number * 2
	# The return statement gives you something back
	# You can only return once
	return bigger

# CALLING A FUNCTION

# You can print the output of a function:
print double( 3 )

# You can store the output of a function:
result = double( 7 )
print result

# DON'T name your variables the same as your function name!
# This gives you `TypeError: 'int' object is not callable`:
## double = 40
## print double( double )
# `double` is no longer a function, but an integer, because we assigned an integer value to a variable with our function name.

# But it's okay to name name your variables the same as your parameter name. What happens in a function stays in a function.
# It's okay to name a variable `number`:
number = 40
print double( number )


# Sometimes you need an exact number of parameters...

def exclaim( sentence ):
	return sentence+"!!!!!!!"

print exclaim( "I hope you can come to my wedding" )
print exclaim( "I'm sorry you have the flu" )
# This gives you `TypeError: exclaim() takes exactly 1 argument (2 given)`:
## print exclaim( "Hello","Goodbye" )

# ...Sometimes some parameters are optional.

# These both work:
print round( 3.4567890 )
print round( 3.4567890,4 )


# One reason you might want to use functions:
# D.R.Y. : Don't Repeat Yourself

# Instead of this,

boat_count = 34
car_count = 56
motorcycle_count = 122

if boat_count > car_count:
	print "Larger"
else:
	print "Smaller"

if motorcycle_count > car_count:
	print "Larger"
else:
	print "Smaller"

# you can do

boat_count = 34
car_count = 56
motorcycle_count = 122

def size_comparison( countA,countB ):
	if countA > countB:
		return "Larger"
	else:
		return "Smaller"

print size_comparison( boat_count,car_count )
print size_comparison( motorcycle_count,car_count )


########################################################################
# Do Now

# 1)
def to_kmh( mph ):
	kmh = mph * 1.60934
	return int( round( kmh ) )

def to_mpm( mph ):
	## mpm = mph * 26.8224
	## return int( round( mpm ) )

	# Or,
	# to avoid "magic numbers", we can do
	kmh = to_kmh( mph )
	mph = kmh * 1000
	mpm = mph / 60
	return int( round( mpm ) )

mph = 40
print "You are driving", mph, "in mph"
print "Driving", to_kmh(mph), "in kmh"
print "Driving", to_mpm(mph), "in kmh"

# 2)
# Originally, this gave us `TypeError: 'int' object is not callable`
# because we assigned an integer value to our function name `total`.
def total(n):
    return n * 10

streets = ['10th Ave', '11th Street', '45th Ave']

## total = len(streets)
# you might do
street_count = len( streets )

## count = total + 1
# you might do
count = street_count + 1

print total(count)