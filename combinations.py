from itertools import combinations
import math

#How many, not necessarily distinct combinatoric values of for 1<=n<=100 are greater than one-million?
#n!/(r!)(n-r)!

def combo():
    count = 0
    for n in range(23, 101):
        for r in range(3, n):
            if math.factorial(n)/(math.factorial(r)*math.factorial(n-r))>1000000:
                count +=1
    return count

print(combo())
