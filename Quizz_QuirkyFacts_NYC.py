# -*- coding: utf-8 -*-
print "Are you a New Yorker? Let's test it!"

point = 0 

#Question 1  75,000 trees 
ans1 = int(raw_input("How many trees does it take to print a Sunday edition of the New York Times? ▧ Hint: It's over 10000.\n"))
if ans1 >= 50000 and ans1 <= 100000:
	point = point +1 

#Question 2  $289,000 
ans2 = int(raw_input("Guess how much was the hightest permit for a one-year hot dog stand in Central Park in 2013? ▧ Hint: More than 100000 bucks! \n"))
if ans2 >= 200000 and ans2 <= 300000 :
	point = point +1 

#Question 3 2 
ans3 = int(raw_input("We know Manhattan is crowded. And during work week its population even becomes  _____ times: "))
if ans3 == 2:
	point = point +1 

#Question 4  25%
ans4 = int(raw_input("The Federal Reserve Bank on New York’s Wall Street contains vaults that are located 80 feet beneath the bank. Guess how many percent of the world’s gold bullion is there?\n"))
if ans4 >= 20 and ans4 <= 35:
	point = point +1 

#Question 5  20,000
ans5 = int(raw_input("Do you know Washington Square Park was once a grave? How many bodies were buried there? ▧ Hint: It's over 10000...\n"))
if ans5 >= 15000 and ans5 <= 25000:
	point = point +1 

if point == 4 or point == 5:
	print "Woohoo! You're undoubtedly a NYC expert!"
elif point == 2 or point == 3: 
	print "Not bad actually. Try to hang out more with some New York folks."
elif point == 0 or point == 1:
	print "Hi NYC newbie :)"


