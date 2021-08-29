from random import randint


def check_answer(challenge: int, answer: int) -> None:
    """
    Checks users guess against the random number. Let's the
    player know if they won, or guessed too high or low.
    """
    for index in reversed(range(challenge)):
        print(f"You have {index} attempt(s) remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You won! It took you {index * -1 + challenge} guesses.")
            return
        elif guess > answer:
            print("Too high.")
        elif guess < answer:
            print("Too low.")
        if index == 1:
            print("You lose...")
            return
        print("Guess again.")


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
is_playing = True

while is_playing:
    ran_num = randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        difficulty = 11
        check_answer(challenge=difficulty, answer=ran_num)
    elif difficulty == "hard":
        difficulty = 6
        check_answer(challenge=difficulty, answer=ran_num)
    flag = input("Do you want to play another game? Type 'y' or 'n': ").lower()
    if flag == "n":
        is_playing = False
print("Thanks for playing!")

# This was the original attempt. I knew it was redundant code. So my next attempt uses a function and you can see
# how much shorter it is with the function. 40 lines of code compared to 15 (not including function code)


# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# is_playing = True

# while is_playing:
#     difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
#     if difficulty == "easy":
#         for i in reversed(range(1, 11)):
#             print(f"You have {i} attempt(s) remaining to guess the number.")
#             guess = int(input("Make a guess: "))
#             if guess == ran_num:
#                 print(f"You won! It took {i} guesses.")
#                 break
#             elif guess > ran_num:
#                 print("Too high.")
#             elif guess < ran_num:
#                 print("Too low.")
#             if i == 1:
#                 print("You lose...")
#                 break
#             print("Guess again.")
#
#     elif difficulty == "hard":
#         for i in reversed(range(1, 6)):
#             print(f"You have {i} attempt(s) remaining to guess the number.")
#             guess = int(input("Make a guess: "))
#             if guess == ran_num:
#                 print(f"You won! It took {i} guesses.")
#                 break
#             elif guess > ran_num:
#                 print("Too high.")
#             elif guess < ran_num:
#                 print("Too low.")
#             if i == 1:
#                 print("You lose...")
#                 break
#             print("Guess again.")
#     flag = input("Do you want to play another game? Type 'y' or 'n': ")
#     if flag == "n":
#         is_playing = False
# print("Thanks for playing!")
