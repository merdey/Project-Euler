'''
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def is_leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

def get_days_in_month(month, year):
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    d = days_in_month[month]
    if month == 2 and is_leap_year(year):
        d += 1
    return d

sundays = 0
num_days = 1
month, year = 1, 1900

while year <= 2000:
    while month <= 12:
        num_days += get_days_in_month(month, year)
        if num_days % 7 == 0 and year in range(1901, 2001):
            sundays += 1
        month += 1
    year += 1
    month = 1

print sundays