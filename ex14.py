# Simple program with style like Zork or Adventure.
# Gets argv when excuted, and asks a series of questions to user.
# This is part of the LPTHW series.
# Programmer:           Victoria Brown
# Date:                 October 2016
# ex14.py

# Import module argv
from sys import argv

# Get arguments from when program is run.
script, user_name = argv

# Variable for prompt
prompt = '> '

# Print out info
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
# Set if likes or not
likes = raw_input(prompt)

# Set where user lives
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

# Set what kind of computer user has
print "What kind of computer do you have?"
computer = raw_input(prompt)

# Print out info you found out
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
