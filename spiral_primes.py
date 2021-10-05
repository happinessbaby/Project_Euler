#what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
import math


primes = []
def spiral_primes():
    side_length = 1
    n=1
    i = 1
    while True:
        spiral_num = side_length*4+4
        primes.extend([check_prime(n+int(spiral_num/4)*i) for i in range(1, 5) if check_prime(n+int(spiral_num/4)*i)!=None])
        side_length += 2
        n+=spiral_num
        i+=4
        if len(primes)/i<0.1:
            return side_length

def check_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return
    return n

print(spiral_primes())
