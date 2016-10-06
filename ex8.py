# Simple program to practice printing in Python language.
# Programmer:           Victoria Brown
# Date:                 October 2016

# Variable:
formatter = "%r %r %r %r"

# Print using formatter variable
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
