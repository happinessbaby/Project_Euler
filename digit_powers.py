#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def digit_powers(N):
    powers = set()
    for i in range(1, N):
        n = str(i)
        fif = [int(d) ** 5 for d in n]
        s = sum(fif)
        if s == i:
            powers.add(s)
    return sum(powers) - 1

print(digit_powers(999999))
