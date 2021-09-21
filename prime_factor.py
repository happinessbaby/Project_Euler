#returns a list of unique prime prime factors

class Prime_Factor():
    def __init__(self):
        self.prime_factors = set()

    def prime_factor(self, N):
        for i in range(2, N):
            while N % i == 0:
                if i not in self.prime_factors:
                    self.prime_factors.add(i)
                N = N / i
        if len(self.prime_factors) == 0:
            return None
        return self.prime_factors


if __name__ == '__main__':
    a = Prime_Factor()
    print(a.prime_factor(413))
