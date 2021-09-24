from itertools import permutations
#Find the sum of all 0 to 9 pandigital numbers whose substrings are divisible by
#2, 3, 5, 7, 11, 13, 17, e.g.:1406357289


def divide_substring():
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    tgp = list(permutations(digits, 3))
    p=[]
    for i in range(len(tgp)):
        x = ''.join(tgp[i])
        if int(x)%17==0:
            p.append(x)
    return sum([int(i+s) for s in substring(p, digits) for i in digits if i not in s])

def substring(p, digits):
    primes = [2, 3, 5, 7, 11, 13]
    while len(primes)>0:
        new = []
        for j in range(len(p)):
            new.extend([i+p[j] for i in digits if i not in p[j] and int(str(i+p[j])[:3])%primes[-1]==0])
        p = new
        primes.pop()
    return new

print(divide_substring())
