########################################################################
# 1: MAKE YOUR MAC SAY STUFF

# In the terminal,
# type
say 'I am your father Luke'

# OR, to specify a voice:
# In the terminal,
# type
say -v Agnes 'I am your father Luke'
# For more voices:
# http://www.gabrielserafini.com/blog/2008/08/19/mac-os-x-voices-for-using-with-the-say-command/



########################################################################
# 2: MAKE YOUR MAC SAY STUFF WHEN YOU RUN A PYTHON FILE

# In SublimeText,
# create a file in your Lede folder called whatever.py
# and type
import os
os.system( "say 'I am your father Luke'" )

# In the terminal,
# run whatever.py



# FOR EXAMPLE:
# So in your homework 8, you can add
import os
for quake in quakes:
	os.system( "say "+eq_to_sentence( quake ) )
# Run your python file, and listen to earthquake reports!



########################################################################
# 3: MAKE YOUR MAC DO STUFF REPEATEDLY

# In the terminal, type
man crontab
# (manual) This is a manual for the command `crontab`
# d for down
# b for back
# q for quit
# Probably not too helpful. I mean, who writes like that?



# In SublimeText,
# create a file in your Lede folder called cron.txt
# and type
* * * * * * say "It's a new minute"
# And ADD AN EXTRA BLANK LINE.
# * * * * * * tells your computer to run this every minute.

# In the terminal,
# move to your Lede folder
# and type
crontab cron.txt
# OR, to save the error messages to a file in the Lede folder called cron_error.txt:
crontab cron.txt  2>> cron_error.txt
	# If you get a message saying "you have mail", you can erase those in the terminal by typing
	> /var/mail/$USER


# OR, to run python files repeatedly:
# In SublimeText,
# create a file in your Lede folder called whatever.py
# and type
import os
os.system( "say 'I am your father Luke'" )
print "print whut"

# In SublimeText,
# create a file in your Lede folder called cron.txt
# and type
* * * * * ~/anaconda/bin/python ~/Desktop/Lede/whatever.py  >> ~/Desktop/Lede/whatever_output.txt  2>> ~/Desktop/Lede/whatever_error.txt
# And ADD AN EXTRA BLANK LINE.
# * * * * * * tells your computer to run this every minute.

# In the terminal,
# move to your Lede folder
# and type
crontab cron.txt
# And blah blah blah same points as above.


# You can specify how often this runs:
# http://www.nncron.ru/help/EN/working/cron-format.htm

# * * * * * * tells your computer to run this every minute.
	# the 1st * means "do this every single minute"
	# the 2nd * means "do this every single hour"
	# the 3rd * means "do this every single day of the month"
	# the 4th * means "do this every single month"
	# the 5th * means "do this every single day of the week"
	# the 6th * means "do this every single year"

# */5 * * * * * tells your computer to run this every 5 minutes.

# 50 12 * * * * tells your computer to run this whenever it's 12:50.

# 0 13 * 6,7 1,3 say -v Bells "Class is over"
# tells your computer to say "Class is over" whenever it's 13:00 on June and July Mondays and Wednesdays.



# If you want to see what you've told cron to do,
crontab -l
# OR, to save it to a file in the Lede folder called cron_existing.txt:
crontab -l  > cron_existing.txt

# If you get tired of it,
crontab -r
# removes your crontab file.



########################################################################
# 4: MAKE YOUR PC DO STUFF REPEATEDLY

# https://technet.microsoft.com/en-us/library/cc725744.aspx
# Courtesy of Mr. Sebastian Munoz-Najar Galvez!
