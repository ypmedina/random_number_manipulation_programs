"""Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
Example:
Input: jUAn DEla CrUZ
Output: JuanDelaCruz"""

user_input = input("Please enter your full name: ").title()
pascal_input = user_input.replace(" ", "")

print(pascal_input)

