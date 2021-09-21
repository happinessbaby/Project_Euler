#What is the sum of the digits of the number 21000?


def power_sum():
    product = 1
    for i in range(1, 1001):
        product *= 2
    return product

def add_digits():
    string = str(power_sum())
    digits = [int(char) for char in string]
    return sum(digits)

print(add_digits())
