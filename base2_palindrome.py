#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def find_palindromes(N):
    sum = 0
    for n in range(1, N):
        if check_palind(n):
            sum += n
    return sum

def check_palind(n):
    x = str(n)
    b = bin(n)[2:]
    if x == x[::-1] and b == b[::-1] and x[-1] != '0' and x[0] != '0' and b[-1] != '0' and b[0] != 0:
        return True
    return False

print(find_palindromes(1000000))
