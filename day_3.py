# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# if number % 2 == 0:
#     print(f"The number {number} is even.")
# else:
#     print(f"The number {number} is odd.")

# print("Welcome to the roller coaster!")
# height = int(input("Please enter your height: "))
#
# bill = 0
#
# if height >= 120:
#     print("You can ride the roller coaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age < 18:
#         bill = 7
#         print("Youth tickets are $7")
#     elif 45 <= age <= 55:
#         print("Everything is going to be okay. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ").casefold()
#     if wants_photo == "y":
#         # Add $3 to their bill
#         bill += 3
#
#     print(f"Please pay ${bill}.")
#
# else:
#     print("Sorry, you have to be taller before you can ride.")

# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# bmi = round(weight / height ** 2, 1)
# if bmi < 18.5:
#     print(f"Your bmi is {bmi}. You are underweight.")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}. You have a normal weight.")
# elif bmi < 30:
#     print(f"Your bmi is {bmi}. You are overweight.")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}. You are obese.")
# else:
#     print(f"your bmi is {bmi}. You are clinically obese.")

# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


# I'm going to come back to this because I was struggling but I didn't draw a flow chart so Imma redo
# after waiting a day and coming back I feel much better about this code. I drew the flow chart to help understand

# for year in range(1800, 2021):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(f"{year} is a leap year")
#             else:
#                 print(f"{year} is not a leap year")
#         else:
#             print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ").casefold()
# add_pepperoni = input("Do you want pepperoni? Y or N ").casefold()
# extra_cheese = input("Do you want extra cheese? Y or N ").casefold()
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# if size == "s":
#     bill = 15
#     if add_pepperoni == "y":
#         bill += 2
# elif size == "m":
#     bill = 20
#     if add_pepperoni == "y":
#         bill += 3
# else:
#     bill = 25
#     if add_pepperoni == "y":
#         bill += 3
# if extra_cheese == "y":
#     bill += 1
#
# print(f"Your total is ${bill}")

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# Write your code below this line 👇
# I know there's a better way to do this. I'm pretty sure I could index through in a loop and match against words
# in a list. But, I'm doing this with the knowledge I've learned from this course so far.

# lower_name1 = name1.lower()
# lower_name2 = name2.lower()
#
# true_name = lower_name1.count("t") + lower_name1.count("r") + lower_name1.count("u") + lower_name1.count(
#     "e") + lower_name2.count("t") + lower_name2.count("r") + lower_name2.count("u") + lower_name2.count("e")
#
# love_name = lower_name1.count("l") + lower_name1.count("o") + lower_name1.count("v") + lower_name1.count(
#     "e") + lower_name2.count("l") + lower_name2.count("o") + lower_name2.count("v") + lower_name2.count("e")
#
# true_love = str(true_name) + str(love_name)
# true_love = int(true_love)
#
# if true_love < 10 or true_love > 90:
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif 40 < true_love < 50:
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}")

# Her solution is more concise and I'm making it even more concise
# combined_string = (name1 + name2).lower()
#
# true_name = combined_string.count("t") + combined_string.count("r") + combined_string.count(
#     "u") + combined_string.count("e")
# love_name = combined_string.count("l") + combined_string.count("o") + combined_string.count(
#     "v") + combined_string.count("e")
#
# true_love = int(str(true_name) + str(love_name))
#
# if true_love < 10 or true_love > 90:
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif 40 <= true_love <= 50:
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}")

# I mixed up the instructions on this one.

# lower_name1 = name1.lower()
# true_name1 = lower_name1.count("t") + lower_name1.count("r") + lower_name1.count("u") + lower_name1.count("e")
# love_name1 = lower_name1.count("l") + lower_name1.count("o") + lower_name1.count("v") + lower_name1.count("e")
#
# lower_name2 = name2.lower()
# true_name2 = lower_name2.count("t") + lower_name2.count("r") + lower_name2.count("u") + lower_name2.count("e")
# love_name2 = lower_name2.count("l") + lower_name2.count("o") + lower_name2.count("v") + lower_name2.count("e")
#
# true_love = str(true_name1 + love_name1) + str(true_name2 + love_name2)
# true_love = int(true_love)
#
# if true_love < 10 or true_love > 90:
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif 40 < true_love < 50:
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}")

# true_love = 10 * (true_name1 + love_name1) + true_name2 + love_name2
