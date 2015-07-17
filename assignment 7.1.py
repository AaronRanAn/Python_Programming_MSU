# Assignment 7.1

# Use words.txt as the file name

import os

os.chdir('/Users/aaron.an/Aaron An/MOOC/MU | Python Programming/Assignments')

fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.strip()

    print line.upper()