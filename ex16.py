# G
# This is part of the LPTHW series.
# Programmer:           Victoria Brown
# Date:                 October 2016
# ex16.py

# Import argv module
from sys import argv

# get script and file name from argv
script, filename = argv

# get permission from user to erase file
print "We're going to erase %r." % filename
print "If you don't wan that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

# delete the file
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

# get 3 lines of input from user
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# write these 3 lines to the file
print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# close the file
print "And finally, we close it."
target.close()
