#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def self_powers():
    return sum([i**i for i in range(1, 1000)])

print(self_powers())
