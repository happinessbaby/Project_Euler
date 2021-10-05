#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#What 12-digit number do you form by concatenating the three terms in this sequence?

from itertools import permutations

def prime_perm():
    three_seq = []
    for n in range(1000, 10000):
        if all(n%i!=0 for i in range(2, n)):
            perm = set([int(''.join(x)) for x in list(permutations(str(n)))])
            primes=sorted([p for p in perm if all(p%i!=0 for i in range(2, n))])
            diff = [primes[i]-primes[i-1] for i in range(1, len(primes))]
            if 3330 in diff:
                three_seq.append(primes)
    return three_seq

print(prime_perm())
