#What is the largest n-digit pandigital prime that exists?


def pan_prime():
    n = 1000000
    max_pan = 0
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while len(str(n))<8:
        if len(set(str(n)))==len(str(n)) and set(str(n)).difference(digits[:len(str(n))])==set():
            for i in range(2, n):
                if n%i==0:
                    prime = False
                    break
                else:
                    prime = True
        else:
            prime=False
        if n>max_pan and prime==True: max_pan=n
        n+=3
    return max_pan

def check_pan():
    primes = find_primes(100000000)
    digits = set(['1', '2', '3', '4', '5','6', '7'])
    for p in primes[::-1]:
        if set(str(p))==digits and len(set(str(p)))==len(str(p)):
            return p


def find_primes(n):
    m = int((n-1)/2)
    arr = [True]*m
    p, i= 3, 0
    primes = []
    while p**2 < n:
        if arr[i]== False:
            p+=2
            i+=1
        else:
            primes.append(p)
            j = int((p**2-3)/2)
            while j < m:
                arr[j]=False
                j+=p
            i+=1
            p+=2
    while i<m:
        if arr[i]==True:
            primes.append(p)
        i+=1
        p+=2
    return primes

print(check_pan())
