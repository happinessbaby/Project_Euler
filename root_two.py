from fractions import Fraction
import sys
sys.setrecursionlimit(1500)

memo={}
count=[]
def root_two(x):
    if x ==0:
        return 0
    if x ==1:
        return Fraction(1, 2)
    memo[x] = Fraction(1, 1) / (Fraction(2,1)+root_two(x-1))
    n = Fraction(1, 1)+memo[x]
    if len(str(n.denominator)) < len(str(n.numerator)):
        count.append(1)
        print(len(count))
    return memo[x]

print(root_two(1000))
