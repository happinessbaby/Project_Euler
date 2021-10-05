
#Which prime, below one-million, can be written as the sum of the most consecutive primes?
S={}
def consec_prime_sum(N):
    n = set(range(2, N))
    primes = set()
    i = 0
    while min(n)**2<N:
        prime = min(n)
        primes.add(prime)
        n = n.difference(set([x for x in n if x%prime==0]))
    primes.update(n)
    primes = sorted(list(primes))
    S = sorted(sum_combo(primes, N).items(), key=lambda x:x[0], reverse=True)
    for k, v in S:
        for x in v:
            if x in primes:
                return x


def sum_combo(s, N):
    i = 2
    S[i]=[sum(s[j:j+i]) for j in range(len(s)-i)]
    while True:
        i+=1
        S.setdefault(i, [])
        for j in range(len(s)-i):
            if (S[i-1][j]+s[i-1+j])>N:
                break
            else:
                S[i].append(S[i-1][j]+s[i-1+j])
        if len(S[i])==0: break
    return S

print(consec_prime_sum(1000000))
