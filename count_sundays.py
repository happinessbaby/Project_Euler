#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#1 Jan 1900 was a Monday.

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug','sep','oct', 'nov', 'dec']

def make_calendar(year):
    calendar = {}
    for i in months:
        if i == "feb" and year != "leap":
            calendar[i] = 28
        elif i == "feb" and year == "leap":
            calendar[i] = 29
        elif i == "apr" or i == 'jun' or i == 'sep' or i == 'nov':
            calendar[i] = 30
        else:
            calendar[i] = 31
    return calendar

def count_sundays():
    countS = 0
    sunday = 7 #initialize the first sunday as 7th of Jan, 1901
    for years in range(1, 100):
        if (years+1900 != 2000) or ((years+1900) % 4 != 0):
            calendar = make_calendar("normal") #go create a calender of normal years
        else:
            calendar = make_calendar("leap") #go create a calendar of leap years
        for month in months:
            while sunday <= calendar[month]:
                sunday += 7
            sunday = sunday - calendar[month]
            if sunday == 1:
                countS += 1
        print(sunday)
    return countS

print(count_sundays())
