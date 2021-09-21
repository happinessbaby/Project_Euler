#0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
#It can be seen that 1/7 has a 6-digit recurring cycle.
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

d = 2
length = {}
while d < 1000:
    x = set()
    remainder = 1
    while remainder not in x:
        x.add(remainder)
        remainder *= 10
        remainder = remainder % d
    length[d] = len(x)
    d += 1
n= 0
for key, value in length.items():
    if value > n:
        n = value
        N = key
print(N)
