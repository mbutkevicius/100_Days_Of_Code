# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# print(programming_dictionary["Bug"])
#
# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)
#
# empty_dictionary = {}
#
# # # Wipe existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)
#
# # Edit item
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary["Bug"])
#
# # Loop through a dictionary prints keys
# for key in programming_dictionary:
#     print(key, programming_dictionary[key], sep=": ")
#     print(programming_dictionary[key])
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_grades[key] = "Exceeds expectations"
#     elif student_scores[key] > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

# Nesting list in dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon",],    # must turn this into list. Otherwise, 1 value per key
#     "Germany": ["Berlin", "Hamburg", "Stuttgart",],
# }

# Nesting dictionary in dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# # Nesting dictionary in list
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# ]

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country, times_visited, cities):
    new_country = {}
    new_country["country"] = country
    new_country["times_visited"] = times_visited
    new_country["cities"] = cities
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
