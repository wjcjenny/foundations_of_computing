########################################################################
# 1: new-ish concepts

########################################################################
# the BOOLEAN data type: True, False

print 5 > 2 # True
print "cat" == "dog" # False
print type( True ) # <type 'bool'>
print type( False ) # <type 'bool'>

is_a_dog = True
if is_a_dog:
	print "woof"
else:
	print "meow"
# prints "woof"

# "" is False in python
ourstring = ""
if ourstring:
	print "NOT empty!"
else:
	print "empty!"
# prints "empty!"

# [] is False in python
ourlist = []
if ourlist:
	print "NOT empty!"
else:
	print "empty!"
# prints "empty!"


########################################################################
# CONDITIONALS in LIST COMPREHENSIONS
num = [4, 99, 32.0, 45.0, 2 ]
even_num = [ n  for n in num  if n % 2 == 0 ]

print even_num # [4, 32.0, 2]


########################################################################
# 2: Do Now

# 1) Write a function called is_even that returns whether a value is even or not.
def is_even( number ):
	return number % 2 == 0 # a Boolean


# 2) Add together the second and fourth members of the list below.
num = [4, 99, 32.0, 45.0, 2 ]

print num[1] + num[3]


# 3) Count the number of Democrats that represent New York State in the Senate.
senators = [
{ 'name': 'Gillibrand', 'party': 'Democrat' },
{ 'name': 'Schumer', 'party': 'Democrat' }
]
# Tip: list comprehension + .count() method

parties = [ senator['party']  for senator in senators ]
print parties.count( 'Democrat' )

# Or,
print len( [ senator  for senator in senators  if senator['party'] == 'Democrat' ] )


# 4a) Using the code below, make a list of all of the Supreme Court Justices' names. 
justices = [{ 'name': 'Scalia', 'vote': 'dissent' }, { 'name': 'Kennedy', 'vote': 'majority' }, { 'name': 'Ginsburg', 'vote': 'majority' }, { 'name': 'Kagan', 'vote': 'majority' }, { 'name': 'Roberts', 'vote': 'dissent' }, { 'name': 'Alito', 'vote': 'dissent' }, { 'name': 'Thomas', 'vote': 'dissent' }, { 'name': 'Breyer', 'vote': 'majority' }, { 'name': 'Sotomayor', 'vote': 'majority' } ]

print [ justice['name']  for justice in justices ]


# 4b) Using a single list comprehension, list only the judges who sided with the majority opinion. 

print [ justice['name']  for justice in justices  if justice['vote'] == 'majority' ]