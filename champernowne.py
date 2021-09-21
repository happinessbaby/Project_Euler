#An irrational decimal fraction is created by concatenating the positive integers:
#0.123456789101112131415161718192021...
#It can be seen that the 12th digit of the fractional part is 1.
#find d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def find_champ():
    s, digits, i, d='', 1, 1, 0
    while True:
        s+=str(i)
        if len(s) >= 10**d:
            digits*=int(s[10**d-1])
            d+=1
        i+=1
        if d>6: break
    return digits

print(find_champ())
