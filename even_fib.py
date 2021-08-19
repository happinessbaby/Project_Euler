#sums the even fibonacci numbers that smaller than 4 million

def find_fib(fib):
    fib[0] = 1
    fib[1] = 1
    n = 2
    while fib[n-1] < 4000000:
        fib[n] = fib[n-1] + fib[n-2]
        n += 1

def sum_even(fib):
    sum = 0
    for key, value in fib.items():
        if value % 2 == 0 and value < 4000000:
            sum += value
    return sum

find_fib(fib)
print(sum_even(fib))
