import random

player_hand = []
# player_score = sum(player_hand)
computer_hand = []
# computer_score = sum(computer_hand)


def deal_card():
    """Assigns random value from list above to both players."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    # player_hand.append(random.choice(cards))
    # computer_hand.append(random.choice(cards))


def calculate_score(cards):
    """Add up the total in player_hand and computer_hand. Reduces value of 11 to 1 if score greater than 21"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    # return player_score, computer_score


def compare(player_score, computer_score):
    """calculates both players scores and determines winner"""
    if player_score > 21 and computer_score > 21:
        return "You went over. You lose."
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a blackjack"
    elif player_score == 0:
        return "Win with a blackjack"
    elif player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."


def keep_playing():
    is_game_over = False
    computer_score = calculate_score(computer_hand)
    player_score = calculate_score(player_hand)
    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append((deal_card()))
    while not is_game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"    Your cards: {player_hand}, current score: {player_score}")
        print(f"    Computer's first card {computer_hand[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
            print()
        else:
            print()
            should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_deal == "y":
                player_hand.append(deal_card())
            else:
                is_game_over = True
    while computer_score < 17 and computer_score != 0:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)
    print(f"    Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"    Computer final hand: {computer_hand}, final score {sum(computer_hand)}")
    print(compare(player_score, computer_score))
    print()
    player_hand.clear()
    computer_hand.clear()


while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
    keep_playing()
print()
print("Thanks for playing! Goodbye.")


# keep_playing()

# def keep_playing():
#     play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
#     if play == "y":
#         deal_cards()
#         deal_cards()
#         print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
#         print(f"Computer's first card {computer_hand[0]}")
#     elif play == "n":
#         print("Goodbye")
#     while input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
#         deal_cards()
#         calculate_score()
#         if sum(player_hand) > 21:
#             print("You lose")
#             print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
#             print(f"Computer final hand: {computer_hand}, final score {sum(computer_hand)}")
#             break
#         elif sum(computer_hand) > 21:
#             print("You win!")
#             print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
#             print(f"Computer final hand: {computer_hand}, final score {sum(computer_hand)}")
#             break
#     # if still_playing == "n":
#     #     if sum(computer_hand) < sum(player_hand) <= 21:
#     #         print("You win!")
#     #     elif sum(player_hand) < sum(computer_hand) <= 21:
#     #         print("Computer wins.")
#     #     else:
#     #         print("Draw")
#     player_hand.clear()
#     computer_hand.clear()
#     keep_playing()
#
#
# keep_playing()

# play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
# if play == "y":
#     deal_cards()
#     deal_cards()
#     print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
#     print(f"Computer's first card {computer_hand[0]}")
#     keep_playing()
    # if sum(computer_hand) < sum(player_hand) <= 21:
    #     print("You win!")
    # elif sum(player_hand) < sum(computer_hand) <= 21:
    #     print("Computer wins.")
    # else:
    #     print("Draw")
# elif play == "n":
#     print("Goodbye")

    # keep_playing = input("Type 'y' to get another card, type 'n' to pass: ")
    # if keep_playing == "y":
    #     deal_cards()
    #     if sum(player_hand) > 21:
    #         print("You lose")
    #         print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
    #         print(f"Computer final hand: {computer_hand}, final score {sum(computer_hand)}")
    #     elif sum(computer_hand) > 21:
    #         print("You win!")
    #         print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
    #         print(f"Computer final hand: {computer_hand}, final score {sum(computer_hand)}")
    # elif keep_playing == "n":
    #     if sum(computer_hand) < sum(player_hand) <= 21:
    #         print("You win!")
    #     elif sum(player_hand) < sum(computer_hand) <= 21:
    #         print("Computer wins.")
    #     else:
    #         print("Draw")

