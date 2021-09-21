
def sum_primes(N):
    sum = 0
    for num in range(N):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime == True:
            sum += num
    return sum

print(sum_primes(2000000))
