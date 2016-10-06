# Simple program to get input from user with Python language.
# Programmer:           Victoria Brown
# Date:                 October 2016

# Get age, height, and weight from user
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh?")

# Print out variables I just got from user
print "So, you're %r old, %r tall, and %r heavy." % (
    age, height, weight)
