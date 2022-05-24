# number day in a month 1 to 12
daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


def numberDayOverFebOfLeepYear(y1, m1, d1, y2, m2, d2):
    day_over_feb = 0
    if y1 == y2 and isLeapYear(y1):
        if m1 > 2:
            return 0
        elif m1 <= 2 and m2 > 2:
            return 1
        else:
            return 0
    else:
        if m1 <= 2 and isLeapYear(y1):
            day_over_feb += 1
        if m2 > 2 and isLeapYear(y2):
            day_over_feb += 1
        return day_over_feb


def daysBetweenDates(y1, m1, d1, y2, m2, d2):

    # fix bug first input date > second input date
    if dateIsBefore(y1, m1, d1, y2, m2, d2) == False:
        return 0

    day = 0
    # number day from d1 m1 to end month m1
    day_m1 = 0
    # number day from start month m2 to end month m2
    day_m2 = 0

    if(y1 == y2):
        if(m1 == m2):
            return d2 - d1
        else:
            for i in range(m1+1, m2):
                day += daysOfMonths[i-1]
            day += daysOfMonths[m1 - 1] - d1 + d2 + \
                numberDayOverFebOfLeepYear(y1, m1, d1, y2, m2, d2)
        return day

    day_m1 = daysOfMonths[m1-1] - d1
    day_m2 = d2

    # #number month from month m1 to end month of year
    # month_m1 = 12 - m1 - 1
    # #number month from start month to month m2
    # month_m2 = m2

    for i in range(m1+1, 13):
        day_m1 += daysOfMonths[i-1]

    for i in range(1, m2):
        day_m2 += daysOfMonths[i-1]

    day_of_year_live = 0

    # # fix bug If born year and current year can be leap year
    # if isLeapYear(y1):
    #     day_m1 += 1

    # y1 + 1 -> start new year , day of old year is day_m1
    # y2 + 1 -> include y2 , day of y2 is day_m2
    for i in range(y1+1, y2+1 - 1):
        if isLeapYear(i):
            day_of_year_live += 366
        else:
            day_of_year_live += 365
    return day_m1 + day_of_year_live + day_m2 + numberDayOverFebOfLeepYear(y1, m1, d1, y2, m2, d2)


#print(daysBetweenDates(1999, 9, 30, 2022, 5, 23))


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if(year1 < year2):
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()
