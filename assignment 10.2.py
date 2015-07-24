# assignment 10.2

# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 
# Note that the autograder does not have support for the sorted() function.

fh = open('mbox-short.txt')

counts = dict()

for line in fh:
    if line.startswith("From "):
        ll = line.split()
        hour = ll[5][0:2]
        counts[hour] = counts.get(hour, 0) + 1

# print sorted ([(k,v) for k,v in counts.items()])

lst=counts.keys()
lst.sort()
    
for key in lst:
    print key, counts[key]