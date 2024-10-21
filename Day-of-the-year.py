def dayOfyear(date):
    year, month, day = map(int, date.split('-'))

    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        return False

    if is_leap(year):
        days_in_month[1] = 29

    day_in_year = sum(days_in_month[:month - 1]) + day

    return day_in_year

date = input("Enter Date (yyyy-mm-dd) : ")
print(dayOfyear(date))
