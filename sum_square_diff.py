#Find the difference between the sum of the squares of the
#first one hundred natural numbers and the square of the sum.

def sum_of_square():
    sum1 = 0
    for i in range(1, 101):
        sum1 += i ** 2
    return sum1


def square_of_sum():
    sum2 = len(range(100)) / 2 * (1 + len(range(100)))
    return sum2 ** 2

print(int(square_of_sum() - sum_of_square()))
