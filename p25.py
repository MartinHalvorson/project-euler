# Finds the first term in the fibonacci sequence to contain 1000 digits

import math

a = 1
b = 1
index = 2

while math.log(b, 10) + 1 < 1000:
    b += a
    a = b - a
    index += 1

print(index)