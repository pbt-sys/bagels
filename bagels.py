"""
The program must do as follows:
create a random 3-digit number (can start with 0)
user must guess the number. 
if no numbers are correct, return "bagels"
if a number is correct, but in the wrong position, return "pico"
if a number is correct, and in the right position, return "fermi
if all three numbers are correct, end the game.
"""

import random
import sys

computerNumber = [str(random.randint(0, 10)) for x in range(3)]
computerNumberString = "".join(computerNumber)

print("You must guess the number I have thought of.")
print("if no numbers are correct, I will return 'bagels' \
\nif a number is correct, but in the wrong position, I will return 'pico' \
\nif a number is correct, and in the right position, I will return 'fermi'")

while True:
	print("\nEnter your guess")
	guess = input("> ")

	if guess == computerNumberString:
		print("CORRECT! You win!")
		break

	counterFermi = 0
	counterPico = 0
	for i in range(3):
		if guess[i] == computerNumberString[i]:
			counterFermi += 1
		elif guess[i] in computerNumberString:
			counterPico += 1
		else:
			continue

	print("pico " * counterPico)
	print("fermi " * counterFermi)


