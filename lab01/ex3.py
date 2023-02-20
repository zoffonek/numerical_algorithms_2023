# Kumulowanie się błędów

import numpy as np
 
def computeOne(iter):
    sum = 0
    addend = np.float32(1/iter)
    for i in range(0, iter):
        sum+= addend
    return sum
 
print(computeOne(1024) - 1)     # 0.0
print(computeOne(1000) - 1)     # 4.7497451305389404e-08

print(abs((computeOne(1000)-1)/1000), "%") # relative error

def absoluteError(iter, approx):
    return abs((computeOne(iter)-approx)/iter)

def relativeError(iter, approx):
    return abs(computeOne(iter)-approx)