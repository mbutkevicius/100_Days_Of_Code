# bIf the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to the tip calculator!")
bill = input("How much is your bill? $")
num_people = int(input("How many people are splitting the bill? "))
tip_percent = input("What tip percentage would you like to leave? %")

tip_decimal = float(tip_percent) / 100 + 1
bill_plus_tip = float(bill) * tip_decimal
bill_per_person = bill_plus_tip / num_people
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")
