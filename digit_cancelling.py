from fractions import Fraction
import functools

def digit_cancelling2():
    fraction = []
    for n in range(1, 10):
        for d in range(1, 10):1 i
            if 9*n*d % (10*d - n) == 0 and d!=n and len(str(int(9*n*d/(10*d-n)))) == 1:
                fraction.append(Fraction(d, n))
    return functools.reduce(lambda x, y: x*y, fraction)

print(digit_cancelling2())
