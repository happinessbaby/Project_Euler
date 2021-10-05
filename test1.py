from itertools import combinations

class S:

    def __init__(self):
        self.primes = []

    def digit_replace(self):
        n=100001
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        idx = range(len(str(n))-1) #keep last digit
        combo = []
        for i in range(1, len(str(n))):
            combo.extend(list(combinations(idx, i))) #find all index combinations
        print(combo)


s=S()
print(s.digit_replace())
