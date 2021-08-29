import day_14_data
import random

print(day_14_data.logo)


def format_account(ran_data: dict):
    return f"{ran_data['name']}, a {ran_data['description']}, from {ran_data['country']}"
    # return ran_data["name"] + ", a " + ran_data["description"] + ", from " + ran_data["country"]


def higher_lower_game():
    greater = 0
    guess = greater

    current_score = 0
    choice_a = random.choice(day_14_data.data)
    while guess == greater:
        choice_b = random.choice(day_14_data.data)

        # # TODO Delete after testing
        # print(choice_a["follower_count"], choice_b["follower_count"])

        if choice_a["follower_count"] > choice_b["follower_count"]:
            greater = choice_a["follower_count"]
        if choice_b["follower_count"] > choice_a["follower_count"]:
            greater = choice_b["follower_count"]

        if current_score >= 1:
            print(f"You're right! Current score: {current_score}.")
        print(f"Compare A: {format_account(choice_a)}.")
        print(day_14_data.vs)
        print(f"Compare B: {format_account(choice_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == "a":
            guess = choice_a["follower_count"]
        elif guess == "b":
            guess = choice_b["follower_count"]
        else:
            print("You've typed an invalid input")
            guess = greater
            continue
        print()
        choice_a = choice_b
        current_score += 1
    print(f"You lost! Your score was: {current_score - 1}.")
    while input("Would you like to play again? Type 'y' or 'n': ").lower() == "y":
        higher_lower_game()
        print()


higher_lower_game()
print("Thanks for playing! Have a good day!")
