#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
#answer: 121313

from itertools import combinations
class S:

    def __init__(self):
        self.primes = []
        self.memo = []

    def digit_replace(self):
        self.find_primes(1000000)
        self.primes = self.primes[8500:] #approximately n/ln(n) primes less than n
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        n=100001
        idx = range(len(str(n))-1) #keep last digit
        combo = []
        for i in range(1, len(str(n))):
            combo.extend(list(combinations(idx, i))) #find all index combinations
        for n in range(100001, 1000000, 2): #last digit odd
            for c in combo:
                s = str(n)
                answer = []
                for d in digits:
                    for i in range(len(c)):
                        s = s[:c[i]]+d+s[c[i]+1:] #digit(s) replacement
                    if s in self.memo:
                        answer.append(s)
                    elif int(s) in self.primes:
                        answer.append(s)
                        self.memo.append(s)
                if len(answer) == 8:
                    return answer
                print(answer)
            print(n)

    def find_primes(self, n):
        m = int((n-1)/2)
        arr = [True]*m
        p, i= 3, 0
        while p**2 < n:
            if arr[i]== False:
                p+=2
                i+=1
            else:
                self.primes.append(p)
                j = int((p**2-3)/2)
                while j < m:
                    arr[j]=False
                    j+=p
                i+=1
                p+=2
        while i<m:
            if arr[i]==True:
                self.primes.append(p)
            i+=1
            p+=2

s=S()
print(s.digit_replace())
