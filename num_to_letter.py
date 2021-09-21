#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
#contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven','twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['onehundredand', 'twohundredand', 'threehundredand', 'fourhundredand', 'fivehundredand', 'sixhundredand',
'sevenhundredand', 'eighthundredand', 'ninehundredand']

onesL = {}
teensL = {}
tensL = {}
def count():
    length = 0
    for i in ones:
        length += len(i)
        onesL[i] = len(i)
    for i in teens:
        length += len(i)
        teensL[i] = len(i)
    for i in tens:
        length += len(i)
        tensL[i] = len(i)
        for j in ones:
            length += len(i) + onesL[j]
    for i in hundreds:
        length += len(i)-3
        for j in ones:
            length += len(i) + onesL[j]
        for j in teens:
            length += len(i) + teensL[j]
        for j in tens:
            length += len(i) + tensL[j]
            for k in ones:
                length += len(i) + tensL[j] + onesL[k]
    length += len("onethousand")
    return length

print(count())
