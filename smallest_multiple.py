#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_multiples():
    n=20
    m = False
    while m==False:
        n+=2
        for d in range(2, 21):
            if n%d != 0:
                m = False
                break
            else:
                m = True
    return n
print(find_multiples())
