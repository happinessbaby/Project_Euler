
memo = {}
def find_primes(): #works
    primes = [2]
    prime = True
    for n in range(3, 1000, 2):
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime == True:
            primes.append(n)
        prime = True
    return primes

def prime_factor(N): #works
    prime_factors = set()
    for i in range(2, N):
        while N % i == 0:
            if i not in prime_factors:
                prime_factors.add(i)
            N = N / i
    if len(prime_factors) == 0:
        return "prime"
    return "not prime"

def find_quadratic_primes():
    primes = find_primes()
    primes.append(1)
    for i in primes:
        for j in primes:
            a, b = i, j
            x, count, num = 1, 0, 'prime'
            while num == 'prime':
                num = x * x + a * x + b
                if num > 0:
                    check = prime_factor(num)
                    if check == "prime":
                        num = 'prime'
                        count += 1
                        x += 1
                    else:
                        num = 'not prime'
                        break
                else:
                    break
            memo[str(a)+','+str(b)] = count
    return memo

def find_prime_length():
    memo = find_quadratic_primes()
    n = 0
    for key, value in memo.items():
        if value > n:
            n = value
            d = key
    return d

print(find_prime_length())
