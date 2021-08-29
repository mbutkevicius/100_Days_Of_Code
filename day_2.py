# Data Types

# String

print("Hello"[4])

print("123" + "345")

# Integer

print(123 + 345)

# 123_456_789     # _ works as ,

# Float

# 3.14159

# Boolean

# True
# False

# num_char = str(len(input("What is your name?\n")))
# print("Your name has " + num_char + " characters.")

a = str(123)
print(type(a))

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit)

print()

print(3 + 5)
print(7 - 4)
print(3 * 2)
print(type(6 / 3))
print(4 ** 4)
print(3 * (3 + 3 / 3 - 3))

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# float_height = float(height)
# float_weight = float(weight)
# bmi = int(float_weight / (float_height ** 2))
# print(bmi)

# I like this way more:

bmi = float(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

# The comma after 3 tells how many digits to round to after decimal
print(round(8 / 3, 2))

# Makes an int
print(8 // 3)

# f-strings
score = 0
height = 1.8
is_winning = True
print(f"your score is {score}, your height is {height}, you are winning "
      f"is {is_winning}")

# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# w = 365 * 90
# x = 52 * 90
# y = 12 * 90
# z = 90
#
# days_left = w - int(age) * 365
# weeks_left = x - int(age) * 52
# months_left = y - int(age) * 12
# years_left = z - int(age)
#
# message = f"You have {days_left} days, {weeks_left} weeks, {months_left} months, and {years_left} years left"
# print(message)

# Shorter way:
years_left = 90 - int(age)

days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, {months_left} months, and {years_left} years left"
print(message)
