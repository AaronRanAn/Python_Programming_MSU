def computepay(h, r):

    if h <= 40:
    
        p = r * h
        
    else:
    
        p = 40 * r + (h - 40) * r * 1.5

    return p

hrs = raw_input("Enter Hours: ")

h = float(hrs)

rate = raw_input("Enter Rate Per Hour: ")

r = float(rate)

if h <= 40:

    p = h * r
    
else:
        
    p = computepay(h, r)
    
print p