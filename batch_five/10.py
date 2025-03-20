"""Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
Example:
Input: jUAn DEla CrUZ
Output: juan_dela_cruz
"""
user_input = input("Please enter your full name: ").lower()
snake_case = user_input.replace(" ", "_")

print(snake_case)
