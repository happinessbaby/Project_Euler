# find the 10001th prime number

primes = [2, 3]
def find_prime(N):
    x = 3
    while len(primes) < N:
        x += 2
        prime = True
        for j in range(2, x):
            if x % j == 0:
                prime = False
                break
        if prime == True:
            primes.append(x)
    return primes[N-1]
    
print(find_prime(10001))
