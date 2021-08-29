import random

# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random() * 5
# print(random_float)
#
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# heads_tails = random.randint(0, 1)
# if heads_tails == 0:
#     print("Tails")
# else:
#     print("Heads")
#
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", ]
#
# states_of_america[1] = "Pencilvania"
# # extend let's you add multiple things to the list instead of append which just does one
# states_of_america.extend(["Angelaland", "Jack Bauer Land"])
#
# print(states_of_america)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# num_names = len(names) - 1
# ran_index = random.randint(0, num_names)
# print(f"{names[ran_index]} is going to buy the meal today!")


# # So this is what I did but I think they want me to use indexing so I'm going to do it again. Yeah can't use choice
# buyer = random.choice(names)
# print(f"{buyer} is going to buy the meal today!")

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
#                "Tomatoes", "Celery", "Potatoes", ]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", ]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes", ]
#
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# I'm going to do this project again later. I was getting a little confused on what was happening for some reason
# After waiting a day and using different variable names, it's much clearer to me now
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

column = int(position[0]) - 1   # 2
row = int(position[1]) - 1      # 3
selected_row = treasure_map[row]
selected_row[column] = "X"

# Okay I'm actually pretty annoyed because I had the right idea at first. I made a variable 'x' and tried to use that.
# apparently the variable is where it messed up my code. This is the way it works:
# treasure_map[row][column] = "X"
# I had:
# x = treasure_map[row][column]
# treasure_map[x] = "X"
# That gives me errors but if I don't use the variable it works. I was so confused why it wasn't working but I had the
# right idea at the time. smh

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
