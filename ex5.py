# Simple program to see more variables in Python language.
# Programmer:           Victoria Brown
# Date:                 October 2016

# Variables:
name = 'Victoria E. Brown'
age = 20
height = 65  # inches
weight = 140 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Print em out!
print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are %s." % teeth

print "If I add %d, %d, and %d I get %d" % (
    age, height, weight, age + height + weight)
