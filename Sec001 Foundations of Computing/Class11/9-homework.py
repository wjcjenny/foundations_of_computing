########################################################################
# 2: homework 9

# 1.
# It's good practice to send back the same data type from a function every time.
def to_cups( amount,measurement ):
	if measurement == "cups":
		return float( amount )
	elif measurement == "tablespoons":
		return float( amount )/16
	elif measurement == "teaspoons":
		return float( amount )/48

def to_tablespoons( amount,measurement ):
	if measurement == "cups":
		return float( amount )*16
	elif measurement == "tablespoons":
		return float( amount )
	elif measurement == "teaspoons":
		return float( amount )/3

def to_teapoons( amount,measurement ):
	if measurement == "cups":
		return float( amount )*48
	elif measurement == "tablespoons":
		return float( amount )*3
	elif measurement == "teaspoons":
		return float( amount )

print to_cups( 3,'tablespoons' )
print to_tablespoons( 9,'teaspoons' )
print to_teapoons( 1,'cups' )


# 2.
dry_ingredients = [ "salt","flour","baking powder","baking soda","cinnamon","yeast" ]
wet_ingredients = [ "water","butter","egg","milk","chocolate","sugar" ]

def to_grams( amount,measurement,ingredient ):
	amount_in_cups = to_cups( amount,measurement )
	# if the ingredient is dry:
	if ingredient in dry_ingredients:
		return amount_in_cups*125
	# if the ingredient is wet:
	elif ingredient in wet_ingredients:
		return amount_in_cups*240

print to_grams( 3,"cups","flour" )
print to_grams( 2,"tablespoons","water" )


# 3.
recipe = [
  { 'amount': 3, 'measurement': 'cups', 'ingredient': 'flour' },
  { 'amount': 1, 'measurement': 'tablespoons', 'ingredient': 'milk' },
  { 'amount': 0.25, 'measurement': 'teaspoons', 'ingredient': 'salt' },
  { 'amount': 1, 'measurement': 'cups', 'ingredient': 'butter' },
  { 'amount': 0.75, 'measurement': 'cups', 'ingredient': 'baking powder' },
  { 'amount': 0.25, 'measurement': 'cups', 'ingredient': 'egg' }
]

weight = 0
for line in recipe:
	grams = to_grams( line['amount'],line['measurement'],line['ingredient'] )
	print grams,"grams"
	weight += grams
print "Total weight is",weight,"grams"

# OR,
print "Total weight is",sum( [ to_grams( line['amount'],line['measurement'],line['ingredient'] )  for line in recipe ] ),"grams"


# 4.