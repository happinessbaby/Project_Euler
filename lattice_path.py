#How many such routes are there through a 20×20 grid?
from math import factorial

#method 1: recursion
path = {}
def find_path(m, n, path):
    if (m, n) in path:
        return path[(m, n)]
    if m == 0 or n == 0:
        return 1
    else:
        path[(m, n)] = find_path(m-1, n, path) + find_path(m, n-1, path)
        return path[(m, n)]

#Method 2: 2n!/(n!n!)
def find_Catalan(n):
    return int(factorial(2*n)/(factorial(n)*factorial(n)))

print(find_path(20, 20, path))
#print(find_Catalan(20))
