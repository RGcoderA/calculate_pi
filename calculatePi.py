import random
import math
import time

inside = 0
outside = 0
iterations = 1000000


random.seed(int(round(time.time()*1000)))
for i in range(0,iterations):
    # select two random numbers between 0 and 1
    x = random.uniform(0,1)
    y = random.uniform(0,1)

    # calculate distance from origin
    # I calculated the distance my math import square root of x time x plus y times y to get the distance.

    distance = math.sqrt(x*x + y*y)

    if distance < 1:
        inside += 1
    else:
        outside += 1



# calculate the value of Pi
pi = 4 * inside/(inside+outside)
# 4 times inside divide by inside plus outside will result in pi

# print result
print(pi)

