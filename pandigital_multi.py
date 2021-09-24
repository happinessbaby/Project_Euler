#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def find_pand():
    n = 0
    digits =  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(1000, 10000):
        test =  str(i*1)+str(i*2)
        if set(test).difference(digits)==set() and len(set(test))==len(test):
            if int(test) > n: n=int(test)
    return n

print(find_pand())
