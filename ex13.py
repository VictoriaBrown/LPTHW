# Programmer:           Victoria Brown
# Date:                 October 2016

# Import module statement
from sys import argv

# argv -> argument variable
# This holds the arguments you pass to the script when you run it
# This line 'unpacks' argv and assigns the 4 variables you can work with
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
