
#Homework 7 
#Jiachuan Wu


#1) I'd like you to make a new column that's the integer difference between the original amount and the current amount. What's the largest? What's the smallest?
#As you know, the variable value is the value of the cell you're working on, but what if you want a different cell? You need to use cells['Column Name']['value'].

#The largest difference is 205000000, purpose is “provide uniformed armed security guard and/or supervisors”.
#The smallest is -239308762, purpose is “Work Order No.12200570”.

#2) You'll need a new column called scale that categorizes each contract based on how large the Original Amount is. 
#if the original amount is 0-9, scale should be 1, if 10-99, 2, if 100-999, 3, etc. Think about converting between data types, and watch out for decimals!
#If you run a text facet for the above, the results should be:

'''
1 - 83
3 - 85
4 - 2942
5 - 15963
6 - 7252
7 - 3229
8 - 561
9 - 42
10 - 4
'''

#original = int(cells["Original Amount"]["value"])
#count = 0
#while original > 0:
#	original = original / 10
#	count +=1
#return count

count = 0
a = 1909000.23
while a > 0:
	a = a / 10
	count = count + 1
	#print a
print count
#write return count in Jython

#3) What's the most popular agency for $100mil-$1bil contracts? 
#How about contracts between $100-$1000? $1000-$10,000?

# if the original amount is in the interval [100,000,000 - 1000,000,000],
#then the scale will be 9. Then make a text facet for "scale", then choose the number 9, there are 42 scales 9
# The most popular agency for $100mil-$1bil contracts is the Department of Education. 
#The most popular agency for contracts between $100-$1000 is the Department of Youth and Community Development. 
#For contracts between $1000-$10,000, the most popular agency is the Department of Education.

#5) How many contracts have had >80 versions?
# Make numeric facet for column "Version"
# Then put the lower slider to 80, and upper to maxium which is 110.
#There are 4 Contracts ahve had greater than 80 version.
#There Contact ID is:
#CT181620141401518
#CT185020131421543
#CTA181620147202251
#CTA181620147202281

#5) Convert End Date to a date and find out how many contracts are ending in 2025 or later.
#There are 68 contracts are ending in 2025 or later.

# Use GREL
#value.toDate('MM/DD/yy').toString('yyyy')

#When sorted with name,
'''
2013 3573
2014 9782
2015 10286
2016 2725
2017 1854
2018 1119
2019 449
2020 181
2021 60
2022 17
2023 22
2024 25
2025 6
2026 1
2028 12
2029 5
2030 4
2031 1
2032 3
2033 14
2034 7
2035 1
2036 4
2038 1
2039 2
2040 2
2041 2
2042 1
2043 1
2073 1
'''

#6) What are the top two vendors for consulting? How about for construction?
##First to put text facet for column "Contract Type"
##CONSULTANT 2655
##For consulting, sort the cureent amount column by number
##The top two vendors for cunsulting is "TELESECTOR RESOURCES GROUP INC A VERIZON SERVICES GROUP" and "AMERICAN TRAFFIC SOLUTIONS, INC.".

##Construction 3224
##For construction, sort the cureent amount column by number
## The top two vendors for counstruction is "Mill Basin Bridge Constructors LLC" and "DORMITORY AUTHORITY STATE OF NY"



















