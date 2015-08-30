#Jiachaun Wu
#June 1 2015
#Homework 2

###LISTS
# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
Just_Numbers = [22, 90, 0, -10, 3, 22, 48]
print Just_Numbers

#1) Display the number of elements in the list
print "There are", len(Just_Numbers), "elements in the list."

#2) Display the 4th element of this list.
print "The 4th element of this list is", Just_Numbers[3],"."

#3) Display the sum of the 2nd and 4th element of the list.
Second = Just_Numbers[1]
Four = Just_Numbers[3]
print "The sum of the 2nd and 4th element of the list is", Second+Four,"."
######???#print "The sum of the 2nd and 4th element of the list is", sum([Just_Numbers[1],Just_Numbers[3]]),"."

#4) Display the 2nd-largest value in the list.
sorted_Just_Numbers = sorted(Just_Numbers)
#print sorted_Just_Numbers
print "The 2nd-largest value in the list is", sorted_Just_Numbers[5], "."
#Second way: print "The 2nd-largest value in the list is", sorted_Just_Numbers[len(sorted_Just_Numbers)-2], "."
#Third way: print "The 2nd-largest value in the list is", sorted_Just_Numbers[-2], "."


#5) Display the last element of the original unsorted list
print "The last element of the original unsorted list is", Just_Numbers[len(Just_Numbers)-1] ,"."

#6) For each number, display a number: 
#If your original number is less than 10, multiply it by 30. If it's also odd, add six. 
#If it's greater than 50 subtract ten. 
#If it's not negative ten, subtract one. 
#(For example: 2 is less than 10, so 2 * 30 = 60, 2 isn't odd,so it stays as 60. 
#2 isn't greater 50 so it stays at 60. 2 is not -10 , so 60 - 1 = 59.
for A_Number in Just_Numbers:
	Result = A_Number 
	if A_Number < 10:
		Result = Result * 30
		if A_Number % 2 != 0:
			Result = Result + 6	
	if A_Number > 50:
		Result = Result-10
	if A_Number != -10:
		Result = Result - 1	
	print Result

#7) Sum the product of each of the numbers divided by two.
print "The sum of each of the numbers divided by two is", sum([Just_Numbers[0]/2,Just_Numbers[1]/2,Just_Numbers[3]/2,Just_Numbers[4]/2,Just_Numbers[5]/2,Just_Numbers[6]/2]), "."


### DICTIONARIES

#8) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. 
#Define a dictionary called movie that works with the following code.
#print "My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director']
movie = {'title': 'Casablanca', 'year':'1942','director':'Michael Curtiz'}
print "My favorite movie is", movie['title'],","
print "which was released in", movie['year']
print "and was directed by", movie['director'],"."

#9) Add entries to the movie dictionary for budget and revenue 
#(NOT in the original dictionary definition), and print out the difference between the two.
movie ['budget'] = 878000
movie ['revenue'] = 3700000
print movie
print "The difference between budget and revenue is", movie ['budget'] - movie ['revenue'],"dollars."

#10) If the movie cost more to make than it made in theaters, print "It was a flop". 
#If the film's revenue was more than five times the amount it cost to make, print "That was a good investment."
if movie ['budget'] > movie ['revenue']:
	print "It was a flop."
if 5 * movie ['budget'] <= movie ['revenue']:
	print "That was a good investment."
else:
	print "That was not bad investment indeed."

#11) Sometimes dictionaries are used to describe the same aspects of many different objects. 
#Make a dictionary that describes the population of the boroughs of NYC. 
#Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. 
#(Tip: keeping it all in millions is a good idea)
NYC_population = {
	'Manhattan': 1.6,
	'Brooklyn':2.6,
	'Bronx': 1.4,
	'Queens': 2.4,
	'Staten Island': 0.47
}
print NYC_population

#12) Display the population of Brooklyn.
print "The population of Brooklyn is", NYC_population ['Manhattan'],"millions."

#13) Display the combined population of all five boroughs.
ToTal_Population = NYC_population['Manhattan'] + NYC_population['Brooklyn'] + NYC_population['Bronx'] + NYC_population['Queens'] + NYC_population['Staten Island']
print "The combined population of all five boroughs is", ToTal_Population, "millions."

#14) Display what percent of NYC's population lives in Manhattan.
percent_NYC_Manhattan = NYC_population['Manhattan'] / ToTal_Population
print "The percentage of NYC's population lives in Manhattan is", "{0:.0f}%".format(float(percent_NYC_Manhattan)*100), "."

#15) Display each borough name and population on separate lines (without a for loop) 
#(Hint: You'll just be typing out the name of the borough, this is the "bad" way)
print 'Bronx', NYC_population['Bronx']
print 'Manhattan', NYC_population['Manhattan']
print 'Staten Island', NYC_population['Staten Island']
print 'Brooklyn', NYC_population['Brooklyn']
print 'Queens', NYC_population['Queens']

#16) Print the name of each borough that has more than one million residents.
borough_names = NYC_population.keys()
for borough_names in NYC_population:
	if NYC_population[borough_names] > 1:
		print borough_names

#17) Print how many boroughs have more than one million residents.
above_the_million = 0
for borough_names in NYC_population:
	if NYC_population[borough_names] > 1:
		above_the_million = above_the_million + 1
print "There are", above_the_million, "boroughs have more than one million residents."

#18) Print the length of the borough name that comes first in the alphabet.
sorted_NYC_population = sorted (NYC_population)
print "The lenghth of the first borough name in the alphabet order is",len(sorted_NYC_population[0]), "."

#19) Display each borough name and population on separate lines (with a for loop).
borough_names = NYC_population.keys()
for borough_names in NYC_population:
	print borough_names, NYC_population[borough_names]
