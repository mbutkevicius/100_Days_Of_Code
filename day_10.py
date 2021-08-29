# def my_function():
#     return 3 * 2
#
#
# output = my_function()
# print(output)

def format_name(f_name, l_name):
    """Take first and lsat name and format it to return the title
     case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"Result: {formatted_f_name} {formatted_l_name}"
    # print(f"{formatted_f_name} {formatted_l_name}")


# formatted_string = format_name("MiChAeL", "BUTKEVICIUS")
# print(formatted_string)
print(format_name("MiChAeL", "BUTKEVICIUS"))
# print(format_name(input("What is your first name? "),
#                   input("What is your last name? ")))


def is_leap(year_to_check):
    """Checks whether the given year is a leap year."""
    if year_to_check % 4 == 0:
        if year_to_check % 100 == 0:
            if year_to_check % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# def days_in_month(year_to_check, month_to_check):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if not is_leap(year_to_check):
#         return month_days[month_to_check - 1]
#     elif is_leap(year_to_check):
#         if month_days[month_to_check - 1] == 28:
#             return 29
#         else:
#             return month_days[month_to_check - 1]

# I guess they both work the same. I thought this way might consolidate it better but guess not.
# Jk after looking at it again I can erase those unnecessary else statements


def days_in_month(year_to_check, month_to_check):
    """Tells how many days are in a month."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_to_check):
        if month_days[month_to_check - 1] == 28:
            return 29
        # else:
        #     return month_days[month_to_check - 1]
    # else:
    return month_days[month_to_check - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
