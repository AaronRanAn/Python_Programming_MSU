# Traversal Through a string with Loop

index = 0

string = 'any string'

while index < len(string):
    letter = string[index]
    index += 1
    print letter


# or you can do:

string = 'any string'

for char in string:
    print char
    
# Counting char 

string = 'any string'

count = 0

for char in string:
    if char == "n":
        count += 1
   # print count: this within loop print gives every value of count
print count

string.count()