#homework 
#Jiachuan Wu

# TIPS

# To find out if a value is in a list, you can use: 'blue' in ['orange', 'yellow', 'red']
# If you're ending up with a lot of 0's where you know there shouldn't be any, 
# think about data types and the difference between 5 / 2 and 5.0 / 2 (try it out in IPython if you want).
# I know I've said it a hundred times, but don't sweat it if the more difficult pieces are more... difficult.

#1. COOKING HELPER
#Cooking from recipes can be tough if you don't know how to convert units. Let's write a program to help that out!
#Write three functions to_cups, to_tablespoons and to_teaspoons. 
#Each function takes two parameters, an amount and a measurement. 
#Convert the amount of that measurement into the target measurement. 
#i.e., to_teaspoons(3, 'tablespoons') should return the number 9, since 3 tablespoons = 9 teaspoons.

# Use these to test your function, and ask Google or Wolfram Alpha 
#(http://www.wolframalpha.com/input/?i=1+cup+in+tablespoons)

def to_cups(a,b):
	if b == "tablespoons":
		return float(a ) / 16
print to_cups(3, 'tablespoons')

def to_tablespoons(c,d):
	if d == "teaspoons":
		return float(c) / 3
print to_tablespoons(9, 'teaspoons')

def to_teaspoons(e,f):
	if f == "cups":
		return float(e) * 48
print to_teaspoons(1, 'cups')



#2. BRANCHING OUT

#If you're baking, measuring by weight is much much better than measuring by volume. 
#Make a function called to_grams that takes an amount, a measurement and an ingredient name. 
#It should return the number of grams the ingredient weighs.
#Unfortunately different ingredients weigh different amounts - one cup of flour is 125 grams, 
#but one cup of water is 240 grams!

# Use these to test your function
dry_ingredients = ['salt', 'flour', 'baking powder', 'baking soda', 'cinnamon', 'yeast']
wet_ingredients = ['water', 'butter', 'egg', 'milk', 'chocolate', 'sugar']

def to_grams(g,h,i):
	if i in dry_ingredients:
		if h == "cups":
			return float(g) * 125
		if h =="tablespoons":
			return float(g) * 125 / 16
		if h =="teaspoons":
			return float(g) * 125 / 48
	if i in wet_ingredients:
		if h == "cups":
			return float(g) * 240
		if h == "tablespoons":
			return float(g) * 240 / 16
		if h == "teaspoons":
			return float(g) * 240 / 48
# print to_grams(3, 'cups', 'flour')
# print to_grams(2, 'tablespoons', 'water')

# Dry ingredients (125 grams per cup): salt, flour, baking powder, baking soda, cinnamon, yeast
# Wet ingredients (240 grams per cup): water, butter, egg, milk, chocolate, sugar
# Warning: This list is reeeaaaally not accurate.

# 3. RING IT UP
# Now we have a big ol' recipe

recipe = [
  { 'amount': 3, 'measurement': 'cups', 'ingredient': 'flour' },
  { 'amount': 1, 'measurement': 'tablespoons', 'ingredient': 'milk' },
  { 'amount': 0.25, 'measurement': 'teaspoons', 'ingredient': 'salt' },
  { 'amount': 1, 'measurement': 'cups', 'ingredient': 'butter' },
  { 'amount': 0.75, 'measurement': 'cups', 'ingredient': 'baking powder' },
  { 'amount': 0.25, 'measurement': 'cups', 'ingredient': 'egg' }
]
# What's the total gram weight of the entire recipe?

l = []
for item in recipe:
	l.append(to_grams(item['amount'],item['measurement'],item['ingredient']))
print sum(l)

# total = 0
# for item in recipe:
# 	print item['amount'], item['measurement'], item['ingredient']
# 	total += to_grams(item['amount'], item['measurement'], item['ingredient'])
# print total




# 4. BREAD CITY

# If you really like either baking or programming or algorithms, you can do this one:
# There's this magic thing called the Baker's Percentage when cooking bread.
# https://en.wikipedia.org/wiki/Baker_percentage
# http://www.craftybaking.com/howto/bakers-percentage-method
# http://thebakersguide.com/the-bakers-percentage
# It's just the weight of an ingredient vs. the weight of flour - 200 grams of water, 4 grams of yeast and 400 grams of flour = 50% water and 10% yeast. It's NOT the percentage of the total recipe, just the amount of the ingredient over the amount of flour (in that case it would be ~33% water).
# Let's say I want to make a yeasted dough (100% flour, 35% water, 35% milk, 4% yeast, 1.8% salt). My friend says she has 6 cups of flour. How many cups of water and milk, and teaspoons of yeast and salt do I need? You don't need a loop or anything, you should be able to do it piece by piece. You'll need to convert from volume to weight, then back to volume.
# Use the code below to convert between grams and other measurements. For example, grams_to_measurement(300, 'flour', 'cups') should convert 3 grams of flour into cups.

weight_flour = to_grams(6, 'cups', 'flour')
weight_water = weight_flour * 0.35
weight_milk = weight_flour * 0.35
weight_yeast = weight_flour * 0.04
weight_salt = weight_flour * 0.018

print weight_water
print weight_milk


def grams_to_measurement(amount, ingredient, measurement):
#   # Convert 1 measurement of the ingredient to grams
#   # to get the tablespoon:grams ratio
   conversion = to_grams(1, measurement, ingredient)
  
#   # Then invert it to get the grams:tablespoon ratio
   inverse = 1 / conversion
  
#   # Then multiply to get the amount of the measurement
   return inverse * amount

print grams_to_measurement(weight_water, 'water', 'cups'), 'water.'
print grams_to_measurement(weight_milk, 'milk', 'cups'), 'milk.'
print grams_to_measurement(weight_yeast, 'yeast', 'teaspoons'), 'yeast.'
print grams_to_measurement(weight_salt, 'salt', 'teaspoons'), 'salt.'










