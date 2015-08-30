print 'Hello world!'

#print "Hello world!'
#This is not going to work
#you can not mix single and double quotes
#You have to keep quotes both same
print "Hello World!"

print 'Hello world!'
#QUoted things are called "strings"
print 10
#Quoted numbers are called integers 
print 10 + 10
#This goes to 20
print "10 + 10"
#This goes to 10 + 10 Quoted integers are treated as strings
#print 10 + "Hello"
#Can not combing interger and string

#Stack overflow answer #1
print 10, "Hello"
#this goes 10 Hello
#Stack overflow answer #2
print 10 + int("10")
#this goes 20
#Stack overflow answer #3
print str(10) + "Hello"
#this goes 10Hello


print "Hello," + "Jiachuan"
#Use the magic of variables
name = "Jiachuan"
print "Hello," + name
#define variable at anytimes
#lastname = "Soma"
#print "Hello," + lastname

person = raw_input('Enter your name:')
print('Hello',person)
print "Enter Your name:",
name = raw_input()
print "Hello", name


year_of_birth = raw_input("Enter your year of birth:")
age = 2015 - int(year_of_birth)
#after int(), strings do not need to quote, number need quotes
#like int(year_of_birth), int("10")
print "You are approximately", age, "years old"
#How old are you?
#Camelcase - year of birth or YearOfBirth
#always keep integers or put int()to the strings

earth_days = 365
mercury_days = 88
ratio = 365/88
print ratio
#only give you 4, without remainders

#Float
earth_days = 365.0
mercury_days = 88.0
ratio = earth_days/mercury_days
print ratio
#this goes with remainders
mercury_years  = int(age * ratio)
print "Your age on mercury is", mercury_years
#keep integer for year, put int()

#see if our birth year is the same as their birth year
#Pseudocode for year of birth twins
#if year_of _birth ==1983 then say "hooray"
if int(year_of_birth) == 1983:
	print "Hooray!!!"
if int(year_of_birth) < 1983:
	print "YOU r Old! :)"
if int(year_of_birth) > 1983:
	print "YOU r Younger than me !!!! :)"





