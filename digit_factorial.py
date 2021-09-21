#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

import math

id = {}
def make_factorial():
    factorials = [math.factorial(i) for i in range(10)]
    for i in range(len(factorials)):
        id[i] = factorials[i]

make_factorial()

def sum_factorial(N):
    final_sum = 0
    for i in range(3, N):
        digits = list(map(lambda x: int(x), str(i)))
        sum_digits = sum([id[n] for n in digits])
        if i == sum_digits:
            print(sum_digits)
            final_sum += sum_digits
    return final_sum

print(sum_factorial(9999999))
