# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# # This seems legit to me but I'm going to watch her solution. This felt too easy. I did it in less than 2 minutes.
# # This is exactly what she did. Just an easy challenge.
# total_height = 0
# num_students = 0
# for height in student_heights:
#     total_height += height
#     num_students += 1
# print(round(total_height / num_students))

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student heights ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is: {highest_score}.")

# # 3rd value us the step value
# for number in range(1, 11, 2):
#     print(number)
#
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# total_even = 0
# for number in range(2, 101, 2):
#     total_even += number
# print(total_even)
#
# # Or:
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         number = "fizz buzz"
#     elif number % 5 == 0:
#         number = "buzz"
#     elif number % 3 == 0:
#         number = "fizz"
#     print(number)
