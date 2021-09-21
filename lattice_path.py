#How many such routes are there through a 20×20 grid?
from math import factorial

path = {}
#inefficient
def find_path(m, n, path):
    index = "m" + "x" + "n"
    if "20x20" in path:
        return path['20x20']
    if m == 0 or n == 0:
        return 1
    else:
        path[index] = find_path(m-1, n, path) + find_path(m, n-1, path)
        return path[index]

#print(find_path(20, 20, path))
#using formula 2n!/(n!n!)
def find_Catalan(n):
    return int(factorial(2*n)/(factorial(n)*factorial(n)))


print(find_Catalan(20))
