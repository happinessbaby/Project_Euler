#How many circular primes are there below one million?


def find_primes(N):
    m = int((N-1)/2) # sieving thru odd numbers
    arr=[True]*m
    i = 0
    p = 3
    primes=set()
    while p**2 < N:
        if arr[i]== False: #takes care of 15 when i == 5 (taken out by 3 already)
            i+=1
            p+=2
        elif arr[i]== True:
            primes.add(p)
            j = int((p**2-3)/2)
            while j < m:
                arr[j] = False
                j += p
            i+=1
            p+=2
    while i<m: #takes care of leftover primes not seived
        if arr[i] == True:
            primes.add(p)
        i+=1
        p+=2
    primes.add(2)
    return primes

def check_circular(N):
    n = find_primes(N)
    count = 0
    for num in n:
        primes = set([int(str(num)[i:] + str(num)[:i]) for i in range(len(str(num)))])
        if primes<n:
            count+=1
    return count


print(check_circular(1000000))
