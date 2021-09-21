#find the 11 truncated primes

trunc = []
def find_truncs():
    i = 11
    n = 0
    while n < 11:
        check=0
        for j in range(len(str(i))):
            check += is_prime(str(i)[j:])
        for j in range(1, len(str(i))):
            check += is_prime(str(i)[:-j])
        if check == 0:
            trunc.append(i)
            n+=1
        i+=2
    return trunc

def is_prime(n):
    n = int(n)
    if n==1: return 1
    if n==2: return 0
    for i in range(2, n):
        if n % i == 0:
            return 1
    return 0

print(find_truncs())
