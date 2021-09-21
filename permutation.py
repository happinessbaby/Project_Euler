import math
string = "0123456789"

def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

def permutation(N):
    s, i, number = string, 9, ''
    while i > 0:
        fac = factorial(i)
        index = int(math.floor((N - 1) / fac))
        x = index
        if (index / i ) > 1:
            x = int(index % i)
        number += s[x]
        s = s.replace(s[x], "")
        N = N - fac * index
        i -= 1
    number += s
    return number

print(permutation(1000000))
