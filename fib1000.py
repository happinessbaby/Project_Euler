fib = {}
def find_fib():
    fib[0] = 1
    fib[1] = 1
    n = 2
    fib_length = 0
    while fib_length < 1000:
        fib[n] = fib[n-1] + fib[n-2]
        fib_length = len(str(fib[n]))
        n += 1
    return n

print(find_fib())
