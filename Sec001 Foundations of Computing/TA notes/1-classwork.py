# Class 1 Classwork
# Terminal commands to remember: pwd, ls, cd, cat

print 'Hello world'

# This isn't going to work
# You can't mix single and double quotes
# print 'Hello world"

# You have to keep them the same
# Quoted things are called 'strings'
print "Hello world"

# Numbers are called integers
print 10

print 10 + 10

# Quoted integers are treated as strings
print "10 + 10"

# Can't combine integer and string
# print 10 + "Hello"

# Stack overflow answer #1
print 10, "Hello"

# Stack overflow answer #2
# Convert the string into an integer
print 10 + int("10")

# Stack overflow answer #3
# Converting the integer into a string
print str(10) + "Hello"

print "Hello, " + "Soma"

# Using variables
name = "Soma"
print "Hello," + name

lastname = "Soma"
print "Hello," + lastname

# Computer 'forgets' the old value of name
# Commenting this out because you don't want to be
# asked two things
# print "Enter Your name:",
# name = raw_input()

print "Hello", name

# Spaces won't work in variable names
#year of birth = 1983
# Dashes won't work in variable names
# year-of-birth = 1983
# You do want some spacing in it, though
# yearofbirth = 1983
# Underscores are pretty good
# year_of_birth = 1983
# Camelcase - yearOfBirth or YearOfBirth

year_of_birth = raw_input("Enter your year of birth:")

age = 2015 - int(year_of_birth)
print "You are approximately", age, "years old"

# Float
earth_days = 365.0
mercury_days = 88.0
ratio = earth_days / mercury_days

# Make sure it's a float
print ratio
mercury_years = int(age * ratio)
print "Your age on mercury is", mercury_years

# See if our birth year is the same as their
# birth year

# Pseudocode for year of birth twins
# if year_of_birth == 1983
# then say "hooray"

if int(year_of_birth) == 1983:
	print "Hooray"

if int(year_of_birth) < 1983:
	print "You are older than me"

if int(year_of_birth) > 1983:
	print "You are younger than me"




