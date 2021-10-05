import math

def lychrel():
    count = 0
    for n in range(10000):
        x = n
        i = 0
        lychrel = True
        while i < 50:
            reverse = int(str(n)[::-1])
            n+=reverse
            if str(n)[:math.floor(len(str(n))/2)]==str(n)[math.ceil(len(str(n))/2):][::-1]:
                lychrel = False
                break
            i+=1
        if lychrel == True:
            count += 1
    return count

print(lychrel())
