#summation of all primes below 2 million
import time


def calc_time(func):
    def inner(*args, **kwargs):
        begin = time.time()
        returned_val = func(*args, **kwargs)
        end = time.time()
        print("time: ", end-begin)
        return returned_val
    return inner

@calc_time
def sum_primes(N):
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
            print(p)
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
    return sum(primes)+2


print(sum_primes(2000000))
