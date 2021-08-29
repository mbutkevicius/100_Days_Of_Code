import math

# def greet():
#     print("Hello")
#     print("Hi")
#     print("Hey")
#
#
# greet()


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"Hi {name}")
#     print(f"Hey {name}")
#
#
# greet_with_name("Michael")
#
# # Functions with more than one input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
# greet_with(name="Michael", location="America")
#
# # Write your code below this line 👇
# # Math import at top of file
#
#
# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans of paint.")
#
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall in m: "))
# test_w = int(input("Width of wall in m: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Write your code below this line 👇


# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if number == 1:
#         print(f"{number} is a prime number.")
#     elif is_prime:
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")

# Okay this was someone else's solution and I was trying to do this originally. I was getting so frustrated.
# I didn't realize I could move the else block like that. It was printing multiple of the same prime numbers
# But pulling it out of indentation like that apparently works and does what I was trying.

# def prime_checker(number):
#
#     for i in range(2, number):
#         if number % i == 0:
#             print(f"{number} is not a prime")
#             break
#     else:
#         print(f"{number} is a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# for n in range(100):
#     prime_checker(number=n)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
direction = "encode"
# text = input("Type your message:\n").lower()
# text = "civilization"
text = "hello i am 3"
shift = 109
# shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         index = alphabet.index(letter)
#         if index + shift_amount > 25:
#             special_shift = (index + shift_amount) - 26
#             index = special_shift
#             shift_amount = 0
#         cipher_text += alphabet[index + shift_amount]
#         shift_amount = shift
#     print(cipher_text)

# Okay so while working on decrypt function I realized I can reverse index encrypt without worrying about going out of
# range. This is the new function which looks much nicer in my opinion.
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         index = alphabet.index(letter) - (26 - shift_amount)
#         cipher_text += alphabet[index]
#     print(f"The encrypted text is: {cipher_text}.")
#
#
# encrypt(plain_text=text, shift_amount=shift)
#
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         index = alphabet.index(letter)
#         plain_text += alphabet[index - shift_amount]
#     print(f"The decoded text is: {plain_text}.")
#
#
# decrypt(cipher_text=text, shift_amount=shift)
#
# if direction == "encrypt":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decrypt":
#     decrypt(cipher_text=text, shift_amount=shift)


def caesar(cipher_direction, txt, shift_amount):
    caesar_text = ""
    index = 0
    for letter in txt:
        if letter not in alphabet:
            caesar_text += letter
            continue
        elif cipher_direction == "encode":
            index = (alphabet.index(letter) - (26 - shift_amount)) % 26
        elif cipher_direction == "decode":
            index = (alphabet.index(letter) - shift_amount) % 26
        caesar_text += alphabet[index]
    print(f'The {cipher_direction}d text is: "{caesar_text}".')


caesar(cipher_direction=direction, txt=text, shift_amount=shift)

play = True
while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(cipher_direction=direction, txt=text, shift_amount=shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        play = False
        print("Goodbye")

#
# def run(yes):
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     if yes == "yes":
#         caesar(direction, text, shift)

# def encrypt(plain_text, shift_amount):
#     cypher_text = ""
#     for letter in plain_text:
#         if letter in alphabet:
#             index = alphabet.index(letter)
#             if index + shift_amount > 25:
#                 special_shift = (index + shift_amount) - 26
#                 index = special_shift
#                 shift_amount = 0
#             cypher_text += alphabet[index + shift_amount]
#             shift_amount = shift
#     print(cypher_text)

# # No idea how this works but it does
# def encrypt(txt = text, shft = shift):
#     output = ''
#     for val in text:
#         output += chr((ord(val) - 97 + shift) % 26 + 97)
#     print(output)
# 
#
# encrypt(text, shift)
