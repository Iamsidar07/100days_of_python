# Functions with outputs


def format_name(f_name, l_name):
    """
    Takes first and last name and returns title case of name.
    """
    if f_name == "" or l_name == "":
        return "You did not provide any values."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


name = format_name("mAnoj", "kUmaR")
print(name)


def is_leap(year):
    """
    Checks for year is leap year or not and return a boolean value
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(year, month):
    # docstring
    """
    Takes a year and month number and return number of days in month
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # check for leap year
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)
