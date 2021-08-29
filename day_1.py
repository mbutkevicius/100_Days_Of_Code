print("Hello world!\n\tHello world!")
print("Hello" + ' ' + "Michael")
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# print("Hello " + input("What's your name?\n") + "!")
#
# print(len(input("What's your name?\n")))

name = input("What is your name?\n")
print("How are you today", name + "?")

# I don't know why but this confused me for awhile. Maybe because it's late
# and I've been coding all day
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

c = a
a = b
b = c

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# I like this way more but we haven't learned .format yet
print("Welcome to band name generator!")
hometown = input("What is the name of the city you grew up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name is: {} {}".format(hometown, pet))

print("Welcome to band name generator!")
hometown = input("What is the name of the city you grew up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name is " + hometown + ' ' + pet + "!")
