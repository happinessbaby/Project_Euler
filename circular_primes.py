#How many circular primes are there below one million?


cir_primes = set([2])
def find_circular_primes(N):
    num = 3
    while num < N:
        if any(int(i)%2==0 or i == 5 for i in str(num))==False or num not in cir_primes:
            primes = [int(str(num)[i:] + str(num)[:i]) for i in range(len(str(num)))]
            check_primes(primes)
        num += 2
    return len(cir_primes)

def check_primes(primes):
    for p in primes:
        for d in range(2, p):
            if p % d == 0:
                return
    cir_primes.update(primes)

print(find_circular_primes(10000))
