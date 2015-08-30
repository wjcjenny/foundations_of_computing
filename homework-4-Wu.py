#Jiachuan Wu
#June 8 2015
#Homework 4

#Rewriting some of your dogs.csv code into list comprehensions would be great 
#(try starting with getting a unique list of borough names), but feel free to also work on the following:

import csv
file = open('Dogs.csv')
dogs = list(csv.DictReader(file))


#1. Make a dictionary where every dog's name maps to the number of dogs with that name.

counts = {}
all_dog_names = [dog['dog_name'] for dog in dogs]
dog_names = list(set(all_dog_names))

for dog_name in dog_names:
	rs = 0
	for dog in dogs:
		if dog['dog_name'] == dog_name:
			rs = rs + 1
	counts[dog_name] = rs
print counts


#2. How many dogs are named Danger?
all_dog_names = [dog['dog_name'] for dog in dogs]
dog_names = list(set(all_dog_names))

results = 0
for dog in dogs:
	if dog['dog_name'] == "Danger":
		results = results + 1
print "There are",results, "named Danger in NYC."



#3. Find the ratio of dogs name Spot to dogs name Spike.
all_dog_names = [dog['dog_name'] for dog in dogs]
dog_names = list(set(all_dog_names))

results_Spot = 0
for dog in dogs:
	if dog['dog_name'] == "Spot":
		results_Spot = results_Spot + 1
#print "There are",results_Spot, "named Spot in NYC."
#There are 45 named Spot in NYC.
results_Spike = 0
for dog in dogs:
	if dog['dog_name'] == "Spike":
		results_Spike = results_Spike + 1
#print "There are",results_Spike, "named Spike in NYC."
#There are 128 named Spike in NYC.

ratio = (float(results_Spot)/results_Spike).as_integer_ratio()
print "The ratio of dogs name Spot to dogs name Spike is",ratio,"."


#4a. Make a list of all of the names that only appear once in the list (Tip: One option is to make a set, then make use of a list's .count() method).
counts = {}
all_dog_names = [dog['dog_name'] for dog in dogs]
dog_names = list(set(all_dog_names))

for dog_name in dog_names:
	rs = 0
	for dog in dogs:
		if dog['dog_name'] == dog_name:
			rs = rs + 1
	counts[dog_name] = rs
#print counts

#the names only show once means the number of the name is 1.
mylist = []
key = counts.get
for key, value in counts.iteritems() :
	#print key,value
	if value == 1:
		print mylist.append(key)

#4b. Display them in alphabetical order.
print "To put them in alphabetical order is:", sorted(mylist),"."



#5. Which borough loves dogs the most? Use the following dictionary to tell me the ratio of dogs to people in each borough.
#population = { 'Staten Island': 468000, 'Brooklyn': 2504000, 'Bronx': 1385000, 'Manhattan': 1585000, 'Queens': 2231000 }
boroughs = []
mylist_all = {}
for dog in dogs:
	if dog['borough'] not in boroughs:
	    boroughs.append(dog['borough'])
for borough in boroughs:
	results = 0
	for dog in dogs:
		if dog['borough'] == borough:
			results = results + 1
	print "There are", results, "dogs in ", borough, "."
	mylist_all[borough] = results
print mylist_all
#This is the dictionary I make for all the dogs in each borough.
mylist_all = {'Bronx': 9293, 'Brooklyn': 19333, 'Staten Island': 9381, 'Manhattan': 26029, 'Queens': 17506}
population = { 'Staten Island': 468000, 'Brooklyn': 2504000, 'Bronx': 1385000, 'Manhattan': 1585000, 'Queens': 2231000 }

ratio_bronx = (float(mylist_all['Bronx'])/ population['Bronx'])
print "The ratio in population of dogs and people in the Bronx is", ratio_bronx.as_integer_ratio()
ratio_brooklyn = (float(mylist_all['Brooklyn'])/ population['Brooklyn'])
print "The ratio in population of dogs and people in the Brooklyn is", ratio_brooklyn.as_integer_ratio()
ratio_staten_island = (float(mylist_all['Staten Island'])/ population['Staten Island'])
print "The ratio in population of dogs and people in the Staten Island is", ratio_staten_island.as_integer_ratio()
ratio_manhattan = (float(mylist_all['Manhattan'])/ population['Manhattan'])
print "The ratio in population of dogs and people in the Manhattan is", ratio_manhattan.as_integer_ratio()
ratio_queens = (float(mylist_all['Queens'])/ population['Queens'])
print "The ratio in population of dogs and people in the Queens is", ratio_queens.as_integer_ratio()

population_ratio_all = {'Manhattan': ratio_manhattan,'Bronx': ratio_bronx, 'Brooklyn': ratio_brooklyn, 'Queens': ratio_queens, 'Staten Island': ratio_staten_island}
print "By ratio, the borough that loves dogs the most is", max(population_ratio_all, key=population_ratio_all.get),"."


#6. Here's a list of neighborhoods by zip code 
#- https://www.health.ny.gov/statistics/cancer/registry/appendix/neighborhoods.htm - 
#how does the Lower East Side compare to the Upper East Side in terms of registering dogs? How about Greenpoint to Sunset Park?
upper_east = [10021, 10028, 10044, 10065, 10075, 10128]
lower_east = [10002, 10003, 10009]
greenpoint = [11211, 11222]
sunset = [11220, 11232]

zipcode_list = []
zipcode_dic = {}
for dog in dogs:
	if dog['zip_code'] not in zipcode_list:
		zipcode_list.append( dog['zip_code'] )
#print zipcode_list

for zipcode in zipcode_list:
	number_of_dogs_in_zipcode = 0
	for dog in dogs:
		if dog['zip_code'] == zipcode:
			number_of_dogs_in_zipcode += 1
	zipcode_dic[zipcode] = number_of_dogs_in_zipcode
#print zipcode_dic
dog_upper_east = 0
for i in upper_east:
	if str(i) in zipcode_list:
		dog_upper_east += zipcode_dic[str(i)]

dog_lower_east = 0
for j in lower_east:
	if str(j) in zipcode_list:
		dog_lower_east += zipcode_dic[str(j)]
	
dog_greenpoint = 0
for k in greenpoint:
	if str(k) in zipcode_list:
		dog_greenpoint += zipcode_dic[str(k)]
	
dog_sunset = 0
for l in sunset:
	if str(l) in zipcode_list:
		dog_sunset += zipcode_dic[str(l)]
	
#print dog_upper_east, dog_lower_east, dog_greenpoint, dog_sunset
print "In comparison, the Upper East Side has", dog_upper_east,"dogs." 
print "The Lower East has", dog_lower_east,"dogs registered."
print "Greenpoint has", dog_greenpoint,"dogs registered." 
print "Sunset Park has", dog_sunset, "dogs registered."