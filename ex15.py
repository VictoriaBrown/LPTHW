# Get file name from user, open it, print it out using Python.
# This is part of the LPTHW series.
# Programmer:           Victoria Brown
# Date:                 October 2016
# ex14.py

# Import argv module
from sys import argv

# argv gets script name and file name and sets to variables
script, filename = argv

# Open the file and set it to a variable
txt = open(filename)

# Print out the file
print "Here's your file %r:" % filename
print txt.read()

# Get the same/different file and set it to a variable
print "Type the filename again:"
file_again = raw_input("> ")

# Open the file
txt_again = open(file_again)

# Print out the file
print txt_again.read()
