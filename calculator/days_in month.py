# Understanding function with output
# code for checking leap year
def is_leap(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# If leap year has 29 days in feb if not days is same as the list
def days_in_month(a_year, a_month):
    """ returns days of the month user input"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # We can use two return statement in this fun acc to course
    # but this is my method
    if is_leap(a_year):
        month_days[1] += 1
    return month_days[a_month - 1]


year = int(input("Enter year: "))
month = int(input("Enter month in number: "))
days = days_in_month(year, month)
month_dict = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "April",
    5: "may",
    6: "june",
    7: "july",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec"
}

print(f"The number of days in month {month_dict[month]} is {days}")
