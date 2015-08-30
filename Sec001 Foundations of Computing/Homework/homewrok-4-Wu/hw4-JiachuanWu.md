# Homework 4

##1.
Correct answer! Just a few points:
```
for dog_name in dog_names:
	rs = 0
	for dog in dogs:
		if dog['dog_name'] == dog_name:
			rs = rs + 1
	counts[dog_name] = rs
```
actually goes through the entire `names` list for every `dog_name` in `dog_names`, which takes a long time.
You might just go through the list once with
```
for dog in dogs:
	if dog['dog_name'] in counts:
		counts[ dog['dog_name'] ] += 1
	else:
		counts[ dog['dog_name'] ] = 1
```
or
```
counts = { dog_name:0  for dog_name in dog_names }
for dog_name in dog_names:
	counts[dog_name] += 1
```

Also
```
			rs = rs + 1
```
can just be
```
			rs += 1
```


##2.
Same points as Q1. Also it was okay just to do
```
print "There are",counts["Danger"], "named Danger in NYC."
```


##3.
Doing `.as_integer_ratio()` wasn't quite what we were looking for, but I won't take points of this.
Same points as Q1. Also it was okay just to do
```
ratio = (float(counts["Spot"])/counts["Spike"]).as_integer_ratio()
print "The ratio of dogs name Spot to dogs name Spike is",ratio,"."
```


##4a. (-0.5)
##4b. (-1)
Same points as Q1.

Also
```
key = counts.get
```
is unnecessary, as the next line
```
for key, value in counts.iteritems() :
```
assigns a different value to `key` anyway.

You printed the names, but didn't make a list out of it.
```
for key, value in counts.iteritems() :
	#print key,value
	if value == 1:
		print key
```
I think you were trying to do
```
mylist = []
for key, value in counts.iteritems() :
	#print key,value
	if value == 1:
		mylist.append( key )
```

In Q4b,
```
for key in counts:
	if key not in mylist:
	    mylist.append(key)
```
can just be
```
counts = mylist.key()
```
which is not quite a list of all of the names that only appear once in the list.


##5.
Again, doing `.as_integer_ratio()` wasn't quite what we were looking for, but I won't take points of this.

Also, how would you rewrite the following so that you don't repeat yourself?
```
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
```

##6.
Same points as Q1:
```
for zipcode in zipcode_list:
	number_of_dogs_in_zipcode = 0
	for dog in dogs:
		if dog['zip_code'] == zipcode:
			number_of_dogs_in_zipcode += 1
	zipcode_dic[zipcode] = number_of_dogs_in_zipcode
```
actually goes through dogs for every zipcode in `zipcode_list` (so that's 81542 times 225), which takes a long time.

Also you go through `zipcode_list` 6 + 3 + 2 + 2 times. How can you go through it only once?
