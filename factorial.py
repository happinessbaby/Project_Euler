#Find the sum of the digits in the number 100!

product = 1
for i in range(1, 101)[::-1]:
    product *= i

sum = 0
product = str(product)
for i in range(len(product)):
    sum += int(product[i])
print(sum)
