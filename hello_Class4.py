#List comprehension
#makes = []
#for car in cars
#	makes.append(car['make'])
#['Chevrolet', 'Honda', 'Honda', 'Toyota']

#list-comprehensions.py
numbers = [1.5,2,3,4]

doubles = []
for number in numbers:
	doubles.append(number*2)
print doubles	
#[3.0, 4, 6, 8]


results = [numbers for number in numbers]
print results
#[[1.5, 2, 3, 4], [1.5, 2, 3, 4], [1.5, 2, 3, 4], [1.5, 2, 3, 4]]

results = [number for number in numbers]
print results
#[1.5, 2, 3, 4]

dogs = [
    { 'dog_name': 'Harry' },
    { 'dog_name': 'Trouble' },
    { 'dog_name': 'Toyota' },
    { 'dog_name': 'Brenda' }
]
names = []
for dog in dogs:
	names.append(dog['dog_name'])
print names

#a list called favorites that includes all cars that are black or produced after 2010. write a for loop to create that list.

#favorites = []
#for car in cars:
#	if car['color'] == 'black' or int(car['year'])
#		>2010:
#		favorites.append(car)
#print favorites

#HOMEWORK3

import csv
file = open('Dogs.csv')
dogs = list(csv.DictReader(file))

#1. Count the dogs in NYC
print len(dogs)

#2. How many dogs are in each borough?
#Using a list comprehension ot get the boroughs
borough = [dog['borough'] for dog in dogs]
print borough

#A way to get rid of duplicates
print list(set(borough))

#B way
boroughs = []
for dog in dogs:
	if dog['borough'] not in boroughs:
	    boroughs.append(dog['borough'])
for borough in boroughs:
	results = 0
	for dog in dogs:
		if dog['borough'] == borough:
			results = results + 1
	print "There are", results, "dogs in ", borough, "."

borough_counts = {}
for borough in boroughs:
	borough_counts['Queens'] = 0


	




