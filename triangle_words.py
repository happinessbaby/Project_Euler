import string


words, num, triang = [], [], []

def triang_words():
    with open('p042_words.txt','r') as file:
        words.append(file.read().replace('"', '').split(','))
    max = find_word_values()
    check(max)
    return len([n for n in num if n in triang])

def find_word_values():
    x = list(string.ascii_uppercase)
    max = 0
    for word in words[0]:
        v=0
        for letter in word:
            v += x.index(letter)+1
        if v>max: max=v
        num.append(v)
    return max

def check(max):
    i,n=1,0
    while n < max:
        n=int(1/2*(i)*(i+1))
        triang.append(n)
        i+=1


print(triang_words())
