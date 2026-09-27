from datetime import datetime

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
    12: 31
}


def is_leap_year(year: int):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def sort_date(input_date: str):
    if len(input_date) > 10:
        date = input_date[:10]
        date = date.split("-")
        date = [int(i) for i in date]
        date.reverse()
    else:
        date = input_date.split("-")
        date = [int(i) for i in date]
    return date


def current_date():
    date = sort_date(str(datetime.now()))
    return date


def date_check(date):
    if date[2] > current_date()[2] or date[2] <= 0:
        return False
    if date[1] > 12 or date[1] <= 0:
        return False
    if date[0] > days_in_month[date[1]] or date[0] <= 0:
        if is_leap_year(date[2]) and date[1] != 29:
            return False
    return True


def days_in_year(date):
    days_since_year = date[0]
    for i in range(1, date[1]):
        days_since_year += days_in_month[i]
    return days_since_year


def main():
    dob = sort_date(input("Please enter your DOB (dd-mm-yyyy): "))
    if date_check(dob) == False:
        print("That is not a valid date!")
        return
    date_today = current_date()
    year_difference = date_today[2] - dob[2]
    if days_in_year(date_today) < days_in_year(dob):
        year_difference -= 1
    print(f"You are {year_difference} years old!")


main()
