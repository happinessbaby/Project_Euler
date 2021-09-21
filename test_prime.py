primes = [ [3, 3] ] # number, multiple

for x in range(5, 100000, 2) :
    isprime = True;
    for pm in primes :
        while pm[1] < x :
            pm[1] += pm[0]
        if pm[1] == x :
            isprime = False;
            break
    if isprime :
        primes.append([x, x]);

print(len(primes))
