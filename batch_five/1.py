"""
Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
Example:
Input:         Juan Dela Cruz
Output: Juan Dela Cruz
"""

user_input = input("Please enter your full name: ").strip()

print(user_input)