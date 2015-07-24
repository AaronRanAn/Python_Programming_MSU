# assignment 9.4

import os

os.chdir('/Users/aaron.an/Aaron An/MOOC/MU | Python Programming/Assignments')

# fname = raw_input("Enter file name: ")

fh = open('mbox-short.txt')

counts = dict()

for line in fh:
    if line.startswith("From "):
        ll = line.split()
        emaddress = ll[1]
        counts[emaddress] = counts.get(emaddress, 0) + 1
        
max_key = max(counts, key=lambda x: x[1])

max_value = max(counts.values())

print max_key, max_value

# Or you can do the following:

bigcount = None
bigword = None
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count

print bigword, bigcount