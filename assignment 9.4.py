# assignment 9.4

import os

os.chdir('/Users/aaron.an/Aaron An/MOOC/MU | Python Programming/Assignments')

fname = raw_input("Enter file name: ")

fh = open(fname)

count = 0

for line in fh:
    if line.startswith("From "):
        ll = line.split()
        emaddress = ll[1]
        count +=1
        print emaddress
         
print "There were", count, "lines in the file with From as the first word"