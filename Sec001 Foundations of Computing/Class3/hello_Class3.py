#Inclass Test
n = 2
if n< 2:
	print "Small"
elif n == 2:
	print"Medium"
else:
	print "Large"


data = {'11283': 23, '10011':47, '10012':10}
#to print a list of all 3 ZIP codes
data.keys()
#to print all three zip codes on separate lines
for zip_codes in data.keys():
   print zip_codes

#Given the following list, add together any numbers greater than 10
values = [20,30,10,5,99]
#Two ways
#First:
total = 0
for value in values:
	if value > 10:
		total=total+value
print total
#Second:
above_ten=[]
for value in values:
	if value > 10:
		above_ten.append(value)
print sum(above_ten)

