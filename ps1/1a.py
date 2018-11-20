__author__ = 'Aman Kumar Das'

# program to compute 1000 th prime number

count = 1                       # 2 is first prime number
i = 3
while count != 1000:            # we are interested in counting till 1000
    for k in range(2,int (i/2)+1):     # dividing from all the number till we reach num/2
        if i%k == 0:                # not a prime
            break
    else:                           #    IS PRIME
        print(i)
        count += 1
    i += 2                           # iterating for odd number only

