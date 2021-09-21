import math

#a+b+c=n; a^2+b^2=c^2
memo = {}
def find_sides(p):
    n = 0
    while n < p:
        count = 0
        n+=1
        for a in range(1, int(n/2)):
            for b in range(a, int(n/2)):
                if a+b+math.sqrt(a**2+b**2) == n:
                    count+=1
        memo[n]=count
    return max(memo.items(), key=lambda x:x[1])

print(find_sides(1000))
