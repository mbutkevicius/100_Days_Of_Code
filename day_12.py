# Modifying Global Scope
# The two variables are actually two different variables despite same name
# Must use global key word to modify it from function
enemies = 1

def increase_enemies():
    # global enemies
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope - exists within functions


def drink_potion():
    potion_strength = 2
    # print(potion_strength)
    print(player_health)

# drink_potion()
# That's why this gives error
# print(potion_strength)

# Global Scope - not within function. Available inside and outside functions
player_health = 10
drink_potion()

# No block scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

# So this actually gives an error but the code works alright
print(new_enemy)

# Global Constants - Never changes throughout code. ie: pi = 3.14159
# Use all caps for global constants
PI = 3.14159

for i in reversed(range(1, 11)):
    print(i)
