#Jiachuan Wu
#May 27 2015
#Homework 1

#1. Prompt the user for their year of birth, and tell them (approximately):
#2. How old they are
year_of_birth = raw_input("Enter your year of birth:")
if int(year_of_birth) > 2015:
	print "The year you enter is in Future, try again!"
	year_of_birth = raw_input("Enter your year of birth:")

age = 2015 - int(year_of_birth)
print "You are approximately", age, "years old."

#3. How many times their heart has beaten? 
#I use 100 times per minute as the normal person's heart beaten rate.
Heart_Beaten = age * 365 * 24 * 60 * 100
print "Your heart has beaten", Heart_Beaten, "times in your life."

#4. How many times a blue whale's heart has beaten
#I use 72 times per minute as the blue whale's heart beaten rate.
Blue_Whale_Heart_Beaten = int(Heart_Beaten) * 72 / 100
print "A blue whale's heart has beaten", Blue_Whale_Heart_Beaten, "times in it life."

#5. How many times a rabbit's heart has beaten
#I use 325 times per minutas as the rabbit's heart beaten rate.
Rabbit_Heart_Beaten = int(Heart_Beaten) * 325 / 100
print "A rabbit's heart has beaten", Rabbit_Heart_Beaten, "times in it life."

#6. If the answer to (5) is more than a billion, say "XXX billion" instead of the very long raw number
Rabbit_HB_Ratio = float(Rabbit_Heart_Beaten) / 1000000000
Rounded_Ratio = round(Rabbit_HB_Ratio,1)
if Rabbit_HB_Ratio > 1:
	print "A rabbit's heart has beaten", Rounded_Ratio, "billion times in it life."
else:
	print "A rabbit's heart has beaten", Rabbit_Heart_Beaten, "times in it life."

#7. How old they are in Venus years
#8. How old they are in Neptune years
#Float
earth_days = 365.0
venus_days = 224.7
neptune_days = 60190.0
ratio1 = earth_days/venus_days
ratio2 = earth_days/neptune_days
venus_years  = int(age * ratio1)
print "Your age on Venus is", venus_years
neptune_years = int(age * ratio2)
print "Your age on Neptune is", neptune_years

#9. Whether they are the same age as you, older or younger
#10. If older or younger, how many years difference
age_difference = int(year_of_birth) - 1990
if int(year_of_birth) == 1990:
	print "Hooray!!!"
if int(year_of_birth) < 1990:
	print "YOU are", -int(age_difference), "years older than me:)"
if int(year_of_birth) > 1990:
	print "YOU are", int(age_difference), "years younger than me !!!!"

#11. If they were born in an even or odd year
if int(year_of_birth) % 2 == 0 :
	print "You born in a even year."
else:
	print "You born in a odd year."

#12. How many times the Pittsburgh Steelers have won the Superbowl.
if int(year_of_birth) <= 1975:
	print "The Pittsburgh Steelers have won the Superbowl 6 times."
elif int(year_of_birth) <= 1976:
	print "The Pittsburgh Steelers have won the Superbowl 5 times."
elif int(year_of_birth) <= 1979:
	print "The Pittsburgh Steelers have won the Superbowl 4 times."
elif int(year_of_birth) <= 1980:
 	print "The Pittsburgh Steelers have won the Superbowl 3 times."
elif int(year_of_birth) <= 2006:
	print "The Pittsburgh Steelers have won the Superbowl 2 time."
elif int(year_of_birth) <= 2009:
 	print "The Pittsburgh Steelers have won the Superbowl 1 time."
else:
 	print "The Pittsburgh Steelers have not won the Superbowl yet."

#13. Which US President was in office when they were born (FDR onward)
if int(year_of_birth) <= 1933:
	print "When you born, Fanklin D.Roosevelt was not yet in office."
elif int(year_of_birth) <= 1944:
	print "When you born, Fanklin D.Roosevelt was in office."
elif int(year_of_birth) <= 1952:
	print "When you born, Harry S. Truman was in office."
elif int(year_of_birth) <= 1960:
	print "When you born, Dwight D. Eisenhower was in office."
elif int(year_of_birth) <= 1962:
	print "When you born, John F. Kennedy was in office."
elif int(year_of_birth) <= 1968:
	print "When you born, Lyndon B. Johnson was in office."
elif int(year_of_birth) <= 1973:
	print "When you born, Richard Nixion was in office."
elif int(year_of_birth) <= 1976:
	print "When you born, Gerald Ford was in office."
elif int(year_of_birth) <= 1980:
	print "When you born, Jimmy Carter was in office."
elif int(year_of_birth) <= 1988:
	print "When you born, Ronald Reagan was in office."
elif int(year_of_birth) <= 1992:
	print "When you born, George H.W. Bush was in office."
elif int(year_of_birth) <= 2000:
	print "When you born, Bill Clinton was in office."
elif int(year_of_birth) <=2008:
	print "When you born, George W. Bush was in office."
elif int(year_of_birth) <=2015:
	print "When you born, Barack Obama was in office."




