####################DOGS

#OPEN DOG FILE
import csv

#csv.reader is bad! list of lists! we want a list of dicts!
#file = open('Dogs.csv')
#dogs = csv.reader(file)
#print type(dogs)
#for dog in dogs:
#	print dog[0]

file = open('sample.csv')
dogs = list(csv.DictReader(file))

for dog in dogs:
	print dog['gender']
for dog in dogs:
	print dog['dog_name']

results = 0
for dog in dogs:
	print dog
#type(dog) show dog is dictionaries
	if dog['dog_name'] == "Trouble":
		results = results + 1
print results

zip_code = '10025'
#zip_code
results=0
for dog in dogs:
	print dog
	if dog['zip_code']=="10025":
		results = results + 1
print "There are", results, "dogs in your zip."


#list of every zip code
zip_codes = []
for dog in dogs:
	print dog['zip_code']
    #if dog['zip_code'] is not in dogs, then..
	if dog['zip_code'] not in zip_codes:
	    #How do you add things to a list?
	    zip_codes.append(dog['zip_code'])
print zip_codes

#find how many dogs in the specific zip
for zip_code in zip_codes:
	results = 0
	for dog in dogs:
		if dog['zip_code']== zip_code:
			results = results + 1
	print "There are", results, "dogs in ", zip_code, "."

#how many dogs are there total?

#how many dogs are in every zip code?

#how many are female/male? ratio?


#what's the most popular name?

#how do we sort the zip code results?

#most popular breeds?

#least popular breeds?

#most popular color? 1b. combine dominat+secondary colors

#counts by borough

#spay %

#make those zip code results into a dictionary, like {'10028':45, '10099':120}


