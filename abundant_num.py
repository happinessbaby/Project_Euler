#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def make_abundant():
    abundant = set()
    for i in range(1, 28124):
        sum_divisors = 0
        for j in range(1, i):
          if i % j == 0:
              sum_divisors += j
        if sum_divisors > i:
            abundant.add(i)
    return abundant

def sum_nonabundant():
    abundant = make_abundant()
    P = set(range(1, 28124))
    A = set()
    sum = 0
    for i in abundant:
        for j in abundant:
            if i + j < 28124:
                A.add(i + j)
    nonabundant = P.difference(A)
    for i in nonabundant:
        sum += i
    return sum

print(sum_nonabundant())
