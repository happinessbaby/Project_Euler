#What is the value of the first triangle number to have over five hundred divisors?


def triangle_num():
    n = 1
    divisors_num = 0
    while divisors_num <= 500:
        tri = find_tri(n)
        divisors_num = find_divisors(tri)
        n += 1
    return tri

def find_tri(n):
    if n % 2 == 0:
        tri = (n + 1) * n / 2
        return int(tri)
    else:
        tri = n * (n - 1) / 2 + n
        return int(tri)

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and n / i not in divisors:
            divisors.append(i)
            divisors.append(n / i)
        elif n % i == 0 and n / i in divisors:
            break
    return len(divisors)

print(triangle_num())
