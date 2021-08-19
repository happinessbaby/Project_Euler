#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


String = str(998001)
factors = []

def palindrom():
    i = 1
    while i < 100:
        half = int(String[slice(3)])
        half = half - i
        whole = int(str(half) + str(half)[::-1])
        if (factor(whole)):
            print(whole)
            print(factors)
            break
        else:
            i += 1

def factor(N):
    i = 999
    while i > 900:
        if N % i == 0 and N / i < 1000:
            factors.append(i)
            factors.append(int(N / i))
            return True
        else:
            i -= 1
    return False

palindrom()
