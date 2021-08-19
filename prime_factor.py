#returns a list of unique prime prime factors

class Prime_Factor():
    def __init__(self):
        self.prime_factors = []

    def prime_factor(self, N):
        for i in range(2, N):
            if N % i == 0:
                if i not in self.prime_factors:
                    self.prime_factors.append(i)
                    self.prime_factor(int(N / i))
                else:
                    self.prime_factor(int(N / i))
        if N not in self.prime_factors:
            self.prime_factors.append(N)
        print(self.prime_factors)
        quit()

if __name__ == '__main__':
    a = Prime_Factor()
    a.prime_factor(1001)
