import math
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#1.find odd composite numbers, 2.find every prime number smaller than the odd number 3. substract and divide by 2 4. check if it's a square of a number
def odd():
    n= 3
    while True:
        if any(n%i==0 for i in range(2, n)):
            primes = [j for j in range(3, n) if all(j%i!=0 for i in range(2, j))]
            primes.append(2)
            if any((n-p)%2==0 and math.sqrt(int((n-p)/2))%1==0 for p in primes)==False:
                break
        n+=2
    return n

print(odd())
