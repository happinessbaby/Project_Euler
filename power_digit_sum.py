from functools import reduce


def digit_sum():
    n = 0
    for i in range(1, 100):
        for j in range(1, 100):
            S = reduce(lambda x, y: int(x)+int(y), str(i ** j))
            if int(S) > n:
                n = int(S)
    return n

print(digit_sum())
