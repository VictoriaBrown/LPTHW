# Simple program to see strings and text in Python language.
# Programmer:           Victoria Brown
# Date:                 October 2016

# Variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Print variables
print x
print y

# Print variables again
print "I said: %r." % x
print "I also said: '%s'." % y

# Joke isn't funny and print that.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# String concatenation
w = "This is the left side of..."
e = "a string with a right side."

print w + e
