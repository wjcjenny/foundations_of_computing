########################################################################
# 1: TAKE THE NOT-A-QUIZ/DO-NOW

# 1) What errors can you spot in the following code?

# n = 2;
# if n < 2:
# 	print "Small"
# elif n = 2:
# 	print "Medium"
# else print "Large"

# should be

n = 2 # ; is NOT necessary in Python
if n < 2:
	print "Small"
elif n == 2: # == NOT =
	print "Medium"
else: # else: NOT else
	print "Large"

# 2) Given the following code, '11238' is a key and 23 is a value
{ '11238':23, '10011':47 }

# 3) How would you add a 'low' of 54 to the following dictionary?
weather = { 'high':66, 'appearance':'cloudy' }
weather['low'] = 54

# 4) How can we easily get the total of the list below?
# How about a count of how many elements are in the list?
numbers = [ 1,2,3,4,5,6,7 ]
print sum( numbers )
print len( numbers )

# 5) Print the 3rd element of a list named dogs.
dogs = [ 'Labrador Retriever', 'Rottweiler', 'Shih Tzu', 'Miniature Schnauzer', 'Lhasa Apso', 'Yorkshire Terrier', 'Bulldog', 'Dobermann Pinscher', 'Bull Terrier', 'Weimaraner', 'Pug' ]
print dogs[2]

# 5a) Given the following dictionary, how can we get a list of all three ZIP codes?
data = { '11238':23, '10011':47, '10012':10 }
print data.keys()

# 5b) Write a for loop that prints all three zip codes on separate lines
for key in data.keys():
	print key

# 6) Given the following list, add together any numbers greater than 10.
values = [ 20,30,10,5,99 ]
sum( [ v  for v in values  if 10 < v ] )

# Or,
values = [ 20,30,10,5,99 ]
bigvalues = []
for v in values:
	if 10 < v:
		bigvalues.append( v )
print sum( bigvalues )

# Or,
values = [ 20,30,10,5,99 ]
total = 0
for v in values:
	if 10 < v:
		total += v # equivalent to total = total + v
print total


########################################################################
# 2: GO OVER HOMEWORK


########################################################################
# 3: Save a CSV file

# http://project.wnyc.org/dogs-of-nyc/

# On the map panel,
# Click "data" on the bottom left corner
# https://www.google.com/fusiontables/data?docid=1pKcxc8kzJbBVzLu_kgzoAMzqYhZyUhtScXjB0BQ#rows:id=1

# File > Download > All rows, CSV, Download

# Move the CSV file to your Lede folder


########################################################################
# 4: Poke around with it in the terminal/Babun

# In the terminal/babun,
# move to your Lede folder
## (pwd, cd, ls are your friends)

# Rename the CSV file, so it has NO spaces, say Dogs.csv
# Type mv D and hit tab
# You'll get mv Dogs\ of\ NYC\ \|\ WNYC.csv
## mv Dogs\ of\ NYC\ \|\ WNYC.csv Dogs.csv
# (move) (but it also renames too)


## wc -l Dogs.csv
# (word count, but count lines instead of words)

## cat Dogs.csv
# (see everything in the file Dogs.csv)

## head -n 10 Dogs.csv
# (see the first 10 lines in the file Dogs.csv)
# You can see the header of the CSV now

## tail -n 10 Dogs.csv
# (see the last 10 lines in the file Dogs.csv)

## head -n 10 Dogs.csv > sample.csv
# (save the first 10 lines in the file Dogs.csv to a new file sample.csv)


########################################################################
# 5: Poke around with it in Python

# IMPORTING PYTHON MODULES/LIBRARIES
# READING CSV'S INTO PYTHON

# In Sublime Text,

import csv
ourfile = open( "sample.csv","rb" )
dogs_csvreader = csv.reader( ourfile )
print type( dogs_csvreader )

# In terminal/babun,
# you get the result
# <type '_csv.reader'>

for dog in dogs_csvreader: # loop over each row
	print dog # the row
	print dog[0] # the row's 1st value

# In terminal/babun,
# you get the result
# ['dog_name', 'gender', 'breed', 'birth', 'dominant_color', 'secondary_color', 'third_color', 'spayed_or_neutered', 'guard_or_trained', 'borough', 'zip_code']
# dog_name
# ['Buddy', 'M', 'Afghan Hound', 'Jan-00', 'BRINDLE', 'BLACK', 'n/a', 'Yes', 'No', 'Manhattan', '10003']
# Buddy
# ['Nicole', 'F', 'Afghan Hound', 'Jul-00', 'BLACK', 'n/a', 'n/a', 'Yes', 'No', 'Manhattan', '10021']
# Nicole
# ['Abby', 'F', 'Afghan Hound', 'Nov-00', 'BLACK', 'TAN', 'n/a', 'Yes', 'No', 'Manhattan', '10034']
# Abby
# ['Chloe', 'F', 'Afghan Hound', 'Jan-02', 'WHITE', 'BLOND', 'n/a', 'Yes', 'No', 'Manhattan', '10024']
# Chloe
# ['Jazzle', 'F', 'Afghan Hound', 'Oct-02', 'BLOND', 'WHITE', 'BLACK', 'Yes', 'No', 'Manhattan', '10022']
# Jazzle
# ['Trouble', 'M', 'Afghan Hound', 'Jan-03', 'BLOND', 'WHITE', 'BLACK', 'Yes', 'No', 'Bronx', '10472']
# Trouble
# ['Grace', 'F', 'Afghan Hound', 'Jun-03', 'CREAM', 'n/a', 'n/a', 'Yes', 'No', 'Manhattan', '10021']
# Grace
# ['Sisu', 'M', 'Afghan Hound', 'Oct-04', 'BLACK', 'WHITE', 'GRAY', 'No', 'No', 'Manhattan', '10023']
# Sisu
# ['Jakie', 'M', 'Afghan Hound', 'Feb-05', 'WHITE', 'n/a', 'n/a', 'No', 'No', 'Queens', '11354']
# Jakie


# INSTEAD OF csv.reader() YOU PROBABLY WANT csv.DictReader()

# In Sublime Text,

import csv
ourfile = open( "sample.csv" )
dogs_listofdicts = list( csv.DictReader( ourfile ) ) # list of dictionaries
print type( dogs_listofdicts )

# In terminal/babun,
# you get the result
# <type 'list'>

for dog in dogs_listofdicts: # loop over each row
	print dog # the row
	print dog['gender'] # the row's 'gender' value

# In terminal/babun,
# you get the result
# {'gender': 'M', 'breed': 'Afghan Hound', 'secondary_color': 'BLACK', 'dominant_color': 'BRINDLE', 'guard_or_trained': 'No', 'birth': 'Jan-00', 'third_color': 'n/a', 'borough': 'Manhattan', 'dog_name': 'Buddy', 'zip_code': '10003', 'spayed_or_neutered': 'Yes'}
# M
# {'gender': 'F', 'breed': 'Afghan Hound', 'secondary_color': 'n/a', 'dominant_color': 'BLACK', 'guard_or_trained': 'No', 'birth': 'Jul-00', 'third_color': 'n/a', 'borough': 'Manhattan', 'dog_name': 'Nicole', 'zip_code': '10021', 'spayed_or_neutered': 'Yes'}
# F
# {'gender': 'F', 'breed': 'Afghan Hound', 'secondary_color': 'TAN', 'dominant_color': 'BLACK', 'guard_or_trained': 'No', 'birth': 'Nov-00', 'third_color': 'n/a', 'borough': 'Manhattan', 'dog_name': 'Abby', 'zip_code': '10034', 'spayed_or_neutered': 'Yes'}
# F
# {'gender': 'F', 'breed': 'Afghan Hound', 'secondary_color': 'BLOND', 'dominant_color': 'WHITE', 'guard_or_trained': 'No', 'birth': 'Jan-02', 'third_color': 'n/a', 'borough': 'Manhattan', 'dog_name': 'Chloe', 'zip_code': '10024', 'spayed_or_neutered': 'Yes'}
# F
# {'gender': 'F', 'breed': 'Afghan Hound', 'secondary_color': 'WHITE', 'dominant_color': 'BLOND', 'guard_or_trained': 'No', 'birth': 'Oct-02', 'third_color': 'BLACK', 'borough': 'Manhattan', 'dog_name': 'Jazzle', 'zip_code': '10022', 'spayed_or_neutered': 'Yes'}
# F
# {'gender': 'M', 'breed': 'Afghan Hound', 'secondary_color': 'WHITE', 'dominant_color': 'BLOND', 'guard_or_trained': 'No', 'birth': 'Jan-03', 'third_color': 'BLACK', 'borough': 'Bronx', 'dog_name': 'Trouble', 'zip_code': '10472', 'spayed_or_neutered': 'Yes'}
# M
# {'gender': 'F', 'breed': 'Afghan Hound', 'secondary_color': 'n/a', 'dominant_color': 'CREAM', 'guard_or_trained': 'No', 'birth': 'Jun-03', 'third_color': 'n/a', 'borough': 'Manhattan', 'dog_name': 'Grace', 'zip_code': '10021', 'spayed_or_neutered': 'Yes'}
# F
# {'gender': 'M', 'breed': 'Afghan Hound', 'secondary_color': 'WHITE', 'dominant_color': 'BLACK', 'guard_or_trained': 'No', 'birth': 'Oct-04', 'third_color': 'GRAY', 'borough': 'Manhattan', 'dog_name': 'Sisu', 'zip_code': '10023', 'spayed_or_neutered': 'No'}
# M
# {'gender': 'M', 'breed': 'Afghan Hound', 'secondary_color': 'n/a', 'dominant_color': 'WHITE', 'guard_or_trained': 'No', 'birth': 'Feb-05', 'third_color': 'n/a', 'borough': 'Queens', 'dog_name': 'Jakie', 'zip_code': '11354', 'spayed_or_neutered': 'No'}
# M

number_of_dogs_named_Trouble = 0
for dog in dogs_listofdicts:
	if dog['dog_name'] == "Trouble":
		number_of_dogs_named_Trouble += 1
print number_of_dogs_named_Trouble

# In terminal/babun,
# you get the result
# 1

myzipcode = "11238"
number_of_dogs_in_my_zipcode = 0
for dog in dogs_listofdicts:
	if dog['zip_code'] == myzipcode:
		number_of_dogs_in_my_zipcode += 1
print number_of_dogs_in_my_zipcode

# In terminal/babun,
# you get the result
# 0

# Wait we want to see the full dogs data now. Change the above to the following:
import csv
ourfile = open( "Dogs.csv" )
dogs_listofdicts = list( csv.DictReader( ourfile ) )

myzipcode = "11238"
number_of_dogs_in_my_zipcode = 0
for dog in dogs_listofdicts:
	if dog['zip_code'] == myzipcode:
		number_of_dogs_in_my_zipcode += 1
print number_of_dogs_in_my_zipcode

# In terminal/babun,
# you get the result
# 594

# NOT IN

zipcode_list = []
for dog in dogs_listofdicts:
	if dog['zip_code'] not in zipcode_list:
		zipcode_list.append( dog['zip_code'] )
print zipcode_list

# In terminal/babun,
# you get the result
# ['10003', '10021', '10034', '10024', '10022', '10472', '10023', '11354', '10469', '10473', '10308', '11385', '11364', '10038', '11373', '10457', '11206', '11357', '11423', '10309', '10310', '11235', '11420', '11421', '11379', '11412', '11207', '10463', '11362', '11368', '11205', '11372', '11377', '10002', '10467', '10128', '11697', '10455', '10037', '10028', '10466', '10014', '11211', '10312', '11434', '10029', '10470', '11356', '11375', '11234', '10009', '11355', '11693', '10305', '11231', '10016', '11212', '11104', '11209', '10465', '11219', '11203', '11224', '11238', '10452', '11215', '10011', '11418', '11218', '11223', '11228', '10013', '11432', '11435', '11249', '11101', '10459', '10036', '10039', '11221', '11102', '11422', '10462', '11414', '10461', '11370', '10301', '11361', '10306', '11236', '10040', '10032', '10302', '11229', '10025', '10471', '10012', '10030', '10026', '10017', '11222', '11419', '10314', '11415', '10069', '10010', '11220', '10456', '10019', '10304', '11204', '11365', '11427', '11106', '10303', '11232', '11214', '11201', '11367', '10035', '11208', '11363', '11413', '10033', '10454', '10001', '10307', '10458', '11374', '11417', '10007', '10460', '10474', '10453', '11237', '11694', '10027', '11217', '10468', '11103', '11226', '11225', '10451', '11369', '11378', '11105', '11216', '11691', '11429', '10031', '11433', '11426', '11358', '11213', '11692', '11233', '10005', '11004', '11210', '10464', '10044', '11428', '11230', '10123', '11416', '10113', '11366', '11202', '11360', '11411', '11436', '11239', '10280', '10018', '11425', '10282', '10004', '10475', '10006', '10313', '10163', '10008', '10120', '11005', '10020', '11243', '10159', '10108', '10150', '10162', '10156', '11386', '10015', '10112', '11690', '10129', '10125', '10080', '10172', '10274', '10043', '11431', '10101', '10276', '11352', '10116', '11353', '10203', '10079', '10185', '11242', '10119', '10153', '10175', '11388', '10045', '10138', '10111', '10107', '10151', '10118', '11430', '11351', '11359', '10154']

for zipcode in zipcode_list:
	number_of_dogs_in_zipcode = 0
	for dog in dogs_listofdicts:
		if dog['zip_code'] == zipcode:
			number_of_dogs_in_zipcode += 1
	print "There are",number_of_dogs_in_zipcode,"dogs in",zipcode

# In terminal/babun,
# you get the result
# There are 1000 dogs in 10003
# There are 1255 dogs in 10021
# There are 392 dogs in 10034
# There are 1684 dogs in 10024
# There are 775 dogs in 10022
# There are 537 dogs in 10472
# There are 1487 dogs in 10023
# There are 317 dogs in 11354
# There are 435 dogs in 10469
# There are 740 dogs in 10473
# There are 747 dogs in 10308
# There are 1025 dogs in 11385
# There are 419 dogs in 11364
# There are 375 dogs in 10038
# There are 481 dogs in 11373
# There are 251 dogs in 10457
# There are 724 dogs in 11206
# There are 645 dogs in 11357
# There are 130 dogs in 11423
# There are 760 dogs in 10309
# There are 448 dogs in 10310
# There are 729 dogs in 11235
# There are 203 dogs in 11420
# There are 323 dogs in 11421
# There are 744 dogs in 11379
# There are 127 dogs in 11412
# There are 370 dogs in 11207
# There are 655 dogs in 10463
# There are 174 dogs in 11362
# There are 315 dogs in 11368
# There are 349 dogs in 11205
# There are 520 dogs in 11372
# There are 723 dogs in 11377
# There are 774 dogs in 10002
# There are 505 dogs in 10467
# There are 1537 dogs in 10128
# There are 66 dogs in 11697
# There are 318 dogs in 10455
# There are 138 dogs in 10037
# There are 1159 dogs in 10028
# There are 298 dogs in 10466
# There are 986 dogs in 10014
# There are 806 dogs in 11211
# There are 1609 dogs in 10312
# There are 167 dogs in 11434
# There are 995 dogs in 10029
# There are 108 dogs in 10470
# There are 233 dogs in 11356
# There are 840 dogs in 11375
# There are 1011 dogs in 11234
# There are 1065 dogs in 10009
# There are 399 dogs in 11355
# There are 172 dogs in 11693
# There are 771 dogs in 10305
# There are 695 dogs in 11231
# There are 775 dogs in 10016
# There are 255 dogs in 11212
# There are 308 dogs in 11104
# There are 1082 dogs in 11209
# There are 788 dogs in 10465
# There are 255 dogs in 11219
# There are 185 dogs in 11203
# There are 402 dogs in 11224
# There are 594 dogs in 11238
# There are 312 dogs in 10452
# There are 1346 dogs in 11215
# There are 1537 dogs in 10011
# There are 262 dogs in 11418
# There are 711 dogs in 11218
# There are 533 dogs in 11223
# There are 560 dogs in 11228
# There are 454 dogs in 10013
# There are 250 dogs in 11432
# There are 245 dogs in 11435
# There are 134 dogs in 11249
# There are 361 dogs in 11101
# There are 272 dogs in 10459
# There are 591 dogs in 10036
# There are 199 dogs in 10039
# There are 438 dogs in 11221
# There are 373 dogs in 11102
# There are 96 dogs in 11422
# There are 586 dogs in 10462
# There are 375 dogs in 11414
# There are 687 dogs in 10461
# There are 263 dogs in 11370
# There are 576 dogs in 10301
# There are 404 dogs in 11361
# There are 1359 dogs in 10306
# There are 409 dogs in 11236
# There are 299 dogs in 10040
# There are 356 dogs in 10032
# There are 259 dogs in 10302
# There are 767 dogs in 11229
# There are 1988 dogs in 10025
# There are 371 dogs in 10471
# There are 601 dogs in 10012
# There are 175 dogs in 10030
# There are 316 dogs in 10026
# There are 278 dogs in 10017
# There are 558 dogs in 11222
# There are 171 dogs in 11419
# There are 1657 dogs in 10314
# There are 174 dogs in 11415
# There are 170 dogs in 10069
# There are 596 dogs in 10010
# There are 607 dogs in 11220
# There are 353 dogs in 10456
# There are 821 dogs in 10019
# There are 564 dogs in 10304
# There are 452 dogs in 11204
# There are 404 dogs in 11365
# There are 142 dogs in 11427
# There are 406 dogs in 11106
# There are 304 dogs in 10303
# There are 213 dogs in 11232
# There are 690 dogs in 11214
# There are 1149 dogs in 11201
# There are 315 dogs in 11367
# There are 310 dogs in 10035
# There are 363 dogs in 11208
# There are 107 dogs in 11363
# There are 142 dogs in 11413
# There are 424 dogs in 10033
# There are 287 dogs in 10454
# There are 459 dogs in 10001
# There are 322 dogs in 10307
# There are 355 dogs in 10458
# There are 385 dogs in 11374
# There are 313 dogs in 11417
# There are 139 dogs in 10007
# There are 279 dogs in 10460
# There are 70 dogs in 10474
# There are 264 dogs in 10453
# There are 248 dogs in 11237
# There are 283 dogs in 11694
# There are 536 dogs in 10027
# There are 616 dogs in 11217
# There are 308 dogs in 10468
# There are 319 dogs in 11103
# There are 316 dogs in 11226
# There are 277 dogs in 11225
# There are 282 dogs in 10451
# There are 203 dogs in 11369
# There are 577 dogs in 11378
# There are 448 dogs in 11105
# There are 315 dogs in 11216
# There are 154 dogs in 11691
# There are 75 dogs in 11429
# There are 366 dogs in 10031
# There are 100 dogs in 11433
# There are 235 dogs in 11426
# There are 518 dogs in 11358
# There are 165 dogs in 11213
# There are 106 dogs in 11692
# There are 289 dogs in 11233
# There are 186 dogs in 10005
# There are 184 dogs in 11004
# There are 198 dogs in 11210
# There are 123 dogs in 10464
# There are 79 dogs in 10044
# There are 117 dogs in 11428
# There are 391 dogs in 11230
# There are 2 dogs in 10123
# There are 137 dogs in 11416
# There are 2 dogs in 10113
# There are 137 dogs in 11366
# There are 5 dogs in 11202
# There are 218 dogs in 11360
# There are 77 dogs in 11411
# There are 72 dogs in 11436
# There are 112 dogs in 11239
# There are 198 dogs in 10280
# There are 162 dogs in 10018
# There are 2 dogs in 11425
# There are 120 dogs in 10282
# There are 87 dogs in 10004
# There are 109 dogs in 10475
# There are 103 dogs in 10006
# There are 5 dogs in 10313
# There are 8 dogs in 10163
# There are 12 dogs in 10008
# There are 1 dogs in 10120
# There are 4 dogs in 11005
# There are 5 dogs in 10020
# There are 13 dogs in 11243
# There are 2 dogs in 10159
# There are 2 dogs in 10108
# There are 6 dogs in 10150
# There are 3 dogs in 10162
# There are 2 dogs in 10156
# There are 4 dogs in 11386
# There are 2 dogs in 10015
# There are 1 dogs in 10112
# There are 5 dogs in 11690
# There are 1 dogs in 10129
# There are 1 dogs in 10125
# There are 2 dogs in 10080
# There are 1 dogs in 10172
# There are 1 dogs in 10274
# There are 2 dogs in 10043
# There are 4 dogs in 11431
# There are 6 dogs in 10101
# There are 2 dogs in 10276
# There are 3 dogs in 11352
# There are 1 dogs in 10116
# There are 1 dogs in 11353
# There are 2 dogs in 10203
# There are 1 dogs in 10079
# There are 2 dogs in 10185
# There are 1 dogs in 11242
# There are 2 dogs in 10119
# There are 1 dogs in 10153
# There are 2 dogs in 10175
# There are 1 dogs in 11388
# There are 1 dogs in 10045
# There are 1 dogs in 10138
# There are 1 dogs in 10111
# There are 1 dogs in 10107
# There are 1 dogs in 10151
# There are 1 dogs in 10118
# There are 1 dogs in 11430
# There are 1 dogs in 11351
# There are 1 dogs in 11359
# There are 1 dogs in 10154
