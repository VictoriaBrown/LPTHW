# Copies one file to another using Python.
# This is part of the LPTHW series.
# Programmer:           Victoria Brown
# Date:                 October 2016
# ex17.py

# import argv and exists modules
from sys import argv
from os.path import exists

# get variables using argv
script, from_file, to_file = argv

# copy file1 to file2
print "Copying from %s to %s" % (from_file, to_file)

# read data from file
indata = open(from_file).read()

# print out what the length in bytes is
print "The input file is %d bytes long" % len(indata)

# copy file file1 to file2
out_file = open(to_file, 'w')
out_file.write(indata)

# close the files
out_file.close()
