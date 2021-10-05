from collections import Counter

def permute_multip():
    n = 1000
    while True:
        M = [str(2*n), str(3*n), str(4*n), str(5*n), str(6*n)]
        if all([Counter(str(n))==Counter(m) for m in M]):
            print(M)
            return n
        n+=1

print(permute_multip())
