# import random
# import hangman_words
#
# print(hangman_words.logo)
#
# word_list = hangman_words.word_list
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# display = []
# for num in range(len(chosen_word)):
#     display += "_"
# print(display)
#
# end_of_game = False
# guess_count = 0
# lives = 6
# letters_guessed = []
#
# # while "_" in display:
# while not end_of_game:
#     guess = input("Please guess a letter:\n").casefold()
#     # letters_guessed += guess
#
#     if guess in display or guess in letters_guessed:
#         print(f"You've already guessed {guess}.")
#         guess_count -= 1
#
#     letters_guessed += guess
#
#     index_position = -1
#     for letter in chosen_word:
#         index_position += 1
#         if letter == guess:
#             display[index_position] = guess
#             # TODO fix this part so that I can repeat letters already guessed
#     if guess not in display:
#         lives -= 1
#         print(f"You guessed {guess}. That's not in the word. You have {lives} lives left.")
#     # elif guess in letters_guessed:
#     #     if guess not in display:
#     #         print("You've already guessed that letter. Try again.")
#     #         guess_count -= 1
#
#     # elif guess in letters_guessed:
#     #     print("You've already guessed that letter. Try again.")
#     #     guess_count -= 1
#     print(hangman_words.stages[lives])
#     print(f"{' '.join(display)}")
#     print(f"letters guessed: {', '.join(letters_guessed)}")
#     guess_count += 1
#
#     if "_" not in display:
#         end_of_game = True
#         print(f"You've won in {guess_count} guesses!")
#     elif lives == 0:
#         end_of_game = True
#         print("You've been hung. You lose.")

import random
import day_7_hangman_words

print(day_7_hangman_words.logo)

word_list = day_7_hangman_words.word_list

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for num in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False
guess_count = 0
lives = 6
letters_guessed = []

while not end_of_game:
    guess = input("Please guess a letter:\n").casefold()

    if guess in display or guess in letters_guessed:
        print(f"You've already guessed {guess}. Try again.")
        guess_count -= 1

    index_position = -1
    for letter in chosen_word:
        index_position += 1
        if letter == guess:
            display[index_position] = guess

    if guess not in letters_guessed and guess not in display:
        lives -= 1
        print(f"You guessed {guess}. That's not in the word. You have {lives} lives left.")
    letters_guessed += guess

    print(day_7_hangman_words.stages[lives])
    print(f"{' '.join(display)}")
    print(f"letters guessed: {', '.join(letters_guessed)}")
    guess_count += 1

    if "_" not in display:
        end_of_game = True
        print(f"You win! It took {guess_count} guesses!")
    elif lives == 0:
        end_of_game = True
        print()
        print("You lost. You're nothing but a hanged man.")
        print(f"""The answer was "{chosen_word}".""")
