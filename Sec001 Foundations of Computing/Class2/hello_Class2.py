print "Hello again"
#name = "Jenny"
#city ='Miami'
#age = 26

#Dictionary
me = {'name': 'Jiachuan', 'city':'Shanghai','age':25}
print me
print me ['city']
#this is printing the Shanghai
#print city
#this is printing Miami, defined previous
print "Four yeaars ago I was", me ['age'] - 4

#print "I own", me['pets']
#looking of "I own 2 cats "
pets = "2 cats"
print "I own" , pets

me ['pets']= "2 cats"
print "I own", me ['pets']

print me
#redifine me, put pets into, it comes out {'city': 'Shanghai', 'age': 25, 'name': 'Jiachuan', 'pets': '2 cats'}

#Key Error:'hometown'
# you dont have anything under that entry
#print me['hoetown']

presidents = {
	'Obama': 2009,
	'Bush':2001,
	'Clinton': 1993,
	'Bush': 1989,
	'Regan': 1981,
	'Carter':1997
}
print "Obama became president in", presidents ['Obama']
print "Bush became president in", presidents ['Bush']

#get a list of keys from a python dictionary?
print presidents.keys()
print type(presidents)
#print <type 'dict'>
print type("Hello")
#print <type 'str'>
print type(5)
#print <type 'int'>
print type(presidents.keys)
#print <type 'list'>
print type(presidents.keys())
#print <type 'builtin_function_or_method'>

print len("Hello")
#this is a function
print "Hello".upper()
#this is a method


#Lists
presidents_names = presidents.keys()
print presidents_names

#me ['name']
#array shu zu from 0
print presidents_names[1]
print presidents_names[2]
print presidents_names[0]

years = [4, 20, 6, 0, 20, 5, 1, 3, 1, 0, 7, 2, 1.5, 11, 0, 15, 2, 2, 10, 0]
print type (years)
#<type 'list'>

#How many elements are in years?
print "there are", len(years), "elements in years"
print len (years)

#Get the last element
print "the last number in the list is", years[19]
#print years [len(years)]
#print years[20]
#IndexError: list index out of range
print years [len(years) - 1]

print "The maximum number is", max(years)
print "The minium number is", min(years)
print "If I add together all the numbers I get", sum(years)
print "An average of the years is", sum(years) / len(years)
print "The median number of the years might be", years[11]
#No, it isnt because it isn't sorted

sorted_years = sorted(years)
print "here are the sorted years", sorted_years
print "years is still unsorted", years

#A function called sorted()
#print sorted(years)

#A method called .sort()
#print years.sort()
#print years

print "The median number of the years is", sorted_years[10]


colors = ['red', 'blue','yellow','green']
print colors[0]
print colors[1]
print colors[2]
print colors[3]

colors.append('purple')
print colors
#list.append(x) Add an item to the end of the list; equivalent to a[len(a):] = [x]


#something cool: for loops
favorite_color = "blue"
for color in colors:
	print color, "is", len(color), "letters long"
	if favorite_color == color:
		print "thats my favorite color too."

for potato_soup in colors:
	print potato_soup, "is", len(potato_soup), "letters long"


#Common pattern for counting
above_the_median = 0
for year in years:
	print "Looking at", year
	if year > 2:
		above_the_median = above_the_median + 1
print above_the_median, "students are above the median."






