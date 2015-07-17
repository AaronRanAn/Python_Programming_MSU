# Assignment 7.2

# Use words.txt as the file name

import os

os.chdir('/Users/aaron.an/Aaron An/MOOC/MU | Python Programming/Assignments')

fname = raw_input("Enter file name: ")

fh= open(fname)

l = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ll = line.split()
    for i in ll:
        try:
            u = float(i)
            l.append(u)
        except:
            pass
print "Average spam confidence:",sum(l)/len(l)
            