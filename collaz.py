#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Which starting number, under one million, produces the longest chain?

chain_length = {}

def find_collaz(N,  chain_length):
    n = 1
    while n < N:
        chain_length[n] = find_length(n)
        n += 1
    sorted_chain = sorted(chain_length.items(), key = lambda x: x[1], reverse = True)
    return sorted_chain[0][0]


def find_length(n):
    length = 0
    N = n
    while n >= 1:
        if n == 1:
            return (length + 1)
        elif n in chain_length:
            print(f"{N} : {n}")
            return (length + chain_length[n])
        else:
            if n % 2 == 0:
                n = int(n / 2)
                length += 1
            else:
                n = int(3 * n + 1)
                length += 1

print(find_collaz(100, chain_length))
