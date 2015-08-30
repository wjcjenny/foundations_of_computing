#Jiachuan Wu
#June 3 2015
#Homework 3

#0. What's the command to make a sample of the first 500 rows of dogs.csv, and save it to thousand.csv?
#the command line should be: 
#head -n 500 Dogs.csv > thousand.csv

import csv
file = open('Dogs.csv')
dogs = list(csv.DictReader(file))

#1. How many registered dogs are in New York City total?
print "There are", len(dogs), "registered dogs in New York City total."

#2. How many dogs are in each borough?
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

#3. Make a list of every dog's name (duplicates are OK)
for dog in dogs:
	print dog['dog_name']

#4a. How many dogs named "Max" (or any other name of your choosing) are in NYC?
results = 0
for dog in dogs:
	if dog['dog_name'] == "Max":
		results = results + 1
print "There are",results, "named Max in NYC."


#4b. How many dogs named "Max" (or any other name of your choosing) are in each borough?
boroughs = []
for dog in dogs:
	if dog['borough'] not in boroughs:
	    boroughs.append(dog['borough'])
for borough in boroughs:
	results = 0
	for dog in dogs:
		if dog['dog_name'] == "Max" and dog['borough'] in borough:
			results = results + 1
	print "There are", results, "dogs named Max in ", borough, "."

#5. How many dogs were registered in 2008? 2011? 
#2008
results = 0
for dog in dogs:
	dog_reg = dog['birth']
	dog_reg = dog_reg[-2:]
	if dog_reg == "08":
		results = results + 1
print "There are", results, "were registered in 2008."
#2011
results = 0
for dog in dogs:
	dog_reg = dog['birth']
	dog_reg = dog_reg[-2:]
	if dog_reg == "11":
		results = results + 1
print "There are", results, "were registered in 2011."


#6a. What percentage of dogs are spayed/neutered?
spayed_or_neutered = 'Yes'
results=0
for dog in dogs:
	if dog['spayed_or_neutered'] == "Yes":
		results = results + 1
print "There are","{0:.0f}%".format(float(results) /len(dogs)*100), "of dogs are spayed/neutered."

#6b. What percentage of female dogs are spayed/neutered? Male dogs?
spayed_or_neutered = 'Yes'
results=0
for dog in dogs:
	if dog['spayed_or_neutered'] == "Yes":
		results = results + 1
#the results are 377 dogs which are spayed/neutered.
results_female_spayed=0
for dog in dogs:
	if dog['spayed_or_neutered'] == "Yes" and dog["gender"] == "F":
		results_female_spayed = results_female_spayed + 1
#the results are 196 female dogs which are spayed/neutered.
print "There are","{0:.0f}%".format(float(results_female_spayed) /results*100), "of female dogs are spayed/neutered."

results_male_spayed=0
for dog in dogs:
	if dog['spayed_or_neutered'] == "Yes" and dog["gender"] == "M":
		results_male_spayed = results_male_spayed + 1
#the results are 179 female dogs which are spayed/neutered.
print "There are","{0:.0f}%".format(float(results_male_spayed) /results*100), "of male dogs are spayed/neutered."


#7a. What are the per-borough percentages of spayed/neutered dogs?

boroughs = []
for dog in dogs:
	if dog['borough'] not in boroughs:
	    boroughs.append(dog['borough'])

counts = {}
for borough in boroughs:
	results_a = 0
	for dog in dogs:
		if dog['borough'] == borough:
			results_a = results_a + 1
	#print results_a, borough, "."
	counts[borough] = results_a
#136 Manhattan .
#71 Bronx .
#120 Queens .
#69 Staten Island .
#103 Brooklyn .

#spayed_percetages = [] 

for borough in boroughs:
	results = 0
	for dog in dogs:
		if dog['spayed_or_neutered'] == "Yes" and dog['borough'] in borough:
			results = results + 1

	#spayed_percetages.append(float(results)/counts[borough]*100)
	#spayed_percetages.sort()

#print "shiwoshiwoshiwo",spayed_percetages

	#print results, borough, "."
#116 Manhattan .
#44 Bronx .
#86 Queens .
#59 Staten Island .
#72 Brooklyn .
	print "There are", "{0:.0f}%".format(float(results) / counts[borough] * 100), "dogs spayed/neutered in ", borough, "."


#7b. Which borough has the lowest % of spayed/neutered dogs?

wu = 0
boroughs = []
for dog in dogs:
	wu+=1
	if dog['borough'] not in boroughs:
		boroughs.append(dog['borough'])

counts = {}
for borough in boroughs:
	results_a = 0
	for dog in dogs:
		if dog['borough'] == borough:
			results_a = results_a + 1
	#print results_a, borough, "."
	counts[borough] = results_a
spayed_percetages = {} 

for borough in boroughs:
	results = 0
	for dog in dogs:
		if dog['spayed_or_neutered'] == "Yes" and dog['borough'] in borough:
			results = results + 1

	spayed_percetages[borough] = float(results)/counts[borough]*100

for key, value in sorted(spayed_percetages.iteritems(), key=lambda (k,v): (v,k)):
	#print "%s: %s" % (key, value)
	print "The lowest is", "%s: %s" % (key, value),"%."
	break


#8. How many ZIP codes are in NYC?
all_zip = []
for dog in dogs:
	if dog['zip_code'] not in all_zip:
		all_zip.append(dog['zip_code'])
print "There are ", len(all_zip), "ZIP codes in NYC."

#9. How many are female vs. how many are male?
all_female = []
all_male = []
for dog in dogs:
	if dog['gender'] == "F":
		all_female.append(dog['gender'])
	if dog['gender'] == "M":
		all_male.append(dog['gender'])
print "There are", len(all_female), "female dogs in NYC."
print "There are", len(all_male), "male dogs in NYC."

#10. How many different dog names are there in NYC?
all_names = []
for dog in dogs:
	if dog['dog_name'] not in all_names:
		all_names.append(dog['dog_name'])
print "There are ", len(all_names), "different dog names in NYC."

#11. How many different breeds of dog are in NYC?
all_breed_names = []
for dog in dogs:
	if dog['breed'] not in all_breed_names:
		all_breed_names.append(dog['breed'])
print "There are ", len(all_breed_names), "different breeds of dog in NYC."

#12. What is the most popular breed of dog?
all_breed_names = []
for dog in dogs:
	if dog['breed'] not in all_breed_names:
		all_breed_names.append(dog['breed'])

counts_1={}
for all_breed in all_breed_names:
	results_b = 0
	for dog in dogs:
		if dog['breed'] ==all_breed:
			results_b = results_b + 1
	counts_1[all_breed] = results_b		
#print counts_1
#in the thousand.csv, {'Akita': 125, 'Akita Crossbreed': 37, 'Afghan Hound': 15, 'American Pit Bull Mix / Pit Bull Mix': 107, 'American Eskimo dog': 215}
#then sorted the values in counts_1 dictionary with matching keys
a = sorted(counts_1, key = counts_1.get)
print "The most popular breed of dog is ", a[len(all_breed_names)-1], "."
#When I print the last breed name, it comes: The most popular breed of dog is  Mixed/Other .
#Since it is not the real breed name of dogs, so if you need the real breed name, then print the second last breed name.
#the code will be: print "The most popular breed of dog is ", a[len(all_breed_names)-2], "."
#When I print the second last breed name, then it comes:The most popular breed of dog is  Yorkshire Terrier .


#13a. How many dogs are each color? Count only the dominant color.
dominant_colors = []
for dog in dogs:
	if dog['dominant_color'] not in dominant_colors:
	    dominant_colors.append(dog['dominant_color'])
dominant_color_dic = {}
for dominant_color in dominant_colors:
	results_d_color = 0
	for dog in dogs:
		if dog['dominant_color'] == dominant_color:
			results_d_color = results_d_color + 1
	print "There are", results_d_color, "dogs are in", dominant_color, "when only counting dominant colors."
	dominant_color_dic[dominant_color] = results_d_color

#13b. How many dogs are each color? Count both dominant, secondary and third colors.
colors = []
for dog in dogs:
	if dog['dominant_color'] not in colors:
		colors.append(dog['dominant_color'])
	if dog['secondary_color'] not in colors:
		colors.append(dog['secondary_color'])
	if dog['third_color'] not in colors:
		colors.append(dog['third_color'])
#print colors
all_color_dic = {}
for all_color in colors:
	results_all_color = 0
	for dog in dogs:
		if dog['dominant_color'] == all_color:
			results_all_color = results_all_color + 1
		if dog['secondary_color'] == all_color:
			results_all_color = results_all_color + 1
		if dog['third_color'] == all_color:
			results_all_color = results_all_color + 1
	print "There are", results_all_color, "dogs are in ", all_color, " when counting all dominant, secondary and third colors."
	all_color_dic[all_color] = results_all_color


#13c. What's the most popular color, if counting only dominant? If counting both dominant, secondary, and third colors?
#if counting only dominant
sorted_only_dominant_color = sorted(dominant_color_dic, key = dominant_color_dic.get)
print "If counting only dominant color,", sorted_only_dominant_color[len(dominant_colors)-1],"is the most popular color."

#if counting all dominant, secondary and third colors
sort_b = sorted(all_color_dic, key = all_color_dic.get)
#print "If counting all dominant, secondary and third colors,", sort_b[len(colors)-1], "is the most popular color."
#the outcome is "N/A", so if we need a real color,
#then the code will be 
print "If counting all dominant, secondary and third colors,", sort_b[len(colors)-2], "is the most popular color."


#14a. Make the ZIP code results from class into a dictionary, e.g. { '10028': 45, '10099': 120 }
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
#	print "There are",number_of_dogs_in_zipcode,"dogs in",zipcode
	zipcode_dic[zipcode] = number_of_dogs_in_zipcode
print zipcode_dic

#14b. Prompt the user for a zip code, and use that dictionary to display the number of dogs in that ZIP code.
your_zipcode = raw_input("Enter your zip code:")
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
print "There are", zipcode_dic[your_zipcode] ,"dogs in your ZIP code."















