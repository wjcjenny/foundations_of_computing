import csv

# head -n 500 dogs.csv > thousand.csv

file = open("sample.csv")
dogs = list(csv.DictReader(file))

print dogs

# Count the dogs in NYC
print len(dogs)

# Using a list comprehension to get the boroughs
boroughs = [dog['borough'] for dog in dogs]
# A way to get rid of duplicates
print list(set(boroughs))

boroughs = []
for dog in dogs:
	if dog['borough'] not in boroughs:
		boroughs.append(dog['borough'])

for borough in boroughs:
	result = 0
	for dog in dogs:
		if borough == dog['borough']:
			result = result + 1
	print borough, result

names = [dog['dog_name'] for dog in dogs]
unique_names = list(set(names))
print names
print unique_names



# borough_counts = {
# 	'Staten Island': 0,
# 	'Brooklyn': 0,
# 	'Manhattan': 0,
# 	'Queens': 0,
# 	'Bronx': 0
# }
#print borough_counts['Staten Island']
#print borough_counts['Queens']
#print borough_counts['Bronx']
#staten_island = 12
#borough_counts['Staten Island'] = 12
#borough_counts['Queens'] = 33

borough_counts = {}
for borough in boroughs:
	borough_counts[borough] = 0
	print borough_counts

for dog in dogs:
	borough = dog['borough']
	borough_counts[borough] = borough_counts[borough] + 1
	# borough_counts['Bronx'] = borough_counts['Bronx'] + 1

# for borough in boroughs:
# 	result = 0
# 	for dog in dogs:
# 		if borough == dog['borough']:
# 			result = result + 1
# 	print borough, result

# How many dogs were registered in 2008? 2011? 

"Jan-00"
"Nov-08"

# -- Checking if things are in things
# Lists:
# if borough in boroughs
# if 'Manhattan' in [ 'Manhattan', 'Brooklyn' ]
# Strings:
# if '08' in dog['year']
# if '08' in 'Jan-08'

# Stay away from this:
# strptime
# strftime





#if birthday == "Jan-00" or birthday == "Feb-00" or birthday == "Mar-00"
# Tip - you want to grab the 
# 1) last two characters of the string, or
# 2) the numbers after the '-'

# If you see n/a as a color, disregard it



# For 7a
# You want two dictionaries, one of # of dogs per borough
# and one of # of spayed dogs per borough
# Your final code should be either:

for borough in boroughs:
	print float(spayed_count[borough]) / dog_count[borough]

# or

print float(spayed['Staten Island']) / dog_count['Staten Island']
print float(spayed['Brooklyn']) / dog_count['Brooklyn']
print float(spayed['Queens']) / dog_count['Queens']
# ...etc

