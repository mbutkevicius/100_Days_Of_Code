MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# So unfortunately I had modify one part of the data given to make my code work. I definitely didn't need to but I
# couldn't figure it out without doing it. I had to add a value of 0 to milk in espresso.
# I'm going to watch solution and see how she does it. Everything else seems good though.


# def check_ingredients(chosen_drink, machine_resources):
#     if machine_resources["water"] >= chosen_drink["water"]:
#         if machine_resources["milk"] >= chosen_drink["milk"]:
#             if machine_resources["coffee"] >= chosen_drink["coffee"]:
#                 return True
#             print("Sorry, there is not enough coffee for this drink")
#         else:
#             print("Sorry, there is not enough milk for this drink")
#     else:
#         print("Sorry, there's not enough water for this drink.")


def check_ingredients(chosen_drink, machine_resources):
    if machine_resources["water"] >= chosen_drink["water"]:
        resources["water"] = machine_resources["water"] - chosen_drink["water"]
        if machine_resources["milk"] >= chosen_drink["milk"]:
            resources["milk"] = machine_resources["milk"] - chosen_drink["milk"]
            if machine_resources["coffee"] >= chosen_drink["coffee"]:
                resources["coffee"] = machine_resources["coffee"] - chosen_drink["coffee"]
                return True
            print("Sorry, there is not enough coffee for this drink")
        else:
            print("Sorry, there is not enough milk for this drink")
    else:
        print("Sorry, there is not enough water for this drink.")


# def check_ingredients(chosen_drink, machine_resources):
#     for resource in machine_resources, chosen_drink:
#         if machine_resources[resource] >= chosen_drink[resource]:
#             resources[resource] = machine_resources[resource] - chosen_drink[resource]
#             return True
#         print(f"Sorry, there's not enough {resource} for this drink.")


def calculate(quarters, dimes, nickels, pennies, cost):
    money = quarters + dimes + nickels + pennies
    change = round(money - cost)
    if money > cost:
        print(f"Here is ${change} in change.")
        return True
    elif money == cost:
        print("Thank you for your payment!")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")


while True:
    drink = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        break
    elif drink == "report":
        for ingredient in resources:
            print(ingredient, resources[ingredient], sep=": ")
        drink = input("  What would you like? (espresso/latte/cappuccino): ").lower()

    num_quarters = int(input("How many quarters?: ")) * 0.25
    num_dimes = int(input("How many dimes?: ")) * 0.1
    num_nickels = int(input("How many nickels?: ")) * 0.05
    num_pennies = int(input("How many pennies?: ")) * 0.01

    drink_price = MENU[drink]["cost"]
    drink_ingredients = MENU[drink]["ingredients"]

    can_make = check_ingredients(chosen_drink=drink_ingredients, machine_resources=resources)
    if can_make:
        will_work = calculate(num_quarters, num_dimes, num_nickels, num_pennies, drink_price)
        if will_work:
            print(f"Here is your {drink}. Enjoy!")


# def check_ingredients(chosen_drink, machine_resources):
#     if machine_resources["water"] >= chosen_drink["water"]:
#         if machine_resources["milk"] >= chosen_drink["milk"]:
#             if machine_resources["coffee"] >= chosen_drink["coffee"]:
#                 return True
#     return "Sorry, there's not enough ingredients for this drink."
#
#
# def calculate(quarters, dimes, nickels, pennies, cost):
#     money = quarters + dimes + nickels + pennies
#     change = round(money - cost)
#     if money > cost:
#         print(f"Here is ${change} in change.")
#         return True
#     elif money == cost:
#         print("Thank you for your payment!")
#         return True
#     else:
#         return " Sorry, that's not enough money. Money refunded."
#
#
# will_work = False
# while True:
#     drink = input("  What would you like? (espresso/latte/cappuccino): ").lower()
#
#     num_quarters = int(input("How many quarters?: ")) * 0.25
#     num_dimes = int(input("How many dimes?: ")) * 0.1
#     num_nickels = int(input("How many nickels?: ")) * 0.05
#     num_pennies = int(input("How many pennies?: ")) * 0.01
#
#     drink_price = MENU[drink]["cost"]
#     drink_ingredients = MENU[drink]["ingredients"]
#
#     will_work = check_ingredients(drink_ingredients, resources)
#     if will_work:
#         will_work = calculate(num_quarters, num_dimes, num_nickels, num_pennies, drink_price)
#         if will_work:
#             print(f"Here is your {drink}. Enjoy!")
