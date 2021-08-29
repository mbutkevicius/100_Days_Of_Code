import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# print("Welcome to Rock, Paper, Scissor! Try to beat the computer!")
# player_choice = int(input("What do you choose? Type 0 for rock, 1 for scissors, or 2 for paper.\n"))
# computer_choice = random.randint(0, 2)
#
# if player_choice == 0:
#     print(rock)
# if player_choice == 1:
#     print(paper)
# if player_choice == 2:
#     print(scissors)
#
# print("Computer chose:")
#
# if computer_choice == 0:
#     print(rock)
# if computer_choice == 1:
#     print(paper)
# if computer_choice == 2:
#     print(scissors)
#
# if player_choice == 0 and computer_choice == 0:
#     print("It's a draw")
# if player_choice == 0 and computer_choice == 1:
#     print("You lose")
# if player_choice == 0 and computer_choice == 2:
#     print("You win")
# if player_choice == 1 and computer_choice == 0:
#     print("You win")
# if player_choice == 1 and computer_choice == 1:
#     print("It's a draw")
# if player_choice == 1 and computer_choice == 2:
#     print("You lose")
# if player_choice == 2 and computer_choice == 0:
#     print("You lose")
# if player_choice == 2 and computer_choice == 1:
#     print("You win")
# if player_choice == 2 and computer_choice == 2:
#     print("It's a draw")

# Alright I know the above code is definitely bad code. I'm going to watch her solution
# I already know in Tim's course he would roast me alive for making code this repetitive


# Nice see this is much cleaner looking code. I'm pretty happy with how this turned out. I think I'm going to try to
# add a for loop that let's me replay and keeps track of score

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# game_images = [rock, scissors, paper]
# print("Welcome to Rock, Paper, Scissor! Try to beat the computer!")
# player_choice = int(input("What do you choose? Type 0 for rock, 1 for scissors, or 2 for paper.\n"))
# computer_choice = random.randint(0, 2)
#
# print(f"You chose: {game_images[player_choice]}")
# print(f"Computer chose: {game_images[computer_choice]}")
#
# if 0 < player_choice >= 4:
#     print("You typed an invalid number, you lose")
# elif player_choice == 0 and computer_choice == 2:
#     print("You lose")
# elif player_choice < computer_choice:
#     print("You win")
# elif player_choice == 2 and computer_choice == 0:
#     print("You win")
# elif player_choice > computer_choice:
#     print("You lose")
# elif player_choice == computer_choice:
#     print("it's a draw")

game_images = [rock, scissors, paper]
print("Welcome to Rock, Paper, Scissor! Try to beat the computer!")
player_choice = input("Press ENTER to begin.\n")

user_score = 0
comp_score = 0
draw_score = 0
num_games = 0

while player_choice != 3:
    player_choice = int(input("What do you choose? Type 0 for rock, 1 for scissors, 2 for paper or 3 to exit.\n"))

    # if 0 < player_choice >= 4:
    if player_choice < 0 or player_choice >= 4:
        print("You typed an invalid number, you lose")
        comp_score += 1
    elif player_choice == 3:
        print(f"Thanks for playing! You won {user_score}, "
              f"lost {comp_score}, and tied {draw_score} out of {num_games} games.")
        break
    else:
        computer_choice = random.randint(0, 2)

        print(f"You chose: {game_images[player_choice]}")
        print(f"Computer chose: {game_images[computer_choice]}")
        if player_choice == 0 and computer_choice == 2:
            print("You lose")
            comp_score += 1
        elif player_choice < computer_choice:
            print("You win")
            user_score += 1
        elif player_choice == 2 and computer_choice == 0:
            print("You win")
            user_score += 1
        elif player_choice > computer_choice:
            print("You lose")
            comp_score += 1
        elif player_choice == computer_choice:
            print("it's a draw")
            draw_score += 1
    num_games += 1
    print(f"You've won {user_score}, lost {comp_score}, and tied {draw_score} out of {num_games} games.")

# I've spent way too much time on this lol. I still can't handle non number inputs. I might fiddle more with it later
# I actually don't think I have the knowledge to fix that right now. I'll come back when I do
